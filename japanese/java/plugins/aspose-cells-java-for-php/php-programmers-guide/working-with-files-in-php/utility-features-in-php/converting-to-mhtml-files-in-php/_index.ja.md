---
title: PHP での MHTML ファイルへの変換
type: docs
weight: 40
url: /ja/java/converting-to-mhtml-files-in-php/
---
## **Aspose.Cells - MHTML ファイルへの変換**
PHP で Aspose.Cells for Java を使用してワークシートを MHTML ファイルに変換するには、ワークシートを呼び出すだけです。_に_Converter モジュールの mhtml() メソッド。

**PHPコード**

{{< highlight "php" >}}

 $sveFormat = new SaveFormat();

//Specify the file path

$filePath = $dataDir . "Book1.xlsx";

//Specify the HTML saving options

$sv = new HtmlSaveOptions($sveFormat->M_HTML);

//Instantiate a workbook and open the template XLSX file

$wb = new Workbook($filePath);

//Save the MHT file

$wb->save($filePath . ".out.mht", $sv);

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**MHTML ファイルへの変換 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingToMhtmlFiles.php)
