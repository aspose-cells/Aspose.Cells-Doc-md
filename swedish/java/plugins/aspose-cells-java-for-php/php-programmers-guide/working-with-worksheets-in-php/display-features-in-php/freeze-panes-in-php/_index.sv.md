---
title: Frys rutor i Php
type: docs
weight: 40
url: /sv/java/freeze-panes-in-php/
---
## **Aspose.Cells - Frys rutor**
 För att frysa rutor i kalkylarksdokumentet med**Aspose.Cells Java for PHP** , helt enkelt åberopa**FreezePanes** modul.

**PHP-kod**

{{< highlight "php" >}}

 //Instantiating a Excel object by excel file path

$workbook = new Workbook($dataDir . "book.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Applying freeze panes settings

$worksheet->freezePanes(3,2,3,2);

//Saving the modified Excel file in default format

$workbook->save($dataDir . "book.out.xls");

{{< /highlight >}}
## **Ladda ner Running Code**
Ladda ner**Frys rutor (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/FreezePanes.php)
