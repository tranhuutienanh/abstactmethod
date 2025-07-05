from abc import ABC, abstractmethod

class MediaPlayer(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class MP3Player(MediaPlayer):
    def play(self):
        print("Đang phát nhạc MP3...")

    def pause(self):
        print("Tạm dừng nhạc MP3.")

    def stop(self):
        print("Dừng nhạc MP3.")


class VideoPlayer(MediaPlayer):
    def play(self):
        print("Đang phát video...")

    def pause(self):
        print("Tạm dừng video.")

    def stop(self):
        print("Dừng video.")


class StreamingPlayer(MediaPlayer):
    def play(self):
        print("Đang phát nội dung trực tuyến...")

    def pause(self):
        print("Tạm dừng nội dung trực tuyến.")

    def stop(self):
        print("Dừng nội dung trực tuyến.")


def media_menu():
    players = {
        "1": MP3Player(),
        "2": VideoPlayer(),
        "3": StreamingPlayer()
    }

    print("Chọn loại media:")
    print("1. MP3 Player")
    print("2. Video Player")
    print("3. Streaming Player")
    loai = input("Nhập lựa chọn (1-3): ")

    if loai not in players:
        print("❌ Lựa chọn không hợp lệ.")
        return

    player = players[loai]

    while True:
        print("\n--- MENU ĐIỀU KHIỂN ---")
        print("1. Play")
        print("2. Pause")
        print("3. Stop")
        print("4. Thoát")
        thao_tac = input("Chọn thao tác (1-4): ")

        if thao_tac == "1":
            player.play()
        elif thao_tac == "2":
            player.pause()
        elif thao_tac == "3":
            player.stop()
        elif thao_tac == "4":
            print("Thoát khỏi trình phát.")
            break
        else:
            print("Lựa chọn không hợp lệ.")

media_menu()