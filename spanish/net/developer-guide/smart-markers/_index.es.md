---
title: Importación inteligente y colocación de datos con marcadores inteligentes
linktitle: Marcadores inteligentes
type: docs
weight: 190
url: /es/net/using-smart-markers/
description: Importar y colocar datos de manera inteligente según las plantillas de archivos de Excel con la biblioteca Aspose.Cells.
---

## **Por qué importar datos a Excel con marcadores inteligentes**
El uso de marcadores inteligentes para importar datos en Excel agiliza la integración de datos combinando un diseño basado en plantillas con enlace dinámico de datos. Este enfoque es especialmente valioso en herramientas como Aspose.Cells, donde los marcadores actúan como marcadores de posición en plantillas para rellenar automáticamente datos de diversas fuentes. A continuación, las principales razones para adoptar este método:

1. Eficiencia en informes repetitivos: Reutilización de plantillas, plantillas de Excel pre-diseñadas con marcadores incrustados (por ejemplo, &=$Variable, &=DataSource.Campo) que pueden reutilizarse en múltiples conjuntos de datos, eliminando la necesidad de reformatear manualmente. Por ejemplo, informes financieros o hojas de inventario solo requieren actualizar la fuente de datos, sin reconstruir los diseños. Enlace de datos automático, los marcadores inteligentes se vinculan directamente con las fuentes de datos (por ejemplo, bases de datos, JavaBeans, arreglos). Los cambios en los datos fuente se reflejan automáticamente en el archivo de Excel generado después del proceso, reduciendo errores de copiar y pegar.

2. Soporte para estructuras de datos complejas: Integración multifuente, una misma plantilla puede combinar datos de varias fuentes (por ejemplo, variables, arreglos, ResultSets). Manejo de datos jerárquicos, datos anidados (por ejemplo, registros agrupados) pueden ser procesados usando marcadores como &=subtotal9:Persona.id para generar resúmenes (sumas, promedios) por grupo directamente en Excel.

3. Preservación de la funcionalidad de Excel: Los marcadores inteligentes coexisten con funciones de Excel como fórmulas, formato condicional y gráficos. Por ejemplo: cálculos dinámicos usando &==C{r}*D{r} aplican fórmulas específicas por fila durante la inyección de datos. Las plantillas mantienen estilos predefinidos (por ejemplo, encabezados, colores de celdas), garantizando coherencia sin ajustes posteriores a la importación.

4. Capacidades avanzadas de automatización: Integración con fuentes de datos personalizadas, los desarrolladores pueden implementar interfaces como ICellsDataTable (en .NET) para mapear estructuras de datos propietarias a los marcadores. Esta flexibilidad soporta datos en tiempo real provenientes de API o sensores. Procesamiento por lotes, herramientas como Aspose.Cells’ WorkbookDesigner permiten operaciones masivas (por ejemplo, generar más de 1,000 facturas en una sola ejecución) recorriendo conjuntos de datos.

5. Menor esfuerzo de desarrollo y mantenimiento: Separación de lógica y diseño, los diseñadores gestionan plantillas en Excel (sin codificación), mientras que los desarrolladores gestionan la lógica de datos. Esta división acelera iteraciones. Reducción de errores, el mapeo automatizado de datos minimiza riesgos de entrada manual. Por ejemplo, datos de sensores analizados en VC++ pueden completarse automáticamente en plantillas de Excel mediante interfaces de objetos, evitando errores de transcripción.

## **Código de ejemplo para importar DataTable con marcadores inteligentes**
El siguiente código de ejemplo tiene una fuente de datos con 6 registros. Queremos mostrar solo 3 registros en una hoja, y los otros registros se moverán automáticamente a la segunda hoja. Ten en cuenta que la segunda hoja también debe tener la misma etiqueta de marcador inteligente y debes llamar al método [WorkbookDesigner.Process(sheetIndex, isPreserved)](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/process/methods/2) en ambas hojas. Consulta el [archivo de Excel generado](SmartMarkerDataTableToExcel.xlsx) por el código como referencia.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-ImportDataTableToExcel.cs" >}}

## **Código de ejemplo para importar datos JSON con marcadores inteligentes**
Aspose.Cells for .NET admite datos JSON en marcadores inteligentes. El código de ejemplo carga una plantilla de tabla, importa datos JSON de manera inteligente para completar, y luego calcula los datos de la tabla. Por favor, revisa [archivo de plantilla](table.xlsx), [archivo JSON](table.json) y la captura de pantalla del archivo Excel generado con el siguiente código.

|**La primera hoja de trabajo del archivo table.xlsx muestra marcadores inteligentes.**|
| :- |
|![todo:image_alt_text](tabletemplate.png)|

|**La captura de pantalla del archivo excel de salida.**|
| :- |
|![todo:image_alt_text](tableresult.png)|

Datos json de la siguiente manera:
```json data
{
	"Items" : [
		{
			"ItemName" : "A123",
			"Description" : "Peonies",
			"Qty" : "55",
			"UnitPrice" : "3.05"			
		},
		{
			"ItemName" : "B456",
			"Description" : "Tulips",
			"Qty" : "45",
			"UnitPrice" : "2.66",
		},
		{
			"ItemName" : "K789",
			"Description" : "Buttercup",
			"Qty" : "68",
			"UnitPrice" : "8.35",
		}
	]
}
```
El ejemplo que sigue muestra cómo funciona esto.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-ImportJsonToTable.cs" >}}

## **Código de ejemplo para importar objetos anidados con marcadores inteligentes**
Aspose.Cells soporta objetos anidados en marcadores inteligentes, los objetos anidados deben ser simples. Utilizamos un archivo de plantilla simple. Consulta la hoja de cálculo de diseño que contiene algunos marcadores inteligentes anidados.

|**La primera hoja de cálculo del archivo SM_NestedObjects.xlsx mostrando marcadores inteligentes anidados.**|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
El ejemplo que sigue muestra cómo funciona esto.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}


## **Temas avanzados**
- [Parámetros de marcadores inteligentes](/cells/es/net/smart-marker-parameters/)
- [Agregar un Objeto Anónimo o Personalizado en los Marcadores Inteligentes](/cells/es/net/adding-anonymous-or-custom-object-into-smartmarkers/)
- [Autocompletar Datos de Marcador Inteligente en Otras Hojas de Cálculo si los Datos son muy Grandes](/cells/es/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [Formateando Marcadores Inteligentes](/cells/es/net/formatting-smart-markers/)
- [Recibir notificaciones mientras se fusionan datos con Marcadores Inteligentes](/cells/es/net/getting-notifications-while-merging-data-with-smart-markers/)
- [Establecer fuente de datos personalizada para WorkbookDesigner](/cells/es/net/set-custom-datasource-for-workbookdesigner/)
- [Mostrar apóstrofo inicial en celdas](/cells/es/net/show-leading-apostrophe-in-cells/)
- [Usar parámetro de fórmula en campo de Marcador Inteligente](/cells/es/net/using-formula-parameter-in-smart-marker-field/)
- [Importación inteligente de elementos de matrices por índice en Excel con marcadores inteligentes](/cells/es/net/how-to-import-array-element-by-index-with-smart-markers/)
- [Importación inteligente de elementos de matrices por segmentador en Excel con marcadores inteligentes](/cells/es/net/how-to-import-array-element-by-slicer-with-smart-markers/)
- [Importación inteligente de JSON en Excel con marcadores inteligentes](/cells/es/net/how-to-import-json-into-excel-with-smart-markers/)
- [Importación inteligente de objetos anidados en Excel con marcadores inteligentes](/cells/es/net/how-to-import-nested-objects-with-smart-markers/)
- [Importación inteligente de matrices variables en Excel con marcadores inteligentes](/cells/es/net/how-to-import-variable-arrays-with-smart-markers/)
- [Cómo usar marcadores de imágenes en marcadores inteligentes](/cells/es/net/how-to-use-image-markers-in-smart-markers/)
- [Cómo agrupar datos en marcadores inteligentes](/cells/es/net/how-to-group-data-in-smart-markers/)

{{< app/cells/assistant language="csharp" >}}
