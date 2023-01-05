---
title: 查看 VBA 项目是否受保护
type: docs
weight: 80
url: /zh/java/find-out-if-vba-project-is-protected/
---
## **可能的使用场景**
您可以使用 Aspose.Cells 查看 Excel 文件的 VBA（Visual Basic 应用程序）项目是否受保护[VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected)方法
## **示例代码**
以下示例代码创建一个工作簿，然后检查其 VBA 项目是否受保护。然后它保护 VBA 项目并再次检查其 VBA 项目是否受到保护。请查看其控制台输出以供参考。保护前，[VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected)回报**错误的**但在保护之后，它返回**真的**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-WorkbookVBAProject-FindoutifVBAProjectisProtected.java" >}}
## **控制台输出**
这是上面示例代码的控制台输出，供参考。

{{< highlight "java" >}}

 IsProtected - Before Protecting VBA Project: false

IsProtected - After Protecting VBA Project: true

{{< /highlight >}}
