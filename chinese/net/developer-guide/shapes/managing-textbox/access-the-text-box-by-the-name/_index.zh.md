---
title: 按名称访问文本框
type: docs
weight: 230
url: /zh/net/access-the-text-box-by-the-name/
---

## 按名称访问文本框

以前，文本框是通过[**Worksheet.TextBoxes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/textboxes)集合中的索引访问的，但现在您也可以通过名称从该集合中访问文本框。如果您已经知道其名称，这是一种方便快捷的访问文本框的方式。

以下示例代码首先创建了一个文本框并分配了一些文本和名称。然后在接下来的行中，我们通过其名称访问相同的文本框并打印其文本。

### 通过名称访问文本框的C#代码

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AccessTextBoxName-AccessTextBoxName.cs" >}}

### 样本代码生成的控制台输出

这是上面示例代码的控制台输出。

{{< highlight java >}}

This is MyTextBox

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
