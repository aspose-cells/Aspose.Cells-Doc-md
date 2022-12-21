---
title: PHP で Excel を PDF ファイルに変換する
type: docs
weight: 30
url: /ja/java/converting-excel-to-pdf-files-in-php/
---
## **Aspose.Cells - Excel から PDF ファイルへの変換**
PHP で Aspose.Cells for Java を使用して Excel を Pdf ファイルに変換するには、Excel を呼び出すだけです。_に_Converter モジュールの pdf() メソッド。

**PHPコード**

{{< highlight "php" >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

        //Save the document in PDF format

$workbook->save($dataDir . "OutBook1.pdf", $saveFormat->PDF);

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**Excel を PDF ファイルに変換する (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/Excel2PdfConversion.php)
