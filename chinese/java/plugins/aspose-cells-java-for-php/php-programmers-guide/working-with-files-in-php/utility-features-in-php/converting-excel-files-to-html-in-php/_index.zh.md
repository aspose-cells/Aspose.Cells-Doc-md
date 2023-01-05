---
title: 在 PHP 中将 Excel 文件转换为 HTML
type: docs
weight: 20
url: /zh/java/converting-excel-files-to-html-in-php/
---
## **Aspose.Cells - 将 Excel 文件转换为 HTML**
要在 PHP 中使用 Aspose.Cells for Java 将 Excel 转换为 HTML，只需调用工作表_到_Converter 模块的 html() 方法。

**PHP代码**

{{< highlight "php" >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

//Save the document in PDF format

$workbook->save($dataDir . "OutBook1.html", $saveFormat->HTML);

{{< /highlight >}}
## **下载运行代码**
下载**将 Excel 文件转换为 HTML (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingExcelFilesToHtml.php)
