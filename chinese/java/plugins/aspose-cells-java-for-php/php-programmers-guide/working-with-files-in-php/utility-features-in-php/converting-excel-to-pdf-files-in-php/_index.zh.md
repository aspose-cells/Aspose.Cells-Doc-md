---
title: 在PHP中将Excel转换为PDF文件
type: docs
weight: 30
url: /zh/java/converting-excel-to-pdf-files-in-php/
---

## **Aspose.Cells - 将Excel转换为PDF文件**
使用PHP中的Aspose.Cells for Java将Excel转换为PDF文件，只需调用Converter模块的excel_to_pdf()方法。

**PHP 代码**

{{< highlight php >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

        //Save the document in PDF format

$workbook->save($dataDir . "OutBook1.pdf", $saveFormat->PDF);

{{< /highlight >}}
## **下载运行代码**
从以下提到的任何社交编码站点下载**将Excel转换为PDF文件（Aspose.Cells）**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/Excel2PdfConversion.php)
