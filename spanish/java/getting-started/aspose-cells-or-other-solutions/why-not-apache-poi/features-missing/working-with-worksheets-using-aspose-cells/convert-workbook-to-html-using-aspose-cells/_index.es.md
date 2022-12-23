---
title: Convierta Workbook a HTML usando Aspose.Cells
type: docs
weight: 20
url: /es/java/convert-workbook-to-html-using-aspose-cells/
---
## **Aspose.Cells - Convertir libro de trabajo a HTML**
 Las API Aspose.Cells brindan soporte para exportar hojas de cálculo al formato HTML. Para este propósito,**Aspose.Cells** usa el**HtmlSaveOptions** clase que permite a los desarrolladores controlar varios aspectos de la salida HTML.

**Java**

{{< highlight "java" >}}

 //Specify the HTML Saving Options

HtmlSaveOptions save = new HtmlSaveOptions(SaveFormat.HTML);

//Instantiate a workbook and open the template XLSX file

Workbook book = new Workbook(dataDir + "book1.xls");

//Save the HTML file

book.save(dataDir + "AsposeHTMLSpreadsheet.html", save);

{{< /highlight >}}
## **Descargar código de ejecución**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeConvertToHTML.java)

{{% alert color="primary" %}} 

 Para más detalles, visite[Conversión de archivos de Excel a HTML](/cells/es/java/converting-workbook-to-different-formats/).

{{% /alert %}}
