---
title: Arbeitsblätter verwalten in Php
type: docs
weight: 10
url: /de/java/managing-worksheets-in-php/
---

## **Aspose.Cells - Arbeitsblätter verwalten**
### **Arbeitsblätter zu einer neuen Excel-Datei hinzufügen**
Um ein Arbeitsblatt zu einer neuen Excel-Datei mit **Aspose.Cells Java für PHP** hinzuzufügen, rufe einfach die Methode **add_worksheet** des Moduls **MangingWorksheets** auf.

**PHP-Code**

{{< highlight php >}}

 //Instantiating a Workbook object

$workbook = new Workbook();

//Adding a new worksheet to the Workbook object

$worksheets = $workbook->getWorksheets();

$sheetIndex = $worksheets->add();

$worksheet = $worksheets->get($sheetIndex);

//Setting the name of the newly added worksheet

$worksheet->setName("My Worksheet");

//Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

{{< /highlight >}}
### **Arbeitsblätter anhand des Blattnamens entfernen**
Um ein Arbeitsblatt anhand des Blattnamens mit **Aspose.Cells Java für PHP** zu entfernen, rufe einfach die Methode **remove_worksheet_by_name** des Moduls **MangingWorksheets** auf.

**PHP-Code**

{{< highlight php >}}

 //Creating a file stream containing the Excel file to be opened

$fstream = new FileInputStream($dataDir . "book.xls");

//Instantiating a Workbook object with the stream

$workbook = new Workbook($fstream);

//Removing a worksheet using its sheet name

$workbook->getWorksheets()->removeAt("Sheet1");

//Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

//Closing the file stream to free all resources

$fstream->close();

{{< /highlight >}}
### **Arbeitsblätter anhand des Blattindex entfernen**
Um ein Arbeitsblatt anhand des Blattindex mit **Aspose.Cells Java für PHP** zu entfernen, rufe einfach die Methode **remove_worksheet_by_index** des Moduls **MangingWorksheets** auf.

**PHP-Code**

{{< highlight php >}}

 //Creating a file stream containing the Excel file to be opened

$fstream=new FileInputStream($dataDir . "book.xls");

//Instantiating a Workbook object with the stream

$workbook = new Workbook($fstream);

//Removing a worksheet using its sheet index

$workbook->getWorksheets()->removeAt(0);

//Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

//Closing the file stream to free all resources

$fstream->close();

{{< /highlight >}}
## **Laufenden Code herunterladen**
Download **Arbeitsblätter verwalten (Aspose.Cells)** von einer der unten genannten sozialen Coding-Seiten:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets)
