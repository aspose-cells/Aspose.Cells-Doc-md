---
title: PHP でファイルを開く
type: docs
weight: 10
url: /ja/net/opening-files-in-php/
---
## **Aspose.Cells - Excel ファイルを開く**
### **パスを介して開く**
ファイルのパスを参照して、Microsoft Excel ファイルを開くだけです。

**PHP コード**

{{< highlight "php" >}}

         $dataDir = '';

        // Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array($dataDir . '/Book1.xls'));

        $worksheets = $ptr->Get($workbook,"Worksheets",array());

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**ファイルを開く (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
