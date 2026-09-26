---
title: Check Password to modify using Aspose.Cells with Golang via C++
linktitle: Check Password to modify
type: docs
weight: 2400
url: /go-cpp/check-password-to-modify-using-aspose-cells/
description: Check if the given password matches the Password to modify using Aspose.Cells with Golang via C++.
---

{{% alert color="primary" %}}
Sometimes, you need to check if the given password matches the **Password to modify** programmatically. Aspose.Cells provides the `WorkbookSettings.WriteProtection.ValidatePassword()` method, which you can use to check if the given Password to modify is correct or not.
{{% /alert %}}

## **Check Password to modify in Microsoft Excel**

You can assign **Password to open** and **Password to modify** while creating your workbooks in Microsoft Excel. Please see this screenshot showing the interface Microsoft Excel provides to specify these passwords.

| ![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png) |
| :--------------------------------------------------------------------- |

## **Check Password to modify using Aspose.Cells**

The following sample code loads the [source Excel](5112232.xlsx) file, which has a Password to open of **1234** and a Password to modify of **5678**. The code first checks whether **567** is the correct Password to modify (returns false) and then checks whether **5678** is the Password to modify (returns true).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckPasswordToModifyUsingAsposeCells.go" >}}

### **Console Output**

Here is the console output of the above sample code after loading the [source Excel](5112232.xlsx) file.

{{< highlight java >}}
Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True
{{< /highlight >}}
{{< app/cells/assistant language="go" >}}
