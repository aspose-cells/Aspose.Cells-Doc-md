---
title: 检查版本号
type: docs
weight: 80
url: /zh/net/check-version-number/
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

要通过 API 查找正在使用的 Aspose.Cells 版本号，使用 [CellsHelper](https://reference.aspose.com/cells/net/aspose.cells/cellshelper) 类的 GetVersion 静态方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-CheckVersionNumber-1.cs" >}}
