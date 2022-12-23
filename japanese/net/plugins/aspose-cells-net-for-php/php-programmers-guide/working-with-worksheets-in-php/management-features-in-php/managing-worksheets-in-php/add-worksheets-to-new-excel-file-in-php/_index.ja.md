---
title: PHP で新しい Excel ファイルにワークシートを追加する
type: docs
weight: 20
url: /ja/net/add-worksheets-to-new-excel-file-in-php/
---
## **新しい Excel ファイルにワークシートを追加**
新しい Excel ファイルにワークシートを追加

**PHP コード**

{{< highlight "php" >}}

         $dataDir = '';

        // Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array());

        $worksheets = $ptr->Get($workbook,"Worksheets",array());

        $worksheet_index = $ptr->Call($worksheets,"Add_2",array());

        $worksheet = $ptr->Get($worksheets,"Item",array($worksheet_index));

        $ptr->Set($worksheet,"Name","My Worksheet",array());

        $ptr->Call($workbook,"Save",array($dataDir."/output.xls"));

        print "Completed." . PHP_EOL;

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**新しい Excel ファイルにワークシートを追加 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithWorksheets/ManagementFeatures/ManagingWorksheets/AddingWorksheetsToNewExcelFile.php)
