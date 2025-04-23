---
title: 使用Aspose.Cells检查修改密码
type: docs
weight: 2400
url: /zh/net/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

有时，您需要通过编程方式检查给定的密码是否与**修改密码**匹配。Aspose.Cells提供WorkbookSettings.WriteProtection.ValidatePassword()方法，您可以使用该方法检查给定的修改密码是否正确。

{{% /alert %}}

## **在Microsoft Excel中检查修改密码**

您可以在创建Microsoft Excel工作簿时指定**打开密码**和**修改密码**。请参阅此截图，显示Microsoft Excel提供的界面以指定这些密码。

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **使用Aspose.Cells检查修改密码**

以下示例代码加载了[源 Excel](5112232.xlsx) 文件。它具有打开密码为1234和修改密码为5678。该代码首先检查是否567为正确的修改密码，并返回false，然后检查是否5678为修改密码，并返回true。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckPasswordToModify-CheckPasswordToModifyUsingAsposeCells.cs" >}}

### **控制台输出**

这是加载了[源 Excel](5112232.xlsx) 文件后的上述示例代码的控制台输出。

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
