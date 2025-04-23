---
title: 删除工作簿中的未使用样式
type: docs
weight: 340
url: /zh/python-net/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}}

Excel文件中的未使用样式不仅占用空间，还会在转换为PDF、HTML等不同格式时引起性能问题。Aspose.Cells for Python via .NET提供了[**Workbook.remove_unused_styles()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/remove_unused_styles)方法，用于移除工作簿内所有未使用的样式。

{{% /alert %}}

下面的代码解释了[**Workbook.remove_unused_styles()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/remove_unused_styles)的用法。该代码加载了可以从提供的链接下载的[模板Excel文件](5115520.xlsx)。它包含一个名为**AsposeStyle**的未使用样式，此样式和所有其他未使用的样式将在执行代码后被移除。

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-RemoveUnusedStyles-1.py" >}}

