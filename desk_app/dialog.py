import tkinter.messagebox as mb

ans = mb.askyesno("質問", "ラーメンは好き？")
if ans == True:
    mb.showinfo("同意", "だよね〜")
else:
    mb.showinfo("マジ？", "義務教育受けた？")