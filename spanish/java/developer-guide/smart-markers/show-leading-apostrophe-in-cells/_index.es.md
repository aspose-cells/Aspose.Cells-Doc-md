---
title: Mostrar el apóstrofo inicial en las celdas
type: docs
weight: 20
url: /es/java/show-leading-apostrophe-in-cells/
---
## **Mostrar el apóstrofo inicial en las celdas**

En Microsoft Excel, el apóstrofo inicial en el valor de la celda está oculto. Aspose.Cells proporciona la función para mostrar el apóstrofo de forma predeterminada. Para esto, el API proporciona[**Libro de trabajo.Configuración.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle)propiedad. Esta propiedad indica si se debe establecer el[**Prefijo de cotización**](https://reference.aspose.com/cells/java/com.aspose.cells/Style#QuotePrefix)propiedad al ingresar un valor de cadena que comienza con una comilla simple en la celda. Configuración de la[**Libro de trabajo.Configuración.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle)propiedad a**falso**mostrará el apóstrofe inicial en el archivo de salida de Excel.

La siguiente captura de pantalla muestra el archivo de salida de Excel con el apóstrofo visible.

![todo:imagen_alternativa_texto](show-leading-apostrophe-in-cells_1.jpg)

El siguiente fragmento de código demuestra esto mediante la adición de datos con marcadores inteligentes en el archivo de origen de Excel. Los archivos de Excel de origen y salida se adjuntan como referencia.

[Archivo fuente](AllowLeadingApostropheSample.xlsx)

[Archivo de salida](AllowLeadingApostropheSample_out.xlsx)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AllowLeadingApostrophe-1.java" >}}

La implementación de*Objeto de datos*la clase se da a continuación

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HelperClasses-DataObject-1.java" >}}
