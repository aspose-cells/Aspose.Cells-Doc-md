---
title: Converti il libro di lavoro in HTML usando Aspose.Cells
type: docs
weight: 20
url: /it/java/convert-workbook-to-html-using-aspose-cells/
---

## **Aspose.Cells - Converti documento di lavoro in HTML**
Le API Aspose.Cells supportano l'esportazione di fogli di calcolo nel formato HTML. A questo scopo, **Aspose.Cells** utilizza la classe **HtmlSaveOptions** che consente agli sviluppatori di controllare diversi aspetti dell'HTML di output.

**Java**

{{< highlight java >}}

 //Specify the HTML Saving Options

HtmlSaveOptions save = new HtmlSaveOptions(SaveFormat.HTML);

//Instantiate a workbook and open the template XLSX file

Workbook book = new Workbook(dataDir + "book1.xls");

//Save the HTML file

book.save(dataDir + "AsposeHTMLSpreadsheet.html", save);

{{< /highlight >}}
## **Scarica il codice in esecuzione**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeConvertToHTML.java)

{{% alert color="primary" %}} 

Per ulteriori dettagli, visita [Conversazione dei file Excel in HTML](/cells/it/java/converting-workbook-to-different-formats/).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
