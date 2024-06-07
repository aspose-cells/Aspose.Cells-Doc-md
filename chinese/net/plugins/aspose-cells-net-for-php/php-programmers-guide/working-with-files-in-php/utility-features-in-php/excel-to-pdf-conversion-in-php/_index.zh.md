---
title: 在PHP中将Excel转换为PDF
type: docs
weight: 20
url: /zh/net/excel-to-pdf-conversion-in-php/
---

## **Aspose.Cells - 将Excel转换为PDF**
将Microsoft Excel文件转换为PDF

**PHP代码**

{{< highlight php >}}

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
从下面提到的任何社交编码网站下载**Excel转PDF转换（Aspose.Cells）**。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/Excel2PDFConversion.php)
