﻿---
title: Convierta el libro de trabajo a HTML en xlsx4j
type: docs
weight: 10
url: /es/java/convert-workbook-to-html-in-xlsx4j/
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
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/converttohtml/AsposeConvertToHTML.java)

{{% alert color="primary" %}} 

 Para más detalles, visite[Conversión de archivos de Excel a HTML](/cells/es/java/converting-workbook-to-different-formats/).

{{% /alert %}}
