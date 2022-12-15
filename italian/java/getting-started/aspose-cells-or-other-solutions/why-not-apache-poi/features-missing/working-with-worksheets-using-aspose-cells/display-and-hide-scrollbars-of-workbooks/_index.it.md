---
title: Mostra e nascondi le barre di scorrimento delle cartelle di lavoro
type: docs
weight: 40
url: /it/java/display-and-hide-scrollbars-of-workbooks/
---
## **Aspose.Cells - Mostra e nascondi le barre di scorrimento delle cartelle di lavoro**
 Aspose.Cells offre un corso,**Cartella di lavoro** che rappresenta un file Excel.**Cartella di lavoro** class fornisce un'ampia gamma di proprietà e metodi per gestire un file Excel. Tuttavia, per controllare la visibilità delle barre di scorrimento nel file Excel, gli sviluppatori possono utilizzare**setVScrollBarVisible** & **setHScrollBarVisible** metodi del**Cartella di lavoro** classe.

**Giava**

{{< highlight "java" >}}

 //Instantiating a Excel object by excel file path

Workbook workbook = new Workbook(dataDir + "book1.xls");

//Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(false);

//Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeSrollbarsHide.xls");

// ===============================================================

//Displaying the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(true);

//Displaying the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(true);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeDisplaySrollbars.xls");


{{< /highlight >}}
## **Scarica il codice in esecuzione**

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDisplayAndHideScrollbars.java)
