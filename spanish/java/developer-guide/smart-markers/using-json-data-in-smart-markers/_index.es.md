---
title: Uso de datos JSON en Marcadores Inteligentes
type: docs
weight: 30
url: /es/java/using-json-data-in-smart-markers/
---

## **¿Por qué usar datos JSON en Marcadores Inteligentes?**
¿Por qué usar datos JSON como datos originales para Marcadores Inteligentes?
JSON (JavaScript Object Notation) es un formato de intercambio de datos ligero y legible por humanos, ideal para estructurar datos jerárquicos. Aquí está por qué es adecuado como datos originales para marcadores inteligentes (espacios reservados dinámicos que se llenan automáticamente en hojas de cálculo, documentos o paneles):

1. Soporte para datos estructurados y jerárquicos
JSON soporta nativamente objetos anidados y arreglos (por ejemplo, { "usuario": { "nombre": "Alicia", "pedidos": [ ... ] } }). Los marcadores inteligentes pueden recorrer esta jerarquía (por ejemplo, {{usuario.pedidos[0].precio}}), facilitando el mapeo de datos complejos a plantillas.

2. Independiente del lenguaje y plataforma
Los analizadores de JSON existen en prácticamente todos los lenguajes de programación (Python, JavaScript, Java, etc.). Herramientas como Excel Power Query, Google Apps Script o plataformas sin código (por ejemplo, Airtable) ingieren JSON sin problemas.

3. Fácil de usar con API
La mayoría de APIs modernas (por ejemplo, REST, GraphQL) devuelven datos en formato JSON. Los marcadores inteligentes pueden consumir directamente JSON en vivo de servicios web, permitiendo actualizaciones de datos en tiempo real (por ejemplo, precios de acciones, clima).

4. Legible por humanos y fácil de depurar
La estructura en texto plano de JSON es fácil de: Validar (por ejemplo, usando JSONLint). Editar manualmente o con scripts. Depurar al mapear datos a marcadores.

5. Escalabilidad y flexibilidad
Agregar/quitar campos en JSON sin romper los marcadores inteligentes existentes (si los campos opcionales se manejan de manera adecuada). Soporta diversos tipos de datos: cadenas, números, booleanos, arreglos y objetos.

6. Compatibilidad con ecosistemas
Funciona con herramientas de datos modernas: Bases de datos: MongoDB, PostgreSQL (JSONB), etc. Herramientas de automatización: Zapier, Integromat. Pipelines de datos: Apache NiFi, Talend.

## ** Uso de plantillas anidadas en Excel con datos JSON**
Aspose.Cells for Java soporta datos JSON en marcadores inteligentes, los datos JSON pueden estar anidados jerárquicamente. Por favor, consulte [archivo de plantilla](smartmarker.xlsx), [archivo JSON](smartmarker.json) y la captura de pantalla del archivo Excel generado con el siguiente código.

|**La primera hoja de trabajo del archivo smartmarker.xlsx mostrando marcadores inteligentes.**|
| :- |
|![todo:image_alt_text](jsontemplate.png)|

|**La captura de pantalla del archivo excel de salida.**|
| :- |
|![todo:image_alt_text](jsonresult.png)|

Datos json de la siguiente manera:
```json data
{
    "EntityCin" : "EntityCin Test",
    "EntityName" : "EntityName Test",
    "FirstName" : "FirstName Test",
    "MiddleName" : "MiddleName Test",
    "LastName" : "LastName Test",
    "DOB" : "2025-02-08",
    "SSN" : "11111111",
    "Directors" : [
        {
            "id" : "director id 1",
            "FirstName" : "director first 1",
            "MiddleName" : "director middle 1",
            "LastName" : "director last 1",
            "Reportees" : [
                {
                    "id" : "aaa",
                    "FirstName" : "first aaa",
                    "MiddleName" : "middle aaa",
                    "LastName" : "last aaa",
                    "Department" : "aaa department",
                    "City" : "aaa city",
                    "GST" : "Yes",
                    "ITR" : "No"
                },
                {
                    "id" : "bbb",
                    "FirstName" : "first bbb",
                    "MiddleName" : "middle bbb",
                    "LastName" : "last bbb",
                    "Department" : "bbb department",
                    "City" : "bbb city",
                    "GST" : "Yes",
                    "ITR" : "Yes"
                },
                {
                    "id" : "ccc",
                    "FirstName" : "first ccc",
                    "MiddleName" : "middle ccc",
                    "LastName" : "last ccc",
                    "Department" : "ccc department",
                    "City" : "ccc city",
                    "GST" : "No",
                    "ITR" : "No"
                }
            ]
        },
        {
            "id" : "director id 2",
            "FirstName" : "director first 2",
            "MiddleName" : "director middle 2",
            "LastName" : "director last 2",
            "Reportees" : [
                {
                    "id" : "eee",
                    "FirstName" : "first eee",
                    "MiddleName" : "middle eee",
                    "LastName" : "last eee",
                    "Department" : "eee department",
                    "City" : "eee city",
                    "GST" : "Yes",
                    "ITR" : "No"
                },
                {
                    "id" : "fff",
                    "FirstName" : "first fff",
                    "MiddleName" : "middle fff",
                    "LastName" : "last fff",
                    "Department" : "fff department",
                    "City" : "fff city",
                    "GST" : "No",
                    "ITR" : "No"
                }
            ]
        }
    ]
}
```
El ejemplo que sigue muestra cómo funciona esto.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-Using-JSON-Data.java" >}}


## ** Uso de plantilla de subtotal en Excel con datos JSON**
Aspose.Cells for Java soporta datos JSON en marcadores inteligentes, los datos JSON pueden estar anidados jerárquicamente. Se utilizó subtotal para estadísticas de datos en la plantilla de Excel. Por favor, consulte [archivo de plantilla](jsonExcelTemplate.xlsx), [archivo JSON](jsonData.json) y la captura de pantalla del archivo Excel generado con el siguiente código.

|**La primera hoja de trabajo del archivo jsonExcelTemplate.xlsx mostrando marcadores inteligentes.**|
| :- |
|![todo:image_alt_text](jsontemplate2.png)|

|**La captura de pantalla del archivo excel de salida.**|
| :- |
|![todo:image_alt_text](jsonresult2.png)|

Datos json de la siguiente manera:
```json data
{
    "number": 10,
    "test": "test abc",
    "date": "2011-10-05T14:48:00.000Z",
    "arrayNumber": [1,2,3,4,5],
    "arrayWords": ["x1","xy2","yz3","z4"],
    "arrayOfObjects": [
      {"valNumber":12,"valString": "aa"},
      {"valNumber":15,"valString": "bb"},
      {"valNumber":1,"valString": "cc"},
      {"valNumber":20,"valString": "dd"}

    ],
    "nestedArray": [
      {"valNumber":12,"valString": "xy","nestArr": [{"val": 1,"some": "aa"}]},
      {"valNumber":15,"valString": "y","nestArr": [{"val": 2,"some": "bb"}]},
      {"valNumber":1,"valString": "yz","nestArr": [{"some": "cc"}]},
      {"valNumber":20,"valString": "z","nestArr": [{"some": "dd"}]}
    ],
  "Products": [
    { "ProductID": "A101", "ProductName": "Apples", "Units": 5 },
    { "ProductID": "A101", "ProductName": "Apples", "Units": 10 },
    { "ProductID": "B202", "ProductName": "Bananas", "Units": 7 },
    { "ProductID": "B202", "ProductName": "Bananas", "Units": 3 },
    { "ProductID": "C303", "ProductName": "Cherries", "Units": 8 }
  ]
}
```
El ejemplo que sigue muestra cómo funciona esto.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SmartMarkers-Using-JSON-Data-Subtotal.java" >}}

{{< app/cells/assistant language="java" >}}
