from Filters import *

filename = "chance.jpg"
filename2 = "chance_filtered.jpg"

original = load_img(filename)

newimg = kody(original)

save_img(newimg,filename2)

show_img(newimg)
