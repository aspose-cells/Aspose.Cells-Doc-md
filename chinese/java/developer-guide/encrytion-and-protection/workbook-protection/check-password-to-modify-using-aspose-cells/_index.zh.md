---
title: 使用Aspose.Cells检查修改密码
type: docs
weight: 190
url: /zh/java/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

在 Microsoft Excel 中创建工作簿时，可以单独分配一个 **打开密码** 和一个 **修改密码**。请参阅此截图，显示了 Microsoft Excel 提供的界面来指定这些密码。

![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)

有时，您需要以编程方式检查给定的密码是否与 **修改密码** 匹配。Aspose.Cells 提供了 [**workbook.getSettings().getWriteProtection().validatePassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/writeprotection#validatePassword(java.lang.String) 方法，您可以使用它来检查所给的修改密码是否正确。

{{% /alert %}}

## 使用 Aspose.Cells 检查修改密码的 Java 代码

以下样例代码加载 [源 Excel](5473057.xlsx) 文件。它的打开密码是 *1234*，修改密码是 *5678*。代码首先检查 *567* 是否正确的修改密码，返回 **false**，然后检查 *5678* 是否修改密码，返回 **true**。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckPassword-CheckPassword.java" >}}

## Java 代码生成的控制台输出

以下是加载 [源 Excel](5473057.xlsx) 文件后上述样例代码生成的控制台输出。

{{< highlight java >}}

Is 567 correct Password to modify: false

Is 5678 correct Password to modify: true

{{< /highlight >}}
