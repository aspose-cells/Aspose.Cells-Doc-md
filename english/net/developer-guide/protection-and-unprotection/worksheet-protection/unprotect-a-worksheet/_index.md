---
title: Unprotect a Worksheet
type: docs
weight: 20
url: /net/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

If a developer needs to remove protection from a protected worksheet at runtime so that some changes can be made to the file? This can easily be done with Aspose.Cells.

{{% /alert %}}

## **Unprotect a Worksheet**

### **Using Microsoft Excel**

To remove protection from a worksheet:

From the **Tools** menu, select **Protection** followed by **Unprotect Sheet**. Protection will be removed unless the worksheet is password protected. In this case, a dialog prompts for the password. Enter the password and worksheet will be unprotected then.

### **Unprotecting a Simply Protected Worksheet Using Aspose.Cells**

A worksheet can be unprotected by calling the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class' [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index) method.
A simply protected worksheet is one which is not protected with a password. Such worksheets can be unprotected by calling the [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/unprotect/index) method without passing a parameter.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingSimplyProtectedWorksheet-1.cs" >}}

### **Unprotecting a Password Protected Worksheet Using Aspose.Cells**

A password protected worksheet is one that is protected with a password. Such worksheets can be unprotected by calling an overloaded version of the [**Unprotect**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/unprotect/methods/1) method that takes the password as a parameter.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Unprotect-UnprotectingPasswordProtectedWorksheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}