---
title: 删除工作表中的空白列和行时更新其他工作表中的引用
type: docs
weight: 700
url: /zh/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---

{{% alert color="primary" %}} 

当在工作表中删除空白列和行时，其他工作表中对它们的引用也会变得无效。如果要避免此行为，并希望在更新这些引用时使其保持有效，请使用[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) 并将其设置为 **true**。

{{% /alert %}} 
## **在删除工作表中的空白列和行时更新其他工作表中的引用**
请查看以下示例代码及其控制台输出。第二个工作表中的单元格E3具有一个公式=Sheet1!C3，该公式参照第一个工作表中的单元格C3。如果您将[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference)属性设置为**true**，此公式将会更新，并变为在第一个工作表中删除空白列和行时=Sheet1!A1。但是，如果您将[DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference)属性设置为**false**，第二个工作表中的单元格E3中的公式将保持=Sheet1!C3并变为无效。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-Updatereferencesinotherworksheetswhiledeletingblankcolumnsandrowsinworksheet-1.java" >}}
## **控制台输出**
这是上述示例代码的控制台输出，当 [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) 属性被设置为 **true** 时。

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

这是上述示例代码的控制台输出，当 [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) 属性被设置为 **false** 时。您可以看到，第二个工作表中单元格E3的公式没有被更新，现在其单元格值为0，而不是无效的4。

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
