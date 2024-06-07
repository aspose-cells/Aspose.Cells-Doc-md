---
title: 查找工作表是否为对话框工作表
type: docs
weight: 70
url: /zh/python-java/find-if-the-worksheet-is-dialog-sheet/
---

## **可能的使用场景**
对话框工作表是一个包含对话框的旧格式工作表。如屏幕截图所示，这种表格可以由较旧版本的Microsoft Excel（例如2003）插入。也可以在较新版本中通过VBA插入，例如Microsoft Excel 2016。

![todo:image_alt_text](DialogSheet.png)
## **查找工作表是否为对话框工作表**
Aspose.Cells for Python via Java提供了检查工作表是否为对话框工作表的能力。为此，它提供了[Worksheet.Type](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type)属性。如果[Worksheet.Type](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type)返回枚举值[SheetType.DIALOG](https://reference.aspose.com/cells/python/asposecells.api/sheettype#DIALOG)，则表示您正在处理对话框工作表。

以下代码片段显示如何检查对话框工作表。代码生成的控制台输出如下供参考。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}
## **控制台输出**
工作表是对话框工作表。
