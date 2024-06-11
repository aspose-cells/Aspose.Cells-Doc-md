---
title: 在PHP中将转换为MHTML文件
type: docs
weight: 40
url: /zh/java/converting-to-mhtml-files-in-php/
---

## **Aspose.Cells - 将文件转换为MHTML文件**
使用PHP中的Aspose.Cells for Java将工作表转换为MHTML文件，只需调用Converter模块的worksheet_to_mhtml()方法。

**PHP 代码**

{{< highlight php >}}

 $sveFormat = new SaveFormat();

//Specify the file path

$filePath = $dataDir . "Book1.xlsx";

//Specify the HTML saving options

$sv = new HtmlSaveOptions($sveFormat->M_HTML);

//Instantiate a workbook and open the template XLSX file

$wb = new Workbook($filePath);

//Save the MHT file

$wb->save($filePath . ".out.mht", $sv);

{{< /highlight >}}
## **下载运行代码**
从以下提到的任何社交编码站点下载**将文件转换为MHTML文件（Aspose.Cells）**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingToMhtmlFiles.php)
