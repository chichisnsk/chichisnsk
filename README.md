import tkinter as tk
from tkinter import messagebox
import random

class BirthdayGiftRecommendationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("생일 선물 추천 프로그램")

        # 레이블
        self.label = tk.Label(root, text="생일 선물 추천 프로그램", font=("Helvetica", 16))
        self.label.pack(pady=10)

        # 추천 버튼
        self.recommend_button = tk.Button(root, text="추천받기", command=self.recommend_gift)
        self.recommend_button.pack(pady=20)

        # 결과 표시 레이블
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def recommend_gift(self):
        # 추천 선물 리스트
        gift_list = ["화장품 세트", "도서", "음악 이벤트 티켓", "음식 기프티콘", "향수", "뷰티", "커피 머신", "여행 상품권"]

        # 무작위로 선물 선택
        recommended_gift = random.choice(gift_list)

        # 결과 레이블 업데이트
        self.result_label.config(text=f"추천 선물: {recommended_gift}")

        # 팝업 메시지로도 표시
        messagebox.showinfo("생일 선물 추천", f"추천 선물: {recommended_gift}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BirthdayGiftRecommendationApp(root)
    root.mainloop()
