import rclpy
from rclpy.node import Node
from peron_msgs.msg import Query

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Person, "person", 10)
n = 0


def cb(request, response):
    if request.name == "あげたこ":
        response.age = 20
    else:
        response.age = 255

    return response
def main():
    srv = node.create_service(Query, "query", cb)
    rclpy.spin(node)

