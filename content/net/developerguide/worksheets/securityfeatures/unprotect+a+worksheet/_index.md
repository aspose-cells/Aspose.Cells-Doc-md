---
title : "Unprotect a Worksheet" 
description : "" 
weight : 16164 
toc : false
type: docs
url: /net/developerguide/worksheets/securityfeatures/unprotect+a+worksheet/
---

# Aspose.Cells for .NET : Unprotect a Worksheet


If a developer needs to remove protection from a protected worksheet at runtime so that some changes can be made to the file? This can easily be done with Aspose.Cells.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Unprotect a Worksheet](#unprotect-a-worksheet)
    *   1.1 [Using Microsoft Excel](#using-microsoft-excel)
    *   1.2 [Unprotecting a Simply Protected Worksheet Using Aspose.Cells](#unprotecting-a-simply-protected-worksheet-using-aspose.cells)
    *   1.3 [Unprotecting a Password Protected Worksheet Using Aspose.Cells](#unprotecting-a-password-protected-worksheet-using-aspose.cells)
{{< /panel >}}
 

## Unprotect a Worksheet

### Using Microsoft Excel

To remove protection from a worksheet:

From the **Tools** menu, select **Protection** followed by **Unprotect Sheet**. Protection will be removed unless the worksheet is password protected. In this case, a dialog prompts for the password. Enter the password and worksheet will be unprotected then.

### Unprotecting a Simply Protected Worksheet Using Aspose.Cells

A worksheet can be unprotected by calling the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class' [Unprotect](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/methods/unprotect/index) method.  
A simply protected worksheet is one which is not protected with a password. Such worksheets can be unprotected by calling the [Unprotect](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/methods/unprotect) method without passing a parameter.

### Unprotecting a Password Protected Worksheet Using Aspose.Cells

A password protected worksheet is one that is protected with a password. Such worksheets can be unprotected by calling an overloaded version of the [Unprotect](https://apireference.aspose.com/net/cells/aspose.cells.worksheet/unprotect/methods/1) method that takes the password as a parameter.

