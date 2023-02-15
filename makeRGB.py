import os, sys
import PIL
from PIL import Image
import zipfile

#folders and paths
parent = os.getcwd()
parent = os.path.join(parent, '')
lst = os.listdir(parent)

print(parent)
input('Press ENTER') #change raw_input to input when running on BECK




#rename the .upf into .zip
for file_name in lst:
    if file_name.endswith(".upf"):
        os.rename(parent + file_name, parent + file_name[:-3] + "zip")
        



#copy files in .zip to parent folder
lst2 = os.listdir(parent)
dest_dir = parent

for file_name in lst2:
    if file_name.endswith(".zip"):
        src_dir = os.path.join(parent, file_name)



with zipfile.ZipFile(src_dir, 'r') as zip_ref:
    zip_ref.extractall(dest_dir)
           
   
    


#loop over images and merge the channels

red1 = Image.open(parent + 'imageset0_camera01_red.jpg').convert('L')
green1 = Image.open(parent + 'imageset0_camera01_green0.jpg').convert('L')
blue1 = Image.open(parent + 'imageset0_camera01_blue.jpg').convert('L')
out1 = Image.merge("RGB", (red1, green1, blue1))
out1.save("img1.jpg", optimize=True)

red2 = Image.open(parent + 'imageset0_camera02_red.jpg').convert('L')
green2 = Image.open(parent + 'imageset0_camera02_green0.jpg').convert('L')
blue2 = Image.open(parent + 'imageset0_camera02_blue.jpg').convert('L')
out2 = Image.merge("RGB", (red2, green2, blue2))
out2.save("img2.jpg", optimize=True)

red3 = Image.open(parent + 'imageset0_camera03_red.jpg').convert('L')
green3 = Image.open(parent + 'imageset0_camera03_green0.jpg').convert('L')
blue3 = Image.open(parent + 'imageset0_camera03_blue.jpg').convert('L')
out3 = Image.merge("RGB", (red3, green3, blue3))
out3.save("img3.jpg", optimize=True)

red4 = Image.open(parent + 'imageset0_camera04_red.jpg').convert('L')
green4 = Image.open(parent + 'imageset0_camera04_green0.jpg').convert('L')
blue4 = Image.open(parent + 'imageset0_camera04_blue.jpg').convert('L')
out4 = Image.merge("RGB", (red4, green4, blue4))
out4.save("img4.jpg", optimize=True)

red5 = Image.open(parent + 'imageset0_camera05_red.jpg').convert('L')
green5 = Image.open(parent + 'imageset0_camera05_green0.jpg').convert('L')
blue5 = Image.open(parent + 'imageset0_camera05_blue.jpg').convert('L')
out5 = Image.merge("RGB", (red5, green5, blue5))
out5.save("img5.jpg", optimize=True)

red6 = Image.open(parent + 'imageset0_camera06_red.jpg').convert('L')
green6 = Image.open(parent + 'imageset0_camera06_green0.jpg').convert('L')
blue6 = Image.open(parent + 'imageset0_camera06_blue.jpg').convert('L')
out6 = Image.merge("RGB", (red6, green6, blue6))
out6.save("img6.jpg", optimize=True)

red7 = Image.open(parent + 'imageset0_camera07_red.jpg').convert('L')
green7 = Image.open(parent + 'imageset0_camera07_green0.jpg').convert('L')
blue7 = Image.open(parent + 'imageset0_camera07_blue.jpg').convert('L')
out7 = Image.merge("RGB", (red7, green7, blue7))
out7.save("img7.jpg", optimize=True)

red8 = Image.open(parent + 'imageset0_camera08_red.jpg').convert('L')
green8 = Image.open(parent + 'imageset0_camera08_green0.jpg').convert('L')
blue8 = Image.open(parent + 'imageset0_camera08_blue.jpg').convert('L')
out8 = Image.merge("RGB", (red8, green8, blue8))
out8.save("img8.jpg", optimize=True)

red9 = Image.open(parent + 'imageset0_camera09_red.jpg').convert('L')
green9 = Image.open(parent + 'imageset0_camera09_green0.jpg').convert('L')
blue9 = Image.open(parent + 'imageset0_camera09_blue.jpg').convert('L')
out9 = Image.merge("RGB", (red9, green9, blue9))
out9.save("img9.jpg", optimize=True)

red10 = Image.open(parent + 'imageset0_camera10_red.jpg').convert('L')
green10 = Image.open(parent + 'imageset0_camera10_green0.jpg').convert('L')
blue10 = Image.open(parent + 'imageset0_camera10_blue.jpg').convert('L')
out10 = Image.merge("RGB", (red10, green10, blue10))
out10.save("img10.jpg", optimize=True)

red11 = Image.open(parent + 'imageset0_camera11_red.jpg').convert('L')
green11 = Image.open(parent + 'imageset0_camera11_green0.jpg').convert('L')
blue11 = Image.open(parent + 'imageset0_camera11_blue.jpg').convert('L')
out11 = Image.merge("RGB", (red11, green11, blue11))
out11.save("img11.jpg", optimize=True)

red12 = Image.open(parent + 'imageset0_camera12_red.jpg').convert('L')
green12 = Image.open(parent + 'imageset0_camera12_green0.jpg').convert('L')
blue12 = Image.open(parent + 'imageset0_camera12_blue.jpg').convert('L')
out12 = Image.merge("RGB", (red12, green12, blue12))
out12.save("img12.jpg", optimize=True)

red13 = Image.open(parent + 'imageset0_camera13_red.jpg').convert('L')
green13 = Image.open(parent + 'imageset0_camera13_green0.jpg').convert('L')
blue13 = Image.open(parent + 'imageset0_camera13_blue.jpg').convert('L')
out13 = Image.merge("RGB", (red13, green13, blue13))
out13.save("img13.jpg", optimize=True)

red14 = Image.open(parent + 'imageset0_camera14_red.jpg').convert('L')
green14 = Image.open(parent + 'imageset0_camera14_green0.jpg').convert('L')
blue14 = Image.open(parent + 'imageset0_camera14_blue.jpg').convert('L')
out14 = Image.merge("RGB", (red14, green14, blue14))
out14.save("img14.jpg", optimize=True)

red15 = Image.open(parent + 'imageset0_camera15_red.jpg').convert('L')
green15 = Image.open(parent + 'imageset0_camera15_green0.jpg').convert('L')
blue15 = Image.open(parent + 'imageset0_camera15_blue.jpg').convert('L')
out15 = Image.merge("RGB", (red15, green15, blue15))
out15.save("img15.jpg", optimize=True)

red16 = Image.open(parent + 'imageset0_camera16_red.jpg').convert('L')
green16 = Image.open(parent + 'imageset0_camera16_green0.jpg').convert('L')
blue16 = Image.open(parent + 'imageset0_camera16_blue.jpg').convert('L')
out16 = Image.merge("RGB", (red16, green16, blue16))
out16.save("img16.jpg", optimize=True)

red17 = Image.open(parent + 'imageset0_camera17_red.jpg').convert('L')
green17 = Image.open(parent + 'imageset0_camera17_green0.jpg').convert('L')
blue17 = Image.open(parent + 'imageset0_camera17_blue.jpg').convert('L')
out17 = Image.merge("RGB", (red17, green17, blue17))
out17.save("img17.jpg", optimize=True)

red18 = Image.open(parent + 'imageset0_camera18_red.jpg').convert('L')
green18 = Image.open(parent + 'imageset0_camera18_green0.jpg').convert('L')
blue18 = Image.open(parent + 'imageset0_camera18_blue.jpg').convert('L')
out18 = Image.merge("RGB", (red18, green18, blue18))
out18.save("img18.jpg", optimize=True)

red19 = Image.open(parent + 'imageset0_camera19_red.jpg').convert('L')
green19 = Image.open(parent + 'imageset0_camera19_green0.jpg').convert('L')
blue19 = Image.open(parent + 'imageset0_camera19_blue.jpg').convert('L')
out19 = Image.merge("RGB", (red19, green19, blue19))
out19.save("img19.jpg", optimize=True)

red20 = Image.open(parent + 'imageset0_camera20_red.jpg').convert('L')
green20 = Image.open(parent + 'imageset0_camera20_green0.jpg').convert('L')
blue20 = Image.open(parent + 'imageset0_camera20_blue.jpg').convert('L')
out20 = Image.merge("RGB", (red20, green20, blue20))
out20.save("img20.jpg", optimize=True)

red21 = Image.open(parent + 'imageset0_camera21_red.jpg').convert('L')
green21 = Image.open(parent + 'imageset0_camera21_green0.jpg').convert('L')
blue21 = Image.open(parent + 'imageset0_camera21_blue.jpg').convert('L')
out21 = Image.merge("RGB", (red21, green21, blue21))
out21.save("img21.jpg", optimize=True)

red22 = Image.open(parent + 'imageset0_camera22_red.jpg').convert('L')
green22 = Image.open(parent + 'imageset0_camera22_green0.jpg').convert('L')
blue22 = Image.open(parent + 'imageset0_camera22_blue.jpg').convert('L')
out22 = Image.merge("RGB", (red22, green22, blue22))
out22.save("img22.jpg", optimize=True)

red23 = Image.open(parent + 'imageset0_camera23_red.jpg').convert('L')
green23 = Image.open(parent + 'imageset0_camera23_green0.jpg').convert('L')
blue23 = Image.open(parent + 'imageset0_camera23_blue.jpg').convert('L')
out23 = Image.merge("RGB", (red23, green23, blue23))
out23.save("img23.jpg", optimize=True)

red24 = Image.open(parent + 'imageset0_camera24_red.jpg').convert('L')
green24 = Image.open(parent + 'imageset0_camera24_green0.jpg').convert('L')
blue24 = Image.open(parent + 'imageset0_camera24_blue.jpg').convert('L')
out24 = Image.merge("RGB", (red24, green24, blue24))
out24.save("img24.jpg", optimize=True)

red25 = Image.open(parent + 'imageset0_camera25_red.jpg').convert('L')
green25 = Image.open(parent + 'imageset0_camera25_green0.jpg').convert('L')
blue25 = Image.open(parent + 'imageset0_camera25_blue.jpg').convert('L')
out25 = Image.merge("RGB", (red25, green25, blue25))
out25.save("img25.jpg", optimize=True)

red26 = Image.open(parent + 'imageset0_camera26_red.jpg').convert('L')
green26 = Image.open(parent + 'imageset0_camera26_green0.jpg').convert('L')
blue26 = Image.open(parent + 'imageset0_camera26_blue.jpg').convert('L')
out26 = Image.merge("RGB", (red26, green26, blue26))
out26.save("img26.jpg", optimize=True)

red27 = Image.open(parent + 'imageset0_camera27_red.jpg').convert('L')
green27 = Image.open(parent + 'imageset0_camera27_green0.jpg').convert('L')
blue27 = Image.open(parent + 'imageset0_camera27_blue.jpg').convert('L')
out27 = Image.merge("RGB", (red27, green27, blue27))
out27.save("img27.jpg", optimize=True)

red28 = Image.open(parent + 'imageset0_camera28_red.jpg').convert('L')
green28 = Image.open(parent + 'imageset0_camera28_green0.jpg').convert('L')
blue28 = Image.open(parent + 'imageset0_camera28_blue.jpg').convert('L')
out28 = Image.merge("RGB", (red28, green28, blue28))
out28.save("img28.jpg", optimize=True)

red29 = Image.open(parent + 'imageset0_camera29_red.jpg').convert('L')
green29 = Image.open(parent + 'imageset0_camera29_green0.jpg').convert('L')
blue29 = Image.open(parent + 'imageset0_camera29_blue.jpg').convert('L')
out29 = Image.merge("RGB", (red29, green29, blue29))
out29.save("img29.jpg", optimize=True)

red30 = Image.open(parent + 'imageset0_camera30_red.jpg').convert('L')
green30 = Image.open(parent + 'imageset0_camera30_green0.jpg').convert('L')
blue30 = Image.open(parent + 'imageset0_camera30_blue.jpg').convert('L')
out30 = Image.merge("RGB", (red30, green30, blue30))
out30.save("img30.jpg", optimize=True)

red31 = Image.open(parent + 'imageset0_camera31_red.jpg').convert('L')
green31 = Image.open(parent + 'imageset0_camera31_green0.jpg').convert('L')
blue31 = Image.open(parent + 'imageset0_camera31_blue.jpg').convert('L')
out31 = Image.merge("RGB", (red31, green31, blue31))
out31.save("img31.jpg", optimize=True)

red32 = Image.open(parent + 'imageset0_camera32_red.jpg').convert('L')
green32 = Image.open(parent + 'imageset0_camera32_green0.jpg').convert('L')
blue32 = Image.open(parent + 'imageset0_camera32_blue.jpg').convert('L')
out32 = Image.merge("RGB", (red32, green32, blue32))
out32.save("img32.jpg", optimize=True)

red33 = Image.open(parent + 'imageset0_camera33_red.jpg').convert('L')
green33 = Image.open(parent + 'imageset0_camera33_green0.jpg').convert('L')
blue33 = Image.open(parent + 'imageset0_camera33_blue.jpg').convert('L')
out33 = Image.merge("RGB", (red33, green33, blue33))
out33.save("img33.jpg", optimize=True)

red34 = Image.open(parent + 'imageset0_camera34_red.jpg').convert('L')
green34 = Image.open(parent + 'imageset0_camera34_green0.jpg').convert('L')
blue34 = Image.open(parent + 'imageset0_camera34_blue.jpg').convert('L')
out34 = Image.merge("RGB", (red34, green34, blue34))
out34.save("img34.jpg", optimize=True)

red35 = Image.open(parent + 'imageset0_camera35_red.jpg').convert('L')
green35 = Image.open(parent + 'imageset0_camera35_green0.jpg').convert('L')
blue35 = Image.open(parent + 'imageset0_camera35_blue.jpg').convert('L')
out35 = Image.merge("RGB", (red35, green35, blue35))
out35.save("img35.jpg", optimize=True)

red36 = Image.open(parent + 'imageset0_camera36_red.jpg').convert('L')
green36 = Image.open(parent + 'imageset0_camera36_green0.jpg').convert('L')
blue36 = Image.open(parent + 'imageset0_camera36_blue.jpg').convert('L')
out36 = Image.merge("RGB", (red36, green36, blue36))
out36.save("img36.jpg", optimize=True)



#delete the old images
lst3 = os.listdir(parent)
for file_name in lst3:
    if file_name.startswith("imageset0_camera"):
        os.remove(os.path.join(parent, file_name))
    if file_name.endswith(".dat"):
        os.remove(os.path.join(parent, file_name))
    if file_name.endswith(".json"):
        os.remove(os.path.join(parent, file_name))
    if file_name.endswith(".v2"):
        os.remove(os.path.join(parent, file_name))
    if file_name.endswith(".txt"):
        os.remove(os.path.join(parent, file_name))
    if file_name.endswith(".zip"):
        os.remove(os.path.join(parent, file_name))


input('DONE ----- Press ENTER to exit') #change raw_input to input when running on Python > 3
