---
title: ドキュメントからデータをインポート
type: docs
weight: 10
url: /ja/net/import-export-data-from-document/
---
## **ドキュメントからデータをインポートする**

データは未加工の事実の集まりであり、これらの未加工の事実をより意味のある方法で提示するために、スプレッドシート ドキュメントまたはレポートを作成します。通常、自分でスプレッドシートにデータを追加しますが、既存のデータ リソースを再利用する必要がある場合があり、さまざまなデータ ソースからスプレッドシートにデータをインポートする必要があります。このトピックでは、さまざまなデータ ソースからワークシートにデータをインポートするいくつかの手法について説明します。

## **Aspose.Cells を使用したデータのインポート**

使用するとき**Aspose.Cells**Excel ファイルを開くと、ファイル内のすべてのデータが自動的にインポートされますが、Aspose.Cells はさまざまなデータ ソースからのデータのインポートもサポートしています。これらのデータ ソースのいくつかを以下に示します。

- **配列**
- **配列リスト**
- **データ表**
- **データ列**
- **データビュー**
- **データグリッド**
- **データリーダー**
- **グリッドビュー**

Aspose.Cells はクラスを提供し、**ワークブック**これは Excel ファイルを表します。 Workbook クラスには、Excel ファイル内の各ワークシートにアクセスできる Worksheets コレクションが含まれています。ワークシートは Worksheet クラスによって表されます。 Worksheet クラスは Cells コレクションを提供します。

Cells コレクションは、さまざまなデータ ソースからデータをインポートするための非常に便利な方法を提供します。

### **アレイからのインポート**

開発者は、配列からワークシートにデータをインポートするには、**ImportArray** Cells コレクションのメソッド。 ImportArray メソッドにはオーバーロードされたバージョンが多数ありますが、典型的なオーバーロードは次のパラメーターを取ります。

- 配列は、内容をインポートする必要がある配列オブジェクトを表します
- 行番号は、データがインポートされる最初のセルの行番号を表します
- 列番号は、データがインポートされる最初のセルの列番号を表します
- データを垂直方向または水平方向にインポートするように指定するブール値です。

{{< highlight "csharp" >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Creating an array containing names as string values

string[]names = new string[]{ "laurence chen", "roman korchagin", "kyle huang" };

//Importing the array of names to 1st row and first column vertically

worksheet.Cells.ImportArray(names, 0, 0, true);

//Saving the Excel file

workbook.Save(MyDir+"DataImport from Array.xls");

{{< /highlight >}}

### **ArrayList からのインポート**

開発者は、ArrayList からワークシートにデータをインポートするには、**ImportArrayList** Cells コレクションのメソッド。 ImportArray メソッドは、次のパラメーターを取ります。**配列リスト** 、内容をインポートする必要がある ArrayList オブジェクトを表します

- Row Number は、データがインポートされる最初のセルの行番号を表します
- 列番号 は、データがインポートされる最初のセルの列番号を表します
- Vertical 、データを垂直または水平にインポートするように指定するブール値

{{< highlight "csharp" >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Instantiating an ArrayList object

ArrayList list = new ArrayList();

//Add few names to the list as string values

list.Add("laurence chen");

list.Add("roman korchagin");

list.Add("kyle huang");

list.Add("tommy wang");

//Importing the contents of ArrayList to 1st row and first column vertically

worksheet.Cells.ImportArrayList(list, 0, 0, true);

//Saving the Excel file

workbook.Save(MyDir + "DataImport from Array List.xls");

{{< /highlight >}}

### **カスタム オブジェクトからのインポート**

開発者は、オブジェクトのコレクションからワークシートにデータをインポートできます。**ImportCustomObjects**.メソッドに列/プロパティのリストを指定して、必要なオブジェクトのリストを表示できます。

{{< highlight "csharp" >}}

//Instantiate a new Workbook

Workbook book = new Workbook();

//Clear all the worksheets

book.Worksheets.Clear();

//Add a new Sheet "Data";

Worksheet sheet = book.Worksheets.Add("Data");

//Define List

List<WeeklyItem> list = new List<WeeklyItem>();

//Add data to the list of objects

list.Add(new WeeklyItem() { AtYarnStage = 1, InWIPStage = 2, Payment = 3, Shipment = 4, Shipment2 = 5 });

list.Add(new WeeklyItem() { AtYarnStage = 5, InWIPStage = 9, Payment = 7, Shipment = 2, Shipment2 = 5 });

list.Add(new WeeklyItem() { AtYarnStage = 7, InWIPStage = 3, Payment = 3, Shipment = 8, Shipment2 = 3 });

//We pick a few columns not all to import to the worksheet

sheet.Cells.ImportCustomObjects((System.Collections.ICollection)list,

new string[]{ "Date", "InWIPStage", "Shipment", "Payment" },

true,

0,

0,

list.Count,

true,

"dd/mm/yyyy",

false);

//Auto-fit all the columns

book.Worksheets[0].AutoFitColumns();

//Save the Excel file

book.Save(MyDir+"ImportedCustomObjects.xls");

{{< /highlight >}}

### **DataTable からのインポート**

開発者は、**データ表**を呼び出してワークシートに**ImportDataTable**Cells コレクションのメソッド。には多くのオーバーロードされたバージョンがあります**ImportDataTable**メソッドですが、典型的なオーバーロードは次のパラメーターを取ります。**データ表**は、**データ表**コンテンツをインポートする必要があるオブジェクト

- **フィールド名は表示されますか**は、DataTable の列の名前を最初の行としてワークシートにインポートするかどうかを指定します
- **スタート Cell**は、DataTable の内容をインポートする開始セル (つまり "A1") の名前を表します

{{< highlight "csharp" >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Instantiating a "Products" DataTable object

DataTable dataTable = new DataTable("Products");

//Adding columns to the DataTable object

dataTable.Columns.Add("Product ID", typeof(Int32));

dataTable.Columns.Add("Product Name", typeof(string));

dataTable.Columns.Add("Units In Stock", typeof(Int32));

//Creating an empty row in the DataTable object

DataRow dr = dataTable.NewRow();

//Adding data to the row

dr[0]= 1;

dr[1]= "Aniseed Syrup";

dr[2]= 15;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Creating another empty row in the DataTable object

dr = dataTable.NewRow();

//Adding data to the row

dr[0]= 2;

dr[1]= "Boston Crab Meat";

dr[2]= 123;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Importing the contents of DataTable to the worksheet starting from "A1" cell,

//where true specifies that the column names of the DataTable would be added to

//the worksheet as a header row

worksheet.Cells.ImportDataTable(dataTable, true, "A1");

workbook.Save(MyDir+"Import From Data Table.xls");

{{< /highlight >}}

## **サンプルコードをダウンロード**

- [ビットバケット](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Import%20to%20Worksheet%20%28Aspose.Cells%29.zip)

## **ドキュメントからデータをエクスポート**

 Aspose.Cells は、ユーザーが外部データ ソースからワークシートにデータをインポートできるようにするだけでなく、ワークシート データを**データ表**.私たちが知っているように**データ表**ADO.NET の一部であり、データを保持するために使用されます。データが**データ表**、ユーザーの要件に応じて任意の方法で使用できます。

## **Aspose.Cells を使用して DataTable (.NET) にデータをエクスポートする**

開発者は、Cells クラスの ExportDataTable または ExportDataTableAsString メソッドを呼び出して、ワークシート データを DataTable オブジェクトに簡単にエクスポートできます。どちらの方法も、以下で詳しく説明するさまざまなシナリオで使用されます。

### **厳密に型指定されたデータを含む列**

スプレッドシートはデータを一連の行と列として保存することがわかっています。ワークシートの列のすべての値が厳密に型指定されている場合 (つまり、列のすべての値が同じデータ型である必要があることを意味します)、**ExportDataTable** Cells クラスのメソッド。**ExportDataTable**メソッドは、次のパラメーターを使用して、ワークシート データを次のようにエクスポートします。**データ表**物体：**行番号** 、データがエクスポートされる最初のセルの行番号を表します

- **列番号**、データがエクスポートされる最初のセルの列番号を表します
- **行の数**、エクスポートする行数を表します
- **列の数**、エクスポートする列の数を表します
- **列名のエクスポート**、ワークシートの最初の行のデータを DataTable の列名としてエクスポートするかどうかを示すブール プロパティ

{{< highlight "csharp" >}}

//Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(FOD_OpenFile.FileName, FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Exporting the contents of 2 rows and 2 columns starting from 1st cell to DataTable

DataTable dataTable = worksheet.Cells.ExportDataTable(0, 0,2, 2, true);

//Binding the DataTable with DataGrid

dataGridView1.DataSource = dataTable;

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

### **厳密に型指定されていないデータを含む列**

ワークシートの列のすべての値が厳密に型指定されていない場合 (つまり、列の値のデータ型が異なる可能性があることを意味します)、**ExportDataTableAsString** Cells クラスのメソッド。**ExportDataTableAsString**メソッドは、のと同じパラメータのセットを取ります**ExportDataTable**ワークシートデータをエクスポートするメソッド**データ表**物体。

{{< highlight "csharp" >}}

//Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(FOD_OpenFile.FileName, FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Exporting the contents of 2 rows and 2 columns starting from 1st cell to DataTable

DataTable dataTable = worksheet.Cells.ExportDataTableAsString(0, 0, 2, 2, true);

//Binding the DataTable with DataGrid

dataGridView2.DataSource = dataTable;

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **サンプルコードをダウンロード**

- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [ビットバケット](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
