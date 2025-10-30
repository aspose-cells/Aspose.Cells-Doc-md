---
title: Importación inteligente de arreglos variables en Excel con marcadores inteligentes
type: docs
weight: 30
url: /es/net/how-to-import-variable-arrays-with-smart-markers/
---

## **Por qué usar arreglos variables para marcadores inteligentes**
Variable arrays (e.g., <<products[0].name>> or <<foreach item in cart>>) enable dynamic handling of repeated data structures in templates. They solve limitations of flat/nested objects when dealing with lists, tables, or collections.

1. Repetición dinámica sin codificación dura: Los marcadores estáticos fallan para datos de longitud variable (por ejemplo, elementos del pedido, permisos del usuario). Los arreglos itera dinámicamente. 
2. Agregación simplificada: Calcular sumas, promedios o filtros directamente. Evitar lógica manual en JavaScript/C# en plantillas.
3. Representación de datos en tablas/listas: Encaje natural: tablas, cuadrículas y listas mapeadas inherentemente a arreglos.
4. Eficiencia de memoria: Los arreglos reducen la complejidad de la plantilla y la sobrecarga de vinculación de datos.
5. Integración con APIs/Fuentes de datos: Se alinea con datos centrados en JSON/arreglos (por ejemplo, APIs REST).

## **Cómo importar arreglos variables con marcadores inteligentes**
El siguiente ejemplo de código muestra cómo usar arrays variables en marcadores inteligentes. Colocamos un marcador de array variable en la celda A1 de la primera hoja de cálculo del libro dinámicamente que contiene una cadena de valores que establecemos para el marcador, procesamos los marcadores para llenar datos en las celdas contra el marcador. Finalmente, guardamos el archivo de Excel.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingVariableArray-1.cs" >}}

## **Cómo importar propiedades HTML con marcadores inteligentes**
The following sample code explains the use of HTML property of the Smart Markers. When it will be processed, it will show "World" in "Hello World" as bold because of HTML <b> tag.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingHTMLProperty-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
