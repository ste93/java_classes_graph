import os
import pydot
from IPython.display import Image, display
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def get_list_of_files(dir_name):
    # create a list of file and sub directories 
    # names in the given directory
    G = pydot.Dot(graph_type="digraph")
    list_of_file = os.listdir(dir_name)
    all_files = list()
    # node = pydot.Node()
    # Iterate over all the entries
    for entry in list_of_file:
        # Create full path
        full_path = os.path.join(dir_name, entry)
        node = pydot.Node(entry, style='filled', fillcolor='green')
        G.add_node(node)
        print(entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(full_path):
            all_files = all_files + get_list_of_files(full_path)
        else:
            all_files.append(full_path)

    im = Image(G.create_png())
    display(im)
    return all_files


# Get the list of all files in directory tree at given path

G = pydot.Dot(graph_type="digraph")
node = pydot.Node(r"C:\Users\ste\Documents\sd\tucson", style='filled', fillcolor='green')
G.add_node(node)
im = Image(G.create_png())
display(im)


#list_of_files = get_list_of_files(r"C:\Users\ste\Documents\sd\tucson")
"""
listOfFilesUpdated = []
listOfPaths = []
for fileLocal in list_of_files:
    if fileLocal.split(".")[-1] == "java" and "test" not in fileLocal:
        listOfFilesUpdated.append(fileLocal)
        listOfPaths.append(fileLocal.replace("\\", "."))


for fileLocal in listOfFilesUpdated:
    if fileLocal.split(".")[-1] == "java" and "test" not in fileLocal:
        print(fileLocal)
        fileOpened = open(fileLocal, "r")
        linesRead = fileOpened.readlines()
        for line in linesRead:
            if line.split(" ")[0] == "import":  # or line.split(" ")[0] == "package":
                print(line)
        fileOpened.close()
"""