productos = [
    {
        "ID": 3232,
        "nombre": "Lapiz",
        "precio": 500,
        "id_categoria": 1
    },
    {
        "ID": 4343,
        "nombre": "Toalla",
        "precio": 10.000,
        "id_categoria": 2
    }
]
categorias = [
    {
        "id_categoria": 1,
        "nombre": "Utiles escolares"
    },
    {
        "id_categoria": 2,
        "nombre": "Aseo"
    }
]

cat_pro = {}

for i in productos:
    for j in categorias:
        if i["id_categoria"] == j["id_categoria"]:
            cat_pro[i["ID"]] = {
                "nombre_producto": i["nombre"],
                "nombre_categoria": j["nombre"]
            }

for imp in cat_pro:
    print("ID del Producto:", imp)
    print("Nombre del Producto:", cat_pro[imp]["nombre_producto"])
    print("Nombre de la Categoría:", cat_pro[imp]["nombre_categoria"])
    print()