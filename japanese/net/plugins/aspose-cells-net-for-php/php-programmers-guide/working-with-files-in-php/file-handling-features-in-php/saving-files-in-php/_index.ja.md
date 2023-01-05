---
title: PHP でファイルを保存する
type: docs
weight: 20
url: /ja/net/saving-files-in-php/
---
## **Aspose.Cells - Excel ファイルの保存**
### **パスを介して開く**
ファイルのパスを参照して Microsoft Excel ファイルを保存する

**PHP コード**

{{< highlight "php" >}}

         $dataDir = '';

        // Create Aspose.Cells Helper Object

        $ptr = new \COM('Aspose.Cells.Interop.InteropHelper');

        // Opening through Path

        // Creating a Workbook object and opening an Excel file using its file path

        $workbook = $ptr->New("Aspose.Cells.Workbook",array());

        //Your Code goes here for any workbook related operations

        $ptr->Call($workbook,"Save",array($dataDir.'/book1.xls'));

        print "File saved successfully!" . PHP_EOL;

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**ファイルの保存 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/SavingFiles.php)
