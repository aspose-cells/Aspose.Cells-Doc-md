---
title: 在 PHP 中将 Excel 转换为 PDF 文件
type: docs
weight: 30
url: /zh/java/converting-excel-to-pdf-files-in-php/
---
## **Aspose.Cells - 将 Excel 转换为 PDF 文件**
要在 PHP 中使用 Aspose.Cells for Java 将 Excel 转换为 Pdf 文件，只需调用 excel_至_Converter 模块的 pdf() 方法。

**PHP代码**

{{< highlight "php" >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

        //Save the document in PDF format

$workbook->save($dataDir . "OutBook1.pdf", $saveFormat->PDF);

{{< /highlight >}}
## **下载运行代码**
下载**将 Excel 转换为 PDF 文件 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/Excel2PdfConversion.php)
