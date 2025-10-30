---
title: Importación inteligente de objetos anidados en Excel con marcadores inteligentes
type: docs
weight: 30
url: /es/net/how-to-import-nested-objects-with-smart-markers/
---

## **Por qué usar objetos anidados para marcadores inteligentes**
Smart Markers (in tools like FoxPro, reporting engines, or modern template systems) are placeholders that dynamically inject data into templates. Using nested objects (e.g., <<customer.address.city>>) enhances flexibility, organization, and expressiveness.

1. Representación de datos jerárquicos: Los datos del mundo real son inherentemente anidados (por ejemplo, un pedido contiene un cliente, que tiene una dirección). Los objetos anidados reflejan esta estructura, evitando campos aplanados/artificiales como cliente_ciudad.
2. Evitar colisiones de nombres: Las estructuras planas corren riesgo de conflictos (por ejemplo, nombre_del_producto vs. nombre_del_proveedor). El anidamiento delimita los nombres de forma natural:
<<product.name>> vs. <<supplier.name>>.
3. Modularidad & Reutilización: Reutilizar sub-objetos en diferentes contextos, el objeto Dirección puede integrarse en Marcadores de Cliente, Vendedor o Empleado. Los cambios en Dirección se propagan universalmente.
4. Simplified Data Binding: Bind entire nested objects to templates, <<order.customer>> auto-expands to all customer fields. Reduces manual mapping for sub-fields.
5. Dynamic Data Traversal: Traverse relationships on-demand, <<invoice.line_items[0].price>> accesses array elements or child objects. Enables complex queries without pre-processing.
6. Clearer Template Logic: Markers self-document relationships, <<user.profile.email>> is more intuitive than <<user_email>>. Reduces ambiguity in large templates.
7. Soporte de frameworks/herramientas: Los motores modernos (por ejemplo, Handlebars, React, FoxPro) resuelven internamente rutas anidadas. Compatible con JSON/APIs donde los datos anidados son estándar.

## **Cómo importar tipos anónimos u objetos personalizados con marcadores inteligentes**
Aspose.Cells también admite tipos anónimos u objetos personalizados en marcadores inteligentes. El ejemplo que sigue muestra cómo funciona esto. Para importar datos de objetos dinámicos utilizando Marcadores Inteligentes, visite el siguiente artículo:

[Importar desde objeto dinámico como origen de datos](/cells/es/net/import-data-into-worksheet/#importdataintoworksheet-importingfromdynamicobjectasdatasource)


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingAnonymousTypes-1.cs" >}}

## **Cómo importar objetos anidados con marcadores inteligentes**
Aspose.Cells soporta objetos anidados en marcadores inteligentes, los objetos anidados deben ser simples. Utilizamos un archivo de plantilla simple. Consulta la hoja de cálculo de diseño que contiene algunos marcadores inteligentes anidados.

|**La primera hoja de cálculo del archivo SM_NestedObjects.xlsx mostrando marcadores inteligentes anidados.**|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
El ejemplo que sigue muestra cómo funciona esto.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}


## **Cómo importar listas genéricas como objetos anidados con marcadores inteligentes**
Ahora Aspose.Cells también soporta usar una lista genérica como objeto anidado. Por favor, revisa la captura de pantalla del archivo excel de salida generado con el siguiente código. Como puedes ver en la captura de pantalla, un objeto de Profesor contiene varios objetos de Estudiante anidados.

|![todo:image_alt_text](using-smart-markers_8.png)|
| :- |

{{< gist  "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-SmartMarkers-UsingGenericList-1.cs" >}}

## **Cómo importar objetos anidados no línea por línea con marcadores inteligentes**
El método de procesamiento predeterminado actual es procesar los marcadores inteligentes línea por línea. Pero a veces los marcadores inteligentes de la misma tabla de datos deben procesarse juntos, sin importar 
si están en la misma fila o no, entonces debes especificar un rango con nombre "_CellsSmartMarkers" y especificar WorkbookDesigner.LineByLine como falso antes de llamar al procesamiento.

|![todo:image_alt_text](using-smart-markers_11.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-LayerByLayer.cs" >}}

{{< app/cells/assistant language="csharp" >}}
