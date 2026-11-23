# GUÍA: Cómo obtener NovaAgent en tu PC

## Lo que vas a hacer

1. Crear una cuenta gratuita en GitHub (5 minutos, solo la primera vez)
2. Subir los archivos de NovaAgent a GitHub (arrastrar y soltar)
3. Esperar 10 minutos mientras GitHub compila el instalador
4. Descargar el instalador y ejecutarlo

TOTAL: Unos 20 minutos. Sin usar la terminal. Sin instalar nada técnico.

---

## PASO 1: Crear una cuenta en GitHub (solo la primera vez)

1. Abre tu navegador y ve a: **https://github.com**
2. Haz clic en el botón negro **"Sign up"** (arriba a la derecha)
3. Escribe tu correo electrónico, contraseña y un nombre de usuario
4. Confirma tu correo con el código que te envían
5. Ya tienes cuenta. Es gratis y no piden tarjeta.

---

## PASO 2: Crear un repositorio nuevo

1. Con tu sesión iniciada, haz clic en el botón verde **"New"** (o ve a https://github.com/new)
2. En **"Repository name"** escribe: `NovaAgent`
3. Marca la casilla **"Public"** (público, obligatorio para Actions gratis)
4. Marca la casilla **"Add a README file"**
5. Haz clic en el botón verde **"Create repository"** abajo

---

## PASO 3: Subir los archivos

1. En la página de tu repositorio, haz clic en **"Add file"** > **"Upload files"**
2. Arrastra todos los archivos del ZIP que te proporcionamos a la zona punteada
3. En el cuadro de texto de abajo escribe: "Subir archivos NovaAgent"
4. Haz clic en el botón verde **"Commit changes"**

---

## PASO 4: Esperar la compilación (automático)

1. Haz clic en la pestaña **"Actions"** arriba
2. Verás una fila con el nombre "Build NovaAgent for Windows"
3. Espera 5-10 minutos hasta que aparezca un ✓ verde
4. Haz clic en esa fila para abrir los detalles

---

## PASO 5: Descargar el instalador

1. Baja hasta la sección **"Artifacts"** (abajo en la página)
2. Verás tres archivos:
   - `NovaAgent-Windows-Installer` ← Descarga este
   - `NovaAgent-Portable`
   - `NovaAgent-Windows-Exe`
3. Haz clic en **"NovaAgent-Windows-Installer"**
4. Se descargará un ZIP. Ábrelo.
5. Dentro está `NovaAgent-Setup-1.0.0.exe`

---

## PASO 6: Instalar NovaAgent

1. Haz doble clic en `NovaAgent-Setup-1.0.0.exe`
2. Sigue las instrucciones (Siguiente, Siguiente, Instalar)
3. Al finalizar, marca "Iniciar NovaAgent ahora"
4. Haz clic en Finalizar

¡Listo! NovaAgent se abrirá y te pedirá descargar un modelo de IA.

---

## Descarga del primer modelo

1. Dentro de NovaAgent, ve a la pestaña **"Modelos"**
2. Selecciona el modelo recomendado (Qwen2.5-7B-Instruct-Q4_K_M)
3. Haz clic en **"Descargar"**
4. Espera (puede tardar 20-60 minutos según tu Internet)
5. Cuando termine, haz clic en **"Cargar modelo"**

Después de esto, NovaAgent funciona **sin Internet**.

---

## ¿Problemas?

### Windows dice "Aplicación desconocida" al instalar
- Es normal, el instalador no está firmado digitalmente
- Haz clic en **"Más información"** > **"Ejecutar de todas formas"**

### La compilación falla en GitHub
- Vuelve a la pestaña Actions
- Haz clic en "Re-run jobs" a la derecha

### El modelo tarda mucho en descargar
- Es normal, son varios GB
- Puedes pausar cerrando NovaAgent y retomarlo después
