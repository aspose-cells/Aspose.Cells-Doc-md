---
title: Creating Hierarchical View Sheet
type: docs
weight: 30
url: /net/aspose-cells-gridweb/create-hierarchical-view-sheet/
keywords: GridWeb,hierarchical
description: This article introduce how to create hierarchical view in GridWeb.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Data binding is a powerful and user-friendly GridWeb feature. Data stored in database tables is fetched to a DataSet and filled with data 

representing the data tables. Using the data binding feature, you can create a hierarchical view (a master-child view) of interlinked data and 

display it in the control to make it more elegant. 

This topic discusses creating a hierarchical view sheet. Some of the rows in the sheet have child views. When a user clicks the row's **Expand**

button {{< emoticons/cross >}}, the child view table of that row is expanded down. This feature is very helpful for building a hierarchical view report. 

**A table with a hierarchical view** 

![todo:image_alt_text](creating-hierarchical-view-sheet_1.png)

{{% /alert %}} 
## **Create Relations for DataTables**
For example, you use ADO.Net API and extract data from the database tables. To create hierarchical view sheet, you must design a DataSet

object based on some tables and create a relationship between them first. Use the VS.NET's **DataSet Designer** to create the relationship. In 

this example, there are three DataTables: Customers, Orders, Order Details. The sheet shows all the customer information by default. When 

the user expands a customer, the grid shows all the orders that customer has placed. When the user expands an order, the grid shows the details 

of that order. The data is hierarchical: order details are listed under orders, and orders are listed under customers.

For this to work, the following to relationships must be established between the data tables:

1. Create a foreign key on DataTable Orders, the key field is CustomerID 

![todo:image_alt_text](creating-hierarchical-view-sheet_2.png)




1. Create a foreign key on DataTable Order Details, the key field is OrderID. 

![todo:image_alt_text](creating-hierarchical-view-sheet_3.png)



The DataSet Designer now looks like this: 

![todo:image_alt_text](creating-hierarchical-view-sheet_4.png)
### **Bind Worksheet**
Now use the **Worksheets Designer** to set the DataSource and DataMember for the worksheet, and configure the data field binding columns. 

The control automatically adds a + icon for each row that corresponds to a record whose binding object (generally a DataRowView object) has 

child views. When the + icon is clicked, the record expands to show the child view. The example below uses the **Worksheets Designer** to bind the 

worksheet to the root parent DataTable Customers. 

![todo:image_alt_text](creating-hierarchical-view-sheet_5.png)
### **Customize the Child Tables Bind Columns**
The control provides an event named GridWeb.BindingChildView which developers use to customize the child tables' bind columns. This example 

needs to display the order details' **UnitPrice** field in a currency format. Add an event handler to change the bind column's number format. 

**C#**

{{< highlight csharp >}}

 // Handles the BindingChildView event to set the UnitPrice column.

private void GridWeb1_BindingChildView(Aspose.Cells.GridWeb.GridWeb childGrid, Aspose.Cells.GridWeb.Data.WebWorksheet childSheet)

{

    DataView view = (DataView)childSheet.DataSource;

    if (view.Table.TableName == "Order Details")

    {

        childSheet.BindColumns["UnitPrice"].NumberType = NumberType.Currency3;

    }

}



{{< /highlight >}}

**VB.NET**

{{< highlight csharp >}}

 'Handles the BindingChildView event to set the UnitPrice column.

Private Sub GridWeb1_BindingChildView(ByVal childGrid As Aspose.Cells.GridWeb.GridWeb, ByVal childSheet As 

Aspose.Cells.GridWeb.Data.WebWorksheet) Handles GridWeb1.BindingChildView

    Dim view As DataView = CType(childSheet.DataSource, DataView)

    If view.Table.TableName = "Order Details" Then

        childSheet.BindColumns("UnitPrice").NumberType = NumberType.Currency3

    End If

End Sub



{{< /highlight >}}
### **Load Data from Database and Binding**
As described in [Binding Worksheet to a DataSet using GridWeb's Worksheets Designer](/cells/net/binding-worksheet-to-a-dataset-using-gridwebs-worksheets-designer/),
you need to add code to the Page_Load block to load data to the DataSet from a database, and bind the DataSet to the sheet in the 

next step. 

The Asppose.Grid.Web.Data.WebWorksheet Class has some useful properties.

- For example, the property EnableCreateBindColumnHeader is used to create the headings of the bound column within the sheet, or the column

headers displays the bound column names. It takes the values **true** or **false**. 

- The properties BindStartRow and BindStartColumn specify the position in the sheet of GridWeb control the source should be bound to.
- The property EnableExpandChildView is used to disable the expanded child view for the worksheet. By default it is set to true.

The class has some useful methods too. 

- The DataBind() method binds a sheet with the source.
- The CreateNewBindRow() adds a new row and binds it to the data source.
- The DeleteBindRow() deletes a bound row.
- The SetRowExpand() method sets the expanded row and shows the child view content in the data binding mode.
- The GetRowExpand() method gets a Boolean value that indicates whether the row is expanded or not.

In code below, the DataSet object "dataSet21" is filled with data based on three tables. The Customers table is filtered to make it the 

first table in the hierarchical display. A WebWorksheet object named "sheet" is created, which clears the sheet first and then sets it 

linked to the data source. 

**C#**

{{< highlight csharp >}}

 private void Page_Load(object sender, System.EventArgs e)

{

    // Put user code to initialize the page here

    if (!IsPostBack)

    {

        BindWithoutInSheetHeaders();

    }

}

private void BindWithoutInSheetHeaders()

{

    DemoDatabase2 db = new DemoDatabase2();

    string path = MapPath(".");

    path = path.Substring(0, path.LastIndexOf("\\"));

    path = path.Substring(0, path.LastIndexOf("\\"));

    db.oleDbConnection1.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + path + "\\Database\\Northwind.mdb";

    try

    {

        // Connects to database and fetches data.

        // Customers Table.

        db.oleDbDataAdapter1.Fill(dataSet21);

        // Orders Table.

        db.oleDbDataAdapter2.Fill(dataSet21);

        // OrderDetailTable.

        db.oleDbDataAdapter3.Fill(dataSet21);

        // Filter data

        dataSet21.Customers.DefaultView.RowFilter = "CustomerID<'BSAAA'";

        WebWorksheet sheet = GridWeb1.WorkSheets[0];

        // Clears the sheet.

        sheet.Cells.Clear();

        // Disables creating in-sheet headers.

        sheet.EnableCreateBindColumnHeader = false;

        // Data cells begin from row 0.

        sheet.BindStartRow = 0;

        // Bind the sheet to the dataset.

        sheet.DataBind();

    }

    finally

    {

        db.oleDbConnection1.Close();

    }

}



{{< /highlight >}}

**VB.NET**

{{< highlight csharp >}}

 Private Sub Page_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load

    'Put user code to initialize the page here

    If Not IsPostBack Then

        BindWithoutInSheetHeaders()

    End If

End Sub

Private Sub BindWithoutInSheetHeaders()

    Dim db As DemoDatabase2 = New DemoDatabase2()

    Dim path As String = MapPath(".")

    path = path.Substring(0, path.LastIndexOf("\"))

    path = path.Substring(0, path.LastIndexOf("\"))

    db.OleDbConnection1.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + path + "\Database\Northwind.mdb"

    Try

        ' Connects to database and fetches data.

        ' Customers Table.

        db.OleDbDataAdapter1.Fill(DataSet21)

        ' Orders Table.

        db.OleDbDataAdapter2.Fill(DataSet21)

        ' OrderDetailTable.

        db.OleDbDataAdapter3.Fill(DataSet21)

        ' Filter data

        DataSet21.Customers.DefaultView.RowFilter = "CustomerID<'BSAAA'"

        Dim sheet As WebWorksheet = GridWeb1.WorkSheets(0)

        ' Clears the sheet.

        sheet.Cells.Clear()

        ' Disables creating in-sheet headers.

        sheet.EnableCreateBindColumnHeader = False

        ' Data cells begin from row 0.

        sheet.BindStartRow = 0

        ' Bind the sheet to the dataset.

        sheet.DataBind()

    Finally

        db.OleDbConnection1.Close()

    End Try

End Sub



{{< /highlight >}}
