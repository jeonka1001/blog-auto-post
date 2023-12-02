from readfile import read_conf

def main():
    data = read_conf("src/conf/secret.json")
    key = "Bearer {0}".format(data["secret_key"])
    print(key)


if __name__ == "__main__":
    main()