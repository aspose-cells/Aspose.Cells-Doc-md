---
title: 更新其他工作表中的引用，同时删除工作表中的空白列和行
type: docs
weight: 5000
url: /zh/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---
{{% alert color="primary" %}}

当您删除工作表中的空白列和行时，它在其他工作表中的引用将变得无效。如果您想避免这种行为并希望其他工作表中对当前工作表的引用也得到更新，那么请使用[**删除选项.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference)属性并将其设置为**真的**.

{{% /alert %}}

## **更新其他工作表中的引用，同时删除工作表中的空白列和行**

请查看以下示例代码及其控制台输出。第二个工作表中的单元格 E3 的公式 =Sheet1!C3 引用第一个工作表中的单元格 C3。如果你将设置[**删除选项.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference)财产作为**真的**，此公式将更新并变为 =Sheet1!A1 删除第一个工作表中的空白列和行。但是，如果您将设置[**删除选项.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference)财产作为**错误的**，第二个工作表的单元格 E3 中的公式将保持 =Sheet1!C3 并变得无效。

### **编程范例**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateReferenceInWorksheets-UpdateReferenceInWorksheets.cs" >}}

### **控制台输出**

这是上面示例代码的控制台输出[**删除选项.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference)属性已设置为**真的**.

{{< highlight "java" >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

这是上面示例代码的控制台输出[**删除选项.UpdateReference**](https://reference.aspose.com/cells/net/aspose.cells/deleteoptions/properties/updatereference)属性已设置为**错误的**.如您所见，第二个工作表的单元格 E3 中的公式未更新，其单元格值现在为 0 而不是无效的 4。

{{< highlight "java" >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}
