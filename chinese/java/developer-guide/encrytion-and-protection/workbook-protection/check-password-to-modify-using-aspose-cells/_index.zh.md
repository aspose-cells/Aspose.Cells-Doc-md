---
title: 使用 Aspose.Cells 检查修改密码
type: docs
weight: 190
url: /zh/java/check-password-to-modify-using-aspose-cells/
---
{{% alert color="primary" %}}

你可以分配一个**打开密码**和一个**修改密码**在 Microsoft Excel 中创建工作簿时。请查看此屏幕截图，其中显示了 Microsoft Excel 提供的用于指定这些密码的界面。

![待办事项：图像_替代_文本](check-password-to-modify-using-aspose-cells_1.png)

有时，您需要检查给定的密码是否与**修改密码**以编程方式。 Aspose.Cells提供[**workbook.getSettings().getWriteProtection().validatePassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/writeprotection#validatePassword(java.lang.String)) 方法，您可以使用该方法检查给定的要修改的密码是否正确。

{{% /alert %}}

## Java 检查密码使用 Aspose.Cells 修改密码

以下示例代码加载[源Excel](5473057.xlsx)文件。它有一个密码可以打开*1234*和密码修改为*5678*.代码首先检查是否*567*是要修改的正确密码并返回**错误的**然后它检查是否*5678*是要修改的密码，它返回**真的**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckPassword-CheckPassword.java" >}}

## Java 代码生成的控制台输出

这是加载后上述示例代码的控制台输出[源Excel](5473057.xlsx)文件。

{{< highlight "java" >}}

Is 567 correct Password to modify: false

Is 5678 correct Password to modify: true

{{< /highlight >}}
