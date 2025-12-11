---  
title: Importing from DataTable  
type: docs  
weight: 40  
url: /net/importing-from-datatable/  
ai_search_scope: cells_net  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

Developers can import data from a **DataTable** to their worksheets by calling the **ImportDataTable** method of the Cells collection. There are many overloaded versions of the **ImportDataTable** method, but a typical overload takes the following parameters: **DataTable**, which represents the **DataTable** object whose contents need to be imported  

- **Is Field Name Shown**, specifies whether the names of the columns of the DataTable should be imported to the worksheet as a first row or not  
- **Start Cell**, represents the name of the start cell (i.e., "A1") from where to import the contents of the DataTable  

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

//Adding the filled row to the DataTable object

dataTable.Rows.Add(dr);

//Creating another empty row in the DataTable object

dr = dataTable.NewRow();

//Adding data to the row

dr[0] = 2;

dr[1] = "Boston Crab Meat";

dr[2] = 123;

//Adding the filled row to the DataTable object

dataTable.Rows.Add(dr);

//Importing the contents of the DataTable to the worksheet starting from the "A1" cell,
//where true specifies that the column names of the DataTable would be added to
//the worksheet as a header row

worksheet.Cells.ImportDataTable(dataTable, true, "A1");

workbook.Save("Import From Data Table.xls");

{{< /highlight >}}  
## **Download Sample Code**  
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Import.to.Worksheet.Aspose.Cells.zip)  
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Import%20to%20Worksheet%20%28Aspose.Cells%29.zip)  
{{< app/cells/assistant language="csharp" >}}
