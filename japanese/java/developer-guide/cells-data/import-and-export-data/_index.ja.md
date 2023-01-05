---
title: データのインポートとエクスポート
type: docs
weight: 130
url: /ja/java/import-and-export-data/
---
{{% alert color="primary" %}}

この記事では、開発者が Aspose.Cells を通じてアクセスできるデータのインポートとエクスポートの手法について説明します。

{{% /alert %}}

## データをワークシートにインポート

データは世界をありのままに表します。データを理解するために、データを分析し、世界を理解します。データは情報に変わります。

分析を実行するには多くの方法があります。データをスプレッドシートに入力し、さまざまな方法で操作することは、一般的な方法の 1 つです。 Aspose.Cells を使用すると、さまざまな外部ソースからデータを取得して分析用に準備するスプレッドシートを簡単に作成できます。

この記事では、開発者が Aspose.Cells を通じてアクセスできるいくつかのデータ インポート手法について説明します。

### Aspose.Cells を使用したデータのインポート

Aspose.Cells の Excel ファイルを開くと、ファイル内のすべてのデータが自動的にインポートされます。 Aspose.Cells は、他のデータ ソースからデータをインポートすることもできます。

- [配列](/cells/ja/java/import-and-export-data/).
- [配列リスト](/cells/ja/java/import-and-export-data/).
- [結果セット](/cells/ja/java/import-and-export-data/).
- [JSON](/cells/ja/java/import-and-export-data/)

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスにはコレクションが含まれています[**ワークシート コレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)これにより、Excel ファイル内の各ワークシートにアクセスできます。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)コレクション。[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)コレクションは、他のデータ ソースからデータをインポートするための非常に便利な方法を提供します。この記事では、これらのメソッドの使用方法について説明します。

#### アレイからのインポート

配列からスプレッドシートにデータをインポートするには、[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)コレクション。 importArray メソッドには多くのオーバーロードされたバージョンがありますが、典型的なオーバーロードは次のパラメーターを取ります。

- **配列**、コンテンツのインポート元の配列オブジェクト。
- **行番号**、データがインポートされる最初のセルの行番号。
- **列番号**、データがインポートされる最初のセルの列番号。
- **垂直です**、データを垂直または水平にインポートするかどうかを指定するブール値。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArray-ImportingFromArray.java" >}}

#### 多次元配列からのインポート

多次元配列からスプレッドシートにデータをインポートするには、関連する importArray オーバーロードを呼び出します[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)コレクション：

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromMultiDimensionalArray-ImportingFromMultiDimensionalArray.java" >}}

#### ArrayList からのインポート

からデータをインポートするには*配列リスト*ワークシートに、[**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean) ) の方法[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)コレクション。の[**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean)メソッドは、次のパラメーターを取ります。

- **配列リスト** 、*配列リスト*コンテンツがインポートされるオブジェクト。
- **行番号**、コンテンツがインポートされるセル範囲の最初のセルの行番号。
- **列番号**、データがインポートされる最初のセルの列番号。
- **垂直です**は、データを垂直または水平にインポートするかどうかを指定するブール値です。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### カスタム オブジェクトから結合領域へのインポート

オブジェクトのコレクションから結合セルを含むワークシートにデータをインポートするには、次を使用します。[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)財産。 Excel テンプレートにセルが結合されている場合は、次の値を設定します。[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)プロパティを true にします。渡す[**ImportTableOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImportTableOptions)オブジェクトを列/プロパティのリストとともにメソッドに渡して、目的のオブジェクトのリストを表示します。次のコード サンプルは、[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)カスタム オブジェクトから結合セルにデータをインポートするためのプロパティ。添付をご覧ください[ソースエクセル](90112035.xlsx)ファイルと[エクセル出力](90112036.xlsx)参照用のファイル。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### JSON からのデータのインポート

Aspose.Cells は[**Jsonユーティリティ**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)JSON を処理するためのクラス。[**Jsonユーティリティ**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)クラスには[**ImportData**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions) ) JSON データをインポートする方法。 Aspose.Cells も提供しています[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)JSON レイアウトのオプションを表すクラス。の[**ImportData**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions) メソッドが受け入れる[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)パラメータとして。の[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)クラスは、次のプロパティを提供します。

- [**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable): 配列内をテーブルとして処理するかどうかを示します。
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ConvertNumericOrDate): JSON の文字列を数値または日付に変換するかどうかを示す値を取得または設定します。
- [**日付形式**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#DateFormat)日付値の形式を取得および設定します。
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle): オブジェクトのプロパティが配列の場合、タイトルを無視するかどうかを示します
- [**Null を無視**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreNull)null 値を無視するかどうかを示します。
- [**オブジェクトタイトルを無視**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreObjectTitle)オブジェクトのプロパティがオブジェクトの場合、タイトルを無視するかどうかを示します。
- [**NumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#NumberFormat): 数値の形式を取得および設定します。
- [**タイトルスタイル**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#TitleStyle)タイトルのスタイルを取得および設定します。

以下のサンプル コードは、[**Jsonユーティリティ**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)と[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) JSON データをインポートするクラス。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportingFromJson-1.java" >}}

## ワークシートからデータをエクスポート

Aspose.Cells では、ユーザーは外部データ ソースからワークシートにデータをインポートできるだけでなく、ワークシート データを配列にエクスポートすることもできます。

### Aspose.Cells を使用したデータのエクスポート - 配列へのデータのエクスポート

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)クラスには[**ワークシート コレクション**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)これにより、Excel ファイル内の各ワークシートにアクセスできます。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)コレクション。

を使用して、データを Array オブジェクトに簡単にエクスポートできます。[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)クラス'[**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int)） 方法。

#### 厳密に型指定されたデータを含む列

スプレッドシートは、データを一連の行と列として保存します。使用[**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int) メソッドを使用して、データをワークシートから配列にエクスポートします。[**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int) ) は、次のパラメータを使用して、ワークシート データを*配列*物体：

- 行番号、データがエクスポートされる最初のセルの行番号。
- 列番号、データがエクスポートされる最初のセルの列番号
- 行数、エクスポートする行数。
- 列数、エクスポートする列数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ExportingDataFromWorksheets-1.java" >}}

## **先行トピック**
- [Microsoft Access データベース ResultSet オブジェクトからワークシートへのデータのインポート](/cells/ja/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/)
- [データをワークシートにインポートする際の数式フィールドの指定](/cells/ja/java/specify-formula-fields-while-importing-data-to-worksheet/)
