---
title: 设置不同页的不同页眉和页脚
type: docs
weight: 35
url: /zh/net/setting-different-headers-and-footers-for-pages-to-Excel/
description: 本文提供了一个示例代码，展示了如何使用C#库和.NET API以编程方式设置Excel工作表页面设置的各种页眉和页脚。您可以为第一页、奇数页和偶数页设置页眉和页脚。
keywords: 设置Excel页眉页脚第一页c#，设置Excel页眉页脚奇数页c#，设置Excel页眉页脚偶数页c#
---

{{% alert color="primary" %}}

自Excel 2007以来，MS Excel支持为第一页、奇数页和偶数页设置不同的页眉和页脚。
Aspose.Cells支持相同的功能。

{{% /alert %}}

## **在MS Excel中设置不同的页眉和页脚**

**![设置不同的页眉和页脚](difpage.png)**

1. 单击**页面布局 > 打印标题 > 页眉/页脚**。
1. 选择**奇偶页不同**或**第一页不同**。
1. 输入不同的页眉和页脚。

## **使用Aspose.Cells设置不同的页眉和页脚**

Aspose.Cells与Excel的行为相同。
1. 设置标识[PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/)和[PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) 
1. 输入不同的页眉和页脚。
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}
{{< app/cells/assistant language="csharp" >}}
