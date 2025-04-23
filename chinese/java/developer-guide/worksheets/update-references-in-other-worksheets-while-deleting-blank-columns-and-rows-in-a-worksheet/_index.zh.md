---
title: 删除工作表中的空白列和行时更新其他工作表中的引用
type: docs
weight: 700
url: /zh/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---

{{% alert color="primary" %}} 

当您删除工作表中的空白列和行时，其在其他工作表中的引用会变得无效。如果您希望避免此行为，并且希望这些引用也被更新，请使用 [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) 并将其设置为 **true**。

{{% /alert %}} 
## **删除工作表中的空白列和行时更新其他工作表中的引用**
请参阅以下示例代码及其控制台输出。第二个工作表中的单元格 E3 具有一个公式 =Sheet1!C3，它引用了第一个工作表中的单元格 C3。如果您将 [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) 属性设置为 **true**，此公式将会被更新为 =Sheet1!A1，当删除第一个工作表中的空白列和行时。然而，如果您将 [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) 属性设置为 **false**，第二个工作表中单元格 E3 的公式将保持为 =Sheet1!C3 并变为无效。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-Updatereferencesinotherworksheetswhiledeletingblankcolumnsandrowsinworksheet-1.java" >}}
## **控制台输出**
这是以上示例代码的控制台输出，当 [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) 属性被设置为 **true** 时。

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

这是以上示例代码的控制台输出，当 [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) 属性被设置为 **false** 时。如您所见，第二个工作表中单元格 E3 的公式没有被更新，其单元格值现在为 0 而非无效。

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
{{< app/cells/assistant language="java" >}}
