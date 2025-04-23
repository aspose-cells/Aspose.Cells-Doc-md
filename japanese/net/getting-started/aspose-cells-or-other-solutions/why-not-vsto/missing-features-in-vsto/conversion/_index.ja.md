---
title: 変換
type: docs
weight: 30
url: /ja/net/conversion/
---

Aspose.Cellsの特徴であり、作業に影響を与えることなくバージョン変換で柔軟性を提供します。
SaveFormatは、以下の表に示す拡張子のドキュメントを変換できる列挙型です。

|**メンバー名**|**値**|**説明**|
| :- | :- | :- |
|CSV |1 |CSVファイルを表します。|
|Xlsx |6 |xlsxファイルを表します。|
|Xlsm |7 |マクロを有効にするxlsmファイルを表します。|
|Xltx |8 |xltxファイルを表します。|
|Xltm |9 |マクロを有効にするxltmファイルを表します。|
|TabDelimited |11 |タブ区切りテキストファイルを表します。|
|Html |12 |HTMLファイルを表します。|
|MHtml |17 |mhtmlファイルを表します。|
|ODS |14 |odsファイルを表します。|
|Excel97To2003 |5 |Excel97-2003 xlsファイルを表します。|
|SpreadsheetML |15 |Excel 2003 xmlファイルを表します。|
|Xlsb |16 |xlsbファイルを表します。|
|Auto |0 |ファイルをディスクに保存する場合、ファイル形式はファイル名の拡張子に準拠します。<br>ストリームに保存する場合、ファイル形式はxlsxです。|
|Unknown |255 |認識されない形式を表し、保存することができません。|
|Pdf |13 |Pdfファイルを表します。|
|XPS |20 |XPSファイルを表します。|
|TIFF |21 |TIFFファイルを表します。|
|SVG |22 |SVGファイルを表します。|
|Dif |30 |データ交換フォーマット。|
以下はxlsからxlsxへの変換を示すコードスニペットです。逆も同様に行うことができます。

{{< highlight csharp >}}

 Workbook workbook = new Workbook("Sample.xls");

workbook.Save("Converted.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}
## **サンプルコードをダウンロード**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Conversion%20between%20Excel%20Formats%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
