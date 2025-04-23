---
title: Mostrar apóstrofe inicial en celdas
type: docs
weight: 70
url: /es/net/show-leading-apostrophe-in-cells/
---

En Microsoft Excel, el apóstrofo inicial en el valor de la celda está oculto. Aspose.Cells proporciona la función para mostrar el apóstrofo de forma predeterminada. Para esto, la API proporciona la propiedad [Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle). Esta propiedad indica si establecer la propiedad [QuotePrefix](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) al ingresar el valor de cadena que comienza con una comilla simple a la celda. Establecer la propiedad [Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle) en **false** mostrará el apóstrofo inicial en el archivo de Excel de salida.

La siguiente captura de pantalla muestra el archivo de Excel de salida con el apóstrofe visible.

![todo:image_alt_text](show-leading-apostrophe-in-cells_1.jpg)

El siguiente fragmento de código demuestra esto agregando datos con Marcadores Inteligentes en el archivo de Excel fuente. Los archivos de Excel fuente y de salida se adjuntan para referencia.

[Archivo de origen](98107425.xlsx)

[Archivo de salida](98107426.xlsx)
## **Código de muestra**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-1.cs" >}}

La implementación de la clase *DataObject* se muestra a continuación

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-2.cs" >}}
{{< app/cells/assistant language="csharp" >}}
