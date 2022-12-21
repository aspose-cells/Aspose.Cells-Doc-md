---
title: SpreadsheetML - XLSX、XML
type: docs
weight: 10
url: /ja/net/spreadsheetml-xlsx-xml/
---
## **SpreadsheetMLについて**
SpreadsheetML は、スプレッドシート ドキュメント用の XML ベースの形式のファミリの名前です。 SpreadsheetML にはいくつかのバージョンがあります。

1. SpreadsheetML バージョン 2003 は、Microsoft Word 2003 で導入されました。SpreadsheetML は、Microsoft によってドキュメント形式をオープンにするための重要な一歩でした。
1. [Office オープン XML](https://en.wikipedia.org/wiki/Office_Open_XML) (OOXML) は、Microsoft Office 2007 アプリケーションで導入された新しい XML ベースの形式です。 Office Open XML は、いくつかの特殊な XML ベースのマークアップ言語のコンテナー形式です。 SpreadsheetML バージョン 2007 は、ドキュメントを格納するために Microsoft Office Excel 2007 で使用されるマークアップ言語です。
1. Microsoft Excel 2010 は、更新された OOXML 標準で定義されているように、ドキュメントを SpreadsheetML バージョン 2010 に保存します。
## **SpreadsheetML in Aspose.Cells**
利用可能な SpreadsheetML の 3 つの「バージョン」があります。

|**SpreadsheetML「バージョン」**|**適用規格・仕様**|**Aspose.Cells for .NET でサポート**|
|:- |:- |:- |
|Microsoft エクセル2003|[Microsoft エクセル 2003 XML](https://en.wikipedia.org/wiki/Microsoft_Office_XML_formats)|はい|
|Microsoft エクセル 2007|[OOXML ECMA-376](https://www.ecma-international.org/publications-and-standards/standards/ecma-376/)|はい|
|Microsoft エクセル2010|OOXML ISO/IEC DIS 29500|はい|
|Microsoft エクセル 2013|OOXML ISO/IEC DIS 29500|はい|
OOXML SpreadsheetML ドキュメントは、ほとんどの場合、ZIP パッケージである XLSX ファイルとして提供されます。 XLSXに加えて。 Aspose.Cells は、SpreadsheetML ドキュメントの読み込み、保存、および変換を幅広くサポートします。 Aspose.Cells は Microsoft Excel ドキュメントの構造を念頭に置いて設計されているため、このような包括的な実装が可能です (また、SpreadsheetML は Microsoft Excel ドキュメントの内部表現を模倣することが知られています)。
### **OOXML はオープンですが、なぜ Aspose.Cells を使用するのですか?**
確かに、Office Open XML テクノロジにより、Aspose.Cells などのサードパーティ ライブラリに依存することなく、XML クラスだけを使用してドキュメント処理および生成アプリケーションを構築できます。 XML やその他のライブラリを使用するのではなく、OOXML ドキュメントを処理します。

OOXML 仕様は、数千ページの長さです。オープンで標準的であることは、単純であることを意味しません。 OOXML ドキュメントを正しく処理または生成するには、フォーマットを十分に学習することに投資する必要があります。

Aspose.Cells は、有効なドキュメントを正しく処理して生成することをより簡単にするだけでなく、XML または他のサードパーティ ライブラリを介して直接 OOXML ファイルを操作する場合にはない次の重要な機能を提供します。

- PDF、HTML、TIFF、および印刷への変換を含む、多くの一般的な Excel 形式間の高品質の変換。
- つまたは複数のドキュメントの断片からドキュメントを作成する機能。同時に、文体の書式設定、チャート、およびグラフィックスによってデータを自動的にマージします。
- Array、ArrayList、DataTable、DataColumn、DataGrid、DataView、DataReader などのさまざまなデータ ソースからデータをインポートしたり、データをエクスポートして DataTable または Array を 1 行のコードで埋めたりするなどの高レベル関数。
- 標準および高度な Microsoft Excel 関数のほぼすべてをサポートする堅牢な数式計算エンジン。

次の例を考えてみましょう。一部のセルには、太字で「Hello World」というテキストが含まれています。ここで、ワークシート内のすべての「Hello World」フレーズを検索し、それらを「Goodbye Earth」に置き換えるプログラムを作成する必要があるとします。
### **Office Open XML ドキュメントのフラグメント**
**XML**

{{< highlight "csharp" >}}

 <?xml version="1.0" encoding="UTF-8" standalone="yes" ?>

\- <worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">

  <dimension ref="A1:M184" />

\- <sheetViews>

\- <sheetView tabSelected="1" workbookViewId="0">

  <selection activeCell="H27" sqref="H27" />

  </sheetView>

  </sheetViews>

  <sheetFormatPr defaultRowHeight="15" />

\- <sheetData>

\- <row r="1" spans="1:7">

\- <c r="A1" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="11" spans="1:7">

\- <c r="D11" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="15" spans="1:7">

\- <c r="G15" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="21" spans="2:7">

\- <c r="G21" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="25" spans="2:7">

\- <c r="F25" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="31" spans="2:7">

\- <c r="B31" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="34" spans="6:13">

\- <c r="M34" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="38" spans="6:13">

\- <c r="F38" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="117" spans="8:8">

\- <c r="H117" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="184" spans="8:8">

\- <c r="H184" s="1" t="s">

  <v>0</v>

  </c>

  </row>

  </sheetData>

  <pageMargins left="0.7" right="0.7" top="0.75" bottom="0.75" header="0.3" footer="0.3" />

</worksheet>



{{< /highlight >}}


Office Open XML ドキュメントに単純な検索および置換操作を実装することさえ困難です。私たちのアドバイス: オープンで標準的というのは単純という意味ではないことを覚えておいてください。Aspose.Cells を使用してください。
