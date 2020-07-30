---
title : "Copy a Worksheet" 
description : "" 
weight : 16687 
toc : false
type: docs
url: /net/developerguide/gridweb/workingwithgridwebworksheets/copy+a+worksheet/
---

# Aspose.Cells for .NET : Copy a Worksheet


[Add Worksheets](https://docs2.aspose.com/cells/net/developerguide/gridweb/workingwithgridwebworksheets/add+worksheets) describes how to add new worksheets to Aspose.Cells.GridWeb. It's also possible to add a copy (or replica) of another worksheet to the Aspose.Cells.GridWeb control. This feature can be useful when identical or similar data in one worksheet is also required in another worksheet. When that's the case, it's easier to copy an existing worksheet and add it to Aspose.Cells.GridWeb as a new worksheet instead of creating it from scratch.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Copying a Worksheet](#copying-a-worksheet)
    *   1.1 [Using Sheet index](#using-sheet-index)
    *   1.2 [Using Sheet Name](#using-sheet-name)
{{< /panel >}}
 

## Copying a Worksheet

### Using Sheet index

The example code below shows how to add a copy of a worksheet to the GridWeb control by specifying the worksheet's index in the `GridWorksheetCollection`'s `AddCopy` method.

### Using Sheet Name

The example code below shows how to add a copy of a worksheet to the GridWeb control by specifying the worksheet's name in the `GridWorksheetCollection`'s `AddCopy` method.

The `AddCopy` method returns the newly added worksheet's index which can be used to access the worksheet instance. For more details on how to access worksheets, read [Access Worksheets](https://docs2.aspose.com/cells/net/developerguide/gridweb/workingwithgridwebworksheets/access+worksheets).

