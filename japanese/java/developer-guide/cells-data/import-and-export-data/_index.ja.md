---
title: データのインポートとエクスポート
type: docs
weight: 130
url: /ja/java/import-and-export-data/
---

{{% alert color="primary" %}}

この記事では、開発者がAspose.Cellsを介してアクセスできるデータのインポートとエクスポートの様々な手法について説明しています。

{{% /alert %}}

## ワークシートへのデータのインポート

データは世界のありのままを表しています。データの意味を理解するために、分析を行い、世界の理解を深めます。データは情報に変わります。

分析を行うための多くの方法があります。データをスプレッドシートに入力し、さまざまな方法で操作することは一般的な方法の1つです。Aspose.Cellsを使用すると、さまざまな外部ソースからデータを受け取り、分析の準備を行うスプレッドシートを簡単に作成することができます。

この記事では、開発者がAspose.Cellsを通じてアクセスできるいくつかのデータインポートテクニックについて説明します。

### Aspose.Cellsを使用したデータのインポート

Aspose.CellsでExcelファイルを開くと、ファイル内のすべてのデータが自動的にインポートされます。Aspose.Cellsは他のデータソースからもデータをインポートすることができます:

- [配列](/cells/ja/java/import-and-export-data/)
- [配列リスト](/cells/ja/java/import-and-export-data/)
- [結果セット](/cells/ja/java/import-and-export-data/)
- [JSON](/cells/ja/java/import-and-export-data/)

Aspose.Cellsは、Microsoft Excelファイルを表すクラスである[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)を提供しています。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)コレクションが含まれており、Excelファイル内の各ワークシートにアクセスできます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)コレクションを提供します。[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)コレクションは他のデータソースからのデータのインポートに非常に役立つメソッドを提供します。この記事では、これらのメソッドの使用方法について説明します。

#### 配列からのインポート

配列からスプレッドシートにデータをインポートするには、[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)コレクションのimportArrayメソッドを呼び出します。importArrayメソッドには多くのオーバーロードされたバージョンがありますが、典型的なオーバーロードでは、次のパラメータが必要です:

- **Array**、インポート元の配列オブジェクト。
- **行番号**、データがインポートされる最初のセルの行番号。
- **列番号**、データがインポートされる最初のセルの列番号。
- **垂直**、データを垂直または水平にインポートするかどうかを指定するブール値。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArray-ImportingFromArray.java" >}}

#### 多次元配列からのインポート

多次元配列からスプレッドシートにデータをインポートするには、[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)コレクションの関連するimportArrayオーバーロードを呼び出します:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromMultiDimensionalArray-ImportingFromMultiDimensionalArray.java" >}}

#### ArrayListからのインポート

ワークシートに*ArrayList*からデータをインポートするには、[**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList-java.util.ArrayList-int-int-boolean-)コレクションの[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)メソッドを呼び出します。[**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList-java.util.ArrayList-int-int-boolean-)メソッドには次のパラメータが必要です:

- **ArrayList**、内容がインポートされる*ArrayList*オブジェクト
- **行番号**、コンテンツがインポートされるセル範囲の最初のセルの行番号
- **列番号**、データがインポートされる最初のセルの列番号
- **垂直かどうか**、データを垂直にするか水平にするかを指定するブール値

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### マージされたエリアへのカスタムオブジェクトからのインポート

結合セルを含むワークシートからオブジェクトのコレクションをインポートするには、[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)プロパティを使用します。Excelテンプレートに結合セルがある場合は、[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)プロパティの値をtrueに設定します。所望のオブジェクトのリストと共に、[**ImportTableOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImportTableOptions)オブジェクトをメソッドに渡して、データを表示します。次のコードサンプルは、カスタムオブジェクトから結合セルへのデータのインポートの使用を示しています。参照用の添付された[ソースExcel](90112035.xlsx)ファイルと[出力Excel](90112036.xlsx)ファイルをご覧ください。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### JSONからのデータのインポート

Aspose.CellsはJSONの処理のための[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)クラスを提供しています。[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)クラスにはJSONデータをインポートするための[**ImportData**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData-java.lang.String-com.aspose.cells.Cells-int-int-com.aspose.cells.JsonLayoutOptions-)メソッドがあります。Aspose.Cellsはまた、JSONレイアウトのオプションを表す[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)クラスも提供しています。[**ImportData**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData-java.lang.String-com.aspose.cells.Cells-int-int-com.aspose.cells.JsonLayoutOptions-)メソッドは[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)をパラメータとして受け取ります。[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)クラスは以下のプロパティを提供します。

- [**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable)：配列内の処理がテーブルとして行われるかどうかを示します。
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ConvertNumericOrDate): JSON内の文字列が数値または日付に変換されるかどうかを取得または設定します。
- [**DateFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#DateFormat)：日付値の形式を取得および設定します。
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle)：オブジェクトのプロパティが配列の場合にタイトルを無視するかどうかを示します
- [**IgnoreNull**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreNull)：null値を無視するかどうかを示します。
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreObjectTitle)：オブジェクトのプロパティがオブジェクトの場合にタイトルを無視するかどうかを示します。
- [**NumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#NumberFormat)：数値値の形式を取得および設定します。
- [**TitleStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#TitleStyle)：タイトルのスタイルを取得および設定します。

以下に示すサンプルコードは、[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) および [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) クラスを使用して JSON データをインポートする方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportingFromJson-1.java" >}}

## ワークシートからデータをエクスポート

Aspose.Cells は、ユーザーが外部データソースからワークシートにデータをインポートするだけでなく、ワークシートデータを配列にエクスポートすることも可能にします。

### Aspose.Cells を使用したデータのエクスポート - 配列へのデータのエクスポート

Aspose.Cells は、Microsoft Excel ファイルを表す [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) クラスには、Excel ファイルの各ワークシートにアクセスできる [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) が含まれています。ワークシートは [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) クラスは [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) コレクションを提供します。

データは、[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) クラスの [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray-int-int-int-int-) メソッドを使用して簡単に配列オブジェクトにエクスポートできます。

#### 強く型付けされたデータを含む列

スプレッドシートは、行および列の連続としてデータを保存します。ワークシートからデータを配列にエクスポートするには、[**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray-int-int-int-int-) メソッドを使用します。[**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray-int-int-int-int-) は、ワークシートデータを *Array* オブジェクトとしてエクスポートするため、次のパラメータを取ります：

- 行番号：データをエクスポートする最初のセルの行番号。
- 列番号：データをエクスポートする最初のセルの列番号
- 行数：エクスポートする行数。
- 列数：エクポートする列数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ExportingDataFromWorksheets-1.java" >}}

## **高度なトピック**
- [Microsoft Access データベース ResultSet オブジェクトからデータをワークシートにインポート](/cells/ja/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/)
- [ワークシートにデータをインポートする際に式フィールドを指定する](/cells/ja/java/specify-formula-fields-while-importing-data-to-worksheet/)
{{< app/cells/assistant language="java" >}}
