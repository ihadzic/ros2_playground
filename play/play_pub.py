import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from . import config


class MyPlayNode(Node):

    def __init__(self):
        super().__init__('play_pub')
        self.publisher = self.create_publisher(String, 'topic',
                                               config.small_queue_size)
        self.timer = self.create_timer(config.heartbeat_period,
                                       self.timer_callback)
        self.i = 0
        self.log = self.get_logger()

    def timer_callback(self):
        self.log.info('logging something for the fun of it')
        msg = String(data='shit happened {}'.format(self.i))
        self.publisher.publish(msg)
        self.i += 1


def main():
    rclpy.init()
    my_pub = MyPlayNode()
    rclpy.spin(my_pub)
    my_pub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
