---
title: 查看 VBA 项目是否已受保护
type: docs
weight: 80
url: /zh/java/find-out-if-vba-project-is-protected/
---

## **可能的使用场景**
您可以使用 Aspose.Cells 的 [VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected) 方法来查找 Excel 文件的 VBA（Visual Basic Applications）项目是否受保护。
## **示例代码**
以下示例代码创建一个工作簿，然后检查其 VBA 项目是否受保护。然后保护 VBA 项目，并再次检查其 VBA 项目是否受保护。请参考控制台输出。保护之前，[VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected) 返回 **false**，但保护后返回 **true**。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-WorkbookVBAProject-FindoutifVBAProjectisProtected.java" >}}
## **控制台输出**
这是上述示例代码的控制台输出供参考。

{{< highlight java >}}

 IsProtected - Before Protecting VBA Project: false

IsProtected - After Protecting VBA Project: true

{{< /highlight >}}
