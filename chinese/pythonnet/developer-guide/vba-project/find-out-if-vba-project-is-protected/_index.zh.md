---
title: 查看 VBA 项目是否已受保护
type: docs
weight: 20
url: /zh/python-net/find-out-if-vba-project-is-protected/
---

## **在Python中检查VBA项目是否已被保护**

您可以使用Aspose.Cells for Python via .NET的[**VbaProject.is_protected**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_protected)属性来判断Excel文件的VBA（Visual Basic Applications）项目是否受到保护。

## **示例代码**

以下示例代码创建一个工作簿，然后检查其 VBA 项目是否受保护。然后保护 VBA 项目并再次检查其是否受保护。请参考控制台输出。在保护之前，[**VbaProject.is_protected**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_protected) 返回 **false**，但在保护后，它返回 **true**。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-FindoutifVBAProjectisProtected.py" >}}

## **控制台输出**

这是上述示例代码的控制台输出供参考。

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
