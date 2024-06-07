---
title: 使用Aspose.Cells添加VBA模块和代码
type: docs
weight: 20
url: /zh/java/adding-vba-module-and-code-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells允许您使用Aspose.Cells添加新的VBA模块和宏代码。请使用[**Workbook.getVbaProject().getModules().add(**)]方法在工作簿中添加新的VBA模块

{{% /alert %}}

## **使用Aspose.Cells添加VBA模块和代码**

以下示例代码创建一个新工作簿，并添加一个新的VBA模块和宏代码，然后以XLSM格式保存输出。一旦您打开输出的XLSM文件并单击**开发人员 > Visual Basic**菜单命令，您将看到一个名为"TestModule"的模块，在其内部，您将看到以下宏代码。

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## 示例代码

以下是一个生成带有VBA模块和宏代码的输出XLSM文件的示例代码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddVBAModuleAndCode-AddVBAModuleAndCode.java" >}}
