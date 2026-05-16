# Instrucciones para estudiantes

## Objetivo de la práctica

Vas a construir un ejemplo pequeño pero completo de programación orientada a objetos en Python. Primero prepararás un entorno virtual, luego crearás clases simples y finalmente implementarás el patrón Observer.

La práctica se guía con issues progresivos en GitHub. Cuando completes una misión, el workflow **Validar progreso de misiones** revisará los criterios verificables, comentará el resultado y creará la siguiente misión.

No cierres los issues manualmente. El cierre lo hace el workflow cuando la misión cumple los criterios.

## Iniciar la práctica en GitHub

Después de crear tu copia del repositorio, inicia las misiones una sola vez:

1. Entra a la pestaña **Actions**.
2. Selecciona **Iniciar práctica**.
3. Haz clic en **Run workflow**.
4. Revisa la pestaña **Issues**.

El workflow **Iniciar práctica** también puede ejecutarse con el primer `push` a `main`. Después de crear la primera misión, el mismo workflow elimina su archivo para no volver a ejecutarse en futuros cambios.

## Crear el entorno virtual

Primero clona tu copia del repositorio y entra a la carpeta del proyecto:

```bash
git clone https://github.com/TU_USUARIO/NOMBRE_DEL_REPOSITORIO.git
cd NOMBRE_DEL_REPOSITORIO
git status
```

Después de clonar el repositorio, completa esta sección durante la primera misión con los comandos para crear, activar y preparar el entorno virtual.

python3 -m venv .venv.
.venv\Scripts\activate
pip install -r requirements.txt

## Estructura esperada

Durante la práctica crearás esta estructura:

```text
src/
  main.py
  observer_practice/
    __init__.py
    observer.py
    suscriptores.py
    canal.py
tests/
  test_observer.py
```

## Crear clases en Python

Una clase define un tipo de objeto. En esta práctica crearás suscriptores con estado interno:

```python
class SuscriptorEmail:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canal = "email"
        self.mensajes = []

    def actualizar(self, mensaje):
        self.mensajes.append(mensaje)

    def __str__(self):
        return f"{self.nombre} por {self.canal}"
```

Observa tres ideas:

- `__init__` inicializa atributos del objeto.
- `self` representa el objeto actual.
- los métodos pueden leer o modificar atributos.

Más adelante crearás también `SuscriptorSMS` y `CanalNoticias`.

## Implementar Observer paso a paso

El patrón Observer separa un objeto que cambia, llamado sujeto observable, de los objetos que reaccionan al cambio, llamados observadores.

En este proyecto:

- `CanalNoticias` es el sujeto observable.  Es una clase que contiene usuarios suscritos para enviarles alguna noticia o notificación
- `SuscriptorEmail` y `SuscriptorSMS` son observadores. Son usuarios que se suscriben a un canal para recibir notificaciónes ya sea por email o SMS
- `suscribir` agrega observadores. La clase principal donde se añaden los tipos de suscripciones 
- `desuscribir` elimina observadores. elimina al usuario de la lista de observadores en el canal para que no reciba notificaciones
- `notificar` llama `actualizar(mensaje)` en cada observador. Notificar recorre la lista de observadores y llama al metodo actualizar para añadir un mensaje a la lista de mensajes de cada suscriptor
- `publicar` guarda el último mensaje y notifica a todos. guarda el mensaje que se quiere enviar y utiliza el metodo notificar para añadirlo a la lista de mensajes de cada suscriptor

Una posible forma de organizarlo:

```python
class CanalNoticias:
    def __init__(self, nombre):
        self.nombre = nombre
        self.observadores = []
        self.ultimo_mensaje = None

    def suscribir(self, observador):
        if observador not in self.observadores:
            self.observadores.append(observador)

    def desuscribir(self, observador):
        if observador in self.observadores:
            self.observadores.remove(observador)

    def notificar(self, mensaje):
        for observador in self.observadores:
            observador.actualizar(mensaje)

    def publicar(self, mensaje):
        self.ultimo_mensaje = mensaje
        self.notificar(mensaje)
```

Puedes usar una clase base abstracta o un `Protocol` para expresar que todo observador debe tener un método `actualizar`.

## Ejecutar la demo

Cuando tengas las clases listas, crea `src/main.py` para demostrar el flujo:

```python
from observer_practice.canal import CanalNoticias
from observer_practice.suscriptores import SuscriptorEmail, SuscriptorSMS


def main():
    canal = CanalNoticias("Python al día")
    ana = SuscriptorEmail("Ana")
    luis = SuscriptorSMS("Luis")

    canal.suscribir(ana)
    canal.suscribir(luis)
    canal.publicar("Nueva clase sobre patrones de diseño")

    print(ana.mensajes)
    print(luis.mensajes)


if __name__ == "__main__":
    main()
```

Ejecuta:

```bash
python src/main.py
```

## Ejecutar pruebas

Las pruebas ya describen el comportamiento esperado:

```bash
python -m pytest
```

Si una prueba falla, lee el mensaje de error y ajusta las clases. La meta es que los suscriptores reciban mensajes, que no se dupliquen suscripciones y que `desuscribir` detenga nuevas notificaciones.

## Ver la calificación

Al terminar las misiones, se creará un issue final de calificación. Ejecuta manualmente el workflow **Validar progreso de misiones** si quieres actualizar la revisión. El comentario del issue mostrará una calificación automática sobre 100.

## Autores

- Juan José Cossio Niño
