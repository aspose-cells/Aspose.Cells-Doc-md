---
title: PHP でExcelファイルをHTMLに変換する
type: docs
weight: 20
url: /ja/java/converting-excel-files-to-html-in-php/
---

## **Aspose.Cells - Excel ファイルを HTML に変換する**
PHPでAspose.Cells for Javaを使用してExcelをHTMLに変換するには、Converterモジュールのworksheet_to_html()メソッドを単純に呼び出します。

**PHPコード**

{{< highlight php >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

//Save the document in PDF format

$workbook->save($dataDir . "OutBook1.html", $saveFormat->HTML);

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下に挙げるいずれかのソーシャルコーディングサイトから、**Converting Excel Files to HTML (Aspose.Cells)** をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingExcelFilesToHtml.php)
