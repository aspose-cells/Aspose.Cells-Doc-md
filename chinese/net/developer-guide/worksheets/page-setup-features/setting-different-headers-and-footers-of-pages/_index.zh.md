---
title: 为不同的页面设置不同的页眉和页脚
type: docs
weight: 35
url: /zh/net/setting-different-headers-and-footers-for-pages-to-Excel/
description: 本文提供的示例代码展示了如何使用 C# 库和 .NET API 以编程方式设置 Excel 工作表页面设置设置的各种页眉和页脚。您可以设置首页、奇数页和偶数页的页眉和页脚。
keywords: set excel header footer first page c#, set excel header footer odd pages c#, set excel header footer even pages c#
---
{{% alert color="primary" %}}

MS Excel自Excel 2007起支持对首页、奇数页、偶数页设置不同的页眉页脚。
Aspose.Cells 支持相同的功能。

{{% /alert %}}

##  **在 MS Excel 中设置不同的页眉和页脚**

**![设置不同的页眉和页脚](difpage.png)**

1. 单击 *页面布局 > 打印标题 > 页眉/页脚**。
1. 查看**不同的奇数页和偶数页**或 *不同的第一页**。
1. 输入不同的页眉和页脚。

##  **使用 Aspose.Cells 设置不同的页眉和页脚**

Aspose.Cells 的行为与 Excel 相同。
1. 设置标志[PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/)和[PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) 
1. 输入不同的页眉和页脚。
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}
