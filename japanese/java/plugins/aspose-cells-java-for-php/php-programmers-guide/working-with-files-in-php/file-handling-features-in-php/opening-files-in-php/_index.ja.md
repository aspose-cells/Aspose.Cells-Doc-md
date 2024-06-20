---
title: PHPでファイルを開く
type: docs
weight: 10
url: /ja/java/opening-files-in-php/
---

## **Aspose.Cells - Excelファイルを開く簡単な方法**
### **ファイルのパスを通じて開く**
単純に、Microsoft Excelファイルをファイルのパスを参照して開きます

**PHPコード**

{{< highlight ruby >}}

 $dataDir = '';

$workbook1 = new Workbook($dataDir . "Book1.xls");

{{< /highlight >}}
### **ストリームを介した開く**
開きたいExcelファイルがストリームとして保存されている場合は、Excelファイルを含むStreamオブジェクトを取る**Open**メソッドのオーバーロードバージョンを使用してファイルを開きます。

**PHPコード**

{{< highlight ruby >}}

 $fstream = new FileInputStream($dataDir . "Book2.xls");

//Creating an Workbook object with the stream object

$workbook2 = new Workbook($fstream);

$fstream->close();

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のいずれかのソーシャルコーディングサイトから、**ファイルを開く（Aspose.Cells）**をダウンロードしてください：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
