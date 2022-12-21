---
title: 変換
type: docs
weight: 30
url: /ja/net/conversion/
---
Aspose.Cells 作業に影響を与えずにバージョン変換の柔軟性を提供する独自の機能。
SaveFormat は、以下の表に示す拡張子のドキュメントを変換できる列挙型です。

|**メンバー名** |**価値** |**説明** |
|:- |:- |:- |
|CSV|1 | CSV ファイルを表します。|
| xlsx|6 | xlsx ファイルを表します。|
| Xlsm|7 |マクロを有効にする xlsm ファイルを表します。|
| Xltx|8 | xltx ファイルを表します。|
| Xltm|9 |マクロを有効にする xltm ファイルを表します。|
|タブ区切り|11 |タブ区切りのテキスト ファイルを表します。|
|HTML|12 | html ファイルを表します。|
| MHtml|17 | mhtml ファイルを表します。|
|ODS|14 | ods ファイルを表します。|
| Excel97To2003|5 | Excel97-2003 xls ファイルを表します。|
|スプレッドシートML|15 | Excel 2003 xml ファイルを表します。|
| Xlsb|16 | xlsb ファイルを表します。|
|自動|0 |ファイルをディスクに保存する場合、ファイル形式の形式はファイル名の拡張子に従います。<br>ファイルをストリームに保存する場合、ファイル形式は xlsx です。|
|知らない|255 |認識できない形式を表しており、保存できません。|
| PDF|13 | Pdf ファイルを表します。|
| XPS|20 | XPS ファイルを表します。|
| TIFF|21 | TIFF ファイルを表します。|
| SVG|22 | SVG ファイルを表します。|
|差分|30 |データ交換フォーマット。|
以下は、xls から xlsx への変換を示すコード スニペットです。逆も同様です。

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook("Sample.xls");

workbook.Save("Converted.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}
## **サンプルコードをダウンロード**
- [ビットバケット](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Conversion%20between%20Excel%20Formats%20%28Aspose.Cells%29.zip)
