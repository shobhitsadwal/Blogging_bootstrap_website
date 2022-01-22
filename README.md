# Blogging_bootstrap_website
A full functional website for Blog writing  by using Bootstrap ,flask , Python (/SCALABLE)

full frontend and backend integration project . 


<a href="https://ibb.co/Zd6wNDY"><img src="https://i.ibb.co/Nx6k7Bm/Screenshot-23.png" alt="Screenshot-23" border="0"></a>
## the above image is the infotainer.com
## the below image is the content in the website
<a href="https://ibb.co/8NWZxMp"><img src="https://i.ibb.co/fqhwNM5/Screenshot-24.png" alt="Screenshot-24" border="0"></a>

# Primary Aim and objectives of this project 
 The main aim of this project is making a blogging webiste that contains the blog that we have made and publishing the blogs online. The website that we have created is called as
 **infotainer.com**. 
 *The website is worked on being deployed on the internet and you may experience some problems* 
 
 about infotainer- 
 
 Infotainer.com brings you a platform where a user can write their own blogs which is specially for the digital genre . 
 
 
# low level documentation 
files to refer -
- main.py

- templates
  - ```index.html```
  - ```about.html```
  - ```footer.html```
  - ```contact.html```
  - ```post.html```
  - ```alternate.html```
  
- static
  - ```assets/img```
  - ```css/styles.css```
  - ```js/scripts.js```
  
## code flow and structure 

we have used the combination of Flask Framework, Bootstrap5,HTML along with necessary Jinja templating inside the HTML . The structure follows a basic pattern of the flask framework  where we 
have to make a base module or an app module which is responsible for the whole funtioning of the code . The methods inside the base module is necessary for the functionality of the website. 
We can see the usage  ***@app.route*** in the ```main.py``` file which is commonly a decorator for the method used in Flask Framework. We have also include an **smtplib — SMTP protocol client** that
will send us an email  whenever a user inserts his/her information in the form which is rendered in the ```contact.html``` page . Below is the ```main.py``` module and we will follow tge exact approach 
for understanding this project.

```python
from flask import Flask , render_template,request
import requests
import smtplib

app=Flask(__name__)

email = 'your email is required here'             #you have to enter your email details .
password = "your password is required here"      #you have to enter your password .



@app.route('/')
def hello():
    req=requests.get('https://api.npoint.io/361fcf85637744a9d7e6')
    jso=req.json()
    return render_template('index.html',things=jso)

@app.route('/index.html')
def router():
    req = requests.get('https://api.npoint.io/361fcf85637744a9d7e6')
    jso = req.json()
    return render_template('index.html', things=jso)
@app.route('/about.html')
def abouter():
    return render_template('about.html')
@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/post.html/<int:value>')
def blogger(value):
    req=requests.get('https://api.npoint.io/361fcf85637744a9d7e6')
    jso=req.json()
    return render_template('post.html',numbers=jso,naam=value)

@app.route('/contact.html',methods=['POST'])
def receive_data():
    data = request.form
    # print(data["your_name"])                                              #smtplib — SMTP protocol client used here for sending the email messages
    # print(data["your_email"])
    # print(data["your_phone_number"])
    # print(data["your_email"])
    # return "<h1>Successfully sent your message</h1>"
    if request.method=='POST':
        the_name=request.form['your_name']
        the_phone_number=request.form['your_phone_number']
        the_mail=request.form['your_email']
        the_message=request.form['your_message']
        # zing=f'the name is {the_name} \n the mail is {the_mail} \n the phone_number is {the_phone_number} \n the mail is {the_mail} \n and the message is {the_message}'
        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(user=email, password=password)
        #     connection.sendmail(email, "burnt1997@gmail.com",zing)    #here you have to mention the email adress of the person that you want to send the message
        #
        #     connection.close()

        print(f'the name is {the_name} \n the mail is {the_mail} \n the phone_number is {the_phone_number} \n the mail is {the_mail} \n and the message is {the_message}')

        # return (f'<h1>the name is {the_name} \n the mail is {the_mail} \n the phone_number is {the_phone_number} \n the mail is {the_mail} \n and the message is {the_message} </h1>')
        return render_template('contact-2.html',msg='successfully sent your message ')


```

note - we have accessed the information for rendering inside the templates with the help of **api.npoint**, which is a site that allows the user to write in json formats for and using 
the format as a restful source , for more documentation please read here https://www.npoint.io/ . 

We have seen that the index.html page has both returns from the hello and router function , these funtions are basically returning the api data that we have given in json format . The Json format is basically 
enclosed in a list and we give a variable name to the the list for the iteration in the index.html .

code snippets for index.html 
```html
<!DOCTYPE html>
<html lang="en">

    <body>
    {%include 'header.html'%}
        <!-- Navigation-->
        <!-- Page Header-->
        <header class="masthead" style="background-image: url('./static/assets/img/techo.jpg')">
            <div class="container position-relative px-4 px-lg-5">
                <div class="row gx-4 gx-lg-5 justify-content-center">
                    <div class="col-md-10 col-lg-8 col-xl-7">
                        <div class="site-heading">
                            <h1 style="font-family:helvetica; background-color:grey">Shobhit's Blog</h1>
                            <span class="subheading">A collection of blogs from the latest tech trends</span>
                        </div>
                    </div>
                </div>
            </div>
        </header>
        <!-- Main Content-->
        <div class="container px-4 px-lg-5">
            <div class="row gx-4 gx-lg-5 justify-content-center">
                <div class="col-md-10 col-lg-8 col-xl-7">
                    <!-- Post preview-->
                    {%for i in things:%}
                        <div class="post-preview">
                            <a href="post.html">
                                <h2 class="post-title">{{i['title']}}</h2>
                                <h3 class="post-subtitle">{{i['subtitle']}}</h3>
                            </a>
                            <p class="post-meta">
                                Posted by
                                <a href="{{url_for('blogger',value=i['id'])}}">{{i["author"]}}</a>
                                on {{i["date"]}}
                            </p>
                        </div>
                    {% endfor %}
                    <!-- Divider-->
                    <hr class="my-4" />
                    <!-- Pager-->
                    <div class="d-flex justify-content-end mb-4"><a class="btn btn-primary text-uppercase" href="#!">Older Posts →</a></div>
                </div>
            </div>
        </div>
        <!-- Footer-->
        {%include 'footer.html'%}

        <!-- Bootstrap core JS-->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
        <!-- Core theme JS-->
        <script src="./static/js/scripts.js"></script>
    </body>
</html>
```
 
if we see carefully we see that there is no header and footer present in the index.html , this is beacuse we have used the bootstrap-templating to fill in the header and footer . The use of seperating header and
footer is not necessary but it helps us to modify the changes and not clutter our HTML page . We can see the use of Jinja templating from the code snippet ```{%for i in things:%}``` . Thus the iteration provides 
the structure to the html page to the points of the iterator. 

Now let us consider this code-snippet from the ```main.py```-
```python
@app.route('/post.html/<int:value>')
def blogger(value):
    req=requests.get('https://api.npoint.io/361fcf85637744a9d7e6')
    jso=req.json()
    return render_template('post.html',numbers=jso,naam=value)
    
```

here we see that after taking action on a certain post in our index.html page we see a full blog for the heading , this contains the whole information about the title and this is perhaps the most important HTML page we
render in our website , the way this page works is taking a callable action from the user and then it returns a interger value of the heading . Suppose we have a heading at row 3 , the index value will be row 3rd . 
Thus using Flask and variable adress option we have made possoble to redirect to a page using the index . This in turns return us the exact title and body of the page 

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="" />
        <title>Clean Blog - Start Bootstrap Theme</title>
        <link rel="icon" type="image/x-icon" href="./static/assets/favicon.ico" />
        <!-- Font Awesome icons (free version)-->
        <script src="https://use.fontawesome.com/releases/v5.15.4/js/all.js" crossorigin="anonymous"></script>
        <!-- Google fonts-->
        <link href="https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic" rel="stylesheet" type="text/css" />
        <link href="https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800" rel="stylesheet" type="text/css" />
        <!-- Core theme CSS (includes Bootstrap)-->
        <link href="./static/css/styles.css" rel="stylesheet" />
    </head>
    <body>
        <!-- Navigation-->
        <nav class="navbar navbar-expand-lg navbar-light" id="mainNav">
            <div class="container px-4 px-lg-5">
                <a class="navbar-brand" href="index.html">infotainer.com</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                    Menu
                    <i class="fas fa-bars"></i>
                </button>
                <div class="collapse navbar-collapse" id="navbarResponsive">
                    <ul class="navbar-nav ms-auto py-4 py-lg-0">
                        <li class="nav-item"><a class="nav-link px-lg-3 py-3 py-lg-4" href="index.html">Home</a></li>
                        <li class="nav-item"><a class="nav-link px-lg-3 py-3 py-lg-4" href="about.html">About</a></li>
                        <li class="nav-item"><a class="nav-link px-lg-3 py-3 py-lg-4" href="contact.html">Contact</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        <!-- Page Header-->
        <header class="masthead" style="background-image: url('./static/assets/img/post-bg.jpg')">
            <div class="container position-relative px-4 px-lg-5">
                <div class="row gx-4 gx-lg-5 justify-content-center">
                    <div class="col-md-10 col-lg-8 col-xl-7">
                        <div class="post-heading">
                            {%for i in numbers: %}
                                {%if i[id]==naam:%}

                                    <h1>{{i['title']}}</h1>
                                    <h2 class="subheading">{{i['subtitle']}}</h2>
                                    <span class="meta">
                                        Posted by
                                    <a href="#!">{{i['author']}}</a>
                                    {{i['date']}}
                                    </span>
                                </div>
                            </div>
                        </div>
                    </div>
                </header>
                <!-- Post Content-->
                <article class="mb-4">
                    <div class="container px-4 px-lg-5">
                        <div class="row gx-4 gx-lg-5 justify-content-center">
                            <div class="col-md-10 col-lg-8 col-xl-7">
                                <p>i['full']</p>
        <!--                        <p>Science cuts two ways, of course; its products can be used for both good and evil. But there's no turning back from science. The early warnings about technological dangers also come from science.</p>-->
        <!--                        <p>What was most significant about the lunar voyage was not that man set foot on the Moon but that they set eye on the earth.</p>-->
        <!--                        <p>A Chinese tale tells of some men sent to harm a young girl who, upon seeing her beauty, become her protectors rather than her violators. That's how I felt seeing the Earth for the first time. I could not help but love and cherish her.</p>-->
        <!--                        <p>For those who have seen the Earth from space, and for the hundreds and perhaps thousands more who will, the experience most certainly changes your perspective. The things that we share in our world are far more valuable than those which divide us.</p>-->
        <!--                        <h2 class="section-heading">The Final Frontier</h2>-->
        <!--                        <p>There can be no thought of finishing for ‘aiming for the stars.’ Both figuratively and literally, it is a task to occupy the generations. And no matter how much progress one makes, there is always the thrill of just beginning.</p>-->
        <!--                        <p>There can be no thought of finishing for ‘aiming for the stars.’ Both figuratively and literally, it is a task to occupy the generations. And no matter how much progress one makes, there is always the thrill of just beginning.</p>-->
        <!--                        <blockquote class="blockquote">The dreams of yesterday are the hopes of today and the reality of tomorrow. Science has not yet mastered prophecy. We predict too much for the next year and yet far too little for the next ten.</blockquote>-->
        <!--                        <p>Spaceflights cannot be stopped. This is not the work of any one man or even a group of men. It is a historical process which mankind is carrying out in accordance with the natural laws of human development.</p>-->
        <!--                        <h2 class="section-heading">Reaching for the Stars</h2>-->
        <!--                        <p>As we got further and further away, it [the Earth] diminished in size. Finally it shrank to the size of a marble, the most beautiful you can imagine. That beautiful, warm, living object looked so fragile, so delicate, that if you touched it with a finger it would crumble and fall apart. Seeing this has to change a man.</p>-->
        <!--                        <a href="#!"><img class="img-fluid" src="assets/img/post-sample-image.jpg" alt="..." /></a>-->
        <!--                        <span class="caption text-muted">To go places and do things that have never been done before – that’s what living is all about.</span>-->
        <!--                        <p>Space, the final frontier. These are the voyages of the Starship Enterprise. Its five-year mission: to explore strange new worlds, to seek out new life and new civilizations, to boldly go where no man has gone before.</p>-->
        <!--                        <p>As I stand out here in the wonders of the unknown at Hadley, I sort of realize there’s a fundamental truth to our nature, Man must explore, and this is exploration at its greatest.</p>-->
        <!--                        <p>-->
        <!--                            Placeholder text by-->
        <!--                            <a href="http://spaceipsum.com/">Space Ipsum</a>-->
        <!--                            &middot; Images by-->
        <!--                            <a href="https://www.flickr.com/photos/nasacommons/">NASA on The Commons</a>-->
        <!--                        </p>-->
                                {%endif%}
                            {%endfor%}
                            </div>
                        </div>
                    </div>
                </article>
        <!-- Footer-->
        <footer class="border-top">
            <div class="container px-4 px-lg-5">
                <div class="row gx-4 gx-lg-5 justify-content-center">
                    <div class="col-md-10 col-lg-8 col-xl-7">
                        <ul class="list-inline text-center">
                            <li class="list-inline-item">
                                <a href="#!">
                                    <span class="fa-stack fa-lg">
                                        <i class="fas fa-circle fa-stack-2x"></i>
                                        <i class="fab fa-twitter fa-stack-1x fa-inverse"></i>
                                    </span>
                                </a>
                            </li>
                            <li class="list-inline-item">
                                <a href="#!">
                                    <span class="fa-stack fa-lg">
                                        <i class="fas fa-circle fa-stack-2x"></i>
                                        <i class="fab fa-facebook-f fa-stack-1x fa-inverse"></i>
                                    </span>
                                </a>
                            </li>
                            <li class="list-inline-item">
                                <a href="#!">
                                    <span class="fa-stack fa-lg">
                                        <i class="fas fa-circle fa-stack-2x"></i>
                                        <i class="fab fa-github fa-stack-1x fa-inverse"></i>
                                    </span>
                                </a>
                            </li>
                        </ul>
                        <div class="small text-center text-muted fst-italic">Copyright &copy; Your Website 2021</div>
                    </div>
                </div>
            </div>
        </footer>
        <!-- Bootstrap core JS-->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
        <!-- Core theme JS-->
        <script src="js/scripts.js"></script>
    </body>
</html>
```


As we follow along the main.py , we see that we have two ```contacts.html``` being rendered in two different functions which are contact() and recieve_data() . The redirection of this method can be done with any methods with both methods overlapping each other . 
For capturing the information and keeping the information in the database we have used SMTP-protocol discussed earlier . In contact.html we have made a form that asks the user information and important details .

image of contact.html

<a href="https://ibb.co/ggyfrgG"><img src="https://i.ibb.co/7yvZSyH/Screenshot-25.png" alt="Screenshot-25" border="0"></a><br />
<a href="https://ibb.co/xCmm1Ht"><img src="https://i.ibb.co/ng337CN/Screenshot-26.png" alt="Screenshot-26" border="0"></a><br />

# scalablity and future refactoring

### adding posts to MongoDB
### adding posts to MySQL
### deploying and hosting the website online for the public
### monetising the website once certain traction is reached and the need of more reachiblity and server growth. 










  

