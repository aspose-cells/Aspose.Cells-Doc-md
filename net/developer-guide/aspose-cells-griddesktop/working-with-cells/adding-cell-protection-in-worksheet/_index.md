---
title: Adding Cell Protection in Worksheet
type: docs
weight: 130
url: /net/adding-cell-protection-in-worksheet/
---

{{% alert color="primary" %}} 

Aspose.Cells for GridDesktop allows you to protect your cells in a worksheet. You first need to protect your worksheet, then you can protect your desired cells in a worksheet. In order to protect worksheet, please set **Worksheet.Protected** property to true, then use **Worksheet.SetProtected()** method to protect the range of cells.

{{% /alert %}} 
## **Protect Cell using Aspose.Cells.GridDesktop**
The following sample code protects all the cells in range **A1:B1** of the active worksheet of GridDesktop. When you will double click any cell in this range, you will not able to edit. It will make these cells readonly.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddCellProtection-1.cs" >}}
