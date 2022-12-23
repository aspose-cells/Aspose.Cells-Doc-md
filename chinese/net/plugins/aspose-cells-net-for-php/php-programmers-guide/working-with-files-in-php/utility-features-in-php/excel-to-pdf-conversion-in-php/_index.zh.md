---
title: 在 PHP 中将 Excel 转换为 PDF
type: docs
weight: 20
url: /zh/net/excel-to-pdf-conversion-in-php/
---
## **Aspose.Cells - Excel 到 PDF 转换**
将 Microsoft Excel 文件转换为 PDF

**PHP代码**

{{< highlight "php" >}}

         $dataDir = '';

        // Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array($dataDir . '/Book1.xls'));

        $ptr->Call($workbook,"Save",array($dataDir."/outBook1.pdf"));

        print "Conversion Completed" . PHP_EOL;

{{< /highlight >}}
## **下载运行代码**
下载**Excel 到 PDF 转换 (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/Excel2PDFConversion.php)
