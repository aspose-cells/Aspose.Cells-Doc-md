---
title: Hantera arbetsblad i Php
type: docs
weight: 10
url: /sv/java/managing-worksheets-in-php/
---

## **Aspose.Cells - Hantera kalkylblad**
### **Lägga till kalkylblad i en ny Excelfil**
För att lägga till arbetsblad i en ny Excelfil med **Aspose.Cells Java for PHP**, anropa helt enkelt **add_worksheet**-metoden i **MangingWorksheets**-modulen.

**PHP-kod**

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
### **Ta bort kalkylblad med hjälp av kalkylbladsnamn**
För att ta bort arbetsblad efter arknamn med **Aspose.Cells Java for PHP**, anropa helt enkelt **remove_worksheet_by_name**-metoden i **MangingWorksheets**-modulen.

**PHP-kod**

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
### **Ta bort kalkylblad med hjälp av kalkylbladsindex**
För att ta bort arbetsblad efter arkindex med **Aspose.Cells Java for PHP**, anropa helt enkelt **remove_worksheet_by_index**-metoden i **MangingWorksheets**-modulen.

**PHP-kod**

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
## **Ladda ned körbar kod**
Ladda ner **Hantera kalkylblad (Aspose.Cells)** från någon av nedan nämnda sociala kodbaser:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets)
