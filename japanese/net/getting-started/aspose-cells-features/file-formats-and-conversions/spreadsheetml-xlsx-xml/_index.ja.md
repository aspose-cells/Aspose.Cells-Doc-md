---
title: SpreadsheetML - XLSX, XML
type: docs
weight: 10
url: /ja/net/spreadsheetml-xlsx-xml/
---

## **SpreadsheetMLについて**
SpreadsheetMLはスプレッドシートドキュメントのための一連のXMLベースのフォーマットの名前です。いくつかのバージョンのSpreadsheetMLがあります。

1. Microsoft Word 2003 で導入されたSpreadsheetMLバージョン2003。SpreadsheetMLは、Microsoftによるドキュメントフォーマットをオープンにするための重要な一歩でした。
1. [Office Open XML](https://en.wikipedia.org/wiki/Office_Open_XML) (OOXML)は、Microsoft Office 2007アプリケーションで導入された新しいXMLベースのフォーマットです。Office Open XMLは、いくつかの専門のXMLベースのマークアップ言語のためのコンテナフォーマットです。SpreadsheetMLバージョン2007は、Microsoft Office Excel 2007でドキュメントを保存するために使用されるマークアップ言語です。
1. Microsoft Excel 2010は、更新されたOOXML標準で定義されているSpreadsheetMLバージョン2010でドキュメントを保存します。
## **Aspose.CellsのSpreadsheetML**
SpreadsheetMLには3つの「バージョン」があります：

|**SpreadsheetMLの“バージョン”**|**適用される標準/仕様**|**Aspose.Cells for .NETでサポート**|
| :- | :- | :- |
|Microsoft Excel 2003|[Microsoft Excel 2003 XML](https://en.wikipedia.org/wiki/Microsoft_Office_XML_formats)|はい|
|Microsoft Excel 2007|[OOXML ECMA-376](https://www.ecma-international.org/publications-and-standards/standards/ecma-376/)|はい|
|Microsoft Excel 2010|OOXML ISO/IEC DIS 29500|はい|
|Microsoft Excel 2013|OOXML ISO/IEC DIS 29500|はい|
OOXML SpreadsheetMLドキュメントはほとんどがZIPパッケージであるXLSXファイルとして提供されます。また、XLSX以外にも、Aspose.CellsはSpreadsheetMLドキュメントの読み込み、保存、変換に幅広いサポートを提供します。この包括的な実装が可能なのは、Aspose.CellsがMicrosoft Excelドキュメントの構造を考慮して設計されているためであり（そして、SpreadsheetMLはMicrosoft Excelドキュメントの内部表現を模倣しているためです）。
### **OOXMLはオープンですが、なぜAspose.Cellsを使用するのですか？**
Office Open XMLテクノロジーを使用して、Aspose.Cellsなどのサードパーティライブラリに頼らずにXMLクラスだけを使用してドキュメント処理および生成アプリケーションを構築することが可能です。しかし、私たちは、OOXMLドキュメントを扱う必要がある場合は、XMLや他のライブラリを経由するのではなく、Aspose.Cellsを使用することが非常に有益だと強く信じています。

OOXML仕様は数千ページに及びます。オープンで標準であるということは、単純であるということを意味するわけではありません。正しくOOXMLドキュメントを処理または生成するには、フォーマットをよく理解するための投資が必要です。

正しいドキュメントを処理または生成することを簡単にするだけでなく、Aspose.Cellsは次の重要な機能を提供します。

多くの人気のあるExcel形式間での品質の高い変換を行うことができ、PDF、HTML、TIFFへの変換や印刷などをサポートしています。
スタイル付けのフォーマット、チャート、グラフィックの自動結合によって、一つまたは複数のドキュメントから断片を組み立てて、ドキュメントを構築する機能があります。
Array、ArrayList、DataTable、DataColumn、DataGrid、DataView、DataReaderなど、さまざまなデータソースからデータをインポートしたり、1行のコードでDataTableやArrayにデータをエクスポートしたりといった高度な機能があります。
- ほぼすべての標準および高度なMicrosoft Excelの関数をサポートする、堅実な式計算エンジン。

次の例を考えてみてください。いくつかのセルに太字の「Hello World」というテキストが含まれています。今、ワークシート内のすべての「Hello World」フレーズを検索して、「Goodbye Earth」に置き換えるプログラムを書く必要があると想像してください。
### **Office Open XMLドキュメントの一部のフラグメント**
**XML**

{{< highlight csharp >}}

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


Office Open XMLドキュメントでのシンプルな検索および置換操作の実装は難しいです。私たちのアドバイス: オープンで標準的であるということは、単純であるということではないことを覚えておくこと、そしてAspose.Cellsを使用すること。
