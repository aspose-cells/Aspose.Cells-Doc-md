---
title : "Remove a Worksheet" 
description : "" 
weight : 16607 
toc : false
type: docs
url: /net/developerguide/griddesktop/worksheet/remove+a+worksheet/
---

# Aspose.Cells for .NET : Remove a Worksheet


This topic discusses removing worksheets using the Aspose.Cells.GridDesktop control. There are a few simple approaches to accomplish this basic task.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Removing a Worksheet](#removing-a-worksheet)
    *   1.1 [Using Worksheet Index](#using-worksheet-index)
    *   1.2 [Using Worksheet Name](#using-worksheet-name)
{{< /panel >}}
 

 

## Removing a Worksheet

To remove a worksheet using Aspose.Cells.GridDesktop control, please follow the steps below:

1.  Add the Aspose.Cells.GridDesktop control to a form.
2.  Call the `Worksheets` collection's `Remove` method in the GridDesktop control.

### Using Worksheet Index

In this approach, simply pass the worksheet index (in the worksheets collection of the grid) of the worksheet to be removed.

### Using Worksheet Name

If the name of the worksheet is known, it is possible to remove a specific worksheet by specifying its name.

`Remove` is a method. Use it to remove a worksheet using its index (in the worksheets collection) or use `RemoveAt` method to remove the worksheet using its index/name.

