import len as len_
import sys
import time
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("-o",type=str,help="Output path",dest="output")
parser.add_argument("-cr",type=int,help="Color stop interval",dest="color_range",default=None)
parsedargs=parser.parse_args()
colorRange:int=16 if not parsedargs.color_range else parsedargs.color_range
__NULL=b"\0"
def addNewLines(f):...
frameworkequivs = {
    # Display property
    "d:{}": lambda x, mode: f".d\\:{x}{{display:{mode}}}".encode(),

    # Background color
    "bg:{}": lambda x, color: f".bg\\:{x}{{background-color:{color}}}".encode(),

    # Text color
    "c:{}": lambda x, color: f".c\\:{x}{{color:{color}}}".encode(),

    # Opacity
    "o:{}": lambda x, opacity: f".o\\:{x}{{opacity:{opacity}}}".encode(),

    # Padding
    "p:{}": lambda x, size: f".p\\:{x}{{padding:{size}}}".encode(),

    # Margin
    "m:{}": lambda x, size: f".m\\:{x}{{margin:{size}}}".encode(),

    # Border-radius
    "rounded:{}": lambda x, radius: f".rounded\\:{x}{{border-radius:{radius}}}".encode(),

    # Font size
    "text:{}": lambda x, size: f".text\\:{x}{{font-size:{size}}}".encode(),

    # Font weight
    "font:{}": lambda x, weight: f".font\\:{x}{{font-weight:{weight}}}".encode(),

    # Width
    "w:{}": lambda x, width: f".w\\:{x}{{width:{width}}}".encode(),

    # Height
    "h:{}": lambda x, height: f".h\\:{x}{{height:{height}}}".encode(),

    # Flex direction
    "flex-dir:{}": lambda x, direction: f".flex-dir\\:{x}{{flex-direction:{direction}}}".encode(),

    # Justify content (for flexbox)
    "justify:{}": lambda x, value: f".justify\\:{x}{{justify-content:{value}}}".encode(),

    # Align items (for flexbox)
    "items:{}": lambda x, value: f".items\\:{x}{{align-items:{value}}}".encode(),

    # Z-index
    "z:{}": lambda x, value: f".z\\:{x}{{z-index:{value}}}".encode(),

    # Cursor style
    "cursor:{}": lambda x, style: f".cursor\\:{x}{{cursor:{style}}}".encode(),

    # Box shadow
    "shadow:{}": lambda x, shadow: f".shadow\\:{x}{{box-shadow:{shadow}}}".encode(),
    "mxh:{}":lambda x,mxh:f".mxh\\:{x}{{max-height:{mxh}}}".encode(),
    "mnh:{}":lambda x,mnh:f".mnh\\:{x}{{min-height:{mnh}}}".encode(),
    "mxw:{}":lambda x,mxw:f".mxh\\:{x}{{max-width:{mxw}}}".encode(),
    "mnw:{}":lambda x,mnw:f".mnh\\:{x}{{min-width:{mnw}}}".encode(),
    
}
units=["px","vh","vw","rem","em","%"]
isTerminated=False
if not parsedargs.output:
    raise ValueError("-o must be filled!")
try:
    with open(parsedargs.output,"wb") as f:
        for i in range(101):
            #f.write(f"/*region:size({i})*/\n")
            f.write(frameworkequivs["o:{}"](str(i)+"\\%",f"{i}%"))

            f.write(frameworkequivs["z:{}"](i,i))

            for unit in units:
                funit=unit if unit not in ["%"] else f"\\{unit}"
                f.write(frameworkequivs["w:{}"](f"{i}{funit}",f"{i}{unit}"))
                f.write(frameworkequivs["h:{}"](f"{i}{funit}",f"{i}{unit}"))

                f.write(frameworkequivs["text:{}"](f"{i}{funit}",f"{i}{unit}"))

                for o in ["mx","mn"]:
                    for d in ["h","w"]:
                        f.write(frameworkequivs[o+d+":{}"](f"{i}{funit}",f"{i}{unit}"))
            time.sleep(.01)
            print(f"{"\\" if i%3==0 else "/"}",end="\r")
            #f.write(f"/*endregion:size({i})*/\n")
        memo={}
        for i in range(0,256,colorRange):
            #f.write(f"/*region:red:{i};*/\n")
            for o in range(0,256,colorRange):
            #    f.write(f"/*region:red:{i};green:{o};*/\n")
                for e in range(0,256,colorRange):
                    if(memo.get(f"r{i},g{o},b{e}")):
                        continue
            #        f.write(f"/*region:red:{i};green:{o};blue:{e}*/\n")
                    f.write(frameworkequivs["c:{}"](f"rgb\\({i}\\,{o}\\,{e}\\)",f"rgb({i},{o},{e})"))

                    f.write(frameworkequivs["bg:{}"](f"rgb\\({i}\\,{o}\\,{e}\\)",f"rgb({i},{o},{e})"))
            print(f"{(i//255)*100}",end="\r")
            #        f.write(f"/*endregion:red:{i};green:{o};blue:{e}*/\n")
            #    f.write(f"/*endregion:red:{i};green:{o};*/\n")
            #f.write(f"/*endregion:red:{i};*/\n")
        f.write(b".f\\:edit{-webkit-user-modify: read-write;}")
        len_.measure(parsedargs.output)
        isTerminated=True
finally:
    if(not isTerminated):
        print("\033[31m Error encountered:string was not terminated\033[0m")
    else:
        print("File created successfully!")
