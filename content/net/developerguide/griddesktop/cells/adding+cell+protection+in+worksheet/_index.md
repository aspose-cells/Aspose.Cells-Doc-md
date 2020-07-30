---
title : "Adding Cell Protection in Worksheet" 
description : "" 
weight : 16649 
toc : false
type: docs
url: /net/developerguide/griddesktop/cells/adding+cell+protection+in+worksheet/
---

# Aspose.Cells for .NET : Adding Cell Protection in Worksheet


Aspose.Cells for GridDesktop allows you to protect your cells in a worksheet. You first need to protect your worksheet, then you can protect your desired cells in a worksheet. In order to protect worksheet, please set **Worksheet.Protected** property to true, then use **Worksheet.SetProtected()** method to protect the range of cells.

## Protect Cell using `Aspose.Cells.GridDesktop`

The following sample code protects all the cells in range **A1:B1** of the active worksheet of GridDesktop. When you will double click any cell in this range, you will not able to edit. It will make these cells readonly.

