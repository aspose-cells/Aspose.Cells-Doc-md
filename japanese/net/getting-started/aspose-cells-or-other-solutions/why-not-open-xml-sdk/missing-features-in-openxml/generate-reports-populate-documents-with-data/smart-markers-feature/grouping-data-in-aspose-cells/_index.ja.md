---
title: Aspose.Cells のデータのグループ化
type: docs
weight: 10
url: /ja/net/grouping-data-in-aspose-cells/
---
一部の Excel レポートでは、読みやすく分析しやすくするために、データをグループに分割する必要がある場合があります。データをグループに分割する主な目的の 1 つは、レコードの各グループに対して計算を実行する (集計操作を実行する) ことです。

Aspose.Cells スマート マーカーを使用すると、フィールドごとにデータをグループ化し、データ セットまたはデータ グループの間に集計行を配置できます。たとえば、Customers.CustomerID でデータをグループ化すると、グループが変更されるたびに集計レコードを追加できます。

次のサンプル コード スニペットは、スマート マーカーを使用して Excel レポートのデータをグループ化する方法を示しています。
## **パラメーター**
以下は、データのグループ化に使用されるスマート マーカー パラメーターの一部です。
**グループ:ノーマル/マージ/リピート**

選択できる 3 種類のグループをサポートしています。

- 通常 - フィールド値によるグループ化は、列内の対応するレコードに対して繰り返されません。代わりに、データ グループごとに 1 回出力されます。
- merge - 通常のパラメーターと同じ動作ですが、各グループ セットのフィールドごとにグループ内のセルを結合します。
- 繰り返し - フィールド値によるグループ化は、対応するレコードに対して繰り返されます。

複数のパラメーターがある場合は、スペースを入れずにコンマで区切ります: parameterA、parameterB、parameterC
### **例**
この例は、実際のグループ化パラメーターの一部を示しています。 Northwind.mdb Microsoft Access データベースを使用し、"Order Details" という名前のテーブルからデータを抽出します。 Microsoft Excel で SmartMarker_Designer.xls というデザイナー ファイルを作成し、ワークシートのさまざまなセルにスマート マーカーを配置します。マーカーは、ワークシートを埋めるために処理されます。データは、グループ フィールドごとに配置および編成されます。

デザイナー ファイルには 2 つのワークシートがあります。最初に、下のスクリーンショットに示すように、グループ化パラメーターを使用してスマート マーカーを配置します。 3 つのスマート マーカー (グループ化パラメーター付き) が配置されます。
&=Order Details.OrderID(group:merge,skip:1),
&=Order Details.Quantity(subtotal9:Order Details.OrderID)、および
&=Order Details.UnitPrice(subtotal9:Order Details.OrderID) はそれぞれ A5、B5、C5 に入ります。

{{< highlight "csharp" >}}

 //Create a connection object, specify the provider info and set the data source.

OleDbConnection con = new OleDbConnection("provider=microsoft.jet.oledb.4.0;data source=Northwind.mdb");

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

wd.Workbook = new Workbook("SmartMarkerDesigner.xls");

//Set the datatable as the data source.

wd.SetDataSource(dt);

//Process the smart markers to fill the data into the worksheets.

wd.Process(true);

//Save the excel file.

wd.Workbook.Save("outSmartMarker_Designer.xls");

{{< /highlight >}}
## **サンプルコードをダウンロード**
- [ビットバケット](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Grouping%20Data%20OLE%20DB%20%28Aspose.Cells%29.zip)
