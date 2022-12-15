---
title: Converti la cartella di lavoro in HTML usando Aspose.Cells
type: docs
weight: 20
url: /it/java/convert-workbook-to-html-using-aspose-cells/
---
## **Aspose.Cells - Converti la cartella di lavoro in HTML**
 Le API Aspose.Cells forniscono supporto per l'esportazione di fogli di calcolo in formato HTML. Per questo scopo,**Aspose.Cells** utilizza il**HtmlSaveOptions** class che consente agli sviluppatori di controllare diversi aspetti dell'output HTML.

**Giava**

{{< highlight "java" >}}

 //Specify the HTML Saving Options

HtmlSaveOptions save = new HtmlSaveOptions(SaveFormat.HTML);

//Instantiate a workbook and open the template XLSX file

Workbook book = new Workbook(dataDir + "book1.xls");

//Save the HTML file

book.save(dataDir + "AsposeHTMLSpreadsheet.html", save);

{{< /highlight >}}
## **Scarica il codice in esecuzione**

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeConvertToHTML.java)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Conversione di file Excel in HTML](/cells/it/java/converting-workbook-to-different-formats/).

{{% /alert %}}
