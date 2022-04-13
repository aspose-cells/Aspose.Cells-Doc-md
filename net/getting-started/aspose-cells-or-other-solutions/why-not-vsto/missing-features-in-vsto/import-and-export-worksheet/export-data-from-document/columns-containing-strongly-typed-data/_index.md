---
title: Columns Containing Strongly Typed Data
type: docs
weight: 20
url: /net/columns-containing-strongly-typed-data/
---

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
