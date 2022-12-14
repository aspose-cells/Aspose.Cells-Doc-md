---
title: Hantera arbetsblad i Php
type: docs
weight: 10
url: /sv/java/managing-worksheets-in-php/
---
## **Aspose.Cells - Hantera arbetsblad**
### **Lägga till arbetsblad i en ny Excel-fil**
För att lägga till kalkylblad i en ny Excel-fil med**Aspose.Cells Java för PHP** , ring helt enkelt**add_worksheet** metod av**Hantera arbetsblad** modul.

**PHP-kod**

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
### **Ta bort kalkylblad med Sheet Name**
 För att ta bort kalkylblad efter arknamn med**Aspose.Cells Java för PHP** , ring helt enkelt**remove_worksheet_by_name** metod av**Hantera arbetsblad** modul.

**PHP-kod**

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
### **Ta bort kalkylblad med Sheet Index**
 För att ta bort kalkylblad för ark index med**Aspose.Cells Java för PHP** , ring helt enkelt**remove_worksheet_by_index** metod av**Hantera arbetsblad** modul.

**PHP-kod**

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
## **Ladda ner Running Code**
Ladda ner**Hantera arbetsblad (Aspose.Cells)**från någon av nedan nämnda webbplatser för social kodning:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets)
