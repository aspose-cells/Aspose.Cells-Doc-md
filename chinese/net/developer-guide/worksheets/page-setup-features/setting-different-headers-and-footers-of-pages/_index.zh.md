---
title: 为不同的页面设置不同的页眉和页脚
type: docs
weight: 35
url: /zh/net/setting-different-headers-and-footers-for-pages-to-Excel/
---
{{% alert color="primary" %}}

MS Excel自Excel 2007起支持对首页、奇数页、偶数页设置不同的页眉页脚。
Aspose.Cells 支持相同的功能。

{{% /alert %}}

## **在 MS Excel 中设置不同的页眉和页脚**

**![设置不同的页眉和页脚](difpage.png)**

1. 点击**页面布局 > 打印标题 > 页眉/页脚**.
1. 查看**不同的奇数页和偶数页**要么**不同的杉木页**.
1. 输入不同的页眉和页脚。

## **使用 Aspose.Cells 设置不同的页眉和页脚**

Aspose.Cells 的行为与 Excel 相同。
1. 设置标志[PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/)和[PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) 
1. 输入不同的页眉和页脚。
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}
