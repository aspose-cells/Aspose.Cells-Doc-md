---
title: PHP でシート インデックスを使用してワークシートを削除する
type: docs
weight: 30
url: /ja/net/removing-worksheets-using-sheet-index-in-php/
---
## **シート インデックスを使用したワークシートの削除**
シート インデックスを使用したワークシートの削除

**PHPコード**

{{< highlight "php" >}}

         $dataDir = '';

        / Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array($dataDir . '/book1.xls'));

        $worksheets = $ptr->Get($workbook,"Worksheets",array());

        $ptr->Call($worksheets,"RemoveAt",array(0));

        $ptr->Call($workbook,"Save",array($dataDir."/output.xls"));

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**シート インデックスを使用してワークシートを削除する (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets/RemovingWorksheetsUsingSheetIndex.php)
