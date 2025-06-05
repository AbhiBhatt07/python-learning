import pyshorteners
import pyperclip

def shorten_url(long_url):
    shortener = pyshorteners.Shortener()

    short_url = shortener.tinyurl.short(long_url)
    print(short_url)

    return short_url

user_url = input("Enter your URL: ")

try: 
    short_url = shorten_url(user_url)
    print("Shortend URL: ", short_url)

    pyperclip.copy(short_url)
    print("Shortend URL copied to clipboard.")

except Exception as e: 
    print("❌ An error occurred:", e)