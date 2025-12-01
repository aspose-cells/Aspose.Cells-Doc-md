---
title: Update references in other worksheets while deleting blank columns and rows in a worksheet
type: docs
weight: 5000
url: /net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

When you delete blank columns and rows in a worksheet, then its references in other worksheets become invalid. If you want to avoid this behavior and want those references of the current worksheet in other worksheets are also updated, then please use the [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) property and set it to **true**.

{{% /alert %}}

## **Update references in other worksheets while deleting blank columns and rows in a worksheet**

Please see the following sample code and its console output. The cell E3 in the second worksheet has a formula =Sheet1!C3 which is referring to cell C3 in the first worksheet. If you will set [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) property as **true**, this formula will be updated and become =Sheet1!A1 on deleting blank columns and rows in the first worksheet. However, if you will set [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) property as **false**, the formula in cell E3 of the second worksheet will remain =Sheet1!C3 and become invalid.

### **Programming Sample**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateReferenceInWorksheets-UpdateReferenceInWorksheets.cs" >}}

### **Console Output**

This is the console output of the above sample code when [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) property has been set as **true**.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

This is the console output of the above sample code when [**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference) property has been set as **false**. As you can see, the formula in cell E3 of the second worksheet is not updated and its cell value is now 0 instead of 4 which is invalid.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
