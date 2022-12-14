---
title: 使用 Aspose.Cells 修改 VBA 或宏代码
type: docs
weight: 90
url: /zh/java/modifying-vba-or-macro-code-using-aspose-cells/
---
{{% alert color="primary" %}} 

您可以使用Aspose.Cells修改VBA或宏代码。Aspose.Cells添加了以下类来读取和修改Excel文件中的VBA项目。

- Vba项目
- Vba模块集合
- Vba模块

本文将向您展示如何使用 Aspose.Cells 更改源 Excel 文件中的 VBA 或宏代码。

{{% /alert %}} 
## **例子**
以下示例代码加载源 Excel 文件，其中包含以下 VBA 或宏代码

{{< highlight "java" >}}

 Sub Button1_Click()

MsgBox "This is test message."

End Sub

{{< /highlight >}}

Aspose.Cells示例代码执行后，VBA或Macro代码会修改成这样

{{< highlight "java" >}}

 Sub Button1_Click()

MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

您可以下载[源Excel文件](5472596.xlsm)和[输出Excel文件](5472597.xlsm)从给定的链接。







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyVBAorMacroCode-ModifyVBAorMacroCode.java" >}}






