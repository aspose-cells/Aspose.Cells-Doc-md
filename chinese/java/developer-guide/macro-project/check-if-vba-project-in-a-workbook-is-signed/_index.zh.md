---
title: 检查工作簿中的VBA项目是否已签名
type: docs
weight: 40
url: /zh/java/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

您可以使用Microsoft Excel通过**工具 > 数字签名**菜单命令来检查您的VBA项目是否已签名或未签名。类似地，您可以使用Aspose.Cells的[**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned)方法来进行编程检查。

{{% /alert %}}

## **检查工作簿中的VBA项目是否已签名**

以下代码加载工作簿并使用[**Workbook.getVbaProject().isSigned()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsSigned)属性检查其VBA项目是否已签名。如果项目已签名，则该属性将返回**true**，否则将返回**false**。

## 示例代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckVbaProjectSigned-CheckVbaProjectSigned.java" >}}
