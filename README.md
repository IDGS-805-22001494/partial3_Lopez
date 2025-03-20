# 🌟 partial3_Lopez - Flask Login Example 

> Este es un ejemplo práctico de una aplicación Flask que utiliza Flask-Login para manejar la autenticación de usuarios. La aplicación incluye un formulario de inicio de sesión, rutas protegidas y un diseño moderno utilizando Tailwind CSS y Flowbite.

## 📋 Requisitos Previos

Antes de ejecutar la aplicación, asegúrate de tener instalado lo siguiente:

- ✅ Python 3.8 o superior
- ✅ Pip (gestor de paquetes de Python)
- ✅ Node.js (para compilar Tailwind CSS)

## 🚀 Instalación

Sigue estos pasos para configurar y ejecutar la aplicación:

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/IDGS-805-22001494/partial3_Lopez.git
   cd partial3_Lopez.git
   ```

2. **Crea un entorno virtual** (opcional pero recomendado):
   ```bash
   python -m venv venv
   
   # En Linux/macOS:
   source venv/bin/activate
   
   # En Windows:
   venv\Scripts\activate
   ```

3. **Instala las dependencias de Python:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura Tailwind CSS:**
   - Instala Node.js si no lo tienes: [Descargar Node.js](https://nodejs.org/)
   - Instala las dependencias de Node.js:
     ```bash
     npm install
     ```
   - Compila Tailwind CSS:
     ```bash
     npx tailwindcss -i ./src/input.css -o ./static/css/output.css --watch
     ```

5. **Ejecuta la aplicación:**
   ```bash
   python app.py
   ```

6. **Accede a la aplicación:**
   - Abre tu navegador y visita [http://localhost:5000](http://localhost:5000)
   - Verás el formulario de inicio de sesión

## ✨ Funcionalidades

### 🔐 Autenticación de Usuarios
- Los usuarios pueden iniciar sesión con un nombre de usuario y contraseña
- **Credenciales válidas:**
  - Usuario: `admin`, Contraseña: `admin123`
  - Usuario: `user`, Contraseña: `user123`

### 🛡️ Rutas Protegidas
- La ruta `/dashboard` solo es accesible para usuarios autenticados
- Si un usuario no autenticado intenta acceder a una ruta protegida, será redirigido al formulario de inicio de sesión

### 🎨 Diseño Moderno
- La interfaz de usuario está diseñada con Tailwind CSS y Flowbite
- El formulario de inicio de sesión y el dashboard son responsivos y fáciles de usar

### 📝 Manejo de Sesiones
- Los usuarios pueden cerrar sesión haciendo clic en el botón "Cerrar sesión"

## 📖 Cómo Usar la Aplicación

### Iniciar Sesión
1. Visita [http://localhost:5000](http://localhost:5000)
2. Ingresa un nombre de usuario y contraseña válidos
3. Haz clic en "Iniciar sesión"

### Acceder al Dashboard
- Después de iniciar sesión, serás redirigido al dashboard
- En el dashboard, verás un mensaje de bienvenida y un botón para cerrar sesión

### Cerrar Sesión
- Haz clic en "Cerrar sesión" en el dashboard
- Serás redirigido al formulario de inicio de sesión

## ⚙️ Personalización

### Agregar Más Usuarios
Edita el diccionario `users` en `app.py` para agregar más usuarios:
```python
users = {
    'admin': {'password': 'admin123'},
    'user': {'password': 'user123'},
    'nuevo_usuario': {'password': 'nueva_contraseña'}
}
```

### Cambiar el Diseño
- Modifica los archivos en la carpeta `templates` para personalizar la interfaz
- Usa Tailwind CSS y Flowbite para agregar nuevos componentes o estilos

### Usar una Base de Datos
- Reemplaza el diccionario de usuarios por una base de datos real (SQLite, PostgreSQL, etc.)
- Usa Flask-SQLAlchemy para manejar la base de datos

## 🔧 Tecnologías Utilizadas

| Tecnología | Descripción |
|------------|-------------|
| **Flask** | Framework web de Python |
| **Flask-Login** | Manejo de autenticación y sesiones |
| **Flask-WTF** | Formularios web |
| **Tailwind CSS** | Framework CSS para diseño moderno |
| **Flowbite** | Biblioteca de componentes UI para Tailwind CSS |

## 📬 Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarme:

- **Nombre:** Alonso Daniel LS
- **Web:** [https://alonsodev.vercel.app/Work](https://alonsodev.vercel.app/Work)
- **GitHub Personal:** [https://github.com/AlonsoD16](https://github.com/AlonsoD16)
- **GitHub Estudiante:** [https://github.com/IDGS-805-22001494](https://github.com/IDGS-805-22001494)

---

<div align="center">
  <img src="https://img.shields.io/badge/Hecho%20con-%E2%9D%A4-red" alt="Hecho con amor">
</div>