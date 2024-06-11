---
title: 在PHP中将Excel文件转换为HTML
type: docs
weight: 20
url: /zh/java/converting-excel-files-to-html-in-php/
---

## **Aspose.Cells - 将Excel文件转换为HTML**
使用PHP中的Aspose.Cells for Java将Excel转换为HTML，只需调用Converter模块的worksheet_to_html()方法。

**PHP 代码**

{{< highlight php >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

//Save the document in PDF format

$workbook->save($dataDir . "OutBook1.html", $saveFormat->HTML);

{{< /highlight >}}
## **下载运行代码**
从以下提到的任何社交编码站点下载**将Excel文件转换为HTML（Aspose.Cells）**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingExcelFilesToHtml.php)
