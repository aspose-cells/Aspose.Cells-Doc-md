---
title: 设置不同页的不同页眉和页脚
type: docs
weight: 35
url: /zh/python-net/setting-different-headers-and-footers-for-pages-to-Excel/
description: 本文提供了示例代码，展示了使用Aspose.Cells for Python API以编程方式设置Excel工作表页面设置的各种页眉和页脚。您可以为第一页、奇数页和偶数页设置页眉和页脚。
keywords: Python Excel库，Python设置Excel页眉页脚的第一页，Python设置Excel页眉页脚的奇数页，Python使用Python设置Excel页眉页脚的偶数页。
---

{{% alert color="primary" %}}

自Excel 2007以来，MS Excel支持为第一页、奇数页和偶数页设置不同的页眉和页脚。
Aspose.Cells for Python via .NET支持相同的功能。

{{% /alert %}}

## **如何在MS Excel中设置不同的页眉和页脚**

**![设置不同的页眉和页脚](difpage.png)**

1. 单击**页面布局 > 打印标题 > 页眉/页脚**。
1. 选择**奇偶页不同**或**第一页不同**。
1. 输入不同的页眉和页脚。

## **如何使用Aspose.Cells for Python Excel库设置不同的页眉和页脚**

Aspose.Cells for Python via .NET 表现与 Excel 相同。
1. 设置标志 [PageSetup.is_hf_diff_odd_even](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_odd_even/) 和 [PageSetup.is_hf_diff_first](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_first/) 
1. 输入不同的页眉和页脚。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-DiffHeaderFooter.py" >}}
