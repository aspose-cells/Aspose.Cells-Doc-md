---
title: 查找工作表是否为对话框工作表
type: docs
weight: 70
url: /zh/python-java/find-if-the-worksheet-is-dialog-sheet/
---

## **可能的使用场景**
对话框工作表是包含对话框的旧格式的工作表。此类工作表可以由较旧版本的 Microsoft Excel（如2003年）插入，如下图所示。它也可以在较新版本（如 Microsoft Excel 2016）中使用 VBA 插入。

![todo:image_alt_text](DialogSheet.png)
## **查找工作表是否为对话框工作表**
Aspose.Cells for Python via Java提供了检查工作表是否为对话框工作表的功能。为此，它提供了[Worksheet.Type](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type)属性。如果[Worksheet.Type](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type)返回枚举值[SheetType.DIALOG](https://reference.aspose.com/cells/python/asposecells.api/sheettype#DIALOG)，那么意味着你正在处理对话框工作表。

以下代码段显示了如何检查对话框工作表。代码生成的控制台输出如下所示。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}
## **控制台输出**
{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
