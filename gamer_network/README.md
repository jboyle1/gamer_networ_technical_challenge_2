### 
 
## Gamer Network Technical Challenge Documentation

### Django Setup

My initial thoughts were to use the Django framework to set up a model template for the challenge. I firstly created a folder in my developer directory called 'Gamer Network' that I could target with my terminal to open up VSCode using the 'code .' command. 

Once the folder was open in the text editor I created a virtual environment using a pre installed package for environment management called 'Anaconda'. I used the 'conda create -name < ENVNAME > django' command to create a venv called 'GNENV.

Then I created a main directory with all the main settings and urls called 'gamerNetPro1'. I cd into this directory and then created a singular application called 'gamerNetApp1'. I then initiated git and created my initial commit.

I continued to create a templates folder in which I created a subdirectory called 'gamerNetApp1' containing only one HTML file for the app. This was the index.html. Following this I created a static folder in a similar fashion containing a sub directory, again called 'gamerNetApp1' and in this, two more directories for the CSS file and a Javascript file if needed.

The next task was to configure the directory path settings for the templates folder and the static folder. This is the standard code that I placed in the relevant section of settings.py:

        TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
        STATIC_DIR = os.path.join(BASE_DIR, "static")

I then input 'gamerNetApp1' into the INSTALLED_APPS list and 'TEMPLATES_DIR' in the TEMPLATES dictionary under 'DIRS'. The final thing to do in settings.py was add the STATICFILES_DIRS list containing 'STATIC_DIR' at the bottom of the file.

### First Approach

#### Model

I thought that a good way to approach this task would be to place the data dictionary I was given into a Django admin database. and display the data via template tagging with a for loop in the HTML page.

Firstly I created a model class in models.py that had two fields, one for the title and one for the column length:

        class Article(models.Model):
            title = models.CharField(max_length=128)
            columns = models.IntegerField()

#### View

Then in views.py I made a function to render the html file:

        from django.shortcuts import render
        from gamerNetApp1.models import Article

        def index(request):
            Article_list = Article.objects.order_by('title')
            Article_dict = { 'Articles': Article_list}
            return render(request, 'gamerNetApp1/index.html', context=Article_dict)

#### URLs

I then created an application specific urls.py file and input the right path settings in this and in the main urls.py file aswell.

#### Admin 

I registered the model in admin.py

#### Migrate

I migrated the models to the Django admin database using the 'python manage.py migrate' command and the 'python manage.py makemigrations' command. This was successful.

#### Create Super User

I created a super user to access the Django admin pannel

#### Data Input

I used the dictionary of data I was given to fill up the database.

#### Develop HTML template

There was no need to make a base.html extension as this application only has one page. 

In the index.html I started by loading the static files at the very top under the !DOCTYPE html tag using:

        {% load staticfiles %}.

Then I continued by adding a title and the bootstrap CDN (just to make the text look a bit nicer for now). I also added a static file link to my own stylesheet to create the grid. At the bottom before the closing body tag I placed my Javascript external link incase I needed to use andy Javascript.

Next I needed to create the template tag that targets the database using an if statement 

        {% if Articles %} '''{% endfor %}

Inside this I made a for loop that iterates through the articles and interpolates the data from the database to display in the browser. I created a class container and an ID container with a child class of item to use for styling the grid later. 

        {% for col in Articles %}
            <div class="container" id="container">
                <div class="item">{{ col.title }}{{ col.columns}}</div>
            </div>
        {% endfor %}

#### CSS Styling

I used Flexbox to style the grid without bootstrap. Using some documentation I targeted the classes and IDs in the HTML file and implemented the body, paragraph, container and item elements and styled them. This created a uniform set of rows with each article taking up one of the three columns.

#### Grouping the different column sizes

I tred to use a python dictionary instead of the database to see if I could write a function that arranges the grid. I placed the dictionary into the views.py file and began working on grouping the articles into collections of different column length. I found some code that groups dictionaries into collections this can be found at:

https://www.saltycrane.com/blog/2014/10/example-using-groupby-and-defaultdict-do-same-task/ 

Here is how I applied the code:

        articles = [
            {"title": "Star Ocean review", "columns": u"2"},
            {"title": "Lego Star Wars review","columns": u"2"},
            {"title": "Prison Architect review","columns": u"1"},
            {"title": "Inside review","columns": u"2"},
            {"title": "Umbrella Corps review","columns": u"2"},
            {"title": "Dino Dini's Kick Off review","columns": u"3"},
            {"title": "Trials of the Dragon review","columns": u"1"},
            {"title": "Mighty No. 9 review","columns": u"1"},
            {"title": "Edge of Nowhere review","columns": u"2"},
            {"title": "Guilty Gear Xrd Revelator review","columns": u"1"},
            {"title": "Sherlock Holmes review","columns": u"2"},
            {"title": "Mirror's Edge Catalyst review","columns": u"3"},
            {"title": "Kirby: Planet Robobot review","columns": u"3"},
            {"title": "Dangerous Golf review","columns": u"1"},
            {"title": "Teenage Mutant Turtles review","columns": u"1"},
            {"title": "The Warcraft movie review","columns": u"2"},
            {"title": "Overwatch Review","columns": u"2"},
            {"title": "The Witcher 3 review","columns": u"2"}
        ]

        def grouping():
            grouped = collections.defaultdict(list)
            for item in articles:
                grouped[item['columns']].append(item)

            for columns, group in grouped.items():
        
                print("\n")
                print("Articles that take up {} columns:".format(columns))
                print(group)

        grouping()


This function collects the articles into these groups:

        Articles that take up 2 columns:
        [{'title': 'Star Ocean review', 'columns': '2'}, {'title': 'Lego Star Wars review', 'columns': '2'}, {'title': 'Inside review', 'columns': '2'}, {'title': 'Umbrella Corps review', 'columns': '2'}, {'title': 'Edge of Nowhere review', 'columns': '2'}, {'title': 'Sherlock Holmes review', 'columns': '2'}, {'title': 'The Warcraft movie review', 'columns': '2'}, {'title': 'Overwatch Review', 'columns': '2'}, {'title': 'The Witcher 3 review', 'columns': '2'}]

        Articles that take up 1 columns:
        [{'title': 'Prison Architect review', 'columns': '1'}, {'title': 'Trials of the Dragon review', 'columns': '1'}, {'title': 'Mighty No. 9 review', 'columns': '1'}, {'title': 'Guilty Gear Xrd Revelator review', 'columns': '1'}, {'title': 'Dangerous Golf review', 'columns': '1'}, {'title': 'Teenage Mutant Turtles review', 'columns': '1'}]

        Articles that take up 3 columns:
        [{'title': "Dino Dini's Kick Off review", 'columns': '3'}, {'title': "Mirror's Edge Catalyst review", 'columns': '3'}, {'title': 'Kirby: Planet Robobot review', 'columns': '3'}]

**I came to a bit of a dead end with this approach so I decided to carry on working from the database rather than a dictionary**

#### JQuery

I decided to use JQuery to target the data from the articles in the Django Admin database. After looking through the JQuery documentation I found a method called 'contains()' that I could use in a selector function. Here is the code:

    <script src="{% static "gamerNetApp1/js/jquery-3.4.1.js" %}"></script>
            <script>
                $("document").ready(function () {
                    $(".item:contains('1')").css("width", "300");
                    $(".item:contains('2')").css("width", "600");
                    $(".item:contains('3')").css("width", "900");
                })
            </script>

The 1, 2 and 3 represent the different article lengths. The 'contains()' method when attached to the 'item' class checks for the data's integer that has been rendered in the templated loop. You place the number you want to target in the parentheses. I decided to use the .css method to style the articles with the right column width (300px, 600px, 900px). Then I added float-left to the '.item' class's css so all the elements aligned in the rows. Obviously now there are still gaps in the grid.

#### Not Able to Complete Task

Unfourtunatly I was not able to complete the task without help, which was to fill the third columns with the single column article. 

Firstly I tried to target and style the articles from the database I created using Jquery. I managed to target the 'columns' datafield and assign it the correct lengths. I thought that by doing this I could also arrainge them in the right order but as the data is iterated and rendered randomly there would always be gaps.

Then I tried to use JQuery in conjunction with Ajax to target the 'article-data.json' file I created but I have only just started to learn this about this method so I was a bit out of depth.

I Hope that my approach to this challenge shows that I am confident using the Django framework and its built in Admin pannel. I feel that I have a good understanding of views, models, url patterns and the overal configuration of the framework. Unfourtunatly I didn't complete the task, I have deployed it anyway.

#### Deployment

I had some difficulties deploying this project with Heroku, so unfortunatly there is no direct URL link.


#### Final browser render

![]({% static "image/final-render" %})




















