{# =============Update extension schema============= #}
{% if data.schema and data.schema != o_data.schema %}
ALTER EXTENSION {{ qtIdent(o_data.name) }}
    SET SCHEMA {{ qtIdent(data.schema) }};
{% endif %}
{# =============Update extension version============= #}
{% if data.version and data.version != o_data.version %}
ALTER EXTENSION {{ qtIdent(o_data.name) }}
    UPDATE TO {{ qtIdent(data.version) }};
{% endif %}
