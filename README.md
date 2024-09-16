# Nuke_Split_Channels
split the channels of your shot


To use this tool, you must save the file split_nodes_v2.py in the root folder of Nuke.xx/Plugins.


Inside the houdini add a NoOp-node and right click on the parameters panel ‘manage user knobs’ and add a ‘Python Button’.

![image](https://github.com/user-attachments/assets/0800839c-929e-4270-bae9-b6318ffe119e)

inside the button we can add the .py code, because if in the button script if you import the module, the tool will only work once until you restart Nuke, due to the characteristics of working windows inside Nuke. 
