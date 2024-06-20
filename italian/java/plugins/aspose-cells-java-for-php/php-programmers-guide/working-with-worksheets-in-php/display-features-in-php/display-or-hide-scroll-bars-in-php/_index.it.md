---
title: Mostra o nascondi le barre di scorrimento in Php
type: docs
weight: 20
url: /it/java/display-or-hide-scroll-bars-in-php/
---

## **Aspose.Cells - Visualizza o Nascondi Barre di Scorrimento**
### **Nascondere le barre di scorrimento**
Per nascondere le barre di scorrimento utilizzando **Aspose.Cells Java per PHP**, chiamare il modulo **displayhidescrollbars**.

**Codice PHP**

{{< highlight php >}}

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
Scarica **Visualizza o Nascondi Barre di Scorrimento (Aspose.Cells)** da uno dei siti di codice sociale sotto indicati:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideScrollBars.php)
