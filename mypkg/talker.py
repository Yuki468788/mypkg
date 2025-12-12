import rclpy
from rclpy.node import Node
from person_msgs.msg import Int16

class Talker():
    def __init__(self,nh):
        self.pub = node.create_publisher(Int16 , "countup" , 10)
        self.n = 0
        nh.create_timer(0.5 , cb)
    def cb(self):
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        self.n += 1    

def main(): 
    rclpy.init()
    node = Node("talker")
    talker = Talker()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
