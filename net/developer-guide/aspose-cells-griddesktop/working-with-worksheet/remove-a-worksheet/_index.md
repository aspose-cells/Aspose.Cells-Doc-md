---
title: Remove a Worksheet
type: docs
weight: 30
url: /net/remove-a-worksheet/
---

{{% alert color="primary" %}} 

This topic discusses removing worksheets using the Aspose.Cells.GridDesktop control. There are a few simple approaches to accomplish this basic task.

{{% /alert %}} 
## **Removing a Worksheet**
To remove a worksheet using Aspose.Cells.GridDesktop control, please follow the steps below:

1. Add the Aspose.Cells.GridDesktop control to a form.
1. Call the Worksheets collection's Remove method in the GridDesktop control.
### **Using Worksheet Index**
In this approach, simply pass the worksheet index (in the worksheets collection of the grid) of the worksheet to be removed.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingIndex.cs" >}}
### **Using Worksheet Name**
If the name of the worksheet is known, it is possible to remove a specific worksheet by specifying its name.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingName.cs" >}}

{{% alert color="primary" %}} 

Remove is a method. Use it to remove a worksheet using its index (in the worksheets collection) or use RemoveAt method to remove the worksheet using its index/name.

{{% /alert %}}
