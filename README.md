# 🏭 Sistema de Relevamiento de Centros Industriales — Django

Este proyecto es una aplicación web desarrollada con **Django** para registrar, visualizar y gestionar centros industriales (máquinas o equipos de trabajo).  
El objetivo es mantener un relevamiento actualizado del estado operativo y la existencia de cada centro, con la posibilidad de asociarlos en el futuro a productos o condiciones de funcionamiento más detalladas.

---

## 🚀 Funcionalidades principales

- ✔ **CRUD completo** de Centros de Trabajo  
- ✔ **Login, Logout y Registro** de usuarios  
- ✔ **Protección de vistas** mediante Mixins y Decoradores  
- ✔ **Búsqueda avanzada** de centros por nombre u operación  
- ✔ **Interfaz moderna y responsiva**, con estilos propios  
- ✔ **Uso de Class-Based Views (CBV)** en edición y eliminación  
- ✔ **Página de inicio** y **página About**  
- ✔ **Carga y visualización de imágenes**  
- ✔ **Administración completa desde Django Admin**  

---

## 📂 Estructura del proyecto

```
TuPrimerPagina-Leone/
├── manage.py
├── requirements.txt
├── .gitignore
├── Pagina/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── usuarios/
│   ├── templates/
│   │   ├── login.html
│   │   ├── logout.html
│   │   └── register.html
│   ├── views.py
│   ├── urls.py
│   └── forms.py
└── pisoplanta/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── templates/
    │   ├── crear_centro.html
    │   ├── editar_centro.html
    │   ├── eliminar_centro.html
    │   ├── listar_centros.html
    │   ├── ver_centro.html
    │   └── homepisoplanta.html
    └── ...
```

---

## 🌐 URLs principales

### 1️⃣ Página principal  
http://127.0.0.1:8000/

### 2️⃣ Listado de Centros  
http://127.0.0.1:8000/centros/

### 3️⃣ Crear Centro  
http://127.0.0.1:8000/crear-centro/

### 4️⃣ Login  
http://127.0.0.1:8000/usuarios/login/

### 5️⃣ Registro  
http://127.0.0.1:8000/usuarios/register/

### 6️⃣ About  
http://127.0.0.1:8000/about/

---

## 🔐 Seguridad

- Rutas sensibles protegidas con **LoginRequiredMixin**  
- Uso de **decoradores** para restringir acciones de creación, edición y borrado  
- Control visual en el menú según estado del usuario  

---

## 📦 Requisitos del proyecto

El archivo `requirements.txt` incluye todas las dependencias necesarias para ejecutar el proyecto.

Para instalarlas:

```
pip install -r requirements.txt
```

---

## ▶ Cómo ejecutar el proyecto

1. Crear entorno virtual  
2. Instalar dependencias  
3. Aplicar migraciones  
4. Ejecutar servidor:

```
python manage.py runserver
```

---

## 📌 Notas importantes para la entrega

- ❗ *No subir `db.sqlite3` al repositorio*  
- ❗ *No subir contenido de `/media`*  
- ✔ Se utiliza herencia de templates  
- ✔ Uso de CBV, Mixins y decoradores  
- ✔ Sistema completo de autenticación de usuarios  
- ✔ CRUD completo funcionando  
- ✔ Video demostrativo solicitado por la cátedra  

---

## 👨‍💻 Autor

Proyecto desarrollado por **Luciano Leone**, estudiante de Ingeniería Electrónica y responsable de TI en Schneider SRL, Paraná, Entre Ríos.