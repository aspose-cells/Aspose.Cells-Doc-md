---
title: 使用Aspose.Cells检查修改密码
type: docs
weight: 2400
url: /zh/net/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

有时，您需要以编程方式检查给定密码是否与**修改密码**匹配。 Aspose.Cells提供了WorkbookSettings.WriteProtection.ValidatePassword()方法，您可以使用此方法检查给定的修改密码是否正确。

{{% /alert %}}

## **检查 Microsoft Excel 修改密码**

在创建 Microsoft Excel 工作簿时，您可以指定 **打开密码** 和 **修改密码**。请参阅此截图，展示了 Microsoft Excel 提供的界面用于指定这些密码。

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **使用 Aspose.Cells 检查修改密码**

以下示例代码加载了[源 Excel](5112232.xlsx)文件。它具有 1234 作为打开密码和 5678 作为修改密码。代码首先检查 567 是否正确的修改密码，返回 false，然后检查 5678 是否为修改密码，返回 true。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckPasswordToModify-CheckPasswordToModifyUsingAsposeCells.cs" >}}

### **控制台输出**

以下是加载[源 Excel](5112232.xlsx)文件后的示例代码的控制台输出。

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
