name = "Zed A. Shaw"
age = 35 # not a lie
height_cm = 74
weight_kg = 180
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d cm tall." % height_cm
print "He's %d kg heavy." % weight_kg
print "Accually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height_cm, weight_kg, age + height_cm + weight_kg)
