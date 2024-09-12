def minify_cssText(w:str):
    return w.strip("\n")
def minify_cssFile(p):
    with open(p,"w") as f:
        f.write(minify_cssText(f.read()))