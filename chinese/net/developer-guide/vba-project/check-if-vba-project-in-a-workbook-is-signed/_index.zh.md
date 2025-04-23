---
title: 检查工作簿中的VBA项目是否已签名
type: docs
weight: 70
url: /zh/net/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

您可以通过**工具 > 数字签名...**菜单命令，使用Microsoft Excel来检查您的VBA项目是否已签名。同样，您也可以使用Aspose.Cells的[**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/issigned)属性以编程方式来检查。

{{% /alert %}}

## **在C#中检查工作簿中的VBA项目是否已签名**

以下代码加载工作簿并使用[**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/issigned)属性检查其VBA项目是否已签名。如果项目已签名，则该属性将返回**true**，否则将返回**false**。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaProjectSigned-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
