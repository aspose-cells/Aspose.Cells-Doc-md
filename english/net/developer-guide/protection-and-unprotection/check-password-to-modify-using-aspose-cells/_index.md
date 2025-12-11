---
title: Check Password to modify using Aspose.Cells
type: docs
weight: 2400
url: /net/check-password-to-modify-using-aspose-cells/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, you need to check if the given password matches the **Password to modify** programmatically. Aspose.Cells provides the `WorkbookSettings.WriteProtection.ValidatePassword()` method, which you can use to check whether the given password to modify is correct or not.

{{% /alert %}}

## **Check Password to Modify in Microsoft Excel**

You can assign **Password to open** and **Password to modify** while creating your workbooks in Microsoft Excel. Please see this screenshot, which shows the interface that Microsoft Excel provides to specify these passwords.

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **Check Password to Modify using Aspose.Cells**

The following sample code loads the [source Excel](5112232.xlsx) file. It has a password to open of **1234** and a password to modify of **5678**. The code first checks if **567** is the correct password to modify, which returns **false**, and then checks if **5678** is the password to modify, which returns **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckPasswordToModify-CheckPasswordToModifyUsingAsposeCells.cs" >}}

### **Console Output**

Here is the console output of the above sample code after loading the [source Excel](5112232.xlsx) file.

{{< highlight csharp >}}
Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True
{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
