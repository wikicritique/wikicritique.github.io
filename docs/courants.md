![](img/courants.png){: style="display: block;margin-left: auto;margin-right: auto;width: 30%;"}

# {{ get_data().courants.titre }}

{{ get_data().courants.intro }}

<div class="grid cards" markdown>
{% for item in get_data().courants.data %}
- ### __{{ item.nom }}__

    {{ item.definition }}

    [:octicons-arrow-right-24: Plus d'éléments]({{ item.lien }})
{% endfor %}
</div>