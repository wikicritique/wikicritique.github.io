![](img/evenements.png){: style="display: block;margin-left: auto;margin-right: auto;width: 30%;"}

# {{ get_data().evenements.titre }}

{{ get_data().evenements.intro }}

## 19ème siècle

<div class="grid cards" markdown>
{% for item in get_data().evenements.data if 1800 <= item.date < 1900 %}
- ### __« {{ item.titre }} »__

    ---

    {{ item.resume }}

    [:octicons-arrow-right-24: Plus d'éléments]({{ item.lien }})
{% endfor %}
</div>

## 20ème siècle

<div class="grid cards" markdown>
{% for item in get_data().evenements.data if 1900 <= item.date < 2000 %}
- ### __« {{ item.titre }} »__

    ---

    {{ item.resume }}

    [:octicons-arrow-right-24: Plus d'éléments]({{ item.lien }})
{% endfor %}
</div>

## 21ème siècle

<div class="grid cards" markdown>
{% for item in get_data().evenements.data if item.date >= 2000 %}
- ### __« {{ item.titre }} »__

    ---

    {{ item.resume }}

    [:octicons-arrow-right-24: Plus d'éléments]({{ item.lien }})
{% endfor %}
</div>