import random
import time

# 코드 설명
# Sender는 데이터를 보내고, 올바른 ACK가 올 때까지 반복 전송합니다.
#
# Receiver는 올바른 패킷만 수락하고, 손상되거나 중복된 패킷은 무시하거나 이전 ACK를 보냅니다.
#
# LOSS_PROB와 CORRUPT_PROB로 네트워크 오류를 시뮬레이션합니다.
#
# Checksum으로 패킷 오류 여부를 판별합니다.

# [Sender] 📤 'Hello' 전송 (seq: 0)
# [Receiver] ❌ 패킷 손실됨
# [Sender] ⏱️ ACK 손실 - 재전송
# 
# [Sender] 📤 'Hello' 전송 (seq: 0)
# [Receiver] ✅ 'Hello' 수신 성공 (seq: 0)
# [Sender] ⚠️ ACK 손상 - 재전송
# 
# [Sender] 📤 'Hello' 전송 (seq: 0)
# [Receiver] ⚠️ 패킷 손상됨 - ACK 재전송
# [Sender] ✅ ACK 수신 완료 (seq: 0)
# 
# [Sender] 📤 'World' 전송 (seq: 1)
# [Receiver] ✅ 'World' 수신 성공 (seq: 1)
# [Sender] ✅ ACK 수신 완료 (seq: 1)
# 
# [Sender] 📤 'rdt3.0' 전송 (seq: 0)
# [Receiver] ✅ 'rdt3.0' 수신 성공 (seq: 0)
# [Sender] ✅ ACK 수신 완료 (seq: 0)
# 
# [Sender] 📤 'Simulation' 전송 (seq: 1)
# [Receiver] ✅ 'Simulation' 수신 성공 (seq: 1)
# [Sender] ✅ ACK 수신 완료 (seq: 1)


# 시뮬레이션 설정
LOSS_PROB = 0.2       # 데이터 손실 확률
CORRUPT_PROB = 0.1    # 데이터 손상 확률

# 도우미 함수
def is_lost():
    return random.random() < LOSS_PROB

def is_corrupt():
    return random.random() < CORRUPT_PROB

# 패킷 클래스
class Packet:
    def __init__(self, data, seq_num):
        self.data = data
        self.seq_num = seq_num
        self.checksum = self.calculate_checksum()

    def calculate_checksum(self):
        return sum(bytearray(self.data.encode('utf-8'))) + self.seq_num

    def is_corrupt(self):
        return self.checksum != self.calculate_checksum()

# 수신자(Receiver)
class Receiver:
    def __init__(self):
        self.expected_seq = 0

    def receive(self, packet):
        if is_lost():
            print("[Receiver] ❌ 패킷 손실됨")
            return None

        if is_corrupt() or packet.is_corrupt():
            print("[Receiver] ⚠️ 패킷 손상됨 - ACK 재전송")
            return Packet("ACK", 1 - self.expected_seq)

        if packet.seq_num == self.expected_seq:
            print(f"[Receiver] ✅ '{packet.data}' 수신 성공 (seq: {packet.seq_num})")
            self.expected_seq = 1 - self.expected_seq
            return Packet("ACK", packet.seq_num)
        else:
            print("[Receiver] ⚠️ 중복 패킷 - 이전 ACK 재전송")
            return Packet("ACK", 1 - self.expected_seq)

# 송신자(Sender)
class Sender:
    def __init__(self):
        self.seq_num = 0

    def send(self, data, receiver):
        while True:
            packet = Packet(data, self.seq_num)
            print(f"\n[Sender] 📤 '{data}' 전송 (seq: {self.seq_num})")
            ack = receiver.receive(packet)

            if ack is None:
                print("[Sender] ⏱️ ACK 손실 - 재전송")
                continue

            if is_corrupt() or ack.is_corrupt():
                print("[Sender] ⚠️ ACK 손상 - 재전송")
                continue

            if ack.seq_num == self.seq_num:
                print(f"[Sender] ✅ ACK 수신 완료 (seq: {ack.seq_num})")
                self.seq_num = 1 - self.seq_num
                break
            else:
                print("[Sender] ⚠️ 잘못된 ACK - 재전송")

# 실행
if __name__ == "__main__":
    sender = Sender()
    receiver = Receiver()

    messages = ["Hello", "World", "rdt3.0", "Simulation"]

    for msg in messages:
        sender.send(msg, receiver)
        time.sleep(1)
