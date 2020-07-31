---
title : "Implementing GridDesktops Data Binding Feature in Worksheets" 
description : "" 
weight : 20347 
toc : false
type: docs
url: /net/developerguide/technicalarticles/gridcontrols/databinding/implementing+griddesktops+data+binding+feature+in+worksheets/
---

# Aspose.Cells for .NET : Implementing GridDesktops Data Binding Feature in Worksheets


Data Binding is an exciting feature offered by the Microsoft .NET Framework. We know that the DataGrid control offered by Microsoft supports data binding, which means that a DataGrid can be bound to any Data Source (using DataSet, DataTable and DataView objects). This feature has made developers' lives a lot easier. Based on the same concept, Aspose.Cells.GridDesktop also supports data binding, which allows developers to bind worksheets to any data source.This article explores the feature.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Creating a Sample Database](#creating-a-sample-database)
*   2 [Create a Sample Application](#create-a-sample-application)
*   3 [Adding Namespace and Declaring Global Variables](#adding-namespace-and-declaring-global-variables)
*   4 [Filling DataSet with Data from Database](#filling-dataset-with-data-from-database)
*   5 [Binding Worksheet with DataSet](#binding-worksheet-with-dataset)
*   6 [Setting Column Headers of Worksheet](#setting-column-headers-of-worksheet)
*   7 [Customizing the Width and Styles of Columns](#customizing-the-width-and-styles-of-columns)
*   8 [Adding Rows](#adding-rows)
*   9 [Deleting Rows](#deleting-rows)
*   10 [Saving Changes to Database](#saving-changes-to-database)
{{< /panel >}}
 

 

## Creating a Sample Database

1.  Create a sample database to use with the example. We used Microsoft Access to create a sample database with a Products table (schema below).  
    ![](https://docs2.aspose.com/cells/net/attachments/5017592/5113063.png)
2.  Three dummy records are added to the Products table.  
    **Records in Products table**  
    ![](https://docs2.aspose.com/cells/net/attachments/5017592/5113064.png)

## Create a Sample Application

Now create a simple desktop application in Visual Studio and do the following.

1.  Drag the "GridControl" Control from toolbox and drop it on the form.
2.  Drop four buttons from toolbox on the bottom of the form and set their text property as **Bind Woksheet**, **Add Row**, **Delete Row** and **Update to Database** respectively.

## Adding Namespace and Declaring Global Variables

Because this example uses a Microsoft Access database, add the `System.Data.OleDb` namespace at the top of the code.

  
You can now use the classes packaged under this namespace.

1.  Declare global variables.

## Filling DataSet with Data from Database

Now connect to the sample database to fetch and fill data into a `DataSet` object.

1.  Use the `OleDbDataAdapter` object to connect with our sample database and fill a `DataSet` with data fetched from Products table in the database, as shown in the code below.

## Binding Worksheet with DataSet

Bind the worksheet with the Products table of the `DataSet`:

1.  Access a desired worksheet.
2.  Bind the worksheet with the `DataSet`'s Products table.

Add the following code to the **Bind Worksheet** button's click event.

## Setting Column Headers of Worksheet

The bound worksheet now loads data successfully but the column headers are labelled A, B and C by default. It would be better to set the column headers to the column names in the database table.

To set the column headers of worksheet:

1.  Get the captions for each column of the DataTable (Products) in the DataSet.
2.  Assign the captions to the headers of worksheet columns.

Append the code written in the **Bind Worksheet** button's click event with the following code snippet. By doing this the old column headers (A, B and C) will be replaced with ProductID, ProductName and ProductPrice.

## Customizing the Width and Styles of Columns

To improve the look of the worksheet further, it is possible to set the width and styles of columns. For example, sometimes, the column header or the value inside the column consists of long number of characters that don't fit inside the cell. To solve such issues, Aspose.Cells.GridDesktop supports changing the widths of columns.

Append the following code to the **Bind Worksheet** button. The column widths will be customized according to the new settings.

  
Aspose.Cells.GridDesktop also supports applying custom styles to columns. The following code, appended to the **Bind Worksheet** button, customizes the column styles to make them more presentable.

  
Now run the application and click the **Bind Worksheet** Button.

## Adding Rows

To add new rows to a worksheet, use the `Worksheet` class `AddRow` method. This appends an empty row at the bottom and a new `DataRow` is added to the data source (here, a new `DataRow` is added to the DataSet's DataTable). Developers can add as many rows as they want by calling the `AddRow` method again and again. When a row has been added, users can enter values into it.

## Deleting Rows

Aspose.Cells.GridDesktop also supports deleting rows by calling the `Worksheet` class `RemoveRow` method. Removing a row using Aspose.Cells.GridDesktop requires the index of the row to be deleted.

  
Adding the above code to the **Delete Row** button and run the application. A few records are displayed before the row is removed. Selecting a row and clicking the **Delete Row** button removes the selected row.

## Saving Changes to Database

Finally, to save any changes made by users to the worksheet back to the database, use the `OleDbDataAdapter` object's `Update` method. The `Update` method takes the data source (DataSet, DataTable etc.) of the worksheet to update the database.

  
  

1.  Add the above code to the **Update to Database** button.
2.  Run the application.
3.  Perform some operations on the worksheet data, maybe adding new rows and editing or removing existing data.
4.  Then click **Update to Database** to save the changes to the database.
5.  Check the database to see that the table records have been updated accordingly.

