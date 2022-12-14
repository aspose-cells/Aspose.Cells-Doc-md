---
title: 在工作表中添加 Cell 保护
type: docs
weight: 130
url: /zh/net/adding-cell-protection-in-worksheet/
---
{{% alert color="primary" %}} 

GridDesktop 的 Aspose.Cells 允许您保护工作表中的单元格。您首先需要保护您的工作表，然后您可以保护工作表中所需的单元格。为了保护工作表，请设置**工作表.Protected**属性为真，然后使用**工作表.SetProtected()**保护单元格范围的方法。

{{% /alert %}} 
## **使用 Aspose.Cells.GridDesktop 保护 Cell**
以下示例代码保护范围内的所有单元格**A1:B1** GridDesktop 的活动工作表。当您双击此范围内的任何单元格时，您将无法编辑。它将使这些单元格只读。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddCellProtection-1.cs" >}}
