from collections import deque
import threading
import time

class ordering_system:
    def __init__(self):
        self.box = deque()
    def order(self, item_list):
        for item in item_list:
            time.sleep(0.5)
            self.box.appendleft(item)
            print("Your order {:s} has been received".format(item))
    def serve(self):
        while len(self.box)>0:
            time.sleep(2)
            print("Your Order {:s} is served".format(self.box.pop()))

system = ordering_system()
orders = ['pizza','samosa','pasta','biryani','burger','dosa','idly','filter coffee', 'aaloo briyani']
order_thread = threading.Thread(target=system.order, args=(orders,))
serve_thread = threading.Thread(target=system.serve)

order_thread.start()
time.sleep(1)
serve_thread.start()

order_thread.join()
serve_thread.join()

