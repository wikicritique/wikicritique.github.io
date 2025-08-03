![](img/contre_arguments2.png){: style="display: block;margin-left: auto;margin-right: auto;width: 30%;"}

# {{ get_data().contre_arguments.titre }}

{{ get_data().contre_arguments.intro }}

<div class="grid cards" markdown>
{% for item in get_data().contre_arguments.data %}
- ### ___« {{ item.argument }} »___

    ---

    {{ item.contre_argument }}

    [:octicons-arrow-right-24: Plus d'éléments]({{ 'contre_arguments/' ~ item.id ~ '.md'}})
{% endfor %}
</div>