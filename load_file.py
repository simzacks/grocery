import xml.etree.ElementTree as ET
import sqlite3
import argparse


def insert_file(tablename, root_fields, obj_fields, obj_node, file_path, db,
                obj2_fields=None, obj2_node=None):
    tree = ET.parse(file_path)
    root = tree.getroot()
    root_vals = [element.text for element in map(root.find, root_fields)]
    all_fields = root_fields + obj_fields
    if obj2_fields:
        all_fields = all_fields + obj2_fields
    fld_cnt = ("?," * len(all_fields))[:-1]
    insert = "insert into {}({}) values({})".format(
        tablename, ",".join(all_fields), fld_cnt)
    data = []
    data_nodes = root.find(obj_node)
    for data_node in data_nodes:
        if obj2_node:
            d2s = data_node.find(obj2_node)
            for d2 in d2s:
                data.append(tuple(root_vals + [element.text for element in 
                            map(data_node.find, obj_fields)] + 
                            [element.text for element in 
                            map(d2.find, obj2_fields)]))
        else:
            data.append(tuple(root_vals + [element.text for element in 
                                map(data_node.find, obj_fields)]))
    
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.executemany(insert, vals)
    conn.commit()
    conn.close()

def stores(file_path, db):
    root_fields = ["chainid"]
    store_fields = ["subchainid", "storeid", "bikoretno", "storetype",
                    "subchainname", "storename", "address", "city", "zipcode"]
    tablename = "stores"
    obj_node = "stores"
    insert_file(tablename, root_fields, store_fields, obj_node, file_path, db)

def promotions(file_path, db):
    root_fields = ["chainid","subchainid", "storeid"]
    promo_fields = ["promotionid", "allowmultiplediscounts",
                    "promotiondescription", "promotionupdatedate",
                    "promotionstartdate", "promotionstarthour",
                    "promotionenddate","promotionendhour", "isweightedpromo",
                    "minqty", "rewardtype", "discountedprice",
                    "minnoofitemofered"]
    tablename = "promotions"
    obj_node = "promotions"
    insert_file(tablename, root_fields, promo_fields, obj_node, file_path, db)

def promotionitems(file_path, db):
    root_fields = ["chainid","subchainid", "storeid"]
    promo1_fields = ["promotionid"]
    promo2_fields = ["itemcode", "itemtype", "isgiftitem"]
    tablename = "promotionitems"
    obj1_node = "promotions"
    obj2_node = "promotionitems"
    insert_file(tablename, root_fields, promo1_fields, obj1_node, file_path, db,
                promo2_fields, obj2_node)

def item_prices(file_path, db):
    root_fields = ["chainid", "subchainid", "storeid"]
    item_fields = ["itemcode", "itemtype",
                   "manufacturername", "manufacturercountry",
                   "manufactureritemdescription", "unitqty", "quantity",
                   "bisweighted", "itemprice", "unitofmeasureprice",
                   "allowdiscount", "itemstatus", "priceupdatedate"]
    tablename = "storeitems"
    obj_node = "items"
    insert_file(tablename, root_fields, item_fields, obj_node, file_path, db)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Import Full Grocery Items and Price",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-p", "--path",
                        help="The path of the full price file", required=True)
    parser.add_argument("-d", "--db",
                        help="The path of the sqlite database", required=True)
    args = parser.parse_args()
    insert_items(args.path, args.db)
