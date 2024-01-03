import xml.etree.ElementTree as ET
import sqlite3
import argparse


def insert_items(item_path, db):
    tree = ET.parse(item_path)
    root = tree.getroot()
    chainid = root[0][0].text
    items = root[0][1]
    item_fields = ["chainid", "subchainid", "storeid", "itemcode", "itemtype",
                   "manufacturername", "manufacturercountry",
                   "manufactureritemdescription", "unitqty", "quantity",
                   "bisweighted", "itemprice", "unitofmeasureprice",
                   "allowdiscount", "itemstatus", "priceupdatedate"]
    item_cnt = ("?," * len(item_fields))[:-1]
    item_insert = "insert into subchainitems({}) values({})".format(
        ",".join(item_fields), item_cnt)
    item_vals = []
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("select storepk from stores where chainid=? and " \
                "subchainid=? and storeid=?", 
    for item in item:
        item_vals.append(tuple([element.text for element in 
                                map(item.find, item_fields)]))
    
    cur.executemany(insert, vals)
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
