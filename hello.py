import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Pillow 라이브러리 사용
import random

class BirthdayGiftRecommendationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("생일 선물 추천 프로그램")

        # 레이블
        self.label = tk.Label(root, text="생일 선물 추천 프로그램", font=("Helvetica", 16))
        self.label.pack(pady=10)

        # 이미지 딕셔너리
        self.image_dict = {
            "화장품 세트": "화장품.png",
            "도서": "도서",
            "음악 이벤트 티켓": "음악.png",
            "음식 기프티콘": "음식.png",
            "향수": "향수.png",
            "커피 머신": "커피.png",
            "여행 상품권": "여행.png"
        }

        # 추천 버튼
        self.recommend_button = tk.Button(root, text="추천받기", command=self.recommend_gift)
        self.recommend_button.pack(pady=20)

        # 이미지 표시 레이블
        self.image_label = tk.Label(root, text="")
        self.image_label.pack(pady=10)

        # 결과 표시 레이블
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def recommend_gift(self):
        # 추천 선물 리스트
        gift_list = list(self.image_dict.keys())

        # 무작위로 선물 선택
        recommended_gift = random.choice(gift_list)

        # 결과 레이블 업데이트
        self.result_label.config(text=f"추천 선물: {recommended_gift}")

        # 이미지 표시 레이블 업데이트
        image_path = self.image_dict[recommended_gift]
        image = Image.open(image_path)
        image = image.resize((100, 100), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo  # 참조를 유지하기 위해 필요

        # 팝업 메시지로도 표시
        messagebox.showinfo("생일 선물 추천", f"추천 선물: {recommended_gift}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BirthdayGiftRecommendationApp(root)
    root.mainloop()

