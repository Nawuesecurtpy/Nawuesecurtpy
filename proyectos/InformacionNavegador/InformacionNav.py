from venv import main
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help ="objetivo")
parser = parser.parse_args()

def funcion():
    if parser.target:
        try:
            objetivo = requests.get(url=parser.target)
            header = dict(objetivo.headers)
            for x in header:
                print(x+ "header"+header[x])
        except:
            print("no me puedo conectar")
    
    else:
        print("vuelva a escribir...")

if __name__ == "__main__":
    main()