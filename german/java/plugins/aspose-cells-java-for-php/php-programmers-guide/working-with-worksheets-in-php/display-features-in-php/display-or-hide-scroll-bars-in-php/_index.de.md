---
title: Anzeigen oder Ausblenden von Bildlaufleisten in Php
type: docs
weight: 20
url: /de/java/display-or-hide-scroll-bars-in-php/
---

## **Aspose.Cells - Scrollleisten anzeigen oder ausblenden**
### **Verbergen von Bildlaufleisten**
Um Bildlaufleisten in **Aspose.Cells Java für PHP** auszublenden, rufen Sie das Modul **displayhidescrollbars** auf.

**PHP-Code**

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
## **Laufenden Code herunterladen**
Laden Sie **Anzeigen oder Ausblenden von Bildlaufleisten (Aspose.Cells)** von einer der unten aufgeführten Social-Coding-Sites herunter:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideScrollBars.php)
