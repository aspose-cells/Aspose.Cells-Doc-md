---
title: 使用 Aspose.Cells 检查修改密码
type: docs
weight: 2400
url: /zh/net/check-password-to-modify-using-aspose-cells/
---
{{% alert color="primary" %}}

有时，您需要检查给定的密码是否与**修改密码**以编程方式。 Aspose.Cells 提供 WorkbookSettings.WriteProtection.ValidatePassword() 方法，您可以使用该方法检查给定的要修改的密码是否正确。

{{% /alert %}}

## **在Microsoft Excel中勾选修改密码**

你可以分配**打开密码**和**修改密码**在 Microsoft Excel 中创建工作簿时。请查看此屏幕截图，其中显示了 Microsoft Excel 提供的用于指定这些密码的界面。

|![待办事项：图像_替代_文本](check-password-to-modify-using-aspose-cells_1.png)|
|:- |

## **使用 Aspose.Cells 检查修改密码**

以下示例代码加载[源Excel](5112232.xlsx)文件。它的打开密码为 1234，修改密码为 5678。代码首先检查 567 是否为正确的修改密码并返回 false，然后检查 5678 是否为修改密码并返回 true。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckPasswordToModify-CheckPasswordToModifyUsingAsposeCells.cs" >}}

### **控制台输出**

这是加载后上述示例代码的控制台输出[源Excel](5112232.xlsx)文件。

{{< highlight "java" >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
