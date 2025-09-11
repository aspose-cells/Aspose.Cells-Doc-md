---
title: Check Password to modify using Aspose.Cells for Python via .NET
type: docs
weight: 2400
url: /python-net/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

Sometimes, you need to check if the given password matches with the **Password to modify** programmatically. Aspose.Cells for Python via .NET provides WorkbookSettings.write_protection.validate_password() method which you can use to check if the given Password to modify is correct or not.

{{% /alert %}}

## **Check Password to modify in Microsoft Excel**

You can assign **Password to open** and **Password to modify** while creating your workbooks in Microsoft Excel. Please see this screenshot which shows the interface Microsoft Excel provides to specify these passwords.

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **Check Password to modify using Aspose.Cells for Python via .NET**

The following sample codes load the [source Excel](5112232.xlsx) file. It has a Password to open as 1234 and Password to modify as 5678. The code first checks if 567 is correct Password to modify and it returns false and then it checks if 5678 is Password to modify and it returns true.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-CheckPasswordToModifyUsingAsposeCells.py" >}}

### **Console Output**

Here is the Console Output of the above sample code after loading the [source Excel](5112232.xlsx) file.

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}