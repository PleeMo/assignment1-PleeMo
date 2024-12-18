#Solution to question 2 goes here
# Questions and their implications
    has_gills = input("Does your mushroom have gills? ").strip().lower() == "yes"
    if has_gills:
        # If it has gills, check further
        grows_in_forest = input("Does your mushroom grow in a forest? ").strip().lower() == "yes"
        if grows_in_forest:
            has_ring = input("Does your mushroom have a ring? ").strip().lower() == "yes"
            if has_ring:
                # Amanite tue-mouche
                print("Your mushroom is Amanite tue-mouche.")
            else:
                # Girolle
                print("Your mushroom is Girolle.")
        else:
            # Check for Coprin chevelu or Agaric jaunissant
            has_convex_cup = input("Does your mushroom have a convex cup? ").strip().lower() == "yes"
            if has_convex_cup:
                # Agaric jaunissant
                print("Your mushroom is Agaric jaunissant.")
            else:
                # Coprin chevelu
                print("Your mushroom is Coprin chevelu.")
    else:
        # If it doesn't have gills, it must be Cepe de bordeaux or Pied Bleu
        grows_in_forest = input("Does your mushroom grow in a forest? ").strip().lower() == "yes"
        if grows_in_forest:
            has_convex_cup = input("Does your mushroom have a convex cup? ").strip().lower() == "yes"
            if has_convex_cup:
                # Pied Bleu
                print("Your mushroom is Pied Bleu.")
            else:
                # This is ambiguous as the user may have chosen Girolle
                print("Your mushroom is Cepe de bordeaux.")
        else:
            # If it grows in meadows, it must be Girolle
            print("Your mushroom is Girolle.")

# Run the function
determine_mushroom()