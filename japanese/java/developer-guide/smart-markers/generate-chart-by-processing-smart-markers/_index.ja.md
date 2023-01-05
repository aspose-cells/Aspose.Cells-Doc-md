---
title: スマート マーカーを処理してチャートを生成する
type: docs
weight: 180
url: /ja/java/generate-chart-by-processing-smart-markers/
---
{{% alert color="primary" %}} 

Aspose.Cells API は、書式設定と数式がデザイナー スプレッドシートに配置され、指定されたデータ ソースに対して処理され、スマート マーカーに従ってデータを埋めるスマート マーカーを操作するための WorkbookDesigner クラスを提供します。スマート マーカーを処理して Excel グラフを作成することもできます。これには、次の手順が必要です。

- デザイナースプレッドシートの作成
- 指定されたデータ ソースに対するデザイナー スプレッドシートの処理
- 入力されたデータに基づくグラフの作成

{{% /alert %}} 
## **デザイナースプレッドシートの作成**
デザイナー スプレッドシートは、Microsoft Excel アプリケーションまたは Aspose.Cells API で作成された単純な Excel ファイルであり、視覚的な書式設定、数式、およびスマート マーカーが含まれており、コンテンツは実行時に入力されます。

{{% alert color="primary" %}} 

スマートマーカーの詳細情報が利用可能です[ここ](/cells/ja/java/smart-markers/).

{{% /alert %}} 

簡単にするために、Aspose.Cells for Java API を使用してデザイナー スプレッドシートを作成し、後でデモンストレーションのために動的に作成されたデータ ソースに対して処理します。

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access the first (default) Worksheet from the collection

Worksheet dataSheet = book.getWorksheets().get(0);

//Name the first Worksheet for referencing

dataSheet.setName("ChartData");

//Access the CellsCollection of ChartData Worksheet

Cells cells = dataSheet.getCells();

//Place the markers in the Worksheet according to desired layout

cells.get("A1").putValue("&=$Headers(horizontal)");

cells.get("A2").putValue("&=$Year2000(horizontal)");

cells.get("A3").putValue("&=$Year2005(horizontal)");

cells.get("A4").putValue("&=$Year2010(horizontal)");

cells.get("A5").putValue("&=$Year2015(horizontal)");

{{< /highlight >}}

この段階で結果のスプレッドシートを保存すると、ワークシートのデータは次のようになります。

![todo:画像_代替_文章](generate-chart-by-processing-smart-markers_1.png)
## **処理デザイナー スプレッドシート**
デザイナー スプレッドシートを処理するには、デザイナー スプレッドシートで使用されるスマート マーカーに対応するデータ ソースが必要です。たとえば、Smart Marker エントリを次のように作成しました。**&=$ヘッダー(横)**、これは名前 Headers で変数を表し、キーは**(横)**データを水平方向に入力する必要があることを示唆しています。

この使用例を示すために、データ ソースを最初から作成し、前の手順で作成したデザイナー スプレッドシートに対して処理します。ただし、リアルタイムのシナリオでは、データが既に使用可能であり、さらに処理できる可能性があるため、データが既に使用可能である場合は、データ ソースの作成をスキップできます。

**Java**

{{< highlight "csharp" >}}

 //Create string arrays which will serve as data sources to the smart markers

String[]headers = new String[]{"", "Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10", "Item 11", "Item 12"};

String[]year2000 = new String[]{"2000", "310", "0", "110", "15", "20", "25", "30", "1222", "200", "421", "210", "133"};

String[]year2005 = new String[]{"2005", "508", "0", "170", "280", "190", "400", "105", "132", "303", "199", "120", "100"};

String[]year2010 = new String[]{"2010", "0", "210", "230", "1420", "1530", "160", "170", "110", "199", "129", "120", "230"};

String[]year2015 = new String[]{"2015", "2818", "320", "340", "260", "210", "310", "220", "0", "0", "0", "0", "122"};

{{< /highlight >}}

スマート マーカーの処理は次のように非常に簡単です。

**Java**

{{< highlight "csharp" >}}

 //Create an instance of WorkbookDesigner

WorkbookDesigner designer = new WorkbookDesigner();

//Set the Workbook property for the instance of WorkbookDesigner

designer.setWorkbook(book);

//Set data sources for smart markers

designer.setDataSource("Headers", headers);

designer.setDataSource("Year2000", year2000);

designer.setDataSource("Year2005", year2005);

designer.setDataSource("Year2010", year2010);

designer.setDataSource("Year2015", year2015);

//Process the designer spreadsheet against the provided data sources

designer.process();

{{< /highlight >}}

この段階でスプレッドシートを保存すると、データは次のようになります。

![todo:画像_代替_文章](generate-chart-by-processing-smart-markers_2.png)

{{% alert color="primary" %}} 

上記のコード スニペットは、最初の手順で作成された Workbook クラスの既存のインスタンスを使用します。デザイナ スプレッドシート ファイルがディスクまたはメモリ上に既にある場合は、既存のデザイナ スプレッドシートをロードして Workbook クラスのインスタンスを作成できます。

{{% /alert %}} 
## **チャートの作成**
データが配置されたら、データ ソースに基づいてグラフを作成するだけです。例を単純にするために、Chart.setChartDataRange メソッドを使用して、チャートをさらに構成する必要がないようにします。







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GenerateChartByProcessingSmartMarkers-GenerateChartByProcessingSmartMarkers.java" >}}





最終的なチャートは次のようになります。

![todo:画像_代替_文章](generate-chart-by-processing-smart-markers_3.png)
