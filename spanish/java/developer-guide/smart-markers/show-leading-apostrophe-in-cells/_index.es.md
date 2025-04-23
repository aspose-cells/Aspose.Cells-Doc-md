---
title: Mostrar apóstrofe inicial en celdas
type: docs
weight: 20
url: /es/java/show-leading-apostrophe-in-cells/
---

## **Mostrar apóstrofo inicial en celdas**

En Microsoft Excel, el apóstrofe inicial en el valor de la celda está oculto. Aspose.Cells proporciona la característica de mostrar el apóstrofe por defecto. Para esto, la API proporciona la propiedad [**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle). Esta propiedad indica si se debe establecer la propiedad [**QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/Style#QuotePrefix) al ingresar un valor de cadena que comienza con una comilla simple en la celda. Establecer la propiedad [**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle) en **falso** mostrará el apóstrofe inicial en el archivo de Excel de salida.

La siguiente captura de pantalla muestra el archivo de Excel de salida con el apóstrofe visible.

![todo:image_alt_text](show-leading-apostrophe-in-cells_1.jpg)

El siguiente fragmento de código demuestra esto agregando datos con Marcadores Inteligentes en el archivo de Excel fuente. Los archivos de Excel fuente y de salida se adjuntan para referencia.

[Archivo Fuente](AllowLeadingApostropheSample.xlsx)

[Archivo de Salida](AllowLeadingApostropheSample_out.xlsx)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AllowLeadingApostrophe-1.java" >}}

La implementación de la clase *DataObject* se muestra a continuación

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HelperClasses-DataObject-1.java" >}}
{{< app/cells/assistant language="java" >}}
