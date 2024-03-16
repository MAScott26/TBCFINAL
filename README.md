

Turn Based Combat Pseudocode

Import random

Create Character class

Name
HP
Armor
hitChance
maxdamage

For each above,
@property
Define [variable] (self)
Return __[variable] = value

@[variable].setter
Define [variable](self,value)
Variable is tested to be in range
Self.[variable] gets value in range


Define testInt
takes in value
        checks to see if it is an int between
        min and max.  If it is not a legal value
        set it to default


Define printStats
Print name
HP
Hit chance,
max damage,
armor.

Define Hit
If random value is less than hit chance, do damage between 1 and [maxDamage]
Print who hits who for how much, but also how much is absorbed by armor.
If damage is greater than armor, deal damage with armor value subtracted.

Define Fight
Print player and enemies HP
Player hits enemy and enemy hits player
If the player's HP is greater than the enemy's HP print”player wins” and vice versa.
Create an input function so as to quit the game.


Define Main
New variable gets character info from class
Other variable gets character info from character class
Variable.printStats runs
Variable2.printStats runs

Run main
