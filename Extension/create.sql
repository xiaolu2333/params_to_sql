{#=========================Create new extension======================#}

{{data.name}}
{{custom_function(data.schema)}}
{{data.version}}

{#===Generates comments and code for SQL tab===#}
{% if display_comments %}
-- Extension: {{ qtIdent(data.name) }}

-- DROP EXTENSION {{ qtIdent(data.name) }};

{% endif %}
{% if data.name %}
CREATE EXTENSION{% if add_not_exists_clause %} IF NOT EXISTS{% endif %} {{ qtIdent(data.name) }}{% if data.schema == '' and data.version == '' %};{% endif %}
{% if data.schema %}

    SCHEMA {{ qtIdent(data.schema) }}{% if data.version == '' %};{% endif %}
{% endif %}
{% if data.version %}

    VERSION {{ qtIdent(data.version) }};
{% endif %}
{% endif %}
