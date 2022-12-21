---
title: ワークブックまたはワークシートの読み込み中にオブジェクトをフィルタリングする
type: docs
weight: 1060
url: /ja/java/filter-objects-while-loading-workbook-or-worksheet/
---
## **考えられる使用シナリオ**
使ってください[LoadOptions.LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#LoadFilter)ワークブックからデータをフィルタリングする際のプロパティ。ただし、個々のワークシートからデータをフィルター処理する場合は、オーバーライドする必要があります[LoadFilter.startSheet](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#startSheet\(com.aspose.cells.Worksheet\) ） 方法。から適切な値を入力してください[LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions)作成中または操作中の列挙[LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter).

の[LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions)列挙には次の値があります。

- [なし](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#NONE)
- [全て](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#ALL)
- [CELL_BLANK](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BLANK)
- [CELL_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_STRING)
- [CELL_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_NUMERIC)
- [CELL_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_ERROR)
- [CELL_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BOOL)
- [CELL_VALUE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_VALUE)
- [方式](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#FORMULA)
- [CELL_DATA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_DATA)
- [チャート](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CHART)
- [形](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE)
- [MERGED_AREA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#MERGED_AREA)
- [条件付き書式](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CONDITIONAL_FORMATTING)
- [データ検証](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DATA_VALIDATION)
- [ピボットテーブル](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#PIVOT_TABLE)
- [テーブル](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#TABLE)
- [ハイパーリンク](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#HYPERLINKS)
- [シート設定](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_SETTINGS)
- [シートデータ](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_DATA)
- [BOOK_SETTINGS](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#BOOK_SETTINGS)
- [設定](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SETTINGS)
- [XML_MAP](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#XML_MAP)
- [構造](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STRUCTURE)
- [DOCUMENT_PROPERTIES](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DOCUMENT_PROPERTIES)
- [DEFINED_NAMES](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)
- [VBA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#VBA)
- [スタイル](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STYLE)
## **ワークブックの読み込み中にオブジェクトをフィルタリングする**
次のサンプル コードは、ワークブックからグラフをフィルター処理する方法を示しています。を確認してください[サンプルエクセルファイル](5472489.xlsx)このコードと[PDF出力](5472488.pdf)それによって生成されます。出力 PDF でわかるように、すべてのグラフがワークブックから除外されています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilterObjectsLoadingWorkbook-FilterObjectsLoadingWorkbook.java" >}}
## **ワークシートの読み込み中にオブジェクトをフィルタリングする**
次のサンプル コードは、[ソースエクセルファイル](5472492.xlsx)カスタム フィルターを使用してワークシートから次のデータをフィルター処理します。

- NoCharts という名前のワークシートからチャートをフィルタリングします。
- NoShapes という名前のワークシートから Shapes をフィルター処理します。
- NoConditionalFormatting という名前のワークシートから条件付き書式をフィルター処理します。

一度、ロードします[ソースエクセルファイル](5472492.xlsx)カスタム フィルターを使用すると、すべてのワークシートの画像を 1 つずつ取得します。参考までに、出力イメージを次に示します。ご覧のとおり、最初の画像にはグラフがなく、2 番目の画像には図形がなく、3 番目の画像には条件付き書式がありません。

- [NoCharts.png](5472493.png)
- [NoShapes.png](5472491.png)
- [NoConditionalFormatting.png](5472490.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterObjectsLoadingWorksheets-1.java" >}}
