---
title: PHP でファイルを開く
type: docs
weight: 10
url: /ja/java/opening-files-in-php/
---
## **Aspose.Cells - Excel ファイルを開く簡単な方法**
### **パスを介して開く**
ファイルのパスを参照して、Microsoft Excel ファイルを開くだけです。

**PHP コード**

{{< highlight "ruby" >}}

 $dataDir = '';

$workbook1 = new Workbook($dataDir . "Book1.xls");

{{< /highlight >}}
### **ストリームを介して開く**
開こうとしている Excel ファイルがストリームとして保存されている場合があります。その場合は、Excel ファイルを含む Stream オブジェクトを受け取る Open メソッドのオーバーロード バージョンを使用して、ファイルを開きます。

**PHP コード**

{{< highlight "ruby" >}}

 $fstream = new FileInputStream($dataDir . "Book2.xls");

//Creating an Workbook object with the stream object

$workbook2 = new Workbook($fstream);

$fstream->close();

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**ファイルを開く (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/FileHandlingFeatures/OpeningFiles.php)
