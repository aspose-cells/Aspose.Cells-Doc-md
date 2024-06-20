---
title: PHPでMHTMLファイルに変換
type: docs
weight: 40
url: /ja/java/converting-to-mhtml-files-in-php/
---

## **Aspose.Cells - MHTML ファイルに変換する**
PHPでAspose.Cells for Javaを使用してWorksheetをMHTMLファイルに変換するには、Converterモジュールのworksheet_to_mhtml()メソッドを単純に呼び出します。

**PHPコード**

{{< highlight php >}}

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
## **ランニングコードのダウンロード**
以下に挙げるいずれかのソーシャルコーディングサイトから、**Converting to MHTML Files (Aspose.Cells)** をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/WorkingWithFiles/UtilityFeatures/ConvertingToMhtmlFiles.php)
