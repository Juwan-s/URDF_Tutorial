import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/juwan/URDF_Tutorial/urdf_ws/install/urdf_test'
