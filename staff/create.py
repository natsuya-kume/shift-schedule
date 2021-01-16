{% extends 'staff/base.html' %}

{% block content %}
{{ form.as_p }}
<input type="submit" class="btn btn-primary" value="Submit">
{% block content %}