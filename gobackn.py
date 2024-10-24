import time
import random
class gbn:
    def __init__(self, window_size, total_frames):
        self.total_frames = total_frames
        self.window_size = window_size
        self.nextframetosend = 0
    def send_frame(self, frame_no):
        print(f"sending frame no {frame_no}")
        time.sleep(random.uniform(0.5,1.5))
    def ack_frame(self, frame_no):
        if random.random()>0.1:
            print(f"recieved ack for frame{frame_no}")
            return True
        else:
            print(f"error while ack {frame_no}, resending {frame_no}...")
            return False
    def start(self):
        while self.nextframetosend < self.total_frames:
            for i in range (self.window_size):
                if self.nextframetosend + i < self.total_frames:
                    self.send_frame(self.nextframetosend+i)
            for i in range (self.window_size):
                if self.nextframetosend + i < self.total_frames:
                    ack_recieved = self.ack_frame(self.nextframetosend + i)
                    if not ack_recieved:
                        self.nextframetosend +=i
                        break
            else:
                self.nextframetosend += self.window_size
if __name__ == "__main__":
    protocol = gbn(window_size=3, total_frames=10)
    protocol.start()