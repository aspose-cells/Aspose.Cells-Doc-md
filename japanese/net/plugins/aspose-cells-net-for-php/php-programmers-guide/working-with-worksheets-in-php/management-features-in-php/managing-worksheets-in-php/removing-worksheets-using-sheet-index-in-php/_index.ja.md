---
title: PHPでシートインデックスを使用してワークシートを削除
type: docs
weight: 30
url: /ja/net/removing-worksheets-using-sheet-index-in-php/
---

## **シートインデックスを使用してワークシートを削除**
シートインデックスを使用してワークシートを削除

**PHPコード**

{{< highlight php >}}

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
## **ランニングコードのダウンロード**
**シートインデックスを使用してワークシートを削除（Aspose.Cells）**を以下のソーシャルコーディングサイトからダウンロードしてください：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets/RemovingWorksheetsUsingSheetIndex.php)
