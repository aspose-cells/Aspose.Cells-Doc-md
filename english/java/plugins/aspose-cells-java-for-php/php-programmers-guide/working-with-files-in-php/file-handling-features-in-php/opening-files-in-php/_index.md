---
title: Opening Files in PHP
type: docs
weight: 10
url: /java/opening-files-in-php/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Simple Ways to Open Excel Files**
### **Opening through Path**
Simply open a Microsoft Excel file by referencing the file's path.

**PHP Code**

{{< highlight php >}}
$dataDir = '';

$workbook1 = new Workbook($dataDir . "Book1.xls");
{{< /highlight >}}

### **Opening through Stream**
Sometimes, the Excel file that you want to open is stored as a stream. In that case, use an overloaded version of the Open method that takes a Stream object containing the Excel file.

**PHP Code**

{{< highlight php >}}
$fstream = new FileInputStream($dataDir . "Book2.xls");

// Creating a Workbook object with the stream object
$workbook2 = new Workbook($fstream);

$fstream->close();
{{< /highlight >}}

## **Download Sample Code**
Download **Opening Files (Aspose.Cells)** from any of the social coding sites mentioned below:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
