#!/usr/bin/env python
import os
import sys
import json

def main():
	print (len(sys.argv), str(sys.argv))
	print (sys.argv)

	dataNames = ['tick','sensor_id','duration','fps','res_x','res_y','rotation','format']
	with open(sys.argv[1]) as json_file:
        	data = json.load(json_file)

		for name in dataNames:
			print(name+','),

    print('\n'),

		for name in dataNames:
			print(data[name]),


if __name__ == "__main__":
	main()



