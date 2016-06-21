import os
import shutil

for root, dirs, files in os.walk("."):
	for file in files:
		if file.endswith(".png"):
			s = root[root.rfind("/")+1:]
			s1 = s + "_" + file
			print s1 
			shutil.move(os.path.join(root,file), "./" + s1) 
