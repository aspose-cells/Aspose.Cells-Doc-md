---
title: Grouping Data in Aspose.Cells
type: docs
weight: 10
url: /net/grouping-data-in-aspose-cells/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

In some Excel reports you might need to break the data into groups to make it easier to read and analyze. One of the primary purposes for breaking data into groups is to run calculations (perform summary operations) on each group of records.

Aspose.Cells smart markers allow you to group your data by field(s) and place summary rows between data sets or data groups. For example, if grouping data by Customers.CustomerID, you can add a summary record every time the group changes.

The example code snippets that follow show how to group data in an Excel report using smart markers.

## **Parameters**
Following are some of the smart marker parameters used for grouping data.  
**group:normal/merge/repeat**

We support three types of groups that you can choose from.

- normal – The group‑by field(s) value is not repeated for the corresponding records in the column; instead, it is printed once per data group.  
- merge – The same behavior as for the normal parameter, except that it merges the cells in the group‑by field(s) for each group set.  
- repeat – The group‑by field(s) value is repeated for the corresponding records.

If you have multiple parameters, separate them with a comma, but no space: `parameterA,parameterB,parameterC`

### **Example**
This example shows some of the grouping parameters in action. It uses the Northwind.mdb Microsoft Access database and extracts data from the table named **"Order Details"**. We create a designer file called **SmartMarker_Designer.xls** in Microsoft Excel and put smart markers into various cells in worksheets. The markers are processed to fill the worksheets. The data is placed and organized by a group field.

The designer file has two worksheets. In the first we put smart markers with grouping parameters as shown in the screenshot below. Three smart markers (with grouping parameters) are placed:

&=Order Details.OrderID(group:merge,skip:1),  
&=Order Details.Quantity(subtotal9:Order Details.OrderID), and  
&=Order Details.UnitPrice(subtotal9:Order Details.OrderID) are placed in A5, B5 and C5 respectively.

{{< highlight csharp >}}
 // Create a connection object, specify the provider info and set the data source.
 OleDbConnection con = new OleDbConnection("provider=microsoft.jet.oledb.4.0;data source=Northwind.mdb");

 // Open the connection object.
 con.Open();

 // Create a command object and specify the SQL query.
 OleDbCommand cmd = new OleDbCommand("Select * from [Order Details]", con);

 // Create a data adapter object.
 OleDbDataAdapter da = new OleDbDataAdapter();

 // Specify the command.
 da.SelectCommand = cmd;

 // Create a DataSet object.
 DataSet ds = new DataSet();

 // Fill the DataSet with the table records.
 da.Fill(ds, "Order Details");

 // Create a DataTable from the DataSet table.
 DataTable dt = ds.Tables["Order Details"];

 // Create a WorkbookDesigner object.
 WorkbookDesigner wd = new WorkbookDesigner();

 // Open the template file (which contains smart markers).
 wd.Workbook = new Workbook("SmartMarkerDesigner.xls");

 // Set the DataTable as the data source.
 wd.SetDataSource(dt);

 // Process the smart markers to fill the data into the worksheets.
 wd.Process(true);

 // Save the Excel file.
 wd.Workbook.Save("outSmartMarker_Designer.xls");
{{< /highlight >}}

## **Download Sample Code**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Grouping%20Data%20OLE%20DB%20%28Aspose.Cells%29.zip)
