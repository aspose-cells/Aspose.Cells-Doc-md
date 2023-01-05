---
title: 如何设置工作簿的自动恢复属性
type: docs
weight: 160
url: /zh/java/how-to-set-autorecover-property-of-workbook/
---
{{% alert color="primary" %}}

您可以使用 Aspose.Cells 设置工作簿的自动恢复属性。该属性的默认值为**真的**.当你设置它**错误的**在工作簿上，Microsoft Excel 在该 Excel 文件上禁用自动恢复（自动保存）。

Aspose.Cells提供[**工作簿.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover)属性来启用或禁用此选项。

{{% /alert %}}

## Java 设置工作簿自动恢复属性的代码

下面的代码解释了如何使用[**工作簿.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover)工作簿的属性。代码首先读取此属性的默认值，即**真的**，然后将其设置为**错误的**并保存工作簿。然后它再次读取工作簿并读取此时为 false 的此属性的值。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetAutoRecoverProperty-SetAutoRecoverProperty.java" >}}

## 示例代码生成的输出

这是上述示例代码的控制台输出。

{{< highlight "java" >}}

AutoRecover: true

AutoRecover: false

{{< /highlight >}}
