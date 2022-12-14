---
title: 检查工作簿中的 VBA 项目是否已签名
type: docs
weight: 40
url: /zh/java/check-if-vba-project-in-a-workbook-is-signed/
---
{{% alert color="primary" %}}

您可以使用 Microsoft Excel 通过以下方式检查您的 VBA 项目是否已签名**工具 > 数字签名...**菜单命令。同样，您可以使用 Aspose.Cells 以编程方式检查它[**工作簿.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned)方法。

{{% /alert %}}

## **检查工作簿中的 VBA 项目是否已签名**

以下代码加载工作簿并检查其 VBA 项目是否已使用签名[**工作簿.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned)财产。该物业将返回**真的**如果项目已签署，否则它将返回**错误的**.

## 示例代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckVbaProjectSigned-CheckVbaProjectSigned.java" >}}
