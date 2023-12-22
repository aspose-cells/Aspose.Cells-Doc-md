---
title: データをワークシートにインポート
type: docs
weight: 170
url: /ja/net/import-data-into-worksheet/
description: Aspose.Cells for .NET API を通じてワークシートにデータをインポートする方法を学習します。
keywords: C# Import Data into Worksheet, Import data into Excel with ICellsDataTable interface, Import data from Array, Import Data from ArrayList, Import Data from Custom Objects, Import Data from Custom Objects to merged area, Import Data from DataTable, Import Data from dynamic object as data source, Import Data from DataColumn, Import Data from DataView, Import Data from DataGrid, Import Data from GridView, Import HTML formatted data, Import Data Data from JSON
---
{{% alert color="primary" %}}

この記事では、開発者が Aspose.Cells を通じてアクセスできるいくつかのデータ インポート テクニックについて説明します。

{{% /alert %}}

##  **データをワークシートにインポートする方法**

Aspose.Cells の Excel ファイルを開くと、ファイル内のすべてのデータが自動的にインポートされます。 Aspose.Cells は、他のデータ ソースからデータをインポートすることもできます。

Aspose.Cells は、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Microsoft Excel ファイルを表すクラス。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。ワークシートは次のように表されます。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスが提供するのは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection は、さまざまなデータ ソースからデータをインポートするための便利なメソッドを提供します。この記事では、これらの方法の使用方法について説明します。

##  **ICellsDataTable インターフェイスを使用して Excel にデータをインポートする方法**
埋め込む[ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable)さまざまなデータソースをラップしてから使用します[Cells.インポートデータ()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata)データを Excel ワークシートにインポートします。
###  **サンプルコード**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

の実装*CustomerDataSource*、*Customer*、および *CustomerList*クラスは以下に与えられます

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


##  **配列から Excel にデータをインポートする方法**

配列からスプレッドシートにデータをインポートするには、[**配列のインポート**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。のオーバーロードされたバージョンが多数あります。[**配列のインポート**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)メソッドですが、一般的なオーバーロードは次のパラメーターを受け取ります。

- *Array**、コンテンツのインポート元の配列オブジェクト。
- *行番号**、データがインポートされる最初のセルの行番号。
- *列番号**、データがインポートされる最初のセルの列番号。
- *垂直方向**。データを垂直方向または水平方向のどちらでインポートするかを指定するブール値です。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

##  **ArrayList から Excel にデータをインポートする方法**

データをインポートするには*配列リスト*ワークシートに対して、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションの[**インポート配列リスト**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist)方法。 ImportArray メソッドは次のパラメータを受け取ります。

-  *配列リスト**、を表します*配列リスト*インポートしているオブジェクト。
- *行番号**は、データがインポートされる最初のセルの行番号を表します。
- *列番号**は、データがインポートされる最初のセルの列番号を表します。
- *垂直方向**。データを垂直方向または水平方向のどちらでインポートするかを指定するブール値です。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

##  **カスタムオブジェクトからExcelにデータをインポートする方法**

オブジェクトのコレクションからワークシートにデータをインポートするには、次を使用します。[**カスタムオブジェクトのインポート**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index)。必要なオブジェクトのリストを表示するには、メソッドに列/プロパティのリストを指定します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

##  **カスタムオブジェクトから結合領域にデータをExcelにインポートする方法**

オブジェクトのコレクションから結合されたセルを含むワークシートにデータをインポートするには、次を使用します。[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)財産。 Excel テンプレートにセルが結合されている場合は、次の値を設定します。[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)プロパティを true に設定します。を渡す[**インポートテーブルオプション**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions)オブジェクトを列/プロパティのリストとともにメソッドに追加して、目的のオブジェクトのリストを表示します。次のコードサンプルは、の使用法を示しています。[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)カスタム オブジェクトから結合されたセルにデータをインポートするプロパティ。添付資料をご覧ください[ソース Excel](90112033.xlsx)ファイルと[Excel出力](90112034.xlsx)参考用のファイルです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

##  **DataTable から Excel にデータをインポートする方法**

*DataTable* からデータをインポートするには、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションの[**インポートデータテーブル**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)方法。のオーバーロードされたバージョンが多数あります。[**インポートデータテーブル**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)メソッドですが、一般的なオーバーロードは次のパラメーターを受け取ります。

-  *データテーブル**、*データ表*コンテンツのインポート元のオブジェクト。
-  *フィールド名が表示されます**。フィールドの名前が表示されるかどうかを指定します。*データ表*列を最初の行としてワークシートにインポートするかどうかを指定する必要があります。
- *開始セル** は、*DataTable* の内容をインポートする開始セルの名前 (たとえば、「A1」) を表します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

##  **データソースとして動的オブジェクトから Excel にデータをインポートする方法**

Aspose.Cells は、動的オブジェクトをデータソースとして操作する機能を提供します。これは、プロパティがオブジェクトに動的に追加されるデータソースの使用に役立ちます。プロパティがオブジェクトに追加されると、Aspose.Cells は最初のエントリをテンプレートとみなし、それに応じて残りを処理します。これは、何らかの動的プロパティが最初の項目にのみ追加され、他のオブジェクトには追加されない場合、Aspose.Cells はコレクション内のすべての項目が同じである必要があるとみなします。

この例では、最初に 2 つの変数のみを含むテンプレート モデルが使用されます。このリストは動的オブジェクトのリストに変換されます。次に、いくつかの追加フィールドがそれに追加され、最終的にワークブックにロードされます。ワークブックは、テンプレート XLSX ファイルにある値のみを選択します。このテンプレート ワークブックでは、パラメーターも含まれるスマート マーカーを使用します。パラメータを使用すると、情報のレイアウト方法を変更できます。スマート マーカーの詳細については、次の記事を参照してください。

[スマートマーカーの使用](/cells/ja/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

##  **DataColumn から Excel にデータをインポートする方法 (.NET)**

A *データ表*または*データビュー*オブジェクトは 1 つ以上の列で構成されます。開発者は、任意の列からデータをインポートすることもできます。*データ表*または*データビュー*に電話することで[**データのインポート**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。の[**データのインポート**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)メソッドは次の型のパラメータを受け取ります[**インポートテーブルオプション**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions)。の[**インポートテーブルオプション**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions)クラスが提供するのは[**列インデックス**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)列インデックスの配列を受け入れるプロパティ。

以下のサンプル コードは、[**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)選択した列をインポートします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

##  **DataView から Excel にデータをインポートする方法 (.NET)**

 *DataView* からデータをインポートするには、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションの[**データのインポート**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)方法。のオーバーロードされたバージョンが多数あります。[**データのインポート**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)メソッドですが、DataView のメソッドは次のパラメーターを受け取ります。

- **データビュー:**の*データビュー*コンテンツをインポートしようとしているオブジェクト。
- **最初の行:**データがインポートされる最初のセルの行番号。
- **最初の列:**データがインポートされる最初のセルの列番号。
- **インポートテーブルオプション:**インポートオプション。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

##  **DataGrid から Excel にデータをインポートする方法 (.NET)**

からデータをインポートすることが可能です*データグリッド*に電話することで[**インポートデータグリッド**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。のオーバーロードされたバージョンが多数あります。[**インポートデータグリッド**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)メソッドですが、一般的なオーバーロードは次のパラメーターを受け取ります。

- *データグリッド**、*データグリッド*コンテンツのインポート元のオブジェクト。
- *行番号**、データがインポートされる最初のセルの行番号。
- *列番号**、データがインポートされる最初のセルの列番号。
- *行の挿入**。データを適合させるためにワークシートに追加の行を追加する必要があるかどうかを示すブール型プロパティです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

##  **GridView から Excel にデータをインポートする方法**

データをインポートするには*グリッドビュー*コントロール、を呼び出します[**インポートグリッドビュー**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。

Aspose.Cells を使用すると、データをスプレッドシートにインポートするときに、HTML でフォーマットされた値を尊重できます。データのインポート中に HTML 解析が有効になっている場合、Aspose.Cells は HTML を対応するセル形式に変換します。

##  **HTML 形式のデータを Excel にインポートする方法**

Aspose.Cells は、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)外部データ ソースからデータをインポートするための非常に便利なメソッドを提供するクラス。この記事では、データのインポート中に HTML の書式設定されたテキストを解析し、HTML を書式設定されたセル値に変換する方法を説明します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

##  **JSON から Excel にデータをインポートする方法**

Aspose.Cells は、[**Jsonユーティリティ**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)JSON を処理するためのクラス。[**Jsonユーティリティ**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)クラスには[**データのインポート**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)JSON データをインポートする方法。 Aspose.Cells では、[**JsonLayoutオプション**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)JSON レイアウトのオプションを表すクラス。の[**データのインポート**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)メソッドは受け入れます[**JsonLayoutオプション**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)パラメータとして。の[**JsonLayoutオプション**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)クラスは次のプロパティを提供します。

- [**テーブルとしての配列**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable)配列内をテーブルとして処理するかどうかを示します。
- [**数値または日付を変換**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate)JSON の文字列を数値または日付のどちらに変換するかを示す値を取得または設定します。
- [**日付形式**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat)日付値の形式を取得および設定します。
- [**配列タイトルを無視する**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle)オブジェクトのプロパティが配列の場合にタイトルを無視するかどうかを示します
- [**Null を無視**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull)null 値を無視するかどうかを示します。
- [**オブジェクトタイトルを無視**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle)オブジェクトのプロパティがオブジェクトの場合にタイトルを無視するかどうかを示します。
- [**数値形式**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat)数値の形式を取得および設定します。
- [**タイトルスタイル**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle)タイトルのスタイルを取得および設定します。

以下のサンプル コードは、[**Jsonユーティリティ**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)そして[**JsonLayoutオプション**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)JSON データをインポートするクラス。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

##  **アドバンストトピック**
- [データをワークシートにインポートするときに数式フィールドを指定する](/cells/ja/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [Cells データテーブル行を挿入するときに最初の行を下にシフトします](/cells/ja/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
