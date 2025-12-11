---
title: Importing Data from a DataTable to Grid
type: docs
weight: 50
url: /net/aspose-cells-griddesktop/import-data-from-a-datatable-to-grid/
keywords: GridDesktop,import,data,datatable
description: This article introduces how to import data in GridDesktop.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Since the release of the .NET Framework, Microsoft has provided an excellent way to store data offline in the form of a DataTable object. Understanding developers' needs, Aspose.Cells.GridDesktop also supports importing data from a DataTable. This topic discusses how to do this.

{{% /alert %}} 
## **Example**
To import the contents of a data table using Aspose.Cells.GridDesktop control:

1. Add Aspose.Cells.GridDesktop control to a form.  
2. Create a DataTable object that contains the data to be imported.  
3. Get the reference of a desired worksheet.  
4. Import the DataTable contents to the worksheet.  
5. Set the column headers of the worksheet according to column names of the DataTable.  
6. Set the width of the columns, if desired.  
7. Display the worksheet.

In the example given below, we have created a DataTable object and filled it with some data fetched from a database table named Products. Finally, we have imported data from that DataTable object to a desired worksheet using Aspose.Cells.GridDesktop.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ImportDataFromDataTable-1.cs" >}}
