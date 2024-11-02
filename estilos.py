landing_page_css = """
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
height: 100vh;
background-color: #f4f4f4;
padding-top: 80px; /* Espaço extra para que o conteúdo não sobreponha a navbar */
"""

form_logout = """
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
width: 80%;
height: 30vh; /* Centraliza o formulário verticalmente na tela */
margin: 0 auto; /* Centraliza horizontalmente */
"""

div_principal = """
display: flex; 
flex-direction: column;
min-height: 100vh;
justify-content: space-between;
background-color: transparent;  /* Remove o fundo branco */

"""

# CSS para a navbar fixa no topo
navbar_css = """
position: fixed;
top: 0;
left: 0;
width: 100%;
display: flex;
justify-content: space-between;
align-items: center;
background-color: #36768c!important;
font-weight: bold;
color: #fff;
padding: 20px 120px 10px 120px;
z-index: 1000; /* Garantir que a navbar fique sobre outros elementos */
"""

anchor_css = {
    "padding": "10px 20px",
    "text-decoration": "none",
    "color": "white",
    "font-family": "Arial, sans-serif",
    "font-size": "18px",
    "border-bottom": "2px solid transparent",
    "transition": "border-bottom 0.3s ease, color 0.3s ease"
}



# CSS para o título principal
titled_css = """
font-size: 48px;
font-family: 'Roboto', sans-serif;
color: #00420c;
border-bottom: 2px solid #005fff;
padding-bottom: 10px;
text-align: center;
margin-top: 120px;
"""

li_css = """
    list-style-type: none;  /* Remove o marcador padrão da lista */
    padding: 10px;  /* Espaçamento interno */
    margin: 5px 0;  /* Espaçamento externo */
    background-color: #f0f0f0;  /* Cor de fundo suave */
    border-radius: 8px;  /* Bordas arredondadas */
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);  /* Sombra leve */
    font-size: 18px;  /* Tamanho da fonte */
    color: #333;  /* Cor do texto */
    font-weight: bold;  /* Texto em negrito */
    "flex-direction": "column", 
    "align-items": "center",            
    "text-align": "center"  
"""

li_css2 = """
    list-style-type: none;  /* Remove o marcador padrão da lista */
    padding: 10px;  /* Espaçamento interno */
    margin: 10px;  /* Espaçamento externo */
    background-color: #f0f0f0;  /* Cor de fundo suave */
    border-radius: 8px;  /* Bordas arredondadas */
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);  /* Sombra leve */
    font-size: 18px;  /* Tamanho da fonte */
    color: #333;  /* Cor do texto */
    font-weight: bold;  /* Texto em negrito */
    "flex-direction": "column", 
    "align-items": "center",            
    "text-align": "center"  
"""



# CSS para o subtítulo
h1_css = """
font-size: 24px;
font-family: Arial, sans-serif;
color: #333;
text-align: center;
margin-top: 10px;
"""

h1_login = """
font-size: 48px;
font-family: 'Roboto', sans-serif;
color: #00420c;
padding-bottom: 10px;
margin-top: 200px;
margin-bottom: 10px;
text-align: center; /* Centraliza o conteúdo dentro do pai */
"""

h1_credencial_invalida = """
font-size: 48px;
font-family: 'Roboto', sans-serif;
color: #00420c;
padding-bottom: 10px;
margin-top: 10px;
text-align: center; /* Centraliza o conteúdo dentro do pai */
"""


# CSS para a seção principal da landing page
content_css = """
display: flex;
flex-direction: column;
align-items: center;
text-align: center;
padding: 40px 20px;
"""


content_css2 = """
max-width: 100%;  
padding: 20px;
margin: 0 auto;
"""

footer_css = """
width: 100%;  
display: flex;
justify-content: center;  
background-color: #36768c!important; 
font-weight: bold; 
color: #fff;  
padding: 10px;
z-index: 1000; 
"flex-direction": "column", 
"align-items": "center",            
"text-align": "center"  
            
"""

table_css = {
    "width": "100%",
    "border-collapse": "collapse",
    "margin-bottom": "40px"
}

th_td_css = {
    "padding": "10px",
    "text-align": "left",
    "border": "1px solid #ddd"
}

th_css = {
    "background-color": "#f4f4f4",
    "font-weight": "bold"
}

th_css_b_left = {
    "background-color": "#f4f4f4",
    'border-left': '1px solid #000',
    'font-weight': 'bold;',
}

th_css_left = {
    "background-color": "#f4f4f4",
    'border-left': '1px solid #000',
}

th_css_grey = {
    "background-color": "#f4f4f4",
}




th_css_b_right ={
"background-color": "#f4f4f4",
'border-right': '1px solid #000',
'font-weight': 'bold;',
}


th_css_right ={
"background-color": "#f4f4f4",
'border-right': '1px solid #000',
}




th_css_b_right_left = {
"background-color": "#f4f4f4",
'border-right': '1px solid #000',
'border-left': '1px solid #000',
}

th_titulo_refeicao_css = {
"background-color": "#f4f4f4",
"font-weight": "bold",
'border-right': '1px solid #000',
'border-left': '1px solid #000',
'text-align': 'center'
}


td_css = {
"background-color": "#fff"
}



logo_mprn = """

width: 120px;
height: 120px;
margin-right: 100px;


"""

thead_css = """
background-color: #f4f4f4;
text-align: left;
font-weight: bold;
padding: 12px 18px;
border-bottom: 2px solid #ddd;
color: #333;
font-size: 16px;
"""

tbody_css = """
padding: 12px 18px;
border: 1px solid #ddd;
color: #555;
font-size: 14px;
line-height: 1.6;
"""

table_css = """
width: 90%;
border-collapse: collapse;
font-family: Arial, sans-serif;
margin: 40px auto;  
border: 1px solid #ddd;
box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
border-radius: 12px;
text-align: center;
background-color: transparent;
"""

row_even_css = """
background-color: #f9f9f9;
"""

row_hover_css = """
background-color: #f1f1f1;
cursor: pointer;
"""


select_css = """
width: 100%;
max-width: 600px;  /* Largura máxima de 600px para telas grandes */
min-width: 200px;  /* Largura mínima de 200px para telas pequenas */
font-size: 16px;  /* Tamanho da fonte apropriado */
padding: 10px;  /* Espaçamento interno */
"""


form_container_css = """
margin-top: 200px;
display: flex;
justify-content: center;
align-items: center;
flex-direction: column;
width: 100%;
margin-top: 250px;  /* Espaçamento aumentado para distanciar do nav */
"""

img_style = "width: 50%; height: auto; margin: 20px auto; display: block;"
