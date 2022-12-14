---
title: Mostra o nascondi le barre di scorrimento in Php
type: docs
weight: 20
url: /it/java/display-or-hide-scroll-bars-in-php/
---
## **Aspose.Cells - Mostra o nascondi le barre di scorrimento**
### **Nascondere le barre di scorrimento**
 Per nascondere le barre di scorrimento utilizzando**Aspose.Cells Java per PHP** , chiamata**displayhidescrollbars** modulo.

**Codice PHP**

{{< highlight "php" >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the vertical scroll bar of the Excel file

$workbook->getSettings()->setVScrollBarVisible(false);

//Hiding the horizontal scroll bar of the Excel file

$workbook->getSettings()->setHScrollBarVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "output.xls");

{{< /highlight >}}
## **Scarica il codice in esecuzione**
Scarica**Visualizzare o nascondere le barre di scorrimento (Aspose.Cells)**da uno qualsiasi dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideScrollBars.php)
