---
title: 检查版本号
type: docs
weight: 80
url: /zh/python-java/check-version-number/
---
{{% alert color="primary" %}}

想知道您使用的是哪个版本的 Aspose.Cells？我们定期发布 Aspose.Cells 的新版本，以引入新功能并修复问题。版本号由主版本号、次版本号和修补程序版本号组成。每个数字必须是从 0 开始的整数。格式如下：

主要.次要.hotfix

当我们发布 Aspose.Cells 的新版本时，我们会更新版本号。

本文介绍如何手动和使用 Aspose.Cells API 检查系统上安装了哪个版本的 Aspose.Cells。

{{% /alert %}}

## **手动检查版本号**

要手动找出您使用的是哪个版本的 Aspose.Cells：

1. 右键单击 Aspose.Cells.dll 文件并选择**特性**.
1. 单击版本（或详细信息）选项卡以检查版本号。

## **使用 Aspose.Cells API 检查版本号**

要通过 API 找出您使用的是哪个版本的 Aspose.Cells，请使用[细胞助手](https://reference.aspose.com/cells/python-java/asposecells.api/cellshelper)类 GetVersion 静态方法获取 Aspose.Cell 的版本号。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CheckVersionNumber.py" >}}
