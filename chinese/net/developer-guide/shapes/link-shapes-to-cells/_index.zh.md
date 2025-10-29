---
title: 如何将Excel形状链接到工作表单元格
linktitle: 链接Excel形状到单元格
type: docs
description: “如何将Excel形状链接到工作表单元格”
weight: 3300
url: /zh/net/link-shapes-to-cells/
---

{{% alert color="primary" %}}

有时候你需要在形状、文本框或图表元素中显示工作表单元格的内容。有时，当单元格或一系列单元格中的数据被修改时，你需要将单元格内容与形状、文本框或图表元素的内容同步。为此，你可以将形状、文本框或图表元素链接到包含你想显示的数据的单元格。

{{% /alert %}}

## 如何在Ms Excel中将形状链接到单元格

下图显示了如何为形状设置链接单元格。

![todo:image_alt_text](link-shapes-to-cells-1.png)

1. 选择一个形状。公式栏通常为空。

2. 输入形状的公式，例如“=A1”

## 如何在Aspose.Cells中链接形状到单元格

以下代码演示了如何使用Aspose.Cells库为形状或文本框设置链接，以动态显示单元格内容。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "link-shapes-to-cells-1.cs"  >}}

## 高级用法

如果您希望形状的文本由两个或更多单元格组成，或希望根据公式选择所需内容，上述示例代码可能不能满足您的需求。在这种情况下，您需要做一些更高级的操作。您首先需要在单元格中放置产生所需结果的公式，然后将形状链接到包含该公式的单元格。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "link-shapes-to-cells-2.cs"  >}}

{{< app/cells/assistant language="csharp" >}}
