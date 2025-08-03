![](img/notions.png){: style="display: block;margin-left: auto;margin-right: auto;width: 30%;"}

# {{ get_data().notions.titre }}

{{ get_data().notions.intro }}

<div class="grid cards" markdown>
{% for item in get_data().notions.data %}
- ### __{{ item.nom }}__

    ![]({{ item.image if item.image else 'img/rien.png' }}){: style="display: block;margin-left: auto;margin-right: auto;width: 40%; margin-bottom: 0%;"}

    {{ item.definition }}

    [:octicons-arrow-right-24: Plus d'éléments]({{ item.lien }})
{% endfor %}
</div>