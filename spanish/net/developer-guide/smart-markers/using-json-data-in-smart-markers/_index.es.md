---
title: Importación inteligente de JSON en Excel con marcadores inteligentes
type: docs
weight: 30
url: /es/net/how-to-import-json-into-excel-with-smart-markers/
alias: [/net/using-json-data-in-smart-markers/]
---

## **Por qué usar datos JSON para marcadores inteligentes**
¿Por qué usar datos JSON como datos originales para marcadores inteligentes?
JSON (JavaScript Object Notation) es un formato ligero, legible por humanos, ideal para estructurar datos jerárquicos. Aquí está por qué es adecuado como datos originales para marcadores inteligentes (marcadores de posición dinámicos que llenan automáticamente hojas de cálculo, documentos o paneles):

1. Soporte para datos estructurados y jerárquicos
JSON admite de forma nativa objetos y arreglos anidados (por ejemplo, { "usuario": { "nombre": "Alicia", "pedidos": [ ... ] } }). Los marcadores inteligentes pueden recorrer esta jerarquía (por ejemplo, {{usuario.pedidos[0].precio}}), facilitando la asignación de datos complejos a plantillas.

2. Aceptado en cualquier lenguaje y plataforma
Los analizadores de JSON existen en prácticamente todos los lenguajes de programación (Python, JavaScript, Java, etc.). Herramientas como Power Query de Excel, Google Apps Script o plataformas sin código (por ejemplo, Airtable) procesan JSON fácilmente.

3. Compatible con API
La mayoría de las API modernas (por ejemplo, REST, GraphQL) devuelven datos en formato JSON. Los marcadores inteligentes pueden consumir directamente JSON en vivo de servicios web, permitiendo actualizaciones en tiempo real (por ejemplo, precios de acciones, clima).

4. Legible y depurable por humanos
La estructura de texto simple de JSON es fácil de: Validar (por ejemplo, usando JSONLint). Editar manualmente o mediante scripts. Depurar al mapear datos a los marcadores.

5. Escalabilidad y flexibilidad
Agregar/quitar campos en JSON sin romper los marcadores inteligentes existentes (si se manejan los campos opcionales de manera adecuada). Soporta diversos tipos de datos: cadenas, números, booleanos, arreglos y objetos.

6. Compatibilidad con ecosistemas
Funciona con herramientas de datos modernas: Bases de datos: MongoDB, PostgreSQL (JSONB), etc. Herramientas de automatización: Zapier, Integromat. flujos de datos: Apache NiFi, Talend.

## **Uso de Plantilla Anidada de Excel con datos JSON**
Aspose.Cells for .NET admite datos JSON en marcadores inteligentes, los datos JSON pueden anidarse jerárquicamente. Por favor, revisa [archivo de plantilla](smartmarker.xlsx), [archivo JSON](smartmarker.json) y la captura de pantalla del archivo Excel generado con el siguiente código.

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

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-JSON-Data.cs" >}}


## **Usando la plantilla de subtotal de Excel con datos JSON**
Aspose.Cells for .NET admite datos JSON en marcadores inteligentes, los datos JSON pueden anidarse jerárquicamente. Se utilizó subtotal para estadísticas de datos en la plantilla de Excel. Por favor, revisa [archivo de plantilla](jsonExcelTemplate.xlsx), [archivo JSON](jsonData.json) y la captura de pantalla del archivo Excel generado con el siguiente código.

|**La primera hoja de jsonExcelTemplate.xlsx mostrando marcadores inteligentes.**|
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

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-JSON-Data-Subtotal.cs" >}}

{{< app/cells/assistant language="csharp" >}}
