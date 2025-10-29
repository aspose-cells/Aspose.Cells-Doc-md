---
title: 检查工作簿中的VBA项目是否已用Golang via C++签名
linktitle: 检查工作簿中的VBA项目是否已签名
type: docs
weight: 70
url: /zh/go-cpp/check-if-vba-project-in-a-workbook-is-signed/
description: 使用C++中的Aspose.Cells检测工作簿中的VBA项目是否已签名
---

{{% alert color="primary" %}}

你可以通过**工具 > 数字签名...**菜单命令在Microsoft Excel中检测你的VBA项目是否已签名。也可以用Aspose.Cells的[**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/go-cpp/vbaproject/issigned/)属性进行程序检测。

{{% /alert %}}

## **用C++检测工作簿中的VBA项目是否已签名**

以下代码加载工作簿，并使用[**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/go-cpp/vbaproject/issigned/)属性检测其VBA项目是否已签名。若已签名，返回**true**；否则返回**false**。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckIfVbaProjectInAWorkbookIsSigned.go" >}}
