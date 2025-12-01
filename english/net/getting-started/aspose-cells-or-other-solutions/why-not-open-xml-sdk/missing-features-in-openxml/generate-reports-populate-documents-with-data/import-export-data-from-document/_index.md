---
title: Import Export data from document
type: docs
weight: 10
url: /net/import-export-data-from-document/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Import data from document**

Data is the collection of raw facts and we create spreadsheet documents or reports to present these raw facts in a more meaningful manner. Normally, we add data to spreadsheets by ourselves but sometimes, we need to reuse existing data resources and here comes the need to import data to spreadsheets from different data sources. In this topic, we will discuss some techniques to import data to worksheets from different data sources.

## **Importing Data Using Aspose.Cells**

When you use **Aspose.Cells** to open an Excel file, all data in the file is automatically imported but Aspose.Cells also supports to import data from different data sources. A few of these data sources are listed below:

- **Array**
- **ArrayList**
- **DataTable**
- **DataColumn**
- **DataView**
- **DataGrid**
- **DataReader**
- **GridView**

Aspose.Cells provides a class, **Workbook** that represents an Excel file. Workbook class contains a Worksheets collection that allows to access each worksheet in the Excel file. A worksheet is represented by the Worksheet class. Worksheet class provides a Cells collection.

Cells collection provides very useful methods to import data from different data sources.

### **Importing from Array**

Developers can import data from an array to their worksheets by calling the **ImportArray** method of the Cells collection. There are many overloaded versions of the ImportArray method but a typical overload takes the following parameters:

- Array, represents the array object whose contents need to import
- Row Number, represents the row number of the first cell where the data will be imported
- Column Number, represents the column number of the first cell where the data will be imported
- Is Vertical, a boolean value that specifies to import data vertically or horizontally

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

### **Importing from ArrayList**

Developers can import data from an ArrayList to their worksheets by calling the **ImportArrayList** method of the Cells collection. ImportArray method takes the following parameters: **ArrayList** , represents the ArrayList object whose contents need to import

- Row Number , represents the row number of the first cell where the data will be imported
- Column Number , represents the column number of the first cell where the data will be imported
- Is Vertical , a boolean value that specifies to import data vertically or horizontally

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

### **Importing from Custom Objects**

Developers can import data from collection of objects to a worksheet using **ImportCustomObjects**. You can provide a list of columns/properties to the method to display your desired list of objects.

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

### **Importing from DataTable**

Developers can import data from a **DataTable** to their worksheets by calling the **ImportDataTable** method of the Cells collection. There are many overloaded versions of the **ImportDataTable** method but a typical overload takes the following parameters:**DataTable** , represents the **DataTable** object whose contents need to import

- **Is Field Name Shown**, specifies that whether the names of the columns of DataTable should be imported to worksheet as a first row or not
- **Start Cell** , represents the name of the start cell (i.e. "A1") from where to import the contents of the DataTable

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

## **Download Sample Code**

- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Import%20to%20Worksheet%20%28Aspose.Cells%29.zip)

## **Export data from document**

Aspose.Cells not only facilitates its users to import data to worksheets from external data sources but also allow them to export their worksheet data to a **DataTable**. As we know that **DataTable** is the part of ADO.NET and is used to hold data. Once the data is stored in a **DataTable**, it can be used in any way according to the requirements of users.

## **Exporting Data to DataTable (.NET) Using Aspose.Cells**

Developers can easily export their worksheet data to a DataTable object by calling either ExportDataTable or ExportDataTableAsString method of the Cells class. Both methods are used in different scenarios, which are discussed below in more detail.

### **Columns Containing Strongly Typed Data**

We know that a spreadsheet stores data as a sequence of rows and columns. If all values in the columns of a worksheet are strongly typed (that means all values in a column must have the same data type) then we can export the worksheet content by calling the **ExportDataTable** method of the Cells class. **ExportDataTable** method takes the following parameters to export worksheet data as **DataTable** object: **Row Number** , represents the row number of the first cell from where the data will be exported

- **Column Number** , represents the column number of the first cell from where the data will be exported
- **Number of Rows** , represents the number of rows to export
- **Number of Columns** , represents the number of columns to export
- **Export Column Names** , a boolean proeprty that indicates whether the data in the first row of the worksheet should be exported as column names of the DataTable or not

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

### **Columns Containing Non-Strongly Typed Data**

If all values in the columns of a worksheet are not strongly typed (that means the values in a column may have the different data types) then we can export the worksheet content by calling the **ExportDataTableAsString** method of the Cells class. **ExportDataTableAsString** method takes the same set of parameters as that of **ExportDataTable** method to export worksheet data as **DataTable** object.

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

## **Download Sample Code**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Export%20from%20Worksheet%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
