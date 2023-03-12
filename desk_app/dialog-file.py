import tkinter.filedialog as fd

path = fd.askopenfilename(title = "処理対象のファイルを指定してください", filetypes=[('PNG', '.png')])
print(path)