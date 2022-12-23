---
title: 使用 Aspose.Cells 添加 VBA 模块和代码
type: docs
weight: 20
url: /zh/java/adding-vba-module-and-code-using-aspose-cells/
---
{{% alert color="primary" %}}

Aspose.Cells 允许您使用 Aspose.Cells 添加新的 VBA 模块和宏代码。请使用[**Workbook.getVbaProject().getModules().add(**)](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#add(com.aspose.cells.Worksheet)) 方法在工作簿中添加新的 VBA 模块

{{% /alert %}}

## **使用 Aspose.Cells 添加 VBA 模块和代码**

以下示例代码创建一个新工作簿并添加一个新的 VBA 模块和宏代码，并以 XLSM 格式保存输出。一次，您将在 Microsoft Excel 中打开输出 XLSM 文件并单击**开发人员 > Visual Basic**菜单命令，您将看到一个名为“TestModule”的模块，在其中，您将看到以下宏代码。

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## 示例代码

下面是使用 VBA 模块和宏代码生成输出 XLSM 文件的示例代码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddVBAModuleAndCode-AddVBAModuleAndCode.java" >}}
