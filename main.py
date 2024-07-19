from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

chrome_options.add_argument("--headless=new") # for Chrome >= 109

app = Flask(__name__)


# this is the first page people will see upon log-in
@app.route('/')
def index():
    name = "index"
    return render_template('index.html', name=name)


# this is a secondary page

@app.route('/about')
def about():
    name = "about"
    return render_template('about.html', name=name)


@app.route('/subcount', methods=['GET', 'POST'])
def subcount():
    name = "subcount"
    title = "subs"
    message = "has"
    if request.method == "POST":
        channel_name = str('http://www.youtube.com/@' + str(request.form["cn"]))
        driver = webdriver.Chrome(options=chrome_options)  # Optional argument, if not specified will search path.
        driver.get(channel_name)


        try: subscriberCount = driver.find_element("xpath",
                                              '//*[@id="page-header"]/yt-page-header-renderer/yt-page-header-view-model/div/div[1]/div/yt-content-metadata-view-model/div[2]/span[1]')
        except:
            return render_template('reddit.html', name=name, title=title, error="Sorry bro couldn't find it, remember - no @")


        subCount = subscriberCount.text
        print(subCount)
        driver.quit()

        return render_template('subcount.html', name=name, title=title, subs=subCount, message=message, bob=str(request.form["cn"]))
    else:
        return render_template('subcount.html', name=name, title=title)


if __name__ == '__main__':
    app.run()
