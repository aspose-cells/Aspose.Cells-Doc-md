---
title : "Insert or Delete Rows in an Excel Worksheet" 
description : "" 
weight : 20469 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/mngrowscolumnsandcells/insert+or+delete+rows+in+an+excel+worksheet/
---

# Aspose.Cells for .NET : Insert or Delete Rows in an Excel Worksheet


When creating a new worksheet, or working with an existing worksheet, you might need to add extra rows or columns to accommodate data. At other times, you might need to delete rows or columns from specified positions in the worksheet.

Aspose.Cells offers two methods for inserting and deleting rows: [Cells.InsertRows](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/insertrows/index) and [Cells.DeleteRows](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/deleterows/index). These methods are optimized for performance and do the job very quickly.

To insert or remove a number of rows, we recommend that you always use the [Cells.InsertRows](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/insertrows/index) and [Cells.DeleteRows](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/deleterows/index) methods instead of using the [Cells.InsertRow](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/insertrow) or [DeleteRow](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/deleterow) methods in a loop.

Aspose.Cells works in the same way as Microsoft Excel does. When rows or columns are added, the worksheet content is shifted down and to the right. When rows or columns are removed, the worksheet content is shifted up or to the left. Any references in other worksheets and cells are updated when rows are added or removed.

