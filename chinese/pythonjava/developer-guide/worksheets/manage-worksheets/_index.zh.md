---
title: 管理工作表
type: docs
weight: 10
url: /zh/python-java/manage-worksheets/
---
通过 Java 为 Python 使用 Aspose.Cells 管理工作表非常容易。在本文中，我们将演示使用 Aspose.Cells API 添加、访问和删除工作表。
## **将工作表添加到新的 Excel 文件**
要创建一个新的工作簿，请创建一个对象[工作簿](https://reference.aspose.com/cells/python/asposecells.api/Workbook)班级。这[工作簿](https://reference.aspose.com/cells/python/asposecells.api/Workbook)类代表一个 Excel 文件。然后通过使用[添加](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#add\(\) 的方法[工作表集合](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection) 新工作表被添加到 Excel 文件中。最后，要保存新创建的 Excel 文件，请调用[节省](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String\) 的方法[工作簿](https://reference.aspose.com/cells/python/asposecells.api/Workbook)班级。

以下代码片段演示了如何创建一个新的 Excel 文件并向其中添加一个工作表。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToNewExcelFile.py" >}}
## **将工作表添加到 Designer 电子表格**
将工作表添加到设计器电子表格与将工作表添加到新的 Excel 文件完全相同。唯一的区别是，我们不是创建一个新的 Excel 文件，而是通过[工作簿](https://reference.aspose.com/cells/python/asposecells.api/Workbook)班级。

以下代码片段演示了将工作表添加到设计器电子表格中。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToDesignerSpreadsheet.py" >}}
## **使用工作表名称访问工作表**
加载工作簿后，开发人员可以使用其索引或名称访问任何工作表。以下代码片段演示了使用工作表名称访问工作表。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AccessingWorksheetsUsingSheetName.py" >}}
## **删除工作表**
有时可能会遇到要从工作簿中删除某些工作表的情况。为此，API 提供了[工作表集合.removeAt](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#removeAt\(int\)） 方法。您可以将要删除的工作表的工作表索引或工作表名称传递给它。以下示例演示如何使用工作表索引和工作表名称删除工作表。
### **使用工作表索引删除工作表**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetIndex.py" >}}
### **使用工作表名称删除工作表**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetName.py" >}}
