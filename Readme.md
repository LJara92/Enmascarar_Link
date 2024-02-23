# Enmascarador de URL

Este programa en Python permite enmascarar una URL, acortándola y modificando su dominio para que parezca legítima. También permite agregar palabras de ingeniería social a la URL enmascarada.

## Requisitos

- Python 3.x
- curl (requerido para el funcionamiento del programa)

## Uso

1. Ejecuta el script `Enmascarar.py`.
2. Se te pedirá que pegues la URL (asegúrate de incluir "http://" o "https://").
3. El programa acortará la URL y te solicitará un dominio para enmascararla.
4. También te pedirá que ingreses palabras de ingeniería social (separadas por guiones).
5. Finalmente, te mostrará la URL enmascarada.

## Funcionamiento

- El programa valida la URL ingresada para garantizar que comience con "http://" o "https://".
- Utiliza el servicio is.gd para acortar la URL.
- Permite al usuario especificar un dominio para enmascarar la URL acortada.
- Permite agregar palabras de ingeniería social para hacer que la URL enmascarada sea más convincente.
- Genera la URL enmascarada y la muestra al usuario.

## Contribución

Las contribuciones son bienvenidas. Si deseas mejorar el código o agregar nuevas características, no dudes en enviar un pull request.

## Nota

Este programa ha sido desarrollado con fines educativos y de prueba. El uso de este software para actividades maliciosas está estrictamente prohibido.

