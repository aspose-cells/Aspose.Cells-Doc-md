---
title: PHP で Excel ファイルを HTML に変換する
type: docs
weight: 20
url: /ja/java/converting-excel-files-to-html-in-php/
---
## **Aspose.Cells - Excel ファイルを HTML に変換する**
PHP で Aspose.Cells for Java を使用して Excel を HTML に変換するには、ワークシートを呼び出すだけです。_に_Converter モジュールの html() メソッド。

**PHP コード**

{{< highlight "php" >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

//Save the document in PDF format

$workbook->save($dataDir . "OutBook1.html", $saveFormat->HTML);

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**Excel ファイルを HTML に変換する (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingExcelFilesToHtml.php)
