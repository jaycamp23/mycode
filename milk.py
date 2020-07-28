#!/user/bin/env python

# Today (July 28th) is National Milk Chocolate Day!
ingredients= [["soap", "bleach", "sponges"], ["milk", "beer", "tabasco"], ["sugar", "vanilla", "cocoa"]]
measurements= ["3 cups", "2 tablespoons", "1/2 teaspoon"]
# Rewrite the following string using a print statement. Replace all ingredients and measurements using the lists above!
# Pour {3 cups} {milk} into blender. Add in {2 tablespoons} {cocoa}, {2 tablespoons} {sugar}, and {1/2 teaspoon} {vanilla}. Blend all ingredients until fully incorporated.

print(f" Pour {measurements[0]} {ingredients[1][0]} into blender. Add in {measurements[1]} {ingredients[2][2]}, {measurements[1]} {ingredients[2][0]}., and {measurements[2]} {ingredients[2][1]}. Blend all ingredients until fully incorporated.")
