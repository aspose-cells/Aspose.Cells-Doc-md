---
title: Importación inteligente de elemento de matriz por Slicer en Excel con Marcadores Inteligentes
type: docs
weight: 30
url: /es/net/how-to-import-array-element-by-slicer-with-smart-markers/
---

## **Por qué acceder a un elemento de matriz por Slicer**
En los Marcadores Inteligentes de FastReport, acceder a los elementos de una matriz usando un slicer (por ejemplo, [matriz[1..3]]) proporciona una forma concisa y eficiente de trabajar con subconjuntos de datos.

1. Extracción de datos simplificada: Iterar manualmente sobre matrices grandes requiere bucles y sintaxis compleja. Los slicers permiten extraer rangos (submatrices) en una sola línea. Ejemplo: [Products[1..5].Name] obtiene los nombres de los primeros 5 productos.
2. Reportes dinámicos: Generar reportes para segmentos variables de datos (por ejemplo, "Top N artículos", vistas paginadas). Ejemplo: [Sales[0..{PageNo*10}]] carga dinámicamente fragmentos de datos para reportes multipágina.
3. Optimización del rendimiento: Evita cargar matrices completas en memoria. Obtén solo los elementos necesarios. Ejemplo: [Logs[^10..^1]] obtiene las últimas 10 entradas de forma eficiente.
4. Sintaxis declarativa: Expresa la intención directamente en los marcadores en la plantilla. Ejemplo: [Employees[3..7].Department] selecciona claramente los departamentos de las entradas 3 a 7.
5. Integración con fuentes de datos: Funciona con matrices provenientes de bases de datos, JSON o código. Ejemplo: Vincula Invoice.Items[0..2] para mostrar los primeros 3 artículos de línea.
6. Los segmentadores en Smart Markers reducen la complejidad del código, mejoran la legibilidad y optimizan el manejo de datos para subconjuntos de matrices. Úsalos cuando necesites acceso rápido basado en rangos—ideal para paginación, listas de los mejores N o vistas de datos en ventana. 

## **Cómo importar un elemento de matriz mediante segmentador en Excel con Smart Markers**
Aspose.Cells admite acceder a elementos de matriz mediante segmentador en smart markers. Por favor, consulta [archivo de plantilla](ElementBySlicer.xlsx), [archivo json](ElementBySlicer.json) y la captura de pantalla del archivo excel generado con el siguiente código.

|**La primera hoja de trabajo del archivo smartmarker.xlsx mostrando marcadores inteligentes.**|
| :- |
|![todo:image_alt_text](ElementBySlicer1.png)|

|**La captura de pantalla del archivo excel de salida.**|
| :- |
|![todo:image_alt_text](ElementBySlicer2.png)|

Datos json de la siguiente manera:
```json data
{
  "EntityCin": "EntityCin Test",
  "EntityName": "EntityName Test",
  "FirstName": "FirstName Test",
  "MiddleName": "MiddleName Test",
  "LastName": "LastName Test",
  "DOB": "2025-02-08",
  "SSN": "11111111",
  "Directors": [
    {
      "id": "director id 1",
      "FirstName": "director first 1",
      "MiddleName": "director middle 1",
      "LastName": "director last 1",
      "Reportees": [
        {
          "id": "aaa",
          "FirstName": "first aaa",
          "MiddleName": "middle aaa",
          "LastName": "last aaa",
          "Department": "aaa department",
          "City": "aaa city",
          "GST": "Yes",
          "ITR": "No"
        },
        {
          "id": "bbb",
          "FirstName": "first bbb",
          "MiddleName": "middle bbb",
          "LastName": "last bbb",
          "Department": "bbb department",
          "City": "bbb city",
          "GST": "Yes",
          "ITR": "Yes"
        },
        {
          "id": "ccc",
          "FirstName": "first ccc",
          "MiddleName": "middle ccc",
          "LastName": "last ccc",
          "Department": "ccc department",
          "City": "ccc city",
          "GST": "No",
          "ITR": "No"
        }
      ]
    },
    {
      "id": "director id 2",
      "FirstName": "director first 2",
      "MiddleName": "director middle 2",
      "LastName": "director last 2",
      "Reportees": [
        {
          "id": "eee",
          "FirstName": "first eee",
          "MiddleName": "middle eee",
          "LastName": "last eee",
          "Department": "eee department",
          "City": "eee city",
          "GST": "Yes",
          "ITR": "No"
        },
        {
          "id": "fff",
          "FirstName": "first fff",
          "MiddleName": "middle fff",
          "LastName": "last fff",
          "Department": "fff department",
          "City": "fff city",
          "GST": "No",
          "ITR": "No"
        }
      ]
    },
    {
      "id": "director id 3",
      "FirstName": "director first 2",
      "MiddleName": "director middle 2",
      "LastName": "director last 2",
      "Reportees": [
        {
          "id": "eee3",
          "FirstName": "first eee3",
          "MiddleName": "middle eee3",
          "LastName": "last eee3",
          "Department": "eee department3",
          "City": "eee city3",
          "GST": "Yes",
          "ITR": "No"
        },
        {
          "id": "fff3",
          "FirstName": "first fff3",
          "MiddleName": "middle fff3",
          "LastName": "last fff3",
          "Department": "fff department3",
          "City": "fff city",
          "GST": "No",
          "ITR": "No"
        }
      ]
    },
    {
      "id": "director id 4",
      "FirstName": "director first 4",
      "MiddleName": "director middle 4",
      "LastName": "director last 4",
      "Reportees": [
        {
          "id": "eee4",
          "FirstName": "first eee4",
          "MiddleName": "middle eee4",
          "LastName": "last eee4",
          "Department": "eee department4",
          "City": "eee city4",
          "GST": "Yes",
          "ITR": "No"
        },
        {
          "id": "fff4",
          "FirstName": "first fff4",
          "MiddleName": "middle fff4",
          "LastName": "last fff4",
          "Department": "fff department4",
          "City": "fff city4",
          "GST": "No",
          "ITR": "No"
        }
      ]
    }
  ]
}
```
El ejemplo que sigue muestra cómo funciona esto.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-AccessElementBySlicer.cs" >}}

{{< app/cells/assistant language="csharp" >}}
