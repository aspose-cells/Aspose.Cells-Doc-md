---
title: 使用 Aspose.Cells 修改 VBA 或宏代码
type: docs
weight: 90
url: /zh/java/modifying-vba-or-macro-code-using-aspose-cells/
---

{{% alert color="primary" %}} 

您可以使用 Aspose.Cells 修改 VBA 或宏代码。Aspose.Cells 已添加以下类以读取和修改 Excel 文件中的 VBA 项目。

- VbaProject
- VbaModuleCollection
- VbaModule

本文将向您展示如何使用Aspose.Cells更改源Excel文件中的VBA或宏代码。

{{% /alert %}} 
## **示例**
以下示例代码加载带有以下VBA或宏代码的源Excel文件

{{< highlight java >}}

 Sub Button1_Click()

MsgBox "This is test message."

End Sub

{{< /highlight >}}

执行Aspose.Cells示例代码后，VBA或宏代码将被修改如下

{{< highlight java >}}

 Sub Button1_Click()

MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

您可以从以下链接下载[源 Excel 文件](5472596.xlsm)和[输出 Excel 文件](5472597.xlsm)。







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyVBAorMacroCode-ModifyVBAorMacroCode.java" >}}






