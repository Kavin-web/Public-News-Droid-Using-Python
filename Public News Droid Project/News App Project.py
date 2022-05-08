import requests
import tkinter as tk


def getNews():
    api_key = "b6df8ae13cff41e38a5734ec180cd6cb"
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey="+api_key
    news = requests.get(url).json()

    articles = news["articles"]

    my_articles = []
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])

    for i in range(10):
        my_news = my_news + str(i+1) + ". " + my_articles[i] + "\n" + "\n"

    label.config(text = my_news)



canvas = tk.Tk()
canvas.geometry("600x900")
canvas.title("News App")

heading = tk.Label(canvas,text="Today's news",font=("Arial", 30), justify = "left")
heading.pack(pady = 20)



label = tk.Label(canvas, font = 18, justify = "left")
label.pack(pady = 20)

button = tk.Button(canvas, font = 24, text = "Reload", command = getNews)
button.pack(pady = 20)

getNews()

canvas.configure(bg='white')

canvas.mainloop()