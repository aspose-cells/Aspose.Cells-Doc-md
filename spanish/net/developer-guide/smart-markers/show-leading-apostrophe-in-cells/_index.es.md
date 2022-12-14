---
title: Mostrar el apóstrofo inicial en las celdas
type: docs
weight: 70
url: /es/net/show-leading-apostrophe-in-cells/
---
 En Microsoft Excel, el apóstrofo inicial en el valor de la celda está oculto. Aspose.Cells proporciona la función para mostrar el apóstrofo de forma predeterminada. Para esto, el API proporciona[Libro de trabajo.Configuración.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle) propiedad. Esta propiedad indica si se debe establecer el[Prefijo de cotización](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)propiedad al ingresar un valor de cadena que comienza con una comilla simple en la celda. Configuración de la[Libro de trabajo.Configuración.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle) propiedad a**falso**mostrará el apóstrofe inicial en el archivo de salida de Excel.

La siguiente captura de pantalla muestra el archivo de salida de Excel con el apóstrofo visible.

![todo:imagen_alternativa_texto](show-leading-apostrophe-in-cells_1.jpg)

El siguiente fragmento de código demuestra esto mediante la adición de datos con marcadores inteligentes en el archivo de origen de Excel. Los archivos de Excel de origen y salida se adjuntan como referencia.

[Archivo fuente](98107425.xlsx)

[Archivo de salida](98107426.xlsx)
## **Código de muestra**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-1.cs" >}}

La implementación de*Objeto de datos*la clase se da a continuación

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-2.cs" >}}
