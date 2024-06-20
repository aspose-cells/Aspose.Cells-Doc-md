---
title: Arbeitsblatt in Php ausblenden oder einblenden
type: docs
weight: 50
url: /de/java/hide-or-unhide-a-worksheet-in-php/
---

## **Aspose.Cells - Arbeitsblatt ausblenden oder einblenden**
### **Arbeitsblatt ausblenden**
Um ein Arbeitsblatt mithilfe von Aspose.Cells Java for PHP auszublenden, rufen Sie einfach das Modul **hideunhideworksheet** auf.

**PHP-Code**

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
## **Laufenden Code herunterladen**
Download von **Arbeitsblatt ausblenden oder einblenden (Aspose.Cells)** von einer der unten genannten sozialen Coding-Seiten:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/HideUnhideWorksheet.php)
