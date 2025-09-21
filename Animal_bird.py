# Approach 1:Import modules to another module
import A
import B
# import A
# import B
#
# A.fly()  #  Calls animal fly and colour methods
# A.colour()
#
# B.fly() #  Calls bird fly and colour methods
# B.colour()



# Approach 2:

from A import fly,colour
# from B import fly,colour
#
# fly()  #output is from bird calling module, as it takes latest calling
# colour()

# Approach 2A :

# from A import *
#
# fly()
# colour()
#
# from B import *
#
# fly()
# colour()