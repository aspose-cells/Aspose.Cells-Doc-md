---
title: Check Password to modify using Aspose.Cells
type: docs
weight: 190
url: /java/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}} 

You can assign a **Password to open** and a **Password to modify** while creating your workbooks in Microsoft Excel. Please see this screenshot which shows the interface Microsoft Excel provides to specify these passwords.

![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)

Sometimes, you need to check if the given password matches with the **Password to modify** programmatically. Aspose.Cells provides [workbook.getSettings().getWriteProtection().validatePassword()](https://apireference.aspose.com/java/cells/com.aspose.cells/writeprotection#validatePassword\(java.lang.String\)) method which you can use to check if the given Password to modify is correct or not.

{{% /alert %}} 
#### **Check Password to modify using Aspose.Cells**
The following sample codes load the [source Excel](5473057.xlsx) file. It has a Password to open as 1234 and Password to modify as 5678. The code first checks if 567 is correct Password to modify and it returns false and then it checks if 5678 is Password to modify and it returns true.

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckPassword-CheckPassword.java" >}}
#### **Console Output**
Here is the Console Output of the above sample code after loading the [source Excel](5473057.xlsx) file.

{{< highlight java >}}

 Is 567 correct Password to modify: false

Is 5678 correct Password to modify: true

{{< /highlight >}}
