---
title: Visa eller dölj flikar i PHP
type: docs
weight: 30
url: /sv/java/display-or-hide-tabs-in-php/
---

## **Aspose.Cells - Visa eller dölj flikar**
### **Gömma flikar**
För att dölja flikar med **Aspose.Cells Java for PHP**, anropa **displayhidetabs**-modulen.

**PHP-kod**

{{< highlight php >}}

 //Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Hiding the tabs of the Excel file

$workbook->getSettings()->setShowTabs(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir + "output.xls");

{{< /highlight >}}
## **Ladda ned körbar kod**
Ladda ner **Dölj eller visa flikar (Aspose.Cells)** från någon av sociala kodningsplatserna nedan:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideTabs.php)
