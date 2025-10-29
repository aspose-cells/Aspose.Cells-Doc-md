---
title: 设置不同页的不同页眉和页脚
type: docs
weight: 35
url: /zh/python-net/setting-different-headers-and-footers-for-pages-to-Excel/
description: 本文提供示例代码，演示如何使用Aspose.Cells for Python API以编程方式设置Excel工作表页面设置中的各种页眉和页脚。你可以为首页、奇数页和偶数页设置页眉和页脚。
keywords: Python Excel库，Python设置Excel首页页眉页脚，设置Excel奇数页页眉页脚，使用Python设置Excel偶数页页眉页脚。
---

{{% alert color="primary" %}}

自Excel 2007以来，MS Excel支持为第一页、奇数页和偶数页设置不同的页眉和页脚。
Aspose.Cells for Python via .NET 支持相同的功能。

{{% /alert %}}

## **如何在MS Excel中设置不同的页眉和页脚**

**![设置不同的页眉和页脚](difpage.png)**

1. 单击**页面布局 > 打印标题 > 页眉/页脚**。
1. 选择**奇偶页不同**或**第一页不同**。
1. 输入不同的页眉和页脚。

## **如何使用Aspose.Cells for Python Excel库设置不同的页眉和页脚**

Aspose.Cells for Python via .NET 的行为与Excel相同。
1. 设置flags [PageSetup.is_hf_diff_odd_even](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_odd_even/) 和 [PageSetup.is_hf_diff_first](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_first/) 
1. 输入不同的页眉和页脚。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-DiffHeaderFooter.py" >}}
{{< app/cells/assistant language="python-net" >}}
