+++
title = "Converting to MHTML Files in PHP" 
description = "" 
weight = 24836 
+++

Aspose.Cells for Java : Converting to MHTML Files in PHP  

# Aspose.Cells for Java : Converting to MHTML Files in PHP


## Aspose.Cells - Converting to MHTML Files

To convert Worksheet to MHTML file using Aspose.Cells for Java in PHP, simply invoke worksheet\_to\_mhtml() method of Converter module.

**PHP Code**

{{< code lang="cs" >}}
$sveFormat = new SaveFormat();

//Specify the file path
$filePath = $dataDir . "Book1.xlsx";

//Specify the HTML saving options
$sv = new HtmlSaveOptions($sveFormat->M_HTML);

//Instantiate a workbook and open the template XLSX file
$wb = new Workbook($filePath);

//Save the MHT file
$wb->save($filePath . ".out.mht", $sv);
{{< /code >}}

## Download Running Code

Download **Converting to MHTML Files (Aspose.Cells)** from any of the below mentioned social coding sites:

*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingToMhtmlFiles.php)

