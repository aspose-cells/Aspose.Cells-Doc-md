---
title: Unprotect a Worksheet with Golang via C++
linktitle: Unprotect a Worksheet
type: docs
weight: 20
url: /go-cpp/unprotect-a-worksheet/
description: Learn how to unprotect a worksheet using Aspose.Cells for Go via C++.
---

{{% alert color="primary" %}}

If a developer needs to remove protection from a protected worksheet at runtime so that some changes can be made to the file, this can easily be done with Aspose.Cells.

{{% /alert %}}

## **Unprotect a Worksheet**

### **Using Microsoft Excel**

To remove protection from a worksheet:

From the **Tools** menu, select **Protection** followed by **Unprotect Sheet**. Protection will be removed unless the worksheet is password protected. In this case, a dialog prompts for the password. Enter the password and the worksheet will be unprotected.

### **Unprotecting a Simply Protected Worksheet Using Aspose.Cells**

A worksheet can be unprotected by calling the [**Worksheet**](https://reference.aspose.com/cells/go-cpp/worksheet/) class' [**Unprotect**](https://reference.aspose.com/cells/go-cpp/worksheet/unprotect/) method. A simply protected worksheet is one that is not protected with a password. Such worksheets can be unprotected by calling the [**Unprotect**](https://reference.aspose.com/cells/go-cpp/worksheet/unprotect/) method without passing a parameter.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UnprotectAWorksheet.go" >}}

### **Unprotecting a Password-Protected Worksheet Using Aspose.Cells**

A password-protected worksheet is one that is protected with a password. Such worksheets can be unprotected by calling an overloaded version of the [**Unprotect**](https://reference.aspose.com/cells/go-cpp/worksheet/unprotect/) method that takes the password as a parameter.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UnprotectAWorksheet-1.go" >}}
{{< app/cells/assistant language="go" >}}
