# Adapted for numpy/ma/cdms2 by convertcdms.py
"""
# Template Boxes and Lines (Pbl) module
"""
##########################################################################
#                                                                               #
# Module:       Template Boxes and Lines (Pbl) module                           #
#                                                                               #
# Copyright:    2000, Regents of the University of California                   #
#               This software may not be distributed to others without          #
#               permission of the author.                                       #
#                                                                               #
# Author:       PCMDI Software Team                                             #
#               Lawrence Livermore NationalLaboratory:                          #
#               support@pcmdi.llnl.gov                                          #
#                                                                               #
# Description:  Python command wrapper for VCS's template boxes and lines       #
#                                                                               #
# Version:      4.0                                                             #
#                                                                               #
##########################################################################
#
#
#
import VCS_validation_functions
import vcs
#############################################################################
#                                                                           #
# Template text (Pbl) Class.                                                #
#                                                                           #
#############################################################################


class Pbl(vcs.bestMatch):

    """
    The Template text object allows the manipulation of line type, width, and color index.

    This class is used to define a line table entry used in VCS, or it
    can be used to change some or all of the line attributes in an
    existing line table entry.

    :Example:

    ::

    # Basic Usage Overview:

    a=vcs.init()
    # Show predefined line objects
    a.show('line')
    # Updates the VCS Canvas at user's request
    a.update()

    #For mode:
    #   If 1, then automatic update.
    #   If 0,use update function to update VCS canvas
    a.mode=1

    #To Create a new instance of line use:
    #    Copies content of 'red' to 'new'
    ln=a.createline('new','red')
    #    Copies content of 'default' to 'new'
    ln=a.createline('new')

    #To Modify an existing line use:
    ln=a.getline('red')

    # Will list all the line attribute values
    ln.list()
    # Range from 1 to 256
    ln.color=100
    # Range from 1 to 300
    ln.width=100

     #Specify the line type:
     # Same as ln.type=0
     ln.type='solid'
     # Same as ln.type=1
     ln.type='dash'
     # Same as ln.type=2
     ln.type='dot'
     # Same as ln.type=3
     ln.type='dash-dot'
     # Same as ln.type=4
     ln.type='long-dash'
    """
    ##########################################################################
    #                                                                           #
    # Initialize the line attributes.                                           #
    #                                                                           #
    ##########################################################################
    __slots__ = [
        "priority",
        "x1",
        "x2",
        "y1",
        "y2",
        "line",
        "member",
        "_priority",
        "_x1",
        "_x2",
        "_y1",
        "_y2",
        "_line"]

    def __init__(self, member):
        #    def __init__(self, template, member=None):
        #                                                         #
        ###########################################################
        # Initialize the line class and its members               #
        # The getPblmember function retrieves the values of the    #
        # line members in the C structure and passes back the     #
        # appropriate Python Object.                              #
        ###########################################################
        #                                                         #
        self.member = member
        self.priority = 0
        self.line = "default"
        if member == "box1":
            self.priority = 1
            self.x1 = 0.0500000007451
            self.y1 = 0.259999990463
            self.x2 = 0.949999988079
            self.y2 = 0.860000014305
        elif member == "box2":
            self.x1 = 0.
            self.y1 = 0.300000011921
            self.x2 = 0.920000016689
            self.y2 = 0.879999995232
        elif member == "box3":
            self.x1 = 0.
            self.y1 = 0.319999992847
            self.x2 = 0.910000026226
            self.y2 = 0.860000014305
        elif member == "box4":
            self.x1 = 0.
            self.y1 = 0.
            self.x2 = 0.
            self.y2 = 0.
        elif member == "line1":
            self.x1 = 0.0500000007451
            self.y1 = 0.560000002384
            self.x2 = 0.949999988079
            self.y2 = 0.560000002384
        elif member == "line2":
            self.x1 = .5
            self.y1 = 0.259999990463
            self.x2 = .5
            self.y2 = 0.860000014305
        elif member == "line3":
            self.x1 = 0.
            self.y1 = 0.52999997139
            self.x2 = 0.899999976158
            self.y2 = 0.52999997139
        elif member == "line4":
            self.x1 = 0.
            self.y1 = 0.990000009537
            self.x2 = 0.899999976158
            self.y2 = 0.990000009537

    ##########################################################################
    #                                                                           #
    # Set template text  attributes.                                            #
    #                                                                           #
    ##########################################################################
    priority = VCS_validation_functions.priority
    x1 = VCS_validation_functions.x1
    x2 = VCS_validation_functions.x2
    y1 = VCS_validation_functions.y1
    y2 = VCS_validation_functions.y2
    line = VCS_validation_functions.line

    ##########################################################################
    #                                                                           #
    # List out template text members (attributes).                              #
    #                                                                           #
    ##########################################################################
    def list(self):
        print "member = ", self.member
        print "     priority =", self.priority
        print "     x1 =", self.x1
        print "     y1 =", self.y1
        print "     x2 =", self.x2
        print "     y2 =", self.y2
        print "     line =", self.line


##########################################################################
#        END OF FILE								#
##########################################################################
