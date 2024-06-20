---
title: エレガントなグラフを使用したフォーマット済みのExcelレポートの動的生成
type: docs
weight: 130
url: /ja/net/aspose-cells-gridweb/dynamically-generate-formatted-excel-reports-with-an-elegant-graph/
keywords: GridWeb,レポート生成,レポート
description: この記事では、GridWebでのレポート生成方法について紹介しています。
---

{{% alert color="primary" %}} 

このドキュメントは、データをデータソースから抽出し、見栄えの良いグリッドのようなコントロールに貼り付け、チャートを含めてそのレポートをMS Excelにエクスポートして分析、比較、印刷を行う方法について提供するよう設計されています。

{{% /alert %}} 
## **概要**
報告とプレゼンテーションの両方を要求する特定のWebシナリオがあります。この記事では、WYSIWYGの方法で動的にスタイリッシュなExcelレポートを設計および生成するのがどれほど簡単かについて説明します。 Aspose.Cells.GridWebコントロールを使用して、XMLファイルからデータをエクスポートし（他のデータソースも利用可能）、MS Excelのように豊かで魅力的なフォーマットを適用し、セルの計算結果を得る環境を提供します。 Aspose.Cellsコンポーネントを使用して、Worksheetソースデータに基づいた洗練されたチャートを生成し、Sales Reportにチャート画像を貼り付けます。最後に、添付されたグラフを含むExcelレポートをAspose.Cellsコンポーネントを使用してディスクに保存します。

この記事には、その機能を備えたソースコードと完全機能のデモプロジェクトが含まれています。

ユーザーがワークシートにデータを入力し、行や列のセルにフォーマットを適用し、データソースの範囲に基づいてグラフを埋め込んでから、Excelレポートをディスクに保存する方法について、詳細な理解を提供します。
## **Asposeのコンポーネント**
私は[Aspose](http://www.aspose.com/)の3つのコンポーネントを使用して、このタスクを簡単に実行しています。 [Aspose](http://www.aspose.com/)は、.NETおよびJavaのコンポーネントのパブリッシャーで、機能豊富なコンポーネントを提供しています。 [Aspose](http://www.aspose.com/)は、ファイル形式コンポーネント、レポート製品、ビジュアルコンポーネント、ユーティリティコンポーネントなど、さまざまな形式のドキュメント（DOC、RTF、WordML、HTML、PDF、XLS、SpreadsheetML、Tab Delimited、CSV、PPT、SWF、EMF、WMF、MPX、MPDなど）をプログラムで開く、変更する、生成する、保存する、マージする、変換するなどの機能を提供しています。

このクエストで使用された3つのコンポーネントをご紹介する機会を頂きたいと思います。
## **Aspose.Cells Grid Controls**
Aspose.Cells Grid Controlsは、総合的なグリッドソリューションです。 Aspose.Cells Grid Controlsには、デスクトップアプリケーションをサポートする2つの異なるGUI .NETコンポーネント（Aspose.Cells.GridDesktopおよびAspose.Cells.GridWeb）がパッケージ化されています。デスクトップアプリケーションおよびWebアプリケーションをサポートするために、両バージョンは同等の機能を備えています。 Aspose.Cells.GridWebは、Excelスプレッドシートへのインポートおよびエクスポートの機能を提供します。Excelに詳しい人（最終ユーザーでも）でも、グリッドの外観や操作をデザインすることができます。 Aspose.Cells.GridWebは、開発者にグリッドの外観、操作や挙動に対する完全な制御機能を提供する使いやすく、機能豊富なAPIを提供しています。製品の詳細や機能については、特長一覧の概要、Aspose.Cells.GridWebドキュメント、 [デモ](https://aspose.github.io/)をオンラインで掲載しているものを確認してください。
## **Aspose.Cells**
**Aspose.Cells**は、Microsoft Excelのインストールをクライアントまたはサーバーサイドで利用しないでExcelスプレッドシートを読み書きできるようにするExcelスプレッドシートレポーティングコンポーネントです。 **Aspose.Cells**は、データの基本的なエクスポート以上の機能を提供する機能豊富なコンポーネントです。 **Aspose.Cells**を使用すると、データのエクスポート、スプレッドシートの細部や各レベルでのフォーマット設定、画像のインポート、チャートのインポート、チャートの作成、チャートの操作、Excelデータのストリーム処理、XLS、CSV、SpreadsheetML、TabDelimited、TXT、XML（[Aspose.Pdf](https://products.aspose.com/pdf/)統合）など、さまざまな形式での保存などができます。 **Aspose.Cells**は、プログラマー向けの使いやすく、機能豊富な**API**を提供しており、多くの機能が用意されています。製品の詳細や機能については、機能一覧、**Aspose.Cells**ドキュメント、オンラインのデモをご確認ください。評価版を [ダウンロード](https://downloads.aspose.com/cells)して無料で利用することができます。
## **インターフェースの設計**
Visual Studio.Net で新しい Asp.Net ウェブアプリケーションの作成を始めます。

最初に、プロジェクトに Aspose.Cells.GridWeb.dll、Aspose.Chart.dll、Aspose.Cells.dll の 3 つのコンポーネントの**参照を追加**します。次に、ページにいくつかのコントロールを配置し、それらのプロパティを設定します（ドロップダウンリスト、コマンドボタン、ラベル）。そして、ツールボックスから**GridWeb**コントロール(**Aspose.Cells.GridWeb**制御)を追加します。この3つのコンポーネントに参照を追加した後、**GridWeb**コントロールがツールボックスに表示されます。他の2つのコンポーネント（**Aspose.Chart**および**Aspose.Cells**）は、ライブラリのみでプロジェクトに参照が追加されます。

また、「file」と「images」の 2 つのフォルダを作成し、「Products.xml」と「chart.gif」をそれぞれ追加します。XML ファイルは、データを**GridWeb**ワークシートに入力するために抽出されるデータソースファイルです。画像ファイルは、**GridWeb**コントロールに配置されるカスタムボタンに画像を提供します。

今、カスタムコマンドボタンを作成します。**GridWeb**コントロールを右クリックし、「カスタムコマンドボタン...」オプションをクリックします。

これにより、カスタムコマンドボタンエディタが起動されます。エディタでは、ツールチップが添付されたカスタムコマンド画像ボタンを作成することができます。ボタンのいくつかのプロパティの値を指定します。 たとえば、コマンド（名前）-> "btnChart"、ImageUrl -> 画像ファイルへのパス（"chart.gif"）、ToolTip -> ツールチップを指定します。

これで、赤い枠で囲まれたカスタムコマンドボタンが次のスクリーンショットで表示されます。

|![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_1.png)|
| :- |


最後に、ラベルとコマンドボタンのフォント属性（太字）を設定します。また、コントロールのサイズを調整して最終的な外観を整えます。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_2.png)
## **XMLファイルからのデータの取得**
プロジェクトで使用される XML ファイル構造は次のとおりです。
### **XMLファイル構造**
**XML**

{{< highlight csharp >}}

 <?xml version="1.0" standalone="yes"?>

<SalesData>

  <Products>

    <ProductName>Data</ProductName>

    <QuantityPerUnit>Data</QuantityPerUnit>

    <CategoryName>Data</CategoryName>

    <UnitPrice>Data</UnitPrice>

    <Sale>Data</Sale>

  </Products>

 .........

</SalesData>



{{< /highlight >}}

{{< highlight java >}}

 private void Page_Load(object sender, System.EventArgs e)

{

if (!IsPostBack)

{

	// Uncomment the code below when you have purchased license

	// for Aspose.Cells.GridWeb, Aspose.Chart and Aspose.Cells. You need

	// to deploy the licenses in the same folder as your executable,

      // alternatively you can add the license files as an embedded

      // resource to your project.

	//

	// Set the license for Aspose.Cells.GridWeb

	// Aspose.Cells.GridWeb.License gridwebLicense = new

	// Aspose.Cells.GridWeb.License();

	// gridwebLicense.SetLicense("Aspose.Grid.lic");

	//

	// // Set the license for Aspose.Chart

	// Aspose.Chart.License chartLicense = new

	// Aspose.Chart.License();

	// chartLicense.SetLicense("Aspose.Chart.lic");

	//

	// // Set the license for Aspose.Cells

	// Aspose.Cells.License cellsLicense = new

	// Aspose.Cells.License();

	// cellsLicense.SetLicense("Aspose.Cells.lic");

	//Create a DataSet object.

	DataSet ds = new DataSet();

	//Get the Virtual Folder Path.

	string path = MapPath(".");

	//Reads XML data from xml file into DataSet object.

	ds.ReadXml(path + "\\file\\Products.xml");

	//Call the custom method to obtain distinct values from

	//CategoryName field and store data into an object array.

	object [] drs = GetDistinctValues(ds.Tables[0],"CategoryName");

	//Fill the drop down list with distinct field items.

	for(int i = 0;i<drs.Length;i++)

	{

		DropDownList1.Items.Add(drs[i].ToString());

	}

}

}

//This method is used to filter distinct values from CategoryName field in the datatable.

private object[] GetDistinctValues(DataTable dtable, string colName)

{

	// Create a Hashtable object.

	Hashtable hTable = new Hashtable();

	// Loop through the datatable rows and add distinct values to

	// Hashtable object minimizing the duplicates in the field.

	foreach (DataRow drow in dtable.Rows)

	if(!hTable.ContainsKey(drow[colName]))

	hTable.Add(drow[colName], string.Empty);

	// Create an object array based on the distinct key values of the Hashtable object.

	object[] objArray = new object[hTable.Keys.Count];

	// Copy the disctinct values to fill the array.

	hTable.Keys.CopyTo(objArray, 0);

	// Return the array object.

	return objArray;

}

{{< /highlight >}}
## **Aspose.Cells.GridWeb コントロールのワークシートにデータを入力する**
**GridWeb**コントロールの API を使用して、ソース XML ファイルからワークシートにデータを入力します。コマンドボタン（ラベル"Show Report"）のクリックイベントハンドラにコードを記述します。データレポートは、ドロップダウンリストから選択されたアイテムに基づいてフィルタリングされます。



{{< highlight java >}}

 //Clears datasheets of the GridWeb control.

GridWeb1.WebWorksheets.Clear();

//Create a DataSet object.

DataSet ds = new DataSet();

//Get the Virtual Folder path.

string path = MapPath(".");

//Reads XML data from xml file into DataSet object.

ds.ReadXml(path + "\\file\\Products.xml");

//Create a DataView based on the datatable.

DataView dv = new DataView(ds.Tables[0]);

//Filter data in the DataView object based on the selected drop down list item.

dv.RowFilter = "CategoryName ='" + DropDownList1.SelectedItem.Text + "'";

//Importing data from the filtered DataView object to create and

//fill "Products" Worksheet start from A4 cell.

GridWeb1.WebWorksheets.ImportDataView(dv, null, null,"Products",3,0);

{{< /highlight >}}
## **セルのデータのフォーマット**
ワークシート上の異なるタイプの情報を区別するため、データを最適に表示し、ワークシートを見やすくするために、ワークシートのフォーマットを行います。**Format**はスタイルを表し、フォントやフォントサイズ、数値形式、セルの境界線、セルの塗りつぶし、インデント、セル内の配置やテキストの向きなどの一連の特性で定義されます。

上記に追加のコードを組み合わせます。レポートのタイトル/サブタイトルを配置し、タイトル、サブタイトル、詳細セルにフォーマットを適用します。2 つのフィールド（UnitPrice および Sale フィールド）に数値形式を適用し、**Aspose.Cells.GridWeb**API を使用して行と列の高さ/幅を調整します。



{{< highlight java >}}

 //Create the title cell (A1) in the sheet and apply formattings.

//The following lines input a string value to the cell, specify

//font size, specify horizontal and vertical align settings, set

//foreground and background colors and merge cells (A1:E2).

WebWorksheet sheet = GridWeb1.WebWorksheets[0];

sheet.Cells["A1"].PutValue("Product Sales By Category");

sheet.Cells["A1"].Style.Font.Size = new FontUnit("20pt");

sheet.Cells["A1"].Style.HorizontalAlign = HorizontalAlign.Center;

sheet.Cells["A1"].Style.VerticalAlign = VerticalAlign.Middle;

sheet.Cells["A1"].Style.BackColor = Color.SkyBlue;

sheet.Cells["A1"].Style.ForeColor = Color.Blue;

sheet.Cells.Merge(0, 0, 2, 5);

//Create the subtitle cell (A3) in the sheet and apply formattings.

//The following lines input a string value to the cell, specify

//font size with attributes, specify horizontal and vertical align

//settings, set foreground and background colors and merge cells

//(A3:E3).

sheet.Cells["A3"].PutValue(DropDownList1.SelectedItem.Text);

sheet.Cells["A3"].Style.Font.Size = new FontUnit("13pt");

sheet.Cells["A3"].Style.Font.Bold = true;

sheet.Cells["A3"].Style.Font.Italic = true;

sheet.Cells["A3"].Style.HorizontalAlign = HorizontalAlign.Left;

sheet.Cells["A3"].Style.VerticalAlign = VerticalAlign.Middle;

sheet.Cells["A3"].Style.BackColor = Color.SeaGreen;

sheet.Cells["A3"].Style.ForeColor = Color.Yellow;

sheet.Cells.Merge(2, 0, 1, 5);

//Obtain the last row and column (which contain data) indexes.

int totalrow = sheet.Cells.MaxRow +1;

int totalcol = sheet.Cells.MaxColumn;

//Get the sheet Cells collections

WebCells cells = sheet.Cells;

//Define the Cell object.

WebCell cell;

//Loop through the data in the sheet and format two fields with

//Currency number style.

for (int i = 4;i<=totalrow;i++)

{

	//Format the Sale Column.

	cell = cells[i,totalcol];

	cell.PutValue(cell.StringValue,true);

	cell.NumberType = NumberType.Currency1;

	//Format the UnitPrice Column.

	cell = cells[i,totalcol-1];

	cell.PutValue(cell.StringValue,true);

	cell.NumberType = NumberType.Currency1;

}

//Insert the Total row with data, formula and formatting style.

//It will calculate the total Sales of a Category.

cells[totalrow,0].PutValue( DropDownList1.SelectedItem.Text + " Total" );

cells[totalrow,0].Style.Font.Bold = true;

cells[totalrow,totalcol].Formula = "=SUM(E5:E" + totalrow.ToString() + ")";

cells[totalrow,totalcol].Style.Font.Bold = true;

//Specify some Row and Column formattings. It will set row height

//and column width accordingly.

cells.SetRowHeight(2, new Unit("17pt"));

cells.SetColumnWidth(0, new Unit("157pt"));

cells.SetColumnWidth(1, new Unit("106pt"));

cells.SetColumnWidth(2, new Unit("87pt"));

cells.SetColumnWidth(3, new Unit("56pt"));

cells.SetColumnWidth(4, new Unit("50pt"));



{{< /highlight >}}
## **Aspose.Cells コンポーネントを使用して、グラフ付きのフォーマット済みレポート（.XLS ファイル）を生成する**
次に、フォーマット済みレポートをディスクに保存するためのコードを記述します。**GridWeb**の**Save**ボタンを利用します。**GridWeb**の**SaveCommand**イベントは、保存ボタンをクリックすると発生し、ここでフォーマット済みレポートを MS Excel にエクスポートし、グラフを生成して出力エクセルファイルに埋め込みます。**Aspose.Chart**コンポーネントで作成されたチャート画像を挿入せずに、**Aspose.Cells**のAPIを使用して類似のチャートを作成し、MS Excel でチャートを編集できるようにします。





{{< highlight java >}}

 //This GridWeb control event is fired when you click on the "Save" button

//of the control. After Clicking this button "File Download" dialog is

//displayed and you may open into MS Excel / save the output excel file //with graph to disk.

private void GridWeb1_SaveCommand(object sender, System.EventArgs e)

{

	//Create MemoryStream object.

	System.IO.MemoryStream ms = new System.IO.MemoryStream();

	//Save the GridWeb's Report to the stream.

	this.GridWeb1.WebWorksheets.SaveToExcelFile(ms);

	//Create a new Workbook.

	Workbook workbook = new Workbook();

	//Open the stream into the Workbook.

	workbook.Open(ms);

	//Call the custom method which creates Chart.

	Workbook book = CellsChart(workbook);

	//Save the excel file displaying "File Download" dialog box.

	book.Save(ms, FileFormatType.Default);

	this.Response.ContentType = "application/vnd.ms-excel";

	this.Response.AddHeader("content-disposition", "attachment; filename=Export.xls");

	this.Response.BinaryWrite(ms.ToArray());

}

//This custom method is used to create the Chart based on the data source

//range in the GridWeb control. In this method we will use Aspose.Cells

//APIs to create the graph which will be saved later into the output //excel file.

private Workbook CellsChart(Workbook workbook)

{

	//Get the first Worksheet.

	Aspose.Cells.Worksheet sheet = workbook.Worksheets[0];

	//Get the Cells collection in the sheet.

	Aspose.Cells.Cells cells = workbook.Worksheets[0].Cells;

	//Get the last row index.

	int maxrow = sheet.Cells.MaxDataRow;

	//Unmerge the cells.

	sheet.Cells.UnMerge(maxrow,0,15,10);

	int chartIndex = 0;

	//Add a new Chart into the sheet's Chart Collection.

chartIndex = sheet.Charts.Add(Aspose.Cells.ChartType.Pie,maxrow,0,maxrow+28,5);

	//Get the Chart object.

	Aspose.Cells.Chart chart = sheet.Charts[chartIndex];

	//Set the Chart Area.

	Aspose.Cells.ChartArea chartarea = chart.ChartArea;

	chartarea.Area.Formatting = FormattingType.Custom;

	chartarea.Border.IsVisible = false;

		chartarea.Area.FillFormat.SetTwoColorGradient(Color.PowderBlue, Color.LightSkyBlue, GradientStyleType.FromCenter,1);

	//Set some properties of Chart Plot Area.

	chart.PlotArea.Area.Formatting = FormattingType.None;

	chart.PlotArea.Border.IsVisible = false;

	//Set properties of Chart Title.

	chart.Title.Text = DropDownList1.SelectedItem.Text + " Sales";

	chart.Title.TextFont.Size = 20;

	//Set properties of NSeries

	int lastdatarow = maxrow-1;

	chart.NSeries.Add("E5:E" + lastdatarow.ToString(), true);

	chart.NSeries.CategoryData = "A5:A" + lastdatarow.ToString();

	//Set the Data Labels in the chart

	Aspose.Cells.DataLabels datalabels;

	for ( int i = 0; i < chart.NSeries.Count ;i ++ )

	{

		datalabels = chart.NSeries[i].DataLabels;

		datalabels.Postion = Aspose.Cells.LabelPositionType.Center;

		datalabels.IsPercentageShown = true;

	}

	//Set the Legend settings.

	Aspose.Cells.Legend legend = chart.Legend;

	legend.Position = Aspose.Cells.LegendPositionType.Bottom;

	legend.Height = 85;

	legend.Width = 330;

	legend.AutoScaleFont = true;

	legend.Border.Color = Color.Blue;

	legend.Area.Formatting = FormattingType.Custom;

	FillFormat fillformat = legend.Area.FillFormat;

	legend.Area.Formatting = FormattingType.None;

	legend.Border.IsVisible = false;

	//Autofit the first column.

	sheet.AutoFitColumn(0);

	//Return the Workbook.

	return workbook;

}



{{< /highlight >}}
## **アプリケーションの実行**
アプリケーションを実行します。ドロップダウンリストには異なるカテゴリが表示されます。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_3.png)

販売レポートを表示したいカテゴリを選択し、「Show Report」ボタンをクリックします。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_4.png)

これにより、選択したカテゴリに基づいて**GridWeb**にレポートが表示されます。レポートは、事前に書かれたコードに基づいてデフォルトでフォーマットされています。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_5.png)

セルのデータをWYSIWYG形式でフォーマットしたい場合は、これを簡単に行うことができます。**Aspose.Cells.GridWeb**は**フォーマットセル**エディタを提供し、セルを選択して右クリックし、「セルの整形...」オプションをクリックします。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_6.png)

「フォーマットセル」ダイアログが表示されます。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_7.png)

フォント属性を指定し、OKをクリックします。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_8.png)

結果が表示されます。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_9.png)

セルのフォーマットだけでなく、セルの値も編集できます。対象のセルをダブルクリックし、値を編集します。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_10.png)

編集結果を送信し、すべての式を再計算するには、レポートを更新するための関連ボタン（赤い枠で囲まれている）をクリックします。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_11.png)

次に、グラフを作成し、コントロールに貼り付けます。データ範囲に基づいて円グラフを作成するためのカスタムコマンドボタン（赤い枠で囲まれている）をクリックします。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_12.png)

最後に、このデータレポートとグラフを MS Excel にエクスポートします。**Save**ボタン（赤い枠で囲まれている）をクリックします。**Save**ボタンをクリックすると、**ファイルのダウンロード**ダイアログが表示されます。出力エクセルファイルとグラフを MS Excel に**開く**かディスクに**保存**できます。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_13.png)

「開く」ボタンをクリックすると、Excel レポートが MS Excel にエクスポートされます。レポートの上部が表示されます。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_14.png)

Excelレポートの下部が表示されます。

![todo:image_alt_text](dynamically-generate-formatted-excel-reports-with-an-elegant-graph_15.png)
