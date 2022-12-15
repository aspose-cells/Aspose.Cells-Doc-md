---
title: Mostra e nascondi le schede della cartella di lavoro utilizzando Aspose.Cells
type: docs
weight: 50
url: /it/java/display-and-hide-tabs-of-workbook-using-aspose-cells/
---
## **Aspose.Cells - Mostra e nascondi le schede della cartella di lavoro**
Aspose.Cells fornisce una classe, Workbook, che rappresenta un file Microsoft Excel. La classe Workbook fornisce un'ampia gamma di proprietà e metodi per la gestione di un file Excel. Per controllare la visibilità delle schede in un file Excel, gli sviluppatori possono utilizzare il metodo setShowTabs della classe Workbook.

**Giava**

{{< highlight "java" >}}

 //Instantiating a Workbook object by excel file path

Workbook workbook = new Workbook(dataDir + "book1.xls");

//Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(false);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeHideTabs.xls");

// ===============================================================

//Displaying the tabs of the Excel file

workbook.getSettings().setShowTabs(true);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeDisplayTabs.xls");

{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDisplayAndHideTabs.java)

