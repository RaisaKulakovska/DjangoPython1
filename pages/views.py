from django.template.response import TemplateResponse


def home(request):
    data = {
        "h1": "Craft",
        "subtitle": "This is a template for a simple marketing or informational website. It includes a large callout called a jumbotron and three supporting pieces of content. Use it as a starting point to create something more unique.",

        "title1": "One",
        "desc1": "One id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui.",

        "title2": "Two",
        "desc2": "Two id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui.",

        "title3": "Tree",
        "desc3": "Tree id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui."
    }
    return TemplateResponse(request, "home.html", data)


def about(request):
    return TemplateResponse(request, "about.html")
