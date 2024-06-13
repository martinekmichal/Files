def load_data(path="DATA/text.txt"):
    with open(path, "r", encoding='utf-8') as f:
    #f = open(path, "r")
        data = f.read()
   # f.close()
    return data

def filter7(data):
    words = data.split(" ")
    #filtered_words = [w for w in words if len(w) > 6]
    filtered_words = []
    for w in words:
        if len(w) > 6:
            filtered_words.append(w)

    return filtered_words

def save_data(path, data):
    try:
        f = open(path, "w")
        f.write(", ".join(data))

    except:
        print("Došlo k chybe")

    finally:
        f.close()

data = load_data()
new_data = filter7(data)
save_data("DATA/filtered_text.txt", new_data)