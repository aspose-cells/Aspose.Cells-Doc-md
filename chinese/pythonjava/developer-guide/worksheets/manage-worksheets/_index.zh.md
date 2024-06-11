---
title: 管理工作表
type: docs
weight: 10
url: /zh/python-java/manage-worksheets/
---

使用Aspose.Cells for Python via Java管理工作表非常容易。在本文中，我们将演示如何使用Aspose.Cells API添加、访问和删除工作表。
## **向新的Excel文件添加工作表**
要创建新的工作簿，请创建[Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook)类的对象。Workbook类表示一个Excel文件。然后，通过[WorksheetCollection](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection)的add方法向Excel文件添加新工作表。最后，调用[Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook)类的save方法保存新创建的Excel文件。

以下代码段演示了如何创建一个新的Excel文件并向其中添加一个工作表。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToNewExcelFile.py" >}}
## **向设计电子表格添加工作表**
向设计师电子表格添加工作表与向新的Excel文件添加工作表完全相同。唯一的区别是，不是创建新的Excel文件，而是通过[Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook)类打开现有文件。

以下代码段演示了向设计师电子表格添加工作表。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToDesignerSpreadsheet.py" >}}
## **使用工作表名称访问工作表**
加载工作簿后，开发人员可以通过其索引或名称访问任何工作表。以下代码片段演示了如何使用工作表名称访问工作表。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AccessingWorksheetsUsingSheetName.py" >}}
## **移除工作表**
有时需要从工作簿中移除一些工作表。为此，API提供了[WorksheetCollection.removeAt](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#removeAt\(int\))方法。您可以传递工作表索引或工作表名称来移除工作表。以下示例演示了如何使用工作表索引和工作表名称来移除工作表。
### **使用工作表索引移除工作表**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetIndex.py" >}}
### **使用工作表名称移除工作表**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetName.py" >}}
