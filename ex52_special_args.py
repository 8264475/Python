# Positional only
def tri_area(b,h,/):
    return b*h/2.

# Keyword only
def rect_area(*,length,width):
    return length*width

# Positional or Keyword
def BMI(weight,height):
    return weight/(height/100)**2


# MAIN
tri_area(12,5)

rect_area(width=100, length=150)

BMI(65, height=170)



