---
title: Cómo usar el parámetro if y variables en SmartMarkers
type: docs
weight: 10
url: /es/net/how-to-use-if-parameter-and-Variables-in-smart-markers/
---

## **Por qué usar el parámetro if y variables en Smart Markers**
Smart Markers son herramientas poderosas utilizadas en diversos contextos. El uso de parámetros y variables dentro de Smart Markers mejora significativamente su flexibilidad, eficiencia y funcionalidad.

1. Manejo dinámico de datos y flexibilidad: Los parámetros y variables permiten que Smart Markers manejen datos de manera dinámica, adaptándose a entradas cambiantes sin necesidad de ajustes manuales en la plantilla o en el código.
2. Control sobre comportamiento y operaciones: Los parámetros ajustan el comportamiento de Smart Markers, permitiendo operaciones como agrupamiento, ordenamiento, subtotalización y formato condicional.
3. Soporte para estructuras de datos complejas: Las variables permiten que Smart Markers trabajen con fuentes de datos complejas, incluyendo matrices, objetos y datos multidimensionales.
4. Eficiencia y automatización: Los parámetros y variables automatizan tareas repetitivas, reduciendo esfuerzo manual y errores potenciales.
5. Lógica condicional y filtrado: Aunque limitado en algunos contextos, los parámetros y variables pueden implementar lógica condicional.
6. Personalización e interacción del usuario: Las variables permiten que las entradas del usuario personalicen dinámicamente el comportamiento de Smart Marker.
7. Optimización del rendimiento: Los parámetros ayudan a optimizar el rendimiento controlando cómo se procesa la data.


## **Cómo usar el parámetro if y variables en SmartMarkers**
A veces, necesitas agregar una condición if para juzgar los parámetros de variable en SmartMarkers. Aspose.Cells hace posible usar el parámetro if y variables en SmartMarkers. Por favor, consulta [archivo de plantilla](template.xlsx), [archivo json](data.json) y la captura de pantalla del archivo excel generado con el siguiente código.

|**La primera hoja del archivo template.xlsx muestra variables.**|
| :- |
|![todo:image_alt_text](variables.png)|

|**La segunda hoja del archivo template.xlsx muestra Smart Markers.**|
| :- |
|![todo:image_alt_text](template.png)|

|**La captura de pantalla del archivo excel de salida.**|
| :- |
|![todo:image_alt_text](result.png)|

Datos json de la siguiente manera:
```json data
{
    "Directors": [
        {
            "FirstName": "director first 1",
            "id": "director id 1",
            "LastName": "director last 1",
            "MiddleName": "director middle 1",
            "Reportees": [
                {
                    "City": "aaa city",
                    "Department": "aaa department",
                    "FirstName": "first aaa",
                    "GST": "Yes",
                    "id": "aaa",
                    "ITR": "No",
                    "LastName": "last aaa",
                    "MiddleName": "middle aaa"
                },
                {
                    "City": "bbb city",
                    "Department": "bbb department",
                    "FirstName": "first bbb",
                    "GST": "Yes",
                    "id": "bbb",
                    "ITR": "Yes",
                    "LastName": "last bbb",
                    "MiddleName": "middle bbb"
                },
                {
                    "City": "ccc city",
                    "Department": "ccc department",
                    "FirstName": "first ccc",
                    "GST": "No",
                    "id": "ccc",
                    "ITR": "No",
                    "LastName": "last ccc",
                    "MiddleName": "middle ccc"
                }
            ]
        },
        {
            "FirstName": "director first 2",
            "id": "director id 2",
            "LastName": "director last 2",
            "MiddleName": "director middle 2",
            "Reportees": [
                {
                    "City": "eee city",
                    "Department": "eee department",
                    "FirstName": "first eee",
                    "GST": "Yes",
                    "id": "eee",
                    "ITR": "No",
                    "LastName": "last eee",
                    "MiddleName": "middle eee"
                },
                {
                    "City": "fff city",
                    "Department": "fff department",
                    "FirstName": "first fff",
                    "GST": "No",
                    "id": "fff",
                    "ITR": "No",
                    "LastName": "last fff",
                    "MiddleName": "middle fff"
                }
            ]
        }
    ],
    "DOB": "2025-02-08",
    "EntityCin": "EntityCin Test",
    "EntityName": "EntityName Test",
    "FirstName": "FirstName Test",
    "LastName": "LastName Test",
    "MiddleName": "MiddleName Test",
    "SSN": "11111111"
}
```
El ejemplo que sigue muestra cómo funciona esto.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-If-Parameter-And-Variables.cs" >}}

{{< app/cells/assistant language="csharp" >}}
