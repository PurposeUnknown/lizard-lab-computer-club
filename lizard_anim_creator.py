import os
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree, Element

# Animation files require Synfig Studio actually render / view assets, but can be opened in any code editor

base_dir = '[BASE_DIRECTORY_HERE]'

# Import master animation file with all assets
animation = input("Enter the base animation: ")

def asset_toggler(liz_num):
    '''For a given lizard number (liz_num),
    iterate through the master animation file and check each layer - 
    if a layer matches an asset in the lizard's folder, toggle the layer view to "true"'''

    tree = ET.parse(animation)
    root = tree.getroot()
    lizard_dir = base_dir + f"/{liz_num}"

    # Check if a lizard directory is valid first
    if os.path.isdir(lizard_dir):
        lizard_files = os.listdir(lizard_dir)
        for layer in root.iter('layer'):
            if (layer.attrib['type'] == 'group') and (layer.attrib['desc'] in lizard_files):
                layer.attrib['active'] = "true" 

        # Write to animation file     
        tree.write(f'LIZARD_ANIM_{liz_num}.sif', encoding='UTF-8', xml_declaration='True')
        
        # Reset all animation layers to "false" to prep for the next lizard
        for layer in root.iter('layer'):
            if (layer.attrib['type'] == 'group') and (layer.attrib['active'] == "true") and (layer.attrib.get('desc', None) != None):
                layer.attrib['active'] = "false" 

for number in range(1, 5001):
    asset_toggler(number)