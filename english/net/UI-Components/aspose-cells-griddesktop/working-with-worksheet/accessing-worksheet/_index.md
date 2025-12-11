---
title: Accessing Worksheet
type: docs
weight: 10
url: /net/aspose-cells-griddesktop/access-worksheet/
keywords: GridDesktop,worksheet
description: This article introduces how to work with worksheet in GridDesktop.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

A worksheet is an integral part of an Excel file. In fact, an Excel file is composed of one or more worksheets. Each worksheet can be composed of up to 65,536 rows and 256 columns only. It is the worksheet that holds data in an Excel file.

Aspose.Cells.GridDesktop can create and manipulate existing and new Excel files, so there is, of course, a way to access worksheets using Aspose.Cells.GridDesktop. This topic discusses how.

{{% /alert %}} 
## **Using Worksheet Index**
Developers can access an instance of any Worksheet by using the worksheet index of any desired worksheet as shown below in the example. This approach is good for iterating through a number of worksheets in an Excel file.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithIndex.cs" >}}
## **Using Worksheet Name**
If the name of the worksheet is known, it is possible to access a worksheet using its name as shown below.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithName.cs" >}}
## **Accessing an Active Worksheet**
It is possible that an Excel file will have more than one worksheet. The one that a user is working on is called the active worksheet. It is possible to access the active sheet.

To access an active worksheet, Aspose.Cells.GridDesktop offers two approaches:
### **Using the ActiveSheetIndex Property**
One way to access an active worksheet using Aspose.Cells.GridDesktop control is to use the GridDesktop control's ActiveSheetIndex property. Using this property, it is possible to get the index of the active worksheet in the Aspose.Cells.GridDesktop control. Then that index can be used to access the worksheet in a traditional manner as shown below.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithActiveWorksheet.cs" >}}
### **Using the GetActiveWorksheet Method**
The other approach is to call the GridDesktop control's GetActiveWorksheet method. This method provides a reference to the worksheet that is currently active in Aspose.Cells.GridDesktop control as shown below.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithGetActiveWorksheet.cs" >}}
