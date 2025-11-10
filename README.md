🏭 Sistema de Relevamiento de Centros Industriales — Django

Este proyecto es una aplicación web desarrollada con Django para registrar, visualizar y gestionar centros industriales (máquinas o equipos de trabajo).
El objetivo es mantener un relevamiento actualizado del estado operativo y la existencia de cada centro, con la posibilidad de asociarlos en el futuro a productos o condiciones de funcionamiento más detalladas.

🚀 Funcionalidades principales

Creación de centros de trabajo mediante parámetros en la URL

Listado general de centros de trabajo  existentes con sus estados

Interfaz visual simple y clara (sin dependencias externas)

Base preparada para futuras expansiones, como asociación con productos o informes de funcionamiento

🧩 Estructura del proyecto
TuPrimerPagina-Leone-main/
├── manage.py
├── requirements.txt
├── .gitignore
├── Pagina/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── pisoplanta/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── templates/
    │   ├── crear_centro.html
    │   ├── homepisoplanta.html
    │   └── listar_centros.html
    └── ...



Abrí en el navegador: 👉 http://127.0.0.1:8000

🌐 URLs del proyecto
1️⃣ Página principal
http://127.0.0.1:8000/


Muestra el inicio de la aplicación (homepisoplanta.html), con acceso a las funciones disponibles.

2️⃣ Listado de centros
http://127.0.0.1:8000/listar-centros/



3️⃣ Creación de un centro (vía URL)
http://127.0.0.1:8000/crear-centro/<nombre>/<operacion>/<activo>/



👤 Autor

Luciano Leone

📧 Contacto: [luciano.leone@gmail.com]

💬 Notas

Este sistema servirá como base para un relevamiento de maquinaria industrial, permitiendo:

Cargar y clasificar centros (máquinas)

Registrar su estado operativo

Asociarlos en el futuro con productos, mantenimiento y condiciones de uso