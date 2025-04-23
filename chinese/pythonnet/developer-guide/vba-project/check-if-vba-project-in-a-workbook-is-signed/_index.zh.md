---
title: 检查工作簿中的VBA项目是否已签名
type: docs
weight: 70
url: /zh/python-net/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

您可以通过Microsoft Excel的**工具 > 数字签名...**菜单命令检查VBA项目是否已签名。同样，也可以使用Aspose.Cells for Python via .NET的[**Workbook.vba_project.is_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_signed)属性编程方式进行验证。

{{% /alert %}}

## **在Python中检查工作簿中的VBA项目是否已签名**

以下代码加载工作簿并使用[**Workbook.vba_project.is_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_signed)属性检查其VBA项目是否已签名。如果项目已签名，则该属性将返回**true**，否则将返回**false**。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CheckVbaProjectSigned-1.py" >}}

