---
title: 查看 VBA 项目是否已受保护
type: docs
weight: 20
url: /zh/net/find-out-if-vba-project-is-protected/
---

## **在 C# 中查看 VBA 项目是否已受保护**

您可以使用 Aspose.Cells 的 [**VbaProject.IsProtected**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected) 属性来检查 Excel 文件的 VBA（Visual Basic Applications）项目是否受保护。

## **示例代码**

以下示例代码创建一个工作簿，然后检查其 VBA 项目是否受保护。然后保护 VBA 项目并再次检查其是否受保护。请参考控制台输出。在保护之前，[**VbaProject.IsProtected**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected) 返回 **false**，但在保护后，它返回 **true**。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-FindoutifVBAProjectisProtected.cs" >}}

## **控制台输出**

这是上述示例代码的控制台输出供参考。

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
