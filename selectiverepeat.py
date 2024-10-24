import time
import random
class SelectiveRepeat:
    def __init__(self, window_size, total_frames, simulate_delay=True):
        self.window_size = window_size
        self.total_frames = total_frames
        self.next_frame_to_send = 0
        self.acks = [False] * total_frames
        self.simulate_delay = simulate_delay
    def send_frame(self, frame):
        print(f"Sending frame {frame}")
        if self.simulate_delay:
            time.sleep(random.uniform(0.5, 1.5)) 
    def receive_ack(self, frame):
        if random.random() > 0.1:  
            print(f"Received ACK for frame {frame}")
            return True
        else:
            print(f"ACK for frame {frame} lost.")
            return False
    def start(self):
        while self.next_frame_to_send < self.total_frames:
            for i in range(self.window_size):
                frame_to_send = self.next_frame_to_send + i
                if frame_to_send < self.total_frames and not self.acks[frame_to_send]:
                    self.send_frame(frame_to_send)
            for i in range(self.window_size):
                frame_to_check = self.next_frame_to_send + i
                if frame_to_check < self.total_frames and not self.acks[frame_to_check]:
                    if self.receive_ack(frame_to_check):
                        self.acks[frame_to_check] = True
            while self.next_frame_to_send < self.total_frames and self.acks[self.next_frame_to_send]:
                self.next_frame_to_send += 1

if __name__ == "__main__":
    protocol = SelectiveRepeat(window_size=3, total_frames=10)
    protocol.start()
