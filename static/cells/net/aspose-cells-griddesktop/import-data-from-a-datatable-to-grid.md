##Importing Data from a DataTable to Grid
This article introduces how to import data in GridDesktop.
Since the release of the .NET Framework, Microsoft has provided an excellent way to store data in offline mode in the form of a DataTable object. Understanding the needs of developers, Aspose.Cells.GridDesktop also supports importing data from a data table. This topic discusses how to do this.
## **Example**
To import the contents of a data table using Aspose.Cells.GridDesktop control:
1. Add Aspose.Cells.GridDesktop control to a form.
1. Create a DataTable object that contains the data to be imported.
1. Get the reference of a desired worksheet.
1. Import the data table contents to the worksheet.
1. Set the column headers of the worksheet according to column names of the data table.
1. Set the width of the columns, if desired/
1. Display the worksheet.
In the example given below, we have created a DataTable object and filled it with some data fetched from a database table named Products. Finally, we have imported data from that DataTable object to a desired worksheet using Aspose.Cells.GridDesktop.
