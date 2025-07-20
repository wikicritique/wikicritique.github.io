# {{ get_data().personnalites.titre }}

{{ get_data().personnalites.intro }}

<div class="grid cards" markdown>
{% for item in get_data().personnalites.data %}
- ### __{{ item.nom }}__

    {{ item.presentation }}

    [:octicons-arrow-right-24: Plus d'éléments]({{ item.lien }})
{% endfor %}
</div>