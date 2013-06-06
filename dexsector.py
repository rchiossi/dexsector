#!/usr/bin/python

import os
import argparse

from dexlib.dex import Dex
from dexlib.libparse.printer import Printer

import sys

def read_data(filename):
    try:
        fd = open(filename)
    except:
        print 'error: Unable to open file %s' % filename
        exit(1)
        
    try:
        data = fd.read()
        
    except:
        print 'error: unable to read from file %s' % filename
        exit(1)
        
    fd.close()

    return data

def execute(args):    
    dex = Dex()    
    dex.parse(read_data(args.dex_file))

    p = Printer()

    if args.header :
        print p.parse(dex.header)

    if args.map :
        print p.parse(dex.map_list)

    if args.string_id_list:
        print p.parse(dex.string_ids)
    if args.string_id != None:
        print p.parse(dex.string_ids[args.string_id])


    if args.string_data_list:
        print p.parse(dex.string_data_table)
    if args.string_data != None:
        print p.parse(dex.string_data_table[args.string_data])

    if args.type_id_list:
        print p.parse(dex.type_ids)
    if args.type_id != None:
        print p.parse(dex.type_data[args.type_id])

    if args.proto_id_list:
        print p.parse(dex.proto_ids)
    if args.proto_id != None:
        print p.parse(dex.proto_ids[args.proto_id])
        
    if args.field_id_list:
        print p.parse(dex.field_ids)
    if args.field_id != None:
        print p.parse(dex.field_ids[args.field_id])
        
    if args.method_id_list:
        print p.parse(dex.method_ids)
    if args.method_id != None:
        print p.parse(dex.method_ids[args.method_id])

    if args.class_def_list:
        print p.parse(dex.class_defs)
    if args.class_def != None:
        print p.parse(dex.class_defs[args.class_def])

    if args.class_data_list:
        print p.parse(dex.class_data_table)
    if args.class_data != None:
        print p.parse(dex.class_data_table[args.class_data])

    if args.code_item_list:
        print p.parse(dex.code_item_table)
    if args.code_item != None:
        print p.parse(dex.code_item_table[args.code_item])


def main():
    parser = argparse.ArgumentParser(description='Display information about the contents of DEX format files.')
    parser.add_argument('dex_file',help='Target DEX file')

    parser.add_argument('-v','--version',action='version',version='readdex 1.0')

    parser.add_argument('-H','--header',action='store_true',help='Dex Header data')
    parser.add_argument('-X','--map',action='store_true',help='Dex Map data')

    parser.add_argument('-I','--string_id_list',action='store_true', help='string_id list data')
    parser.add_argument('-i','--string_id',type=int, help='string_id data at given index')

    parser.add_argument('-S','--string_data_list',action='store_true',help='string_data list data')
    parser.add_argument('-s','--string_data',type=int,help='string_data data at given index')

    parser.add_argument('-T','--type_id_list',action='store_true',help='type_id list data')
    parser.add_argument('-t','--type_id',type=int,help='type_id at given index')

    parser.add_argument('-P','--proto_id_list',action='store_true',help='proto_id list data')
    parser.add_argument('-p','--proto_id',type=int,help='proto_id at given index')

    parser.add_argument('-F','--field_id_list',action='store_true',help='field_id list data')
    parser.add_argument('-f','--field_id',type=int,help='field_id at given index')

    parser.add_argument('-M','--method_id_list',action='store_true',help='method_id list data')
    parser.add_argument('-m','--method_id',type=int,help='method_id data at given index')

    parser.add_argument('-D','--class_def_list',action='store_true',help='class_def_item list data')
    parser.add_argument('-d','--class_def',type=int,help='class_def_item data at given index')

    parser.add_argument('-L','--class_data_list',action='store_true',help='class_data_item list data')
    parser.add_argument('-l','--class_data',type=int,help='class_data_item data at given index')

    parser.add_argument('-C','--code_item_list',action='store_true',help='code_item list data')
    parser.add_argument('-c','--code_item',type=int,help='code_item data at given index')


    args = parser.parse_args()

    if not os.path.exists(args.dex_file):
        parser.error("File %s does not exist" % args.dex_file)

    execute(args)

if __name__ == "__main__":
    main()
