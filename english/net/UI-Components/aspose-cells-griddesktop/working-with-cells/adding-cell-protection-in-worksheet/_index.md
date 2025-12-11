---
title: Add Protection in Worksheet
type: docs
weight: 130
url: /net/aspose-cells-griddesktop/adding-cell-protection-in-worksheet/
keywords: GridDesktop,protect
description: This article introduces how to protect cells in the Worksheet in GridDesktop.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Aspose.Cells for GridDesktop allows you to protect cells in a worksheet. First you need to protect your worksheet, then you can protect your desired cells in the worksheet. In order to protect the worksheet, please set **Worksheet.Protected** property to true, then use **Worksheet.SetProtected()** method to protect the range of cells.

{{% /alert %}} 
## **Protect Cells using Aspose.Cells.GridDesktop**
The following sample code protects all the cells in range **A1:B1** of the active worksheet of GridDesktop. When you double‑click any cell in this range, you will not be able to edit it. It will make these cells read‑only.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddCellProtection-1.cs" >}}
