---
title: 删除工作表中的空白列和行时更新其他工作表中的引用
type: docs
weight: 5000
url: /zh/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---

{{% alert color="primary" %}}

当您删除工作表中的空白列和行时，其他工作表中对它们的引用将变得无效。如果您想避免此行为，并希望其他工作表中对当前工作表的引用也得到更新，那么请使用[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference)属性并将其设置为**true**。

{{% /alert %}}

## **删除工作表中的空白列和行时更新其他工作表中的引用**

请参阅以下示例代码及其控制台输出。第二个工作表中的单元格E3具有一个涉及到第一个工作表中单元格C3的公式=Sheet1!C3。如果您将[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference)属性设置为**true**，此公式将得到更新并变成在删除第一个工作表中的空白列和行后=Sheet1!A1。但是，如果您将[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference)属性设置为**false**，则第二个工作表中单元格E3的公式将保持=Sheet1!C3并变得无效。

### **编程示例**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateReferenceInWorksheets-UpdateReferenceInWorksheets.cs" >}}

### **控制台输出**

上述示例代码当[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference)属性设置为**true**时的控制台输出。

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

上述示例代码当[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference)属性设置为**false**时的控制台输出。您可以看到，第二个工作表中单元格E3的公式没有得到更新，它的单元格值现在是0而不是4，这是无效的。

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
