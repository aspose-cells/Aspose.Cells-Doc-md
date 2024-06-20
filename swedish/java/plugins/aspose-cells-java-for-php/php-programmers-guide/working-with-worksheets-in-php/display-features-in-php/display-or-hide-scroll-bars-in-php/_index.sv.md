---
title: Visa eller dölj rullningsfält i PHP
type: docs
weight: 20
url: /sv/java/display-or-hide-scroll-bars-in-php/
---

## **Aspose.Cells - Visa eller dölj rullningsfält**
### **Dölja bildrullningsfält**
För att dölja rullningsfält med **Aspose.Cells Java för PHP**, anropa **displayhidescrollbars** modulen.

**PHP-kod**

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
## **Ladda ned körbar kod**
Ladda ner **Visa eller dölj rullningsfält (Aspose.Cells)** från någon av sociala kodningsplatserna nedan:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideScrollBars.php)
