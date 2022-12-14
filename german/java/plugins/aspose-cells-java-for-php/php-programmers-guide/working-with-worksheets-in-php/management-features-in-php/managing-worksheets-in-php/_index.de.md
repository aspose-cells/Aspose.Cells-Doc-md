---
title: Arbeitsblätter verwalten in Php
type: docs
weight: 10
url: /de/java/managing-worksheets-in-php/
---
## **Aspose.Cells – Verwalten von Arbeitsblättern**
### **Hinzufügen von Arbeitsblättern zu einer neuen Excel-Datei**
Um ein Arbeitsblatt zu einer neuen Excel-Datei hinzuzufügen, verwenden Sie**Aspose.Cells Java für PHP** , einfach anrufen**add_worksheet** Methode von**Arbeitsblätter verwalten** Modul.

**PHP-Code**

{{< highlight "php" >}}

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
### **Entfernen von Arbeitsblättern unter Verwendung des Blattnamens**
 So entfernen Sie Arbeitsblätter nach Blattnamen mit**Aspose.Cells Java für PHP** , einfach anrufen**remove_worksheet_by_name** Methode von**Arbeitsblätter verwalten** Modul.

**PHP-Code**

{{< highlight "php" >}}

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
### **Arbeitsblätter mit Blattindex entfernen**
 Um Arbeitsblatt für Blattindex zu entfernen, verwenden Sie**Aspose.Cells Java für PHP** , einfach anrufen**remove_worksheet_by_index** Methode von**Arbeitsblätter verwalten** Modul.

**PHP-Code**

{{< highlight "php" >}}

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
## **Laufcode herunterladen**
Download**Arbeitsblätter verwalten (Aspose.Cells)**von einer der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets)
