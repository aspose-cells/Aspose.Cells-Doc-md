---
title : "Opening Files in PHP" 
description : "" 
weight : 24830 
toc : false
type: docs
url: /java/plugins/php/guide/filesinphp/filehandling/opening+files+in+php/
---

# Aspose.Cells for Java : Opening Files in PHP


## Aspose.Cells - Simple Ways to Open Excel Files

##### Opening through Path

Simply open a Microsoft Excel file by referencing the file's path

**PHP Code**

{{< code lang="cs" >}}
$dataDir = '';
$workbook1 = new Workbook($dataDir . "Book1.xls");
{{< /code >}}

##### Opening through Stream

Sometimes, the Excel file that you want to open is stored as a stream. In that case, use an overloaded version of the`Open`method that takes the`Stream`object that contains the Excel file to open the file.

**PHP Code**

{{< code lang="cs" >}}
$fstream = new FileInputStream($dataDir . "Book2.xls");
//Creating an Workbook object with the stream object
$workbook2 = new Workbook($fstream);
$fstream->close();
{{< /code >}}

## Download Running Code

Download **Opening Files (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)

