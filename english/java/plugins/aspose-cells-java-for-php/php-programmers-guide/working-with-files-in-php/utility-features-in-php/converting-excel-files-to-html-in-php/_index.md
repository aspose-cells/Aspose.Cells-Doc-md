---
title: Converting Excel Files to HTML in PHP
type: docs
weight: 20
url: /java/converting-excel-files-to-html-in-php/
---

## **Aspose.Cells - Converting Excel Files to HTML**
To convert Excel to HTML using Aspose.Cells for Java in PHP, simply invoke worksheet_to_html() method of Converter module.

**PHP Code**

{{< highlight php >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

//Save the document in PDF format

$workbook->save($dataDir . "OutBook1.html", $saveFormat->HTML);

{{< /highlight >}}
## **Download Running Code**
Download **Converting Excel Files to HTML (Aspose.Cells)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingExcelFilesToHtml.php)
