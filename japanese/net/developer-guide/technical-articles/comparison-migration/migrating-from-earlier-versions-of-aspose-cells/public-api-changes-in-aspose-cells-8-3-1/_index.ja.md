---
title: Aspose.Cells 8.3.1のパブリックAPIの変更
type: docs
weight: 110
url: /ja/net/public-api-changes-in-aspose-cells-8-3-1/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cells APIのバージョン8.3.0から8.3.1への変更について、モジュール/アプリケーション開発者に興味を持っていただけるかもしれない変更について説明しています

{{% /alert %}} 
## **APIの追加**
### **DataLabels.ShowCellRangeプロパティを追加しました**
DataLabelsクラスにShowCellRangeプロパティが追加され、実行時にExcelの機能であるチャートのデータラベルの書式設定を模倣できます。Excelはこの機能を以下の手順で提供しています。 

データラベルを表示するための記事をご覧ください
1. **データラベルの書式設定...**をクリックし、**ラベルオプション**が表示されます。
1. チェックボックス **ラベルに - セルの値が含まれている** をチェックまたはチェックを外します。

以下のサンプルコードでは、チャートシリーズのデータラベルにアクセスし、DataLabels.ShowCellRangeメソッドをtrueに設定して、Excelの **ラベルに - セルの値が含まれている** 機能を模倣します。

**C#**

{{< highlight csharp >}}

 //Create workbook from the source Excel file

Workbook workbook = new Workbook("sample.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the chart inside the worksheet

Chart chart = worksheet.Charts[0];

//Check the "Label Contains - Value From Cells"

DataLabels dataLabels = chart.NSeries[0].DataLabels;

dataLabels.ShowCellRange = true;

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}

ワークシートで GridDesktop データ バインディング機能を実装する

{{< highlight csharp >}}



'Create workbook from the source Excel file

Dim m_workbook As Workbook = New Workbook("sample.xlsx")

'Access the first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Access the chart inside the worksheet

Dim m_chart As Chart = m_worksheet.Charts(0)

'Check the "Label Contains - Value From Cells"

Dim m_dataLabels As DataLabels = m_chart.NSeries(0).DataLabels

m_dataLabels.ShowCellRange = True

'Save the workbook

m_workbook.Save("output.xlsx")


{{< /highlight >}}

{{% alert color="primary" %}} 

詳細については、[Showing Cell Range as the Data Labels](http://aspose.com/docs/display/cellsnet/Showing+Cell+Range+as+the+Data+Labels)をご覧ください。

{{% /alert %}} 

### **Cell.GetTableおよびListObject.PutCellValueメソッドが追加され、ユーザーがセルからListObjectにアクセスし、行や列のオフセットを使用して値を追加できるようになりました。以下のサンプルコードは、元のスプレッドシートを読み込み、テーブル内に値を追加します。**
Cell.GetTableメソッドとListObject.PutCellValueメソッドがAspose.Cells for .NET 8.3.1で追加され、セルからListObjectにアクセスし、行と列のオフセットを使用して値を追加することができるようになりました。次のサンプルコードでは、ソースのスプレッドシートを読み込み、テーブル内に値を追加しています。

**C#**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cell D5 which lies inside the table

Cell cell = worksheet.Cells["D5"];

//Put value inside the cell D5

cell.PutValue("D5 Data");

//Access the Table from this cell

ListObject table = cell.GetTable();

//Add some value using Row and Column Offset

table.PutCellValue(2, 2, "Offset [2,2]");

//Save the workbook

workbook.Save("output.xlsx");


{{< /highlight >}}

ワークシートで GridDesktop データ バインディング機能を実装する

{{< highlight csharp >}}

 'Create workbook from source Excel file

Dim m_workbook As Workbook = New Workbook("source.xlsx")

'Access first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Access cell D5 which lies inside the table

Dim m_cell As Cell = m_worksheet.Cells("D5")

'Put value inside the cell D5

m_cell.PutValue("D5 Data")

'Access the Table from this cell

Dim table As ListObject = m_cell.GetTable()

'Add some value using Row and Column Offset

table.PutCellValue(2, 2, "Offset [2,2]")

'Save the workbook

m_workbook.Save("output.xlsx")


{{< /highlight >}}

{{% alert color="primary" %}} 

詳細については、[セルからテーブルにアクセスし、行および列のオフセットを使用して値を追加する](http://aspose.com/docs/display/cellsnet/Accessing+Table+from+Cell+and+Adding+Values+inside+it+using+Row+and+Column+Offsets)の記事をご確認ください。

{{% /alert %}} 

### **OdsSaveOptionsクラスにIsStrictSchema11プロパティが追加され、開発者がスプレッドシートをODF v1.2仕様に準拠した形式で保存できるようになりました。IsStrictSchema11プロパティのデフォルト値はfalseであり、Aspose.Cells API 8.3.1からはODSファイルはデフォルトでODFフォーマットバージョン1.2として保存されます。**
OdsSaveOptionsクラスにIsStrictSchema11プロパティが追加され、開発者がスプレッドシートをODF v1.2仕様に準拠した形式で保存できるようになりました。IsStrictSchema11プロパティのデフォルト値はfalseであり、Aspose.Cells API 8.3.1からはODSファイルはデフォルトでODFフォーマットバージョン1.2として保存されます。

以下のコードスニペットは、ODSファイルをODF 1.2形式で保存します。

**C#**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Put some value in cell A1

Cell cell = worksheet.Cells["A1"];

cell.PutValue("Welcome to Aspose!");

//Save ODS in ODF 1.2 version which is default

OdsSaveOptions options = new OdsSaveOptions();

workbook.Save("ODF1.2.ods", options);

//Save ODS in ODF 1.1 version

options.IsStrictSchema11 = true;

workbook.Save("ODF1.1.ods", options);


{{< /highlight >}}

ワークシートで GridDesktop データ バインディング機能を実装する

{{< highlight csharp >}}

 'Create workbook 

Dim m_workbook As Workbook = New Workbook()

'Access first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Put some value in cell A1

Dim m_cell As Cell = m_worksheet.Cells("A1")

m_cell.PutValue("Welcome to Aspose!")

'Save ODS in ODF 1.2 version which is default

Dim options As OdsSaveOptions = New OdsSaveOptions()

m_workbook.Save("ODF1.2.ods", options)

'Save ODS in ODF 1.1 version

options.IsStrictSchema11 = True

m_workbook.Save("ODF1.1.ods", options)

{{< /highlight >}}

{{% alert color="primary" %}} 

詳細については、[Save ODS file in ODF 1.1 and 1.2 Specifications](http://aspose.com/docs/display/cellsnet/Save+ODS+file+in+ODF+1.1+and+1.2+Specifications)をご覧ください。

{{% /alert %}} 

### **SparklineCollection.Add(string dataRange, int row, int column)メソッドを公開し、Sparklineグループのデータ範囲と配置を指定することができるようになりました。Excelは同様の機能を以下の手順で提供しています。**
SparklineCollection.Add(string dataRange, int row, int column)メソッドを公開し、Sparklineグループのデータ範囲と配置を指定することができるようになりました。Excelは同様の機能を以下の手順で提供しています。 

1. スパークラインを含むセルを選択します。
1. **デザイン**タブ内の**スパークライン**セクションから**データの編集**を選択します
1. **グループの場所とデータの編集**を選択します。
1. **データ範囲**および**場所**を指定します。

以下のサンプルコードでは、ソーススプレッドシートをロードし、最初のスパークライングループにアクセスし、新しいデータ範囲と場所を追加しています。 

**C#**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the first sparkline group

SparklineGroup group = worksheet.SparklineGroupCollection[0];

//Add Data Ranges and Locations inside this sparkline group

group.SparklineCollection.Add("D5:O5", 4, 15);

group.SparklineCollection.Add("D6:O6", 5, 15);

group.SparklineCollection.Add("D7:O7", 6, 15);

group.SparklineCollection.Add("D8:O8", 7, 15);

//Save the workbook

workbook.Save("output.xlsx");


{{< /highlight >}}

ワークシートで GridDesktop データ バインディング機能を実装する

{{< highlight csharp >}}

 'Create workbook from source Excel file

Dim m_workbook As Workbook = New Workbook("source.xlsx")

'Access first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Access the first sparkline group

Dim group As SparklineGroup = m_worksheet.SparklineGroupCollection(0)

'Add Data Ranges and Locations inside this sparkline group

group.SparklineCollection.Add("D5:O5", 4, 15)

group.SparklineCollection.Add("D6:O6", 5, 15)

group.SparklineCollection.Add("D7:O7", 6, 15)

group.SparklineCollection.Add("D8:O8", 7, 15)

'Save the workbook

m_workbook.Save("output.xlsx")


{{< /highlight >}}

{{% alert color="primary" %}} 

[Copy Sparkline by Specifying Data Range and Location of Sparkline Group](http://aspose.com/docs/display/cellsnet/Copy+Sparkline+by+Specifying+Data+Range+and+Location+of+Sparkline+Group) の記事を詳しく知りたい方は参照してください。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
