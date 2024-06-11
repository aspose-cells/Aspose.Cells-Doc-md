---
title: 删除工作表中的空白列和行时更新其他工作表中的引用
type: docs
weight: 5000
url: /zh/python-net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
description: 本文展示了如何使用 Aspose.Cells for Python via .NET API 在删除工作表中的空白列和行时更新其他工作表中的引用。
keywords: Python Excel 库，Python 删除空白列和行时更新其他工作表中的引用，删除工作表中的空白列和行时更新引用。
---

{{% alert color="primary" %}}

当您删除工作表中的空白列和行时，其他工作表中对它们的引用将变得无效。如果您想避免此行为，并希望其他工作表中对当前工作表的引用也得到更新，那么请使用[**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/)属性并将其设置为**true**。

{{% /alert %}}

## **删除工作表中的空白列和行时更新其他工作表中的引用**

请参阅以下示例代码及其控制台输出。第二个工作表中的单元格E3具有一个涉及到第一个工作表中单元格C3的公式=Sheet1!C3。如果您将[**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/)属性设置为**true**，此公式将得到更新并变成在删除第一个工作表中的空白列和行后=Sheet1!A1。但是，如果您将[**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/)属性设置为**false**，则第二个工作表中单元格E3的公式将保持=Sheet1!C3并变得无效。

### **编程示例**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-UpdateReferenceInWorksheets.py" >}}

### **控制台输出**

上述示例代码当[**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/)属性设置为**true**时的控制台输出。

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

上述示例代码当[**DeleteOptions.update_reference**](https://reference.aspose.com/cells/python-net/aspose.cells/deleteoptions/update_reference/)属性设置为**false**时的控制台输出。您可以看到，第二个工作表中单元格E3的公式没有得到更新，它的单元格值现在是0而不是4，这是无效的。

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
