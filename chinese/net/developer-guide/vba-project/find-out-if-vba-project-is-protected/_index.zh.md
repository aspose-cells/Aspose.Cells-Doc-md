---
title: 查找 VBA 项目是否受保护
type: docs
weight: 20
url: /zh/net/find-out-if-vba-project-is-protected/
---

## **在 C# 中查找 Excel 文件的 VBA 项目是否受保护**

您可以使用 Aspose.Cells 的 [**VbaProject.IsProtected**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected) 属性找出您的 Excel 文件的 VBA（Visual Basic Applications）项目是否受保护。

## **示例代码**

以下示例代码创建一个工作簿，然后检查其VBA项目是否受保护。然后保护VBA项目，再次检查其VBA项目是否受保护。请查看控制台输出以供参考。在保护之前，[**VbaProject.IsProtected**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected)返回**false**，但在保护之后，它返回**true**。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-FindoutifVBAProjectisProtected.cs" >}}

## **控制台输出**

这是上述示例代码的控制台输出以供参考。

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
