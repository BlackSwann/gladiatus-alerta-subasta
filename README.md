# Gladiatus Alerta Subasta
Esta pequeño script reproduce una alarma cuando la subasta llega a "muy corto" en el juego online Gladiatus. Cada 60 segundos va a revisar la subasta y cuando llegue a corto generará un cartel de alerta. Luego en muy corto suena una alarma y el mismo botón. 

### Modo de uso

Nota: hay que tener python instalado.
Nota: funciona con firefox.
Nota: hay que estar conectado en el juego desde el navegador firefox.
Nota: cargar la página de la subasta y copiar el link de la barra de navegación.

```sh
$ git clone https://github.com/BlackSwann/gladiatus-alerta-subasta.git gladiatus-alerta-subasta
$ cd gladiatus-alerta-subasta
$ python main.py {link de la subasta}
```

### Todo

  - Crear una versión ejecutable
  - Ampliar para el uso de Chrome


