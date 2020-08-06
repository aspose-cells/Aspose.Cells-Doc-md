---
title: Exporting Data from Grid
type: docs
weight: 60
url: /net/exporting-data-from-grid/
---

{{% alert color="primary" %}} 

In our previous topic, we have talked about importing the contents of a DataTable to Aspose.Cells.GridDesktop control but we purposely didn't mention that Aspose.Cells.GridDesktop supports the reverse process too. So, in this topic, we will discuss about exporting the data inside Aspose.Cells.GridDesktop control to a DataTable.

{{% /alert %}} 
## **Exporting Grid Contents**
### **Exporting To a Specific DataTable**
To export the Grid contents to a specific DataTable object, please follow the steps below:Add Aspose.Cells.GridDesktop control to your **Form**.

- Create a specific DataTable object according to your needs.
- Export the data of a selected **Worksheet** to your specified DataTable object.

In the example given below, we have created a specific DataTable object having four columns inside. Finally, we exported worksheet data (starting from first cell with 69 rows and 4 columns) to a DataTable object already created by us.

**Example:**

{{< gist "aspose-cells" "12f660d9525e46ef9ab404004d07c3e8" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToSpecificDataTable.cs" >}}
### **Exporting To a New DataTable**
Sometimes, developers may not be interested in creating their own DataTable object and might have a simple need to just export the worksheet data to a new DataTable object. It would be more quickest way for the developers to just export the worksheet data.

In the example given below, we have tried a different way to explain the usage of ExportDataTable method. We have taken the reference of the worksheet that is currently active and then we exported the complete data of that active worksheet to a new DataTable object. Now, this DataTable object can be used in any way a developer wants. Just for an instance, a developer may bind this DataTable object to a DataGrid to view the data.

**Example:**

{{< gist "aspose-cells" "12f660d9525e46ef9ab404004d07c3e8" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToNewDataTable.cs" >}}

{{% alert color="primary" %}} 

In above case, we will use an overloaded version of ExportDataTable method that will simply return a new DataTable object containing data exported from worksheet.

{{% /alert %}}
