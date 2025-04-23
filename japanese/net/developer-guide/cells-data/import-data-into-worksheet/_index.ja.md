---
title: ワークシートにデータをインポート
type: docs
weight: 170
url: /ja/net/import-data-into-worksheet/
description: Aspose.Cells for .NET APIを介してワークシートにデータをインポートする方法を学ぶ。
keywords: C#ワークシートにデータをインポート、ICellsDataTableインターフェイスを使用したExcelへのデータインポート、配列からのデータインポート、ArrayListからのデータインポート、カスタムオブジェクトからのデータインポート、カスタムオブジェクトからマージされたエリアへのデータインポート、DataTableからのデータインポート、動的オブジェクトからのデータソースとしてのデータインポート、DataColumnからのデータインポート、DataViewからのデータインポート、DataGridからのデータインポート、GridViewからのデータインポート、HTMLフォーマットデータのインポート、JSONからのデータインポート
---

{{% alert color="primary" %}}

この記事では、開発者がAspose.Cellsを通じてアクセスできるいくつかのデータインポートテクニックについて説明します。

{{% /alert %}}

## **ワークシートにデータをインポートする方法**

Aspose.CellsでExcelファイルを開くと、ファイル内のすべてのデータが自動的にインポートされます。 Aspose.Cellsは他のデータソースからもデータをインポートできます。

Aspose.CellsはMicrosoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスにはExcelファイルの各ワークシートにアクセスするための[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションを提供します。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションにはさまざまなデータソースからデータをインポートするための便利なメソッドが用意されています。この記事では、これらのメソッドの使用方法について説明します。

## **ICellsDataTableインターフェイスを使用してExcelにデータをインポートする方法**
[ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable)を実装してさまざまなデータソースをラップし、[Cells.ImportData()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata)を使用してExcelワークシートにデータをインポートします。
### **サンプルコード**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

*CustomerDataSource*, *Customer*, *CustomerList* クラスの実装は以下のとおりです

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


## **配列からExcelにデータをインポートする方法**

配列からスプレッドシートにデータをインポートするには、[**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)コレクションの[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)メソッドを呼び出します。[**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)メソッドには多くのオーバーロードバージョンがありますが、典型的なオーバーロードでは次のパラメータが必要です:

- **Array**、インポート元の配列オブジェクト。
- **行番号**、データがインポートされる最初のセルの行番号。
- **列番号**、データがインポートされる最初のセルの列番号。
- **垂直**、データを垂直または水平にインポートするかどうかを指定するブール値。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

## **配列リストからExcelにデータをインポートする方法**

*ArrayList*からワークシートにデータをインポートするには、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションの[**ImportArrayList**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist)メソッドを呼び出します。ImportArrayメソッドには次のパラメータが必要です:

- **ArrayList**、インポート元の*ArrayList*を表す。
- **行番号**、データがインポートされる最初のセルの行番号を表す。
- **列番号**、データがインポートされる最初のセルの列番号を表す。
- **垂直**、データを垂直または水平にインポートするかどうかを指定するブール値。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

## **カスタムオブジェクトからExcelにデータをインポートする方法**

オブジェクトのコレクションからワークシートにデータをインポートするには、[**ImportCustomObjects**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index)を使用します。表示する希望のオブジェクトのリストをメソッドに提供します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

## **カスタムオブジェクトからExcelにデータをインポートし、マージされたエリアをチェックする方法**

オブジェクトのコレクションからマージされたセルを含むワークシートにデータをインポートするには、[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)プロパティを使用します。Excelテンプレートにマージされたセルがある場合は、[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)プロパティの値をtrueに設定します。メソッドに表示する希望のオブジェクトのリストとともに[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions)オブジェクトを渡します。次のコードサンプルは、[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)プロパティを使用してカスタムオブジェクトからマージされたセルにデータをインポートする方法を示しています。参考のために添付の[ソースExcel](90112033.xlsx)ファイルと[出力Excel](90112034.xlsx)ファイルをご覧ください。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

## **ExcelからDataTableにデータをインポートする方法**

DataTableからデータをインポートするには、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションの[**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)メソッドを呼び出します。[**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)メソッドにはオーバーロードされたバージョンが多数ありますが、典型的なオーバーロードは次のパラメータを取ります:

- **Data table**: インポート元の*DataTable*オブジェクト。
- **フィールド名の表示**: *DataTable*の列名をワークシートに最初の行としてインポートするかどうかを指定します。
- **開始セル**: *DataTable*の内容をインポートする開始セルの名前 (例: "A1") を表します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

## **Excelから動的オブジェクトをデータソースとしてデータをインポートする方法**

Aspose.Cellsは、動的オブジェクトをデータソースとして使用する機能を提供しています。そこでは、プロパティがオブジェクトに動的に追加されます。プロパティがオブジェクトに追加された後、Aspose.Cellsは最初のエントリをテンプレートとして扱い、それ以降に応じて処理します。つまり、最初のアイテムのみに動的プロパティが追加され、他のオブジェクトには追加されていない場合、Aspose.Cellsはコレクション内のすべてのアイテムが同じであると見なします。

この例では、最初は2つの変数のみを含むテンプレートモデルが使用されています。このリストは動的オブジェクトのリストに変換されます。その後、追加のフィールドが追加され、最後にワークブックにロードされます。ワークブックはテンプレートXLSXファイル内の値のみを取得します。このテンプレートワークブックにはパラメータを含むスマートマーカーが使用されています。パラメータを使用すると、情報の配置方法を変更できます。スマートマーカーの詳細については、次の記事から取得できます:

[スマートマーカーの使用](/cells/ja/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

## **DataColumnをExcelにインポートする方法**

A *DataTable*または*DataView*オブジェクトは1つ以上の列で構成されています。開発者は、*DataTable*または*DataView*の列/列からデータをインポートするために、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションの[**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)メソッドを呼び出すこともできます。[**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)メソッドは[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions)型のパラメータを受け入れます。[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions)クラスは[**ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)プロパティを提供し、列のインデックスの配列を受け入れます。

以下に示すサンプルコードは、[**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)の使用を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

## **DataViewをExcelにインポートする方法**

DataViewからデータをインポートするには、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションの[**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)メソッドを呼び出します。[**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)メソッドにはオーバーロードされたバージョンが多数ありますが、DataView用の典型的なオーバーロードは次のパラメータを取ります:

- **DataView:**　インポート元の*DataView* オブジェクト。
- **最初の行:** データがインポートされる最初のセルの行番号。
- **最初の列:** データがインポートされる最初のセルの列番号。
- **ImportTableOptions:** インポートオプション。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

## **DataGridをExcelにインポートする方法**

*DataGrid*からデータをインポートすることができます。その際には、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションの[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)メソッドを呼び出します。[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)メソッドには多数のオーバーロードバージョンがありますが、典型的なオーバーロードは次のパラメータを取ります:

- **Data grid:** インポート元の*DataGrid* オブジェクト。
- **Row Number:** データがインポートされる最初のセルの行番号。
- **Column Number:** データがインポートされる最初のセルの列番号。
- **Insert Rows:** データを格納するためにワークシートに余分な行を追加するかどうかを示すブール値。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

## **GridViewをExcelにインポートする方法**

*GridView* コントロールからデータをインポートするには、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションの[**ImportGridView**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview)メソッドを呼び出します。

Aspose.Cellsを使用すると、データをスプレッドシートにインポートする際にHTML形式の値を正しく解釈することができます。HTMLの解析を有効にしてデータをインポートすると、Aspose.CellsはHTMLを対応するセルの書式設定に変換します。

## **ExcelにHTML形式のデータをインポートする方法**

Aspose.Cellsは、外部データソースからデータをインポートするための非常に有用なメソッドを提供する[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) クラスを提供しています。この記事では、データをインポートする際にHTML形式のテキストを解析し、HTMLを書式設定されたセルの値に変換する方法を示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

## **JSONからExcelにデータをインポートする方法**

Aspose.Cellsは、JSONを処理するための[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)クラスを提供しています。[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)クラスには、JSONデータをインポートするための[**ImportData**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)メソッドがあります。Aspose.Cellsは、JSONレイアウトのオプションを表す[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)クラスも提供しています。[**ImportData**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)メソッドは、パラメータとして[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)を受け入れます。[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)クラスには、以下のプロパティが用意されています。

- [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable)：配列内の処理がテーブルとして行われるかどうかを示します。
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate)：JSON内の文字列を数値または日付に変換するかどうかを取得または設定します。
- [**DateFormat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat)：日付値の形式を取得および設定します。
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle)：オブジェクトのプロパティが配列の場合に、タイトルを無視するかどうかを示します。
- [**IgnoreNull**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull)：null値を無視するかどうかを示します。
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle)：オブジェクトのプロパティがオブジェクトの場合に、タイトルを無視するかどうかを示します。
- [**NumberFormat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat)：数値値の形式を取得および設定します。
- [**TitleStyle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle)：タイトルのスタイルを取得および設定します。

以下のサンプルコードは、[**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)および[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)クラスを使用してJSONデータをインポートする方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

## **高度なトピック**
- [ワークシートにデータをインポートする際に式フィールドを指定する](/cells/ja/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [セルデータテーブル行を挿入するときに、最初の行を下にシフト](/cells/ja/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
{{< app/cells/assistant language="csharp" >}}
