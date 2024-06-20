---
title: ドキュメントからのインポートおよびエクスポートデータ
type: docs
weight: 10
url: /ja/net/import-export-data-from-document/
---

## **ドキュメントからのデータのインポート**

データは、生の事実の集まりであり、これらの生の事実をより意味のある形で提示するためにスプレッドシートドキュメントやレポートを作成します。通常、スプレッドシートにデータを追加しますが、既存のデータリソースを再利用する必要がある場合があります。その際に異なるデータソースからワークシートにデータをインポートする必要があります。このトピックでは、異なるデータソースからワークシートにデータをインポートするためのいくつかの技術について説明します。

## **Aspose.Cellsを使用したデータのインポート**

**Aspose.Cells**を使用してExcelファイルを開くと、ファイルのすべてのデータが自動的にインポートされますが、Aspose.Cellsは異なるデータソースからのデータのインポートもサポートしています。いくつかのデータソースのうちいくつかを以下に示します。

- **Array**
- **ArrayList**
- **DataTable**
- **DataColumn**
- **DataView**
- **DataGrid**
- **DataReader**
- **GridView**

Aspose.Cellsは、Excelファイルを表す**Workbook**クラスを提供しています。Workbookクラスには、Excelファイルの各ワークシートにアクセスすることができるWorksheetsコレクションが含まれています。ワークシートはWorksheetクラスで表されます。WorksheetクラスはCellsコレクションを提供しています。

Cellsコレクションは、異なるデータソースからのデータのインポートに非常に有用なメソッドを提供しています。

### **配列からのインポート**

開発者は、Cells コレクションの **ImportArray** メソッドを呼び出すことで、配列からデータをワークシートにインポートできます。ImportArray メソッドには多くのオーバーロードされたバージョンがありますが、典型的なオーバーロードは次のパラメーターを取ります：

- 配列、インポートする内容の配列オブジェクトを表します
- 行番号、データをインポートする最初のセルの行番号を表します
- 列番号、データをインポートする最初のセルの列番号を表します
- 垂直かどうかを指定するブール値、データを縦方向または横方向にインポートするかどうかを指定します

{{< highlight csharp >}}

//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Creating an array containing names as string values

string[] names = new string[] { "laurence chen", "roman korchagin", "kyle huang" };

//Importing the array of names to 1st row and first column vertically

worksheet.Cells.ImportArray(names, 0, 0, true);

//Saving the Excel file

workbook.Save(MyDir+"DataImport from Array.xls");

{{< /highlight >}}

### **ArrayListからのインポート**

開発者は、Cells コレクションの **ImportArrayList** メソッドを呼び出すことで、ArrayList からデータをワークシートにインポートできます。ImportArray メソッドには次のパラメーターがあります：**ArrayList**、インポートする内容の ArrayList オブジェクトを表します

- 行番号、データをインポートする最初のセルの行番号を表します
- 列番号、データをインポートする最初のセルの列番号を表します
- 垂直かどうかを指定するブール値、データを縦方向または横方向にインポートするかどうかを指定します

{{< highlight csharp >}}

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

### **カスタムオブジェクトからのインポート**

開発者は、**ImportCustomObjects** を使用して、オブジェクトのコレクションからワークシートにデータをインポートできます。このメソッドに自分の希望のオブジェクトリストを表示するための列/プロパティのリストを指定できます。

{{< highlight csharp >}}

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

new string[] { "Date", "InWIPStage", "Shipment", "Payment" },

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

### **DataTableからのインポート**

開発者は、Cells コレクションの **ImportDataTable** メソッドを呼び出すことで、**DataTable** からデータをワークシートにインポートできます。**ImportDataTable** メソッドには多くのオーバーロードされたバージョンがありますが、典型的なオーバーロードは次のパラメーターを取ります：**DataTable**、インポートする内容の **DataTable** オブジェクトを表します

- **フィールド名が表示される**、DataTable の列の名前をワークシートに最初の行としてインポートするかどうかを指定します
- **開始セル**、**DataTable** のコンテンツをインポートする開始セル（たとえば「A1」）の名前を表します

{{< highlight csharp >}}

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

dr[0] = 1;

dr[1] = "Aniseed Syrup";

dr[2] = 15;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Creating another empty row in the DataTable object

dr = dataTable.NewRow();

//Adding data to the row

dr[0] = 2;

dr[1] = "Boston Crab Meat";

dr[2] = 123;

//Adding filled row to the DataTable object

dataTable.Rows.Add(dr);

//Importing the contents of DataTable to the worksheet starting from "A1" cell,

//where true specifies that the column names of the DataTable would be added to

//the worksheet as a header row

worksheet.Cells.ImportDataTable(dataTable, true, "A1");

workbook.Save(MyDir+"Import From Data Table.xls");

{{< /highlight >}}

## **サンプルコードをダウンロード**

- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Import%20to%20Worksheet%20%28Aspose.Cells%29.zip)

## **ドキュメントからのデータのエクスポート**

**Aspose.Cells**は、ユーザーが外部データソースからワークシートにデータをインポートするだけでなく、ワークシートデータを**DataTable**にエクスポートすることも可能です。**DataTable**はADO.NETの一部であり、データを保持するために使用されます。データが**DataTable**に格納されると、ユーザーの要件に応じて任意の方法で使用することができます。

## **Aspose.Cellsを使用した**DataTable**へのデータのエクスポート**

開発者は、CellsクラスのExportDataTableまたはExportDataTableAsStringメソッドを呼び出すことで、ワークシートデータを簡単にDataTableオブジェクトにエクスポートできます。両方のメソッドは、以下で詳しく説明されている異なるシナリオで使用されます。

### **型指定データを含む列**

スプレッドシートはデータを行と列の連続として保存することを知っています。ワークシートの列のすべての値が強く型付けされている場合（つまり、ワークシートの列のすべての値が同じデータ型でなければならない）、Cells クラスの **ExportDataTable** メソッドを呼び出すことでワークシートの内容をエクスポートできます。**ExportDataTable** メソッドは、**DataTable** オブジェクトとしてワークシートのデータをエクスポートするために次のパラメーターを取ります： **行番号**、データのエクスポートを開始する最初のセルの行番号を表します

- **列番号**、データのエクスポートを開始する最初のセルの列番号を表します
- **行数**、エクスポートする行の数を表します
- **列数**、エクスポートする列の数を表します
- **エクスポートする列名**、ワークシートの最初の行のデータを DataTable の列名としてエクスポートするかどうかを表すブール値プロパティ

{{< highlight csharp >}}

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

### **非型指定データを含む列**

ワークシートの列のすべての値が強く型付けされていない場合（つまり、列の値が異なるデータ型を持つ可能性がある場合）は、Cellsクラスの**ExportDataTableAsString**メソッドを呼び出してワークシートのコンテンツをエクスポートすることができます。**ExportDataTableAsString**メソッドは、**ExportDataTable**メソッドと同じパラメータセットを取り、ワークシートデータを**DataTable**オブジェクトとしてエクスポートします。

{{< highlight csharp >}}

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

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
