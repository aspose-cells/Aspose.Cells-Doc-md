---
title: 检查版本号
type: docs
weight: 80
url: /zh/python-net/check-version-number/
---

{{% alert color="primary" %}}

想知道您正在使用的Aspose.Cells版本？我们定期发布Aspose.Cells的新版本，既引入新功能，也修复问题。版本号由主版本号、次版本号和热修复版本号组成。每个数字必须是从0开始的整数。格式如下：

主版本号.次版本号.热修复版本号

当我们发布Aspose.Cells的新版本时，我们会更新版本号。

本文介绍如何手动检查系统上安装的Aspose.Cells版本，以及如何使用Aspose.Cells API。

{{% /alert %}}

## **手动检查版本号**

要手动查找您正在使用的Aspose.Cells版本：

1.右键单击Aspose.Cells.dll文件，然后选择**属性**。
1. 单击版本（或详情）选项卡来查看版本号。

## **使用Aspose.Cells API检查版本号**

要通过API查找您正在使用的 Aspose.Cells 版本，使用 CellsHelper 类的 GetVersion 静态方法获取 Aspose.Cell 的版本号。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CheckVersionNumber.py" >}}
{{< app/cells/assistant language="python-net" >}}
