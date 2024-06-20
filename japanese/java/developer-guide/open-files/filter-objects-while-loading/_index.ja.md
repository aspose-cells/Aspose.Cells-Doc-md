---
title: ワークブックまたはワークシートをロードする際にオブジェクトをフィルタリングする
type: docs
weight: 1060
url: /ja/java/filter-objects-while-loading-workbook-or-worksheet/
---

## **可能な使用シナリオ**
ワークブックからデータをフィルタリングする際に[LoadOptions.LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#LoadFilter)プロパティを使用してください。個々のワークシートからデータをフィルタリングする場合は、[LoadFilter.startSheet](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#startSheet\(com.aspose.cells.Worksheet\))メソッドをオーバーライドする必要があります。[LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter)の作成または使用時には、[LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions)列挙型から適切な値を提供してください。

[LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions)列挙型には、以下の値が含まれます。

- [なし](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#NONE)
- [すべて](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#ALL)
- [CELL_BLANK](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BLANK)
- [CELL_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_STRING)
- [CELL_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_NUMERIC)
- [CELL_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_ERROR)
- [CELL_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BOOL)
- [CELL_VALUE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_VALUE)
- [数式](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#FORMULA)
- [セルデータ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_DATA)
- [チャート](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CHART)
- [図形](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE)
- [結合された領域](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#MERGED_AREA)
- [条件付き書式](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CONDITIONAL_FORMATTING)
- [データの検証](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DATA_VALIDATION)
- [ピボットテーブル](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#PIVOT_TABLE)
- [表](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#TABLE)
- [ハイパーリンク](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#HYPERLINKS)
- [シートの設定](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_SETTINGS)
- [シートのデータ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_DATA)
- [ブックの設定](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#BOOK_SETTINGS)
- [設定](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SETTINGS)
- [XML マップ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#XML_MAP)
- [構造](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STRUCTURE)
- [文書のプロパティ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DOCUMENT_PROPERTIES)
- [定義済み名](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)
- [VBA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#VBA)
- [スタイル](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STYLE)
## **ワークブックの読み込み中にフィルターオブジェクト**
次のサンプルコードは、ワークブックからチャートをフィルタリングする方法を示しています。このコードで使用される[サンプルエクセルファイル](5472489.xlsx)およびそれによって生成された[出力PDF](5472488.pdf)をご確認ください。出力PDFでは、すべてのチャートがワークブックからフィルタリングされていることがわかります。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilterObjectsLoadingWorkbook-FilterObjectsLoadingWorkbook.java" >}}
## **ワークシートの読み込み中にフィルターオブジェクト**
次のサンプルコードは、[ソースエクセルファイル](5472492.xlsx)をロードし、カスタムフィルタを使用してそのワークシートから次のデータをフィルタリングする方法を説明しています。

- NoChartsという名前のワークシートからグラフをフィルタリングします。
- NoShapesという名前のワークシートから形状をフィルタリングします。
- NoConditionalFormattingという名前のワークシートから条件付き書式をフィルタリングします。

一度、カスタムフィルタを使用して[ソースエクセルファイル](5472492.xlsx)を読み込むと、ワークシートのすべての画像を1つずつ取得します。参照のために、こちらに出力画像を示します。出力画像をご覧いただくと、最初の画像にはチャートがなく、2番目の画像には図形がなく、3番目の画像には条件付き書式がないことがわかります。

- [NoCharts.png](5472493.png)
- [NoShapes.png](5472491.png)
- [NoConditionalFormatting.png](5472490.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterObjectsLoadingWorksheets-1.java" >}}
