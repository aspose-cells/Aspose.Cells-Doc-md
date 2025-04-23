---
title: 使用 Aspose.Cells 添加 VBA 模块和代码
type: docs
weight: 20
url: /zh/java/adding-vba-module-and-code-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells 允许你通过 Aspose.Cells 添加新的 VBA 模块和宏代码。请使用 [**Workbook.getVbaProject().getModules().add(**)](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#add-com.aspose.cells.Worksheet-) 方法在工作簿中添加新 VBA 模块。

{{% /alert %}}

## **使用 Aspose.Cells 添加 VBA 模块和代码**

以下示例代码创建一个新工作簿，并添加一个新的VBA模块和宏代码，将输出保存为XLSM格式。一旦您打开输出的XLSM文件并单击“开发人员> Visual Basic”菜单命令，您将看到一个名为“TestModule”的模块，并在其中看到以下宏代码。

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## 示例代码

下面是一个生成带有 VBA 模块和宏代码输出 XLSM 文件的示例代码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddVBAModuleAndCode-AddVBAModuleAndCode.java" >}}
{{< app/cells/assistant language="java" >}}
