name = "Zed A. Shaw"
my_age = 35 # not a lie
my_height_cm = 74
my_weight_kg = 180
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % name
print "He's %d cm tall." % my_height_cm
print "He's %d kg heavy." % my_weight_kg
print "Accually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height_cm, my_weight_kg, my_age + my_height_cm + my_weight_kg)
