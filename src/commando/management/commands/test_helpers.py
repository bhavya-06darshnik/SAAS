import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..")))


import helpers

print("Helpers module loaded!")
print("Available attributes:", dir(helpers))
