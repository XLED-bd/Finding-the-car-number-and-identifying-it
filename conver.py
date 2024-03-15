import xml.etree.ElementTree as ET
import os

def convert_annotation():
    path_txt = "./data/train/image/"
    path_xml = "./data/annotations__/"

    for file_name in os.listdir(path_xml):  
        xml_file = ET.parse(path_xml + file_name)
        list_object = xml_file.findall("object")

        height = xml_file.find("size/height").text
        width = xml_file.find("size/width").text

        with open(path_txt + "Cars" + file_name.replace("Cars", "").replace(".xml", "")
                    + ".txt", 'w') as f:
             for object in range(0, len(list_object)): 
                xmin = list_object[object].find("bndbox/xmin").text
                ymin = list_object[object].find("bndbox/ymin").text
                xmax = list_object[object].find("bndbox/xmax").text
                ymax = list_object[object].find("bndbox/ymax").text
                
                b_center_x = (float(xmin) + float(xmax)) / 2.0
                b_center_y = (float(ymin) + float(ymax)) / 2.0
                b_width = (float(xmax) - float(xmin))
                b_height = (float(ymax) - float(ymin))

                b_center_x /= float(width)
                b_center_y /= float(height)
                b_width /= float(width)
                b_height /= float(height)
                
                f.write("0 ")
                f.write(str(b_center_x) + " ")
                f.write(str(b_center_y) + " ")
                f.write(str(b_width) + " " )
                f.write(str(b_height) + " " + '\n')


convert_annotation()