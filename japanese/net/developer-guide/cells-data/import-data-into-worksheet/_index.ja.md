---
title: データをワークシートにインポート
type: docs
weight: 170
url: /ja/net/import-data-into-worksheet/
---
{{% alert color="primary" %}}

この記事では、開発者が Aspose.Cells を通じてアクセスできるいくつかのデータ インポート手法について説明します。

{{% /alert %}}

## **データをワークシートにインポート**

Aspose.Cells の Excel ファイルを開くと、ファイル内のすべてのデータが自動的にインポートされます。 Aspose.Cells は、他のデータ ソースからデータをインポートすることもできます。

Aspose.Cells は[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)Microsoft Excel ファイルを表すクラス。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection は、さまざまなデータ ソースからデータをインポートするための便利な方法を提供します。この記事では、これらのメソッドの使用方法について説明します。

## **ICellsDataTable インターフェイスを使用した Excel へのデータのインポート**
埋め込む[ICellsDataTable](https://reference.aspose.com/cells/net/aspose.cells/icellsdatatable)さまざまなデータソースをラップしてから使用します[Cells.ImportData()](https://reference.aspose.com/cells/net/aspose.cells/cells/importdata/#importdata)データを Excel ワークシートにインポートします。
### **サンプルコード**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "ImportICellsDataTableIntoWorksheet.cs" >}}

の実装*顧客データソース*, *お客様*、 と*顧客リスト*クラスは以下に与えられます

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ICellsDataTableDataSourceForWorkbookDesigner-2.cs" >}}


## **アレイからのインポート**

配列からスプレッドシートにデータをインポートするには、[**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。には多くのオーバーロードされたバージョンがあります[**ImportArray**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarray/index)メソッドですが、典型的なオーバーロードは次のパラメーターを取ります。

- **配列**、コンテンツのインポート元の配列オブジェクト。
- **行番号**、データがインポートされる最初のセルの行番号。
- **列番号**、データがインポートされる最初のセルの列番号。
- **垂直です**、データを垂直または水平にインポートするかどうかを指定するブール値。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArray-1.cs" >}}

## **ArrayList からのインポート**

からデータをインポートするには*配列リスト*ワークシートに、[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションの[**ImportArrayList**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importarraylist)方法。 ImportArray メソッドは、次のパラメーターを取ります。

- **配列リスト**は、*配列リスト*インポートするオブジェクト。
- **行番号**は、データがインポートされる最初のセルの行番号を表します。
- **列番号**は、データがインポートされる最初のセルの列番号を表します。
- **垂直です**、データを垂直または水平にインポートするかどうかを指定するブール値。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromArrayList-1.cs" >}}

## **カスタム オブジェクトからのインポート**

オブジェクトのコレクションからワークシートにデータをインポートするには、次を使用します。[**ImportCustomObjects**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importcustomobjects/index).メソッドに列/プロパティのリストを指定して、必要なオブジェクトのリストを表示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromCustomObject-1.cs" >}}

## **カスタム オブジェクトから結合領域へのインポート**

オブジェクトのコレクションから結合セルを含むワークシートにデータをインポートするには、次を使用します。[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)財産。 Excel テンプレートにセルが結合されている場合は、次の値を設定します。[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)プロパティを true にします。渡す[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions)オブジェクトを列/プロパティのリストとともにメソッドに渡して、目的のオブジェクトのリストを表示します。次のコード サンプルは、[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/checkmergedcells)カスタム オブジェクトから結合セルにデータをインポートするためのプロパティ。添付をご覧ください[ソースエクセル](90112033.xlsx)ファイルと[エクセル出力](90112034.xlsx)参照用のファイル。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportCustomObjectsToMergedArea-1.cs" >}}

## **DataTable からのインポート**

からデータをインポートするには*データ表*を呼び出す[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションの[**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)方法。には多くのオーバーロードされたバージョンがあります[**ImportDataTable**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatatable/index)メソッドですが、典型的なオーバーロードは次のパラメーターを取ります。

- **データ表** 、*データ表*コンテンツをインポートするオブジェクト。
- **フィールド名は表示されますか**、の名前かどうかを指定します*データ表*列を最初の行としてワークシートにインポートする必要があります。
- **開始セル**は、内容をインポートする開始セルの名前 (「A1」など) を表します。*データ表*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataTable-1.cs" >}}

## **動的オブジェクトからデータ ソースとしてインポートする**

Aspose.Cells は、動的オブジェクトをデータソースとして操作する機能を提供します。プロパティがオブジェクトに動的に追加されるデータソースを使用するのに役立ちます。プロパティがオブジェクトに追加されると、Aspose.Cells は最初のエントリをテンプレートと見なし、それに応じて残りを処理します。つまり、動的プロパティが最初の項目のみに追加され、他のオブジェクトには追加されない場合、Aspose.Cells はコレクション内のすべての項目が同じであると見なします。

この例では、最初に 2 つの変数のみを含むテンプレート モデルが使用されます。このリストは動的オブジェクトのリストに変換されます。次に、いくつかの追加フィールドがそれに追加され、最終的にワークブックにロードされます。ワークブックは、テンプレート XLSX ファイルにある値のみを選択します。このテンプレート ワークブックは、パラメーターも含むスマート マーカーを使用します。パラメータを使用すると、情報のレイアウト方法を変更できます。スマート マーカーの詳細については、次の記事を参照してください。

[スマート マーカーの使用](/cells/ja/net/using-smart-markers/)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDynamicDataTable-1.cs" >}}

## **DataColumn (.NET) からのインポート**

あ*データ表*また*データビュー*オブジェクトは 1 つ以上の列で構成されます。開発者は、任意の列からデータをインポートすることもできます*データ表*また*データビュー*を呼び出すことによって[**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。の[**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)メソッドは型のパラメータを受け入れます[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions).の[**ImportTableOptions**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions)クラスは[**列インデックス**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)列インデックスの配列を受け入れるプロパティ。

以下のサンプル コードは、[**ImportTableOptions.ColumnIndexes**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/columnindexes)選択した列をインポートします。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataColumn-1.cs" >}}

## **DataView からのインポート (.NET)**

からデータをインポートするには*データビュー*を呼び出す[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクションの[**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)方法。には多くのオーバーロードされたバージョンがあります[**ImportData**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdata/index)メソッドですが、DataView のメソッドは次のパラメーターを取ります。

- **データビュー:**の*データビュー*コンテンツをインポートしようとしているオブジェクト。
- **最初の行:**データがインポートされる最初のセルの行番号。
- **最初の列:**データがインポートされる最初のセルの列番号。
- **ImportTableOptions:**インポート オプション。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataView-1.cs" >}}

## **DataGrid (.NET) からのインポート**

からデータをインポートできます。*データグリッド*を呼び出すことによって[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。には多くのオーバーロードされたバージョンがあります[**ImportDataGrid**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importdatagrid/index)メソッドですが、典型的なオーバーロードは次のパラメーターを取ります。

- **データグリッド** 、*データグリッド*コンテンツをインポートするオブジェクト。
- **行番号**、データがインポートされる最初のセルの行番号。
- **列番号**、データがインポートされる最初のセルの列番号。
- **行を挿入**、データに合わせて余分な行をワークシートに追加する必要があるかどうかを示すブール型プロパティ。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromDataGrid-1.cs" >}}

## **GridView からのインポート**

からデータをインポートするには*グリッドビュー*コントロール、呼び出し[**ImportGridView**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/importgridview)の方法[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)コレクション。

Aspose.Cells を使用すると、データをスプレッドシートにインポートする際に HTML 形式の値を尊重できます。データのインポート中に HTML 解析が有効になっている場合、Aspose.Cells は HTML を対応するセル形式に変換します。

## **HTML 形式のデータのインポート**

Aspose.Cells は[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)外部データ ソースからデータをインポートするための非常に便利なメソッドを提供するクラスです。この記事では、データのインポート中に HTML 形式のテキストを解析し、HTML を形式設定されたセル値に変換する方法を示します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportHtmlFormattedData-1.cs" >}}

## **JSON からのデータのインポート**

Aspose.Cells は[**Jsonユーティリティ**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) JSON を処理するためのクラス。[**Jsonユーティリティ**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)クラスには[**ImportData**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)JSON データをインポートするメソッド。 Aspose.Cells も提供しています[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)JSON レイアウトのオプションを表すクラス。の[**ImportData**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility/methods/importdata)メソッドが受け入れる[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)パラメータとして。の[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)クラスは、次のプロパティを提供します。

- [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable): 配列内をテーブルとして処理するかどうかを示します。
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/convertnumericordate): JSON の文字列を数値または日付に変換するかどうかを示す値を取得または設定します。
- [**日付形式**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/dateformat)日付値の形式を取得および設定します。
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle): オブジェクトのプロパティが配列の場合、タイトルを無視するかどうかを示します
- [**Null を無視**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorenull)null 値を無視するかどうかを示します。
- [**オブジェクトタイトルを無視**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignoreobjecttitle)オブジェクトのプロパティがオブジェクトの場合、タイトルを無視するかどうかを示します。
- [**NumberFormat**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/numberformat): 数値の形式を取得および設定します。
- [**タイトルスタイル**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/titlestyle)タイトルのスタイルを取得および設定します。

以下のサンプル コードは、[**Jsonユーティリティ**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)と[**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) JSON データをインポートするためのクラス。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Importing-ImportingFromJson-1.cs" >}}

## **先行トピック**
- [データをワークシートにインポートする際の数式フィールドの指定](/cells/ja/net/specify-formula-fields-while-importing-data-to-worksheet/)
- [Cells データ テーブル行を挿入するときに最初の行を下にシフトする](/cells/ja/net/shift-first-row-down-when-inserting-cells-data-table-rows/)
