---
title: 取消保护工作表
type: docs
weight: 20
url: /zh/net/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

如果开发人员需要在运行时从受保护的工作表中移除保护，以便对文件进行一些更改？这可以很容易地通过Aspose.Cells来完成。

{{% /alert %}}

## **取消保护工作表**

### **使用Microsoft Excel**

要从工作表中取消保护：

从**工具**菜单中，选择**保护**，然后选择**取消保护工作表**。保护将被移除，除非工作表受密码保护。在这种情况下，会提示输入密码。输入密码后，工作表将被取消保护。

### **使用Aspose.Cells取消简单保护的工作表**

可以通过调用[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类的[**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index)方法来取消工作表的保护。
简单受保护的工作表是指未受密码保护的工作表。通过调用[**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index)方法而不传递参数可以取消此类工作表的保护。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingSimplyProtectedWorksheet-1.cs" >}}

### **使用Aspose.Cells取消密码保护的工作表**

受密码保护的工作表是指受密码保护的工作表。可以通过调用接受密码作为参数的[**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/unprotect/methods/1)方法的重载版本来取消此类工作表的保护。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingPasswordProtectedWorksheet-1.cs" >}}
