---
title: Managing Worksheets in PHP
type: docs
weight: 10
url: /java/managing-worksheets-in-php/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Managing Worksheets**
### **Adding Worksheets to a New Excel File**
To add a worksheet to a new Excel file using **Aspose.Cells Java for PHP**, simply call the **add_worksheet** method of the **ManagingWorksheets** module.

**PHP Code**

{{< highlight php >}}

 // Instantiating a Workbook object

$workbook = new Workbook();

// Adding a new worksheet to the Workbook object

$worksheets = $workbook->getWorksheets();

$sheetIndex = $worksheets->add();

$worksheet = $worksheets->get($sheetIndex);

// Setting the name of the newly added worksheet

$worksheet->setName("My Worksheet");

// Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

{{< /highlight >}}
### **Removing Worksheets using Sheet Name**
To remove a worksheet by sheet name using **Aspose.Cells Java for PHP**, simply call the **remove_worksheet_by_name** method of the **ManagingWorksheets** module.

**PHP Code**

{{< highlight php >}}

 // Creating a file stream containing the Excel file to be opened

$fstream = new FileInputStream($dataDir . "book.xls");

// Instantiating a Workbook object with the stream

$workbook = new Workbook($fstream);

// Removing a worksheet using its sheet name

$workbook->getWorksheets()->removeAt("Sheet1");

// Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

// Closing the file stream to free all resources

$fstream->close();

{{< /highlight >}}
### **Removing Worksheets using Sheet Index**
To remove a worksheet by sheet index using **Aspose.Cells Java for PHP**, simply call the **remove_worksheet_by_index** method of the **ManagingWorksheets** module.

**PHP Code**

{{< highlight php >}}

 // Creating a file stream containing the Excel file to be opened

$fstream = new FileInputStream($dataDir . "book.xls");

// Instantiating a Workbook object with the stream

$workbook = new Workbook($fstream);

// Removing a worksheet using its sheet index

$workbook->getWorksheets()->removeAt(0);

// Saving the Excel file

$workbook->save($dataDir . "book.out.xls");

// Closing the file stream to free all resources

$fstream->close();

{{< /highlight >}}
## **Download Running Code**
Download **Managing Worksheets (Aspose.Cells)** from any of the below‑mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets)
