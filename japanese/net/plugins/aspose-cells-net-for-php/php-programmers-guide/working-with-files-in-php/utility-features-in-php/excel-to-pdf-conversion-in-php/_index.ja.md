---
title: PHPでのExcelからPDFへの変換
type: docs
weight: 20
url: /ja/net/excel-to-pdf-conversion-in-php/
---

## **Aspose.Cells - ExcelからPDFへの変換**
Microsoft ExcelファイルをPDFに変換

**PHPコード**

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
## **ランニングコードのダウンロード**
以下に記載されているソーシャルコーディングサイトから、**ExcelからPDFへの変換 (Aspose.Cells)** をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/Excel2PDFConversion.php)
