import streamlit as st

# --------------------------------
# 🔧 CONFIGURACIÓN (EDITABLE AQUÍ)
# --------------------------------
config = {
    "site_title": "NM GAMES",
    "tagline": "Calidad en helados, excelencia en eventos.",
    "about_us": """
        Somos una empresa familiar ecuatoriana dedicada a ofrecer deliciosos helados artesanales
        y a organizar experiencias únicas como las competencias de karaoke Karaoke Cup.
    """,
    "services": [
        "Venta de helados artesanales",
        "Organización de eventos",
        "Competencias de karaoke (Karaoke Cup)"
    ],
    "contact_info": {
        "phone": "+593 999 999 999",
        "email": "contacto@nmgames.com",
        "instagram": "@nmgames_ec"
    },
    "image_banner_url": "https://cdn.pixabay.com/photo/2017/07/16/10/43/ice-cream-2500928_1280.jpg",  # Puedes cambiar esta imagen
    "theme_color": "#F2A900"
}

# --------------------------------
# 🌐 CONFIGURACIÓN DE LA PÁGINA
# --------------------------------
st.set_page_config(page_title=config["site_title"], layout="wide")

st.markdown(f"""
    <style>
    .title {{
        text-align: center;
        color: {config['theme_color']};
    }}
    </style>
""", unsafe_allow_html=True)

# --------------------------------
# 🧊 CONTENIDO DEL SITIO
# --------------------------------
st.markdown(f"<h1 class='title'>{config['site_title']}</h1>", unsafe_allow_html=True)
st.subheader(config["tagline"])

# Imagen principal desde URL
st.image(config["image_banner_url"], use_column_width=True)

# Sobre nosotros
st.header("Sobre Nosotros")
st.write(config["about_us"])

# Servicios
st.header("Servicios")
for service in config["services"]:
    st.markdown(f"- {service}")

# Contacto
st.header("Contáctanos")
contact = config["contact_info"]
st.markdown(f"📞 Teléfono: {contact['phone']}")
st.markdown(f"✉️ Correo: {contact['email']}")
st.markdown(f"📸 Instagram: {contact['instagram']}")
