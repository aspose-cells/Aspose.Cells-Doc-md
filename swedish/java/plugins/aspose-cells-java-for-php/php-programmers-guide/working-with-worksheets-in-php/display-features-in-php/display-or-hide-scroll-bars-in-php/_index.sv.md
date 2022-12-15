---
title: Visa eller dölj rullningslister i Php
type: docs
weight: 20
url: /sv/java/display-or-hide-scroll-bars-in-php/
---
## **Aspose.Cells - Visa eller dölj rullningslister**
### **Döljer rullningslister**
 För att dölja rullningslister med**Aspose.Cells Java for PHP** , ringa upp**visa gömmer rullningslister** modul.

**PHP-kod**

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
## **Ladda ner Running Code**
Ladda ner**Visa eller dölj rullningslister (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideScrollBars.php)
