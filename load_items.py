import xml.etree.ElementTree as ET
import sqlite3
import argparse


def insert_items(item_path, db):
    tree = ET.parse(item_path)
    root = tree.getroot()
    root_fields = ["chainid", "subchainid", "storeid"]
    root_vals = [element.text for element in map(root.find, root_fields)]
    item_fields = ["itemcode", "itemtype",
                   "manufacturername", "manufacturercountry",
                   "manufactureritemdescription", "unitqty", "quantity",
                   "bisweighted", "itemprice", "unitofmeasureprice",
                   "allowdiscount", "itemstatus", "priceupdatedate"]
    all_fields = root_fields + item_fields
    fld_cnt = ("?," * len(all_fields))[:-1]
    item_insert = "insert into storeitems({}) values({})".format(
        ",".join(all_fields), fld_cnt)
    item_vals = []
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    items = root.find("items")
    for item in items:
        item_vals.append(tuple(root_vals + [element.text for element in 
                                map(item.find, item_fields)]))
    
    cur.executemany(item_insert, vals)
    conn.commit()
    conn.close()

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
