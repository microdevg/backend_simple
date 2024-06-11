## Backend super basico para probar lector RFID con ESP32


Para correr este programa se recomienda instalar un entorno virtual y luego instalar las dependencias que se encuentran en el archivo `requerimientos.txt`
```
# Para window (Suponiendo Python instalado)
python -m venv .venv
.venv/Scripts/activate
pip install requerimientos.txt

```




Utilizando un cliente MQTT (librería PAHO-MQTT) me suscribo al tópico  `/REQ` y proceso las peticiones,
Próximamente implementare base de datos para verificar los `user_id` que recibo mediante `/REQ`. Actualmente solo se revisa desde una tupla (USERS)


```

## Base de datos ultra básica jaja
## Para agregar usuario, agregar a la tupla
USERS =[
    "1234",
    "593189658514",
]
```




## Extras
#### Link del repositorio del lector RFID:  [link](https://github.com/microdevg/lector_RFID.git)