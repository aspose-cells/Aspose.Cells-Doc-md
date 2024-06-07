---
title: 为不同页面设置不同的页眉和页脚
type: docs
weight: 35
url: /zh/net/setting-different-headers-and-footers-for-pages-to-Excel/
description: 本文提供了展示如何使用C#库和.NET API以编程方式设置Excel工作表Page Setup设置的各种页眉和页脚的示例代码。您可以为第一页、奇数页和偶数页设置页眉和页脚。
keywords: 为Excel设置第一页页眉页脚C#，为Excel设置奇数页页眉页脚C#，为Excel设置偶数页页眉页脚C#
---

{{% alert color="primary" %}}

自Excel 2007以来，MS Excel支持为第一页、奇数页和偶数页设置不同的页眉和页脚。
Aspose.Cells支持相同的功能。

{{% /alert %}}

## **在MS Excel中设置不同的页眉和页脚**

**![设置不同页眉和页脚](difpage.png)**

1. 单击**页面布局 > 打印标题 > 页眉/页脚**。
1. 选中**不同的奇偶页**或**不同的第一页**。
1. 输入不同的页眉和页脚。

## **使用Aspose.Cells设置不同的页眉和页脚**

Aspose.Cells的行为与Excel相同。
1. 设置标志[PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/)和[PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) 
1. 输入不同的页眉和页脚。
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}
