---
title: PHPでファイルを保存する
type: docs
weight: 20
url: /ja/net/saving-files-in-php/
---

## **Aspose.Cells - Excelファイルを保存する**
### **ファイルのパスを通じて開く**
Microsoft Excelファイルをファイルのパスを参照して保存する

**PHPコード**

{{< highlight php >}}

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
## **ランニングコードのダウンロード**
以下のいずれかのソーシャルコーディングサイトから、**ファイルを保存する（Aspose.Cells）**をダウンロードしてください：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Plugins/Aspose_Cells_NET_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/SavingFiles.php)
