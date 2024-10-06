# So You Want To Organize Your Folders?
Then let me introduce you to: the windows folder tag.

A poorly documented, basically unused feature of windows that lets you tag folders and some media files.

This tool is a Python Based CLI interface that lets you assign tags to folders en masse by defining tags in a text file within the folder.

As a forewarning the tagging system built into windows is incredibly basic, if you want anything more than being able to group folders by a tag you should look for something else.

This has only been tested on windows 10.

# Prerequisites:
> python
> https://www.python.org/

# inputs:

|input|description|
|------|----------|
|input INPUT|topmost folder to add tags to. Required|
|--tags TAG|name of file in folder that contains tags. Default is tags.txt|
|--seperator SEPERATOR|Character in tags.txt that indicates a new tag. Default is newline(\n). Cannot be a semicolon|
|--append|appends found tags to existing ones rather than overwriting them|

