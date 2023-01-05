---
title: Visa eller dölj rutnät i Php
type: docs
weight: 10
url: /sv/java/display-or-hide-gridlines-in-php/
---
## **Aspose.Cells - Visa eller dölj rutnätslinjer**
### **Dölja rutnät**
 För att dölja kalkylblad med**Aspose.Cells Java for PHP** , ringa upp**visahidegridlines** modul.

**PHP-kod**

{{< highlight "php" >}}

 data_dir = File.dirname(File.dirname(File.dirname(__FILE__))) + '/data/'

//Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Hiding the grid lines of the first worksheet of the Excel file

$worksheet->setGridlinesVisible(false);

//Saving the modified Excel file in default (that is Excel 2000) format

$workbook->save($dataDir . "output.xls");


{{< /highlight >}}
## **Ladda ner Running Code**
Ladda ner**Visa eller dölj rutnät (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/DisplayHideGridlines.php)
