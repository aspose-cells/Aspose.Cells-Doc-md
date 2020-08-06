---
title: Hide or Unhide a Worksheet in Php
type: docs
weight: 50
url: /java/hide-or-unhide-a-worksheet-in-php/
---

## **Aspose.Cells - Hide or Unhide a Worksheet**
##### **Hiding a Worksheet**
To hide worksheet using Aspose.Cells Java for PHP, call **hideunhideworksheet** module.

**PHP Code**

{{< highlight php >}}

 //Instantiating a Workbook object by excel file path

$workbook = new Workbook($dataDir . "book1.xls");

//Accessing the first worksheet in the Excel file

$worksheets = $workbook->getWorksheets();

$worksheet = $worksheets->get(0);

//Hiding the first worksheet of the Excel file

$worksheet->setVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

$workbook->save($dataDir . "output.xls");


{{< /highlight >}}
## **Download Running Code**
Download **Hide or Unhide a Worksheet (Aspose.Cells)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/HideUnhideWorksheet.php)
