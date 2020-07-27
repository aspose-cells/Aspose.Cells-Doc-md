+++
title = "Exporting Data from Grid" 
description = "" 
weight = 16610 
+++

Aspose.Cells for .NET : Exporting Data from Grid  

# Aspose.Cells for .NET : Exporting Data from Grid


In our previous topic, we have talked about importing the contents of a `DataTable` to `Aspose.Cells.GridDesktop` control but we purposely didn't mention that `Aspose.Cells.GridDesktop` supports the reverse process too. So, in this topic, we will discuss about exporting the data inside `Aspose.Cells.GridDesktop` control to a `DataTable`.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Exporting Grid Contents](#ExportingDatafromGrid-ExportingGridContents)
    *   1.1 [Exporting To a Specific DataTable](#ExportingDatafromGrid-ExportingToaSpecificDataTable)
    *   1.2 [Exporting To a New DataTable](#ExportingDatafromGrid-ExportingToaNewDataTable)
{{< /panel >}}
 

 

## Exporting Grid Contents

### Exporting To a Specific DataTable

To export the Grid contents to a specific `DataTable` object, please follow the steps below:Add `Aspose.Cells.GridDesktop` control to your **Form**.

*   Create a specific `DataTable` object according to your needs.
*   Export the data of a selected **Worksheet** to your specified `DataTable` object.

In the example given below, we have created a specific `DataTable` object having four columns inside. Finally, we exported worksheet data (starting from first cell with 69 rows and 4 columns) to a `DataTable` object already created by us.

**Example:**

### Exporting To a New DataTable

Sometimes, developers may not be interested in creating their own `DataTable` object and might have a simple need to just export the worksheet data to a new `DataTable` object. It would be more quickest way for the developers to just export the worksheet data.

In the example given below, we have tried a different way to explain the usage of `ExportDataTable` method. We have taken the reference of the worksheet that is currently active and then we exported the complete data of that active worksheet to a new `DataTable` object. Now, this `DataTable` object can be used in any way a developer wants. Just for an instance, a developer may bind this `DataTable` object to a `DataGrid` to view the data.

**Example:**

In above case, we will use an overloaded version of `ExportDataTable` method that will simply return a new `DataTable` object containing data exported from worksheet.

