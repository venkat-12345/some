import pixellib
from pixellib.tune_bg import alter_bg

print(1)
change_bg = alter_bg()
print(1)
change_bg.load_pascalvoc_model("deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
print(1)

change_bg.change_bg_img(f_image_path = "img.png",b_image_path = "Ing.jpg", output_image_name="new_img.jpg")
print(1)
Image(filename='new_img.jpg',width=300,height=350)
print(1)
