---
title: 删除工作表中的空白列和行时更新其他工作表中的引用
type: docs
weight: 5000
url: /zh/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---

{{% alert color="primary" %}}

当您在工作表中删除空白列和行时，其他工作表中对该工作表的引用就会变得无效。如果您想避免这种行为，希望在其他工作表中也更新对当前工作表的引用，请使用[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference)属性并将其设置为**true**。

{{% /alert %}}

## **在删除工作表中的空白列和行时更新其他工作表中的引用**

请参阅以下示例代码及其控制台输出。第二个工作表中的单元格E3具有公式=Sheet1!C3，该公式指向第一个工作表中的单元格C3。如果您将[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference)属性设置为**true**，此公式将会被更新，并变为在删除第一个工作表中的空白列和行时的=Sheet1!A1。但是，如果您将[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference)属性设置为**false**，第二个工作表中的单元格E3中的公式将保持为=Sheet1!C3，变为无效。

### **编程示例**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateReferenceInWorksheets-UpdateReferenceInWorksheets.cs" >}}

### **控制台输出**

这是设置[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference)属性为**true**时上述示例代码的控制台输出。

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

这是设置[**DeleteOptions.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference)属性为**false**时上述示例代码的控制台输出。如您所见，第二个工作表中的单元格E3中的公式未被更新，其单元格值现在为0，而非4，这是无效的。

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
