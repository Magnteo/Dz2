def get_cats_info(path):
    try:
        cats=[]
        with open(path,'r', encoding="utf-8") as file:
            for  cat in file :
                try:
                    cat_id, name, age =cat.strip().split(",") 
                    cat_dict ={"id": cat_id, "name": name, "age": age}
                    cats.append(cat_dict)
                except ValueError:
                    print("рядок не має 3 частин")
                    continue
        return cats
    except FileNotFoundError:
        return "невірний шлях"
cats_info = get_cats_info("2\cat.txt")
print(cats_info)
