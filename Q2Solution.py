def id_mushrooms():
    mushrdooms=[
        "Agaric jaunissant",
        "Cepe de bordeaux",
        "Amanite tue-mouche",
        "Coprin chevelu",
        "Girolle",
        "Pied Bleu"
    ]

    gills=input("Does your mushroom have gills ? (yes/no): ").strip().lower()=='yes'
    forest = input("Does your mushroom grow in a forest? (yes/no): ").strip().lower() == 'yes'
    ring = input("Does your mushroom have a ring? (yes/no): ").strip().lower() == 'yes'
    convex_cup = input("Does your mushroom have a convex cup? (yes/no): ").strip().lower() == 'yes'

    if gills:
        if forest:
            if not convex_cup:
               print("Your mushroom is: Girolle " )
            if convex_cup:
                if not ring:
                   print("Your mushroom is : Pied Bleu ")
                if ring:
                    print("Your mushroom is: Amanite tue-mouche")
        else:
            if ring:
                if not convex_cup:
                     print("Your mushroom is:Coprin chevelu")
                if convex_cup:
                    print("Your mushroom is : Agaric jaunissant")

    else:
        if forest:
          print("Your mushroom is :Cepe de bordeaux")
        else:
            print("No mushroom with such characteristics")

#function call
id_mushrooms()
#Solution to question 2 goes here
