import dns.resolver

def main():
    try:
        objetivo = dns.resolver.query("google.com", "NS")
        for x in objetivo:
            print(x)
    except:
        print("No se pudo encontrar la informacion")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
