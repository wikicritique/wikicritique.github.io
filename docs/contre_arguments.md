# {{ get_data().contre_arguments.titre }}

{{ get_data().contre_arguments.intro }}

<div class="grid cards" markdown>
{% for item in get_data().contre_arguments.data %}
- ### ___« {{ item.argument }} »___

    ---

    {{ item.contre_argument }}

    [:octicons-arrow-right-24: Plus d'éléments]({{ item.lien }})
{% endfor %}
</div>