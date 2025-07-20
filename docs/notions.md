# {{ get_data().notions.titre }}

{{ get_data().notions.intro }}

<div class="grid cards" markdown>
{% for item in get_data().notions.data %}
- ### __{{ item.nom }}__

    {{ item.definition }}

    [:octicons-arrow-right-24: Plus d'éléments]({{ item.lien }})
{% endfor %}
</div>