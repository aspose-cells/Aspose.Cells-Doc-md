---
title: Unprotect a Worksheet
type: docs
weight: 20
url: /python-net/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

If a developer needs to remove protection from a protected worksheet at runtime so that some changes can be made to the file? This can easily be done with Aspose.Cells for Python via .NET.

{{% /alert %}}

## **Unprotect a Worksheet**

### **Using Microsoft Excel**

To remove protection from a worksheet:

From the **Tools** menu, select **Protection** followed by **Unprotect Sheet**. Protection will be removed unless the worksheet is password protected. In this case, a dialog prompts for the password. Enter the password and worksheet will be unprotected then.

### **Unprotecting a Simply Protected Worksheet Using Aspose.Cells for Python via .NET**

A worksheet can be unprotected by calling the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class' [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/unprotect) method.
A simply protected worksheet is one which is not protected with a password. Such worksheets can be unprotected by calling the [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/unprotect) method without passing a parameter.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-UnprotectingSimplyProtectedWorksheet-1.py" >}}

### **Unprotecting a Password Protected Worksheet Using Aspose.Cells for Python via .NET**

A password protected worksheet is one that is protected with a password. Such worksheets can be unprotected by calling an overloaded version of the [**unprotect**](https://reference.aspose.com/cells/python-net/aspose.cells.worksheet/unprotect) method that takes the password as a parameter.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-UnprotectingPasswordProtectedWorksheet-1.py" >}}

