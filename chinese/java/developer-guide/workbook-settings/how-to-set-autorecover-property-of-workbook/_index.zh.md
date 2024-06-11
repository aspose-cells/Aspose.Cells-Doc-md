---
title: 如何设置工作簿的AutoRecover属性
type: docs
weight: 160
url: /zh/java/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

您可以使用Aspose.Cells来设置工作簿的AutoRecover属性。此属性的默认值为**true**。 当您在工作簿上将其设为**false**时，Microsoft Excel将禁用该Excel文件的自动恢复（自动保存）。

Aspose.Cells提供了[**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover)属性来启用或禁用此选项。

{{% /alert %}}

## 设置工作簿的AutoRecover属性的Java代码

以下代码解释了如何使用工作簿的[**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover)属性。 该代码首先读取此属性的默认值，即**true**，然后将其设置为**false**并保存工作簿。然后再次读取工作簿，并读取此属性的值，此时该属性的值为false。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetAutoRecoverProperty-SetAutoRecoverProperty.java" >}}

## 示例代码生成的输出

这是上面示例代码的控制台输出。

{{< highlight java >}}

AutoRecover: true

AutoRecover: false

{{< /highlight >}}
