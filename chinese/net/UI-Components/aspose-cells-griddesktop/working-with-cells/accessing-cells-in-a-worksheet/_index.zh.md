---
title: 在工作表中访问 Cells
type: docs
weight: 10
url: /zh/net/accessing-cells-in-a-worksheet/
---
{{% alert color="primary" %}} 

到目前为止，我们已经讨论了如何使用工作表、行和列，但现在是时候更深入地讨论单元格了。因此，在本主题中，我们将开始讨论具有访问单元格的基本功能的单元格。

{{% /alert %}} 
## **在工作表中访问 Cells**
我们可以使用 Aspose.Cells.GridDesktop 的 API 访问工作表的任何单元格。访问单元格可能有以下三种可能的方法：

- **使用 Cell 名称**
- **使用 Cell 的行和列索引**
- **集中注意力 Cell**

让我们一一讨论以上三种方法。
### **使用 Cell 名称**
工作表中的所有单元格都有唯一的名称。例如，A1、A2、B1、B2 等。 Aspose.Cells.GridDesktop 允许开发人员使用其单元格名称访问任何所需的单元格。我们所要做的就是将单元格名称（作为索引）传递给**Cells**的集合**工作表**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByName.cs" >}}
### **使用 Cell 的行和列索引**
工作表中的单元格也可以根据其行索引和列索引使用其位置来识别。我们所要做的就是将单元格的行和列索引传递给**Cells**的集合**工作表**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByIndices.cs" >}}
### **集中注意力 Cell**
如果您不准确地知道要访问哪个单元格。然后 Aspose.Cells.GridDesktop 还允许您访问当前处于用户焦点的单元格。使用此功能，您可以允许用户选择任何单元格，然后您可以在后端访问该单元格。它可以简单地通过使用来实现**获取焦点单元格**的方法**工作表**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessFocusedCell.cs" >}}
