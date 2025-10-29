---
title: 取消保护工作表
type: docs
weight: 20
url: /zh/python-net/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

如果开发人员需要在运行时移除受保护工作表的保护，以便对文件进行某些更改？这可以通过Aspose.Cells for Python via .NET轻松实现。

{{% /alert %}}

## **取消保护工作表**

### **使用Microsoft Excel**

要取消工作表的保护：

在**工具**菜单中，选择**保护**，然后选择**取消保护工作表**。 除非工作表受到密码保护，否则保护将被移除。 在这种情况下，会提示输入密码。 输入密码，工作表将取消保护。

### **使用Aspose.Cells for Python via .NET解除简单保护的工作表**

可以通过调用[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)类的[**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/unprotect)方法来取消工作表的保护。
简单受保护的工作表是没有设置密码保护的工作表。 可以通过调用[**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/unprotect)方法来取消这样的工作表的保护而不传递参数。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-UnprotectingSimplyProtectedWorksheet-1.py" >}}

### **使用Aspose.Cells for Python via .NET解除密码保护的工作表**

受密码保护的工作表是使用密码保护的工作表。 可以通过调用带有密码参数的重载版本的[**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/unprotect/)方法来取消这样的工作表的保护。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-UnprotectingPasswordProtectedWorksheet-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
