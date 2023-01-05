---
title: 取消保护工作表
type: docs
weight: 20
url: /zh/net/unprotect-a-worksheet/
---
{{% alert color="primary" %}}

如果开发人员需要在运行时从受保护的工作表中删除保护，以便可以对文件进行一些更改？使用 Aspose.Cells 可以轻松完成此操作。

{{% /alert %}}

## **取消保护工作表**

### **使用 Microsoft Excel**

要取消对工作表的保护：

来自**工具**菜单，选择**保护**其次是**取消保护工作表**.除非工作表受密码保护，否则保护将被取消。在这种情况下，会出现一个对话框提示输入密码。输入密码，然后工作表将不受保护。

### **使用 Aspose.Cells 取消保护简单保护的工作表**

可以通过调用[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级'[**取消保护**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index)方法。
简单保护的工作表是不受密码保护的工作表。可以通过调用[**取消保护**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index)不传递参数的方法。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingSimplyProtectedWorksheet-1.cs" >}}

### **使用 Aspose.Cells 取消保护受密码保护的工作表**

受密码保护的工作表是受密码保护的工作表。可以通过调用重载版本的[**取消保护**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/unprotect/methods/1)将密码作为参数的方法。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingPasswordProtectedWorksheet-1.cs" >}}
