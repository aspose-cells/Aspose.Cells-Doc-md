---
title: データのグルーピング
type: docs
weight: 10
url: /ja/net/grouping-data/
---

Excelの報告書では、データをグループ化して読みやすくし、分析しやすくする必要があることがあります。データをグループに分割する主な目的の1つは、各レコードのグループごとに計算（集計演算）を実行することです。

Aspose.Cellsのスマートマーカーを使用すると、フィールドごとにデータをグループ化し、データセットまたはデータグループ間に要約行を配置できます。 たとえば、Customers.CustomerIDごとにデータをグループ化する場合、グループが変更されるたびに要約レコードを追加できます。

次のコードスニペットの例は、スマートマーカーを使用してExcelレポートでデータをグループ化する方法を示しています。
## **パラメータ**
次に、データのグループ化に使用されるスマートマーカーパラメータをいくつか紹介します。
**group:normal/merge/repeat**

選択できる3種類のグループをサポートしています。

- 通常 - グループ化フィールドの値は、対応するレコードの列に対して繰り返されず、代わりにデータグループごとに一度だけ印刷されます。
- マージ - 通常パラメータと同じ動作ですが、各グループセットのグループ化フィールドをセルにマージします。
- 繰り返し - グループ化フィールドの値は、対応するレコードに対して繰り返されます。

複数のパラメータを持つ場合は、コンマで区切りますが、スペースは入れません：parameterA,parameterB,parameterC。
### **例**
この例では、グルーピングパラメータのいくつかを実演しています。Microsoft AccessデータベースのNorthwind.mdbを使用し、「Order Details」という名前のテーブルからデータを抽出します。Microsoft ExcelでSmartMarker_Designer.xlsという名前の設計ファイルを作成し、ワークシートのさまざまなセルにスマートマーカーを配置します。マーカーはワークシートを埋めるように処理されます。データはグループフィールドによって配置および整理されます。

設計ファイルには2つのワークシートがあります。1番目のワークシートには、以下のスクリーンショットに示すように、グルーピングパラメータを持つスマートマーカーを配置します。3つのスマートマーカー（グルーピングパラメータを持つ）が配置されます：
&=Order Details.OrderID(group:merge,skip:1),
&=Order Details.Quantity(subtotal9:Order Details.OrderID)及び
&=Order Details.UnitPrice(subtotal9:Order Details.OrderID)は、それぞれA5、B5、C5に配置されます。

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Grouping Data OLE DB.xlsx";

//Create a connection object, specify the provider info and set the data source.

OleDbConnection con = new OleDbConnection("provider=microsoft.jet.oledb.4.0;data source=~\\..\\..\\..\\Data\\Northwind.mdb");

//Open the connection object.

con.Open();

//Create a command object and specify the SQL query.

OleDbCommand cmd = new OleDbCommand("Select * from [Order Details]", con);

//Create a data adapter object.

OleDbDataAdapter da = new OleDbDataAdapter();

//Specify the command.

da.SelectCommand = cmd;

//Create a dataset object.

DataSet ds = new DataSet();

//Fill the dataset with the table records.

da.Fill(ds, "Order Details");

//Create a datatable with respect to dataset table.

DataTable dt = ds.Tables["Order Details"];

//Create WorkbookDesigner object.

WorkbookDesigner wd = new WorkbookDesigner();

//Open the template file (which contains smart markers).

wd.Workbook = new Workbook(FileName);

//Set the datatable as the data source.

wd.SetDataSource(dt);

//Process the smart markers to fill the data into the worksheets.

wd.Process(true);

//Save the excel file.

wd.Workbook.Save(FileName);

{{< /highlight >}}
## **サンプルコードをダウンロード**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Grouping%20Data%20OLE%20DB%20%28Aspose.Cells%29.zip)
