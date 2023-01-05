---
title: Bildlaufleisten in Php anzeigen oder ausblenden
type: docs
weight: 20
url: /de/java/display-or-hide-scroll-bars-in-php/
---
## **Aspose.Cells – Bildlaufleisten anzeigen oder ausblenden**
### **Bildlaufleisten ausblenden**
 So blenden Sie Bildlaufleisten mit aus**Aspose.Cells Java for PHP** , Anruf**Bildlaufleisten ausblenden** Modul.

**PHP-Code**

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
## **Laufcode herunterladen**
Download**Bildlaufleisten anzeigen oder ausblenden (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideScrollBars.php)
