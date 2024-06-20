---
title: スマートマーカーの処理によるチャートの生成
type: docs
weight: 180
url: /ja/java/generate-chart-by-processing-smart-markers/
---

{{% alert color="primary" %}} 

Aspose.CellsのAPIは、ワークブックデザイナークラスを提供し、スマートマーカーを使用する場合、フォーマットや数式がデザイナースプレッドシートに配置され、指定されたデータソースに対してスマートマーカーに従ってデータを埋め込むことが可能です。また、スマートマーカーの処理によってExcelチャートを作成することも可能であり、そのためには以下の手順が必要です。

- デザイナースプレッドシートの作成
- 指定されたデータソースに対するデザイナースプレッドシートの処理
- 埋め込まれたデータに基づいたチャートの作成

{{% /alert %}} 
## **デザイナースプレッドシートの作成**
デザイナースプレッドシートは、実行時に埋め込む内容を含むスマートマーカー、視覚的なフォーマット、数式を含む、Microsoft ExcelアプリケーションまたはAspose.CellsAPIを使用して作成されたシンプルなExcelファイルです。

{{% alert color="primary" %}} 

スマートマーカーの詳細情報は[こちら](/cells/ja/java/smart-markers/)でご覧いただけます。

{{% /alert %}} 

シンプルさを重視するために、デモンストレーション目的でデザイナースプレッドシートをAspose.CellsのAspose.Cells for Java APIを使用して作成し、後で動的に作成されたデータソースに対して処理します。

**Java**

{{< highlight csharp >}}

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

この時点で結果のスプレッドシートを保存すると、ワークシート内のデータは以下のようになります。

![todo:image_alt_text](generate-chart-by-processing-smart-markers_1.png)
## **デザイナースプレッドシートの処理**
デザイナースプレッドシートを処理するためには、デザイナースプレッドシートで使用されるスマートマーカーに対応するデータソースが必要です。たとえば、**&=$Headers(horizontal)** というスマートマーカーエントリを作成しました。これは、ヘッダーという名前の変数を表し、キーの**(horizontal)** はデータを水平に埋め込むことを示しています。

このユースケースをデモンストレーションするために、データソースをゼロから作成し、前のステップで作成したデザイナースプレッドシートに対して処理します。ただし、リアルタイムのシナリオでは、データがすでに利用可能な場合はデータソースの作成をスキップすることができます。

**Java**

{{< highlight csharp >}}

 //Create string arrays which will serve as data sources to the smart markers

String[] headers = new String[]{"", "Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10", "Item 11", "Item 12"};

String[] year2000 = new String[]{"2000", "310", "0", "110", "15", "20", "25", "30", "1222", "200", "421", "210", "133"};

String[] year2005 = new String[]{"2005", "508", "0", "170", "280", "190", "400", "105", "132", "303", "199", "120", "100"};

String[] year2010 = new String[]{"2010", "0", "210", "230", "1420", "1530", "160", "170", "110", "199", "129", "120", "230"};

String[] year2015 = new String[]{"2015", "2818", "320", "340", "260", "210", "310", "220", "0", "0", "0", "0", "122"};

{{< /highlight >}}

スマートマーカーの処理は以下のように非常に簡単です。

**Java**

{{< highlight csharp >}}

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

この時点でスプレッドシートを保存すると、データは以下のようになります。

![todo:image_alt_text](generate-chart-by-processing-smart-markers_2.png)

{{% alert color="primary" %}} 

上記のコードスニペットでは、最初のステップで作成したWorkbookクラスの既存のインスタンスを使用しています。デザイナースプレッドシートファイルがディスクまたはメモリに既にある場合は、既存のデザイナースプレッドシートをロードしてWorkbookクラスのインスタンスを作成できます。

{{% /alert %}} 
## **チャートの作成**
データが揃ったら、必要なのはデータソースに基づいたチャートを作成することだけです。例をシンプルに保つために、Chart.setChartDataRangeメソッドを使用して、さらなるチャートの設定をする必要がありません。







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GenerateChartByProcessingSmartMarkers-GenerateChartByProcessingSmartMarkers.java" >}}





最終的なチャートは以下のようになります。

![todo:image_alt_text](generate-chart-by-processing-smart-markers_3.png)
