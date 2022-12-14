j = input("File name: ").strip().lower()

def test(j):
    if "." in j:
        a,b = j.split(".")

        match b:
            case "gif":
                return "image/gif"
            case "jpg":
                return "image/jpeg"
    else:
        return "application/octet-stream "


print(test(j))





    