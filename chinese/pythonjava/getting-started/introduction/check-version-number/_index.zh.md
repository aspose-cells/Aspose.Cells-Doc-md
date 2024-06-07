---
title: 检查版本号
type: docs
weight: 80
url: /zh/python-java/check-version-number/
---

{{% alert color="primary" %}}

想知道你正在使用哪个版本的 Aspose.Cells 吗？我们定期发布 Aspose.Cells 的新版本，旨在引入新功能和修复问题。版本号由主版本号、次版本号和热修复版本号组成。每个数字必须是从 0 开始的整数。格式如下：

主版本号.次版本号.热修复版本号

当我们发布 Aspose.Cells 的新版本时，我们会更新版本号。

本文介绍如何手动检查系统上安装的 Aspose.Cells 版本以及使用 Aspose.Cells API。

{{% /alert %}}

## **手动检查版本号**

要手动查找正在使用的 Aspose.Cells 版本：

1. 右键单击 Aspose.Cells.dll 文件，然后选择**属性**。
1. 点击“版本”（或“详细信息”）选项卡以查看版本号。

## **使用 Aspose.Cells API 检查版本号**

要通过API找出您正在使用的Aspose.Cells的版本号，请使用[CellsHelper](https://reference.aspose.com/cells/python-java/asposecells.api/cellshelper)类的GetVersion静态方法获取Aspose.Cell的版本号。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CheckVersionNumber.py" >}}
