+++
title = "Converting Excel Files to HTML in PHP" 
description = "" 
weight = 24834 
+++

Aspose.Cells for Java : Converting Excel Files to HTML in PHP  

# Aspose.Cells for Java : Converting Excel Files to HTML in PHP


## Aspose.Cells - Converting Excel Files to HTML

To convert Excel to HTML using Aspose.Cells for Java in PHP, simply invoke worksheet\_to\_html() method of Converter module.

**PHP Code**

{{< code lang="cs" >}}
$saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

//Save the document in PDF format
$workbook->save($dataDir . "OutBook1.html", $saveFormat->HTML);
{{< /code >}}

## Download Running Code

Download **Converting Excel Files to HTML (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingExcelFilesToHtml.php)

