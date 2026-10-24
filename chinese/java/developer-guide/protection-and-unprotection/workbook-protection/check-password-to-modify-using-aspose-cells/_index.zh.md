---
title: 使用Aspose.Cells检查修改密码
type: docs
weight: 190
url: /zh/java/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

在 Microsoft Excel 中创建工作簿时，您可以为**打开密码**和**修改密码**分配密码。请参阅此屏幕截图，该屏幕截图显示了微软 Excel 提供的界面以指定这些密码。

![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)

有时，您需要检查给定密码是否与**程序密码**匹配。Aspose.Cells提供了 [**workbook.getSettings().getWriteProtection().validatePassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/writeprotection#validatePassword-java.lang.String-) 方法，您可以使用它来检查给定的修改密码是否正确。

{{% /alert %}}

## 使用 Aspose.Cells 检查修改密码的 Java 代码

以下示例代码加载了 [source Excel](5473057.xlsx) 文件。它具有打开密码 *1234* 和修改密码 *5678*。代码首先检查 *567* 是否是正确的修改密码，如果返回 **false**，然后检查 *5678* 是否为修改密码，如果返回 **true**。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckPassword-CheckPassword.java" >}}

## Java代码生成的控制台输出

这是以上示例代码加载 [源Excel](5473057.xlsx) 文件后的控制台输出。

{{< highlight java >}}

Is 567 correct Password to modify: false

Is 5678 correct Password to modify: true

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
