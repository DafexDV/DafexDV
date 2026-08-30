# Hi 👋

{{ description }}

## Skills

![Skills]({{ skills_img_url }})

## Contact

{% for contact in contacts %}
- **{{ contact.label }}:** {% if contact.type == "link" %}[{{ contact.value }}]({{ contact.link }}){% else %}{{ contact.value }}{% endif %}
{% endfor %}
