---
title: Ein Arbeitsblatt in Php ein- oder ausblenden
type: docs
weight: 50
url: /de/java/hide-or-unhide-a-worksheet-in-php/
---
## **Aspose.Cells – Ausblenden oder Einblenden eines Arbeitsblatts**
### **Ausblenden eines Arbeitsblatts**
 Um das Arbeitsblatt mit Aspose.Cells Java für PHP auszublenden, rufen Sie an**verbergenarbeitsblatt einblenden** Modul.

**PHP-Code**

{{< highlight "php" >}}

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
## **Laufcode herunterladen**
Download**Ein Arbeitsblatt ein- oder ausblenden (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/DisplayFeatures/HideUnhideWorksheet.php)
