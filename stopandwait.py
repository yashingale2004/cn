import time
import random
class snw:
    def __init__(self, total_frames):
        self.total_frames = total_frames
    def send_frame(self, frame_no):
        print(f"sending frame no {frame_no}")
        time.sleep(random.uniform(0.5,1.5))
    def ack_frame(self, frame_no):
        if random.random()>0.1:
            print(f"recieved ack for frame{frame_no}")
            return True
        else:
            print(f"error while ack, resending...")
            return False
    def start(self):
        for frame in range(self.total_frames):
            while True:
                self.send_frame(frame)
                if self.ack_frame(frame):
                    break
if __name__ == "__main__":
    protocol = snw(total_frames=5)
    protocol.start()