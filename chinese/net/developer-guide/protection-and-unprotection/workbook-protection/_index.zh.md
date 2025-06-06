---
title: 保护和取消保护工作簿结构
type: docs
weight: 40
url: /zh/net/protect-and-unprotect-workbook-structure/
description: 使用 C# 代码保护和取消保护 Excel 文件的工作簿结构。
---


{{% alert color="primary" %}}
为防止其他用户查看隐藏工作表、添加、移动、删除或隐藏工作表，并重命名工作表，您可以使用密码保护 Excel 工作簿的结构。
{{% /alert %}}


## **在 MS Excel 中保护和取消保护工作簿结构**

**![保护和取消保护工作簿结构](protect-and-unprotect-workbook-structure.png)**

1. 点击 **审阅 > 保护工作簿**。
1. 在 **密码框** 中输入密码。
1. 选择 **确定**，重新输入密码以确认，然后再次选择 **确定**。


## **使用 Aspose.Cell for .Net 保护工作簿结构**
只需要以下简单代码行来实现保护 Excel 文件的工作簿结构。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Example-Protect-Workbook-Structure.cs" >}}

## **使用 Aspose.Cell for .Net 取消保护工作簿结构**
使用 Aspose.Cells API 轻松取消工作簿结构保护。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Example-Unprotect-Workbook-Structure.cs" >}}

{{% alert color="primary" %}}
注意：需要正确的密码。
{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
