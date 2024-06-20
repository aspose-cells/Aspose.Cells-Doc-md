---
title: PHPでExcelをPDFファイルに変換
type: docs
weight: 30
url: /ja/java/converting-excel-to-pdf-files-in-php/
---

## **Aspose.Cells - Excel を PDF ファイルに変換する**
PHPでAspose.Cells for Javaを使用してExcelをPDFファイルに変換するには、Converterモジュールのexcel_to_pdf()メソッドを単純に呼び出します。

**PHPコード**

{{< highlight php >}}

 $saveFormat = new SaveFormat();

$workbook = new Workbook($dataDir . "Book1.xls");

        //Save the document in PDF format

$workbook->save($dataDir . "OutBook1.pdf", $saveFormat->PDF);

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下に挙げるいずれかのソーシャルコーディングサイトから、**Converting Excel to PDF Files (Aspose.Cells)** をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/Excel2PdfConversion.php)
