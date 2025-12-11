---
title: Exporting Data from Grid
type: docs
weight: 60
url: /net/aspose-cells-griddesktop/export-data-from-grid/
keywords: GridDesktop,export,data,export data
description: This article introduces how to export data in GridDesktop.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

In our previous topic, we talked about importing the contents of a DataTable into Aspose.Cells.GridDesktop control, but we intentionally did not mention that Aspose.Cells.GridDesktop supports the reverse process as well. So, in this topic, we will discuss exporting the data inside Aspose.Cells.GridDesktop control to a DataTable.

{{% /alert %}} 
## **Exporting Grid Contents**
### **Exporting To a Specific DataTable**
To export the Grid contents to a specific DataTable object, please follow the steps below: Add Aspose.Cells.GridDesktop control to your **form**.

- Create a specific DataTable object according to your needs.
- Export the data of a selected **Worksheet** to your specified DataTable object.

In the example given below, we have created a specific DataTable object having four columns. Finally, we exported worksheet data (starting from the first cell, containing 69 rows and 4 columns) to the DataTable object already created by us.

**Example:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToSpecificDataTable.cs" >}}
### **Exporting To a New DataTable**
Sometimes, developers may not be interested in creating their own DataTable object and might have a simple need to just export the worksheet data to a new DataTable object. It would be the quickest way for developers to export the worksheet data.

In the example given below, we have taken a different approach to demonstrate the usage of the `ExportDataTable` method. We obtained a reference to the currently active worksheet and then exported the complete data of that worksheet to a new DataTable object. This DataTable object can be used in any way a developer wishes. For example, a developer may bind this DataTable object to a DataGrid to view the data.

**Example:**

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ExportDataToDataTable-ExportToNewDataTable.cs" >}}

{{% alert color="primary" %}} 

In the above case, we will use an overloaded version of the `ExportDataTable` method that simply returns a new DataTable object containing data exported from the worksheet.

{{% /alert %}}
