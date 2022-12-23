---
title: パブリック API Aspose.Cells の変更点 8.3.1
type: docs
weight: 110
url: /ja/net/public-api-changes-in-aspose-cells-8-3-1/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.3.0 から 8.3.1 への Aspose.Cells API への変更について説明します。

{{% /alert %}} 
## **追加された API**
### **プロパティ DataLabels.ShowCellRange が追加されました**
実行時にグラフのデータ ラベルをフォーマットする Excel の機能を模倣するために、プロパティ ShowCellRange が DataLabels クラスに追加されました。 Excel は、次の手順でこの機能を提供することに注意してください。

1. シリーズのデータ ラベルを選択し、右クリックしてポップアップ メニューを開きます。
1. クリック**データ ラベルの書式設定...**そしてそれは表示されます**ラベル オプション**.
1. チェックボックスをオンまたはオフにする**ラベルの内容 - Cells からの値**.

以下のサンプル コードは、グラフ シリーズのデータ ラベルにアクセスし、DataLabels.ShowCellRange メソッドを true に設定して、Excel の機能を模倣します。**ラベルの内容 - Cells からの値**.

**C#**

{{< highlight "csharp" >}}

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

**VB.NET**

{{< highlight "csharp" >}}



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

記事をご確認ください[Cell 範囲をデータ ラベルとして表示](http://aspose.com/docs/display/cellsnet/Showing+Cell+Range+as+the+Data+Labels)詳細については。

{{% /alert %}} 

### **メソッド Cell.GetTable & ListObject.PutCellValue を追加**
メソッド Cell.GetTable & ListObject.PutCellValue が Aspose.Cells for .NET 8.3.1 で追加され、ユーザーがセルから ListObject にアクセスし、行と列のオフセットを使用してその中に値を追加できるようになりました。次のサンプル コードは、ソース スプレッドシートを読み込み、テーブル内に値を追加します。

**C#**

{{< highlight "csharp" >}}

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

**VB.NET**

{{< highlight "csharp" >}}

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

記事をご確認ください[Cell からテーブルにアクセスし、行と列のオフセットを使用してテーブル内に値を追加する](http://aspose.com/docs/display/cellsnet/Accessing+Table+from+Cell+and+Adding+Values+inside+it+using+Row+and+Column+Offsets)詳細については。

{{% /alert %}} 

### **プロパティ OdsSaveOptions.IsStrictSchema11 が追加されました**
開発者が ODF v1.2 仕様に準拠した形式でスプレッドシートを保存できるようにするために、プロパティ IsStrictSchema11 が OdsSaveOptions クラスに追加されました。 IsStrictSchema11 プロパティのデフォルト値は false です。これは、Aspose.Cells API のバージョン 8.3.1 以降、デフォルトで ODS ファイルが ODF フォーマット バージョン 1.2 として保存されることを意味します。

以下のコード スニペットは、ODS ファイルを ODF 1.2 形式で保存します。

**C#**

{{< highlight "csharp" >}}

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

**VB.NET**

{{< highlight "csharp" >}}

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

記事をご確認ください[ODS ファイルを ODF 1.1 および 1.2 仕様で保存](http://aspose.com/docs/display/cellsnet/Save+ODS+file+in+ODF+1.1+and+1.2+Specifications)詳細については。

{{% /alert %}} 

### **メソッド SparklineCollection.Add が追加されました**
Aspose.Cells API は SparklineCollection.Add(string dataRange, int row, int column) メソッドを公開して、スパークライン グループのデータ範囲と場所を指定しました。 Excel は、次の手順で同じ機能を提供することに注意してください。

1. スパークラインを含むセルを選択します。
1. 選択する**スパークラインからデータを編集する**セクション内**デザイン**タブ
1. 選ぶ**グループの場所とデータの編集**.
1. 特定**データ範囲** & **位置**.

次のサンプル コードは、ソース スプレッドシートを読み込み、最初のスパークライン グループにアクセスし、スパークライン グループに新しいデータ範囲と場所を追加します。

**C#**

{{< highlight "csharp" >}}

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

**VB.NET**

{{< highlight "csharp" >}}

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

記事をご確認ください[スパークライン グループのデータ範囲と場所を指定してスパークラインをコピーする](http://aspose.com/docs/display/cellsnet/Copy+Sparkline+by+Specifying+Data+Range+and+Location+of+Sparkline+Group)詳細については。

{{% /alert %}}
