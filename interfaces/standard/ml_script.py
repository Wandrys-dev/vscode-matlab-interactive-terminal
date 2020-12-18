# Copyright (c) 2020 Aurelien Pommel

from matlab_interface import MatlabInterface
import sys

matlab = MatlabInterface()
# Run the initial script given in arg
matlab.run_script(sys.argv[1])
matlab.interactive_loop()
