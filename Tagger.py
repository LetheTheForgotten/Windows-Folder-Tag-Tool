##-- imports --##
import argparse
import os
import re
import ctypes

##-- global variables --##
tag_header =r"[{F29F85E0-4FF9-1068-AB91-08002B27B3D9}]"
tag_prefix =r"Prop5=31,"
regex = tag_prefix+'.*\n'

def assign_tags(directory):
    #check if tags.txt is in directory
    if(args.tags in os.listdir(directory)):
        #read tags.txt
        tags = open(directory+"\\"+args.tags,'r')
        tags_read = tags.read()
        tags.close()
        tags_read=tags_read.strip()
        tags_read=tags_read.replace(args.seperator,";")
        print(tags_read)
        update_desktop_ini(directory,tags_read)
    else:
        print(directory+" has no tags file!")
    return

def update_desktop_ini(directory,inserted_tags):
    #generate desktop.ini path
    desktop_ini_path =  directory+"\\Desktop.ini"
    # Set data string
    data =""
    # Check if desktop.ini already exists
    if os.path.exists(desktop_ini_path):
        desktop = open(desktop_ini_path,"r")
        data = desktop.read()
        desktop.close()
        os.remove(desktop_ini_path)

        #check if it already contains tags
        if (tag_header in data):
            #append or overwrite?
            if(args.append):
                existing_tags=re.search(regex,s).group(1)+';'
            else:
                existing_tags=""
            data = re.sub(regex,tag_prefix+existing_tags+inserted_tags+'\n',data)
        #if no tags append to data
        else:
            data+=("\n "+ tag_header +
                   "\n "+ tag_prefix + inserted_tags)
    #if it does not exist, generate it
    else:
        data = (tag_header +
                   "\n "+ tag_prefix + inserted_tags)
    # write desktop.ini
    desktop = open(desktop_ini_path,"w")
    desktop.write(data)
    desktop.close()

    # set file to hidden
    check = ctypes.windll.kernel32.SetFileAttributesW(desktop_ini_path,0x02)
    if(not check):
        print(desktop_ini_path + " not set hidden")

    return

##-- setup --##

parser = argparse.ArgumentParser(description="takes text in given txt folder and assigns them as tags to folder")

parser.add_argument("input",
                    help="topmost folder to add tags to",
                    type=str)

parser.add_argument("--tags",
                    help=("name of file in folder that contains tags." +
                          "default is tags.txt."),
                          default="tags.txt",
                          type=str
                          )

parser.add_argument("--seperator",
                    help=("Character in tags.txt that indicates a new tag." +
                          "Default is newline."+
                          "Cannot be a semicolon(;)."),
                    default="\n",
                    type=str)

parser.add_argument("--append",
                    help="appends found tags to existing ones rather than overwriting them",
                    action="store_true")


args=parser.parse_args()

##-- Main --##

for root, dirs, files in os.walk(args.input):
    for folder in dirs:
        assign_tags(os.path.join(root,folder))
return
