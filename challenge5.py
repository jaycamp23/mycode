#!/usr/bin/env python


dict  = {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "Highest", "strength": "Money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}

char_name = input('Which character do you want to know about? Flash, Batman, Superman: ')
char_stat = input(' What statistic do you want to know about? strength, speed, or intelligence: ')

answer = 0

while True:
    if char_name  == "flash" and char_stat == "speed":
        print("flash's speed is " + dict["flash"]["speed"])
        break
    elif char_name == "flash" and char_stat == "intelligence":
        print("flash's intelligence is " + dict["flash"]["intelligence"])
        break
    elif char_name == "flash" and char_stat == "strength":
        print("flash's strength is " + dict["flash"]["strenght"])
        break





    if char_name == "batman" and char_stat == "speed":
        print("batman's speed is " + dict["batman"]["speed"])
        break
    elif char_name == "batman" and char_stat == "intelligence":
        print("batman's intelligence is" + dict["batman"]["intelligence"])
        break
    elif char_name == "batman" and char_stat == "strength":
        print("batman's strength  is" + dict["batman"]["strength"])
        break

    if char_name == "superman" and char_stat == "speed":
        print("super's speed is "+  dict["superman"]["speed"])
        break
    elif char_name == "superman" and char_stat == "intelligence":
        print("superman's intelligence is " +  dict["superman"]["intelligence"])
        break
    elif char_name == "superman" and char_stat == "strength":
        print("superman's strength is "+  dict["superman"]["strength"])
        break
        

 
