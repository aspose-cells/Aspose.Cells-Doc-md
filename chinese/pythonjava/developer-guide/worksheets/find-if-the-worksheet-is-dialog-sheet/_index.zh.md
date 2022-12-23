---
title: 查找工作表是否为对话框表
type: docs
weight: 70
url: /zh/python-java/find-if-the-worksheet-is-dialog-sheet/
---
## **可能的使用场景**
对话框工作表是一种包含对话框的工作表的旧格式。这样的工作表可以由旧版本的 Microsoft Excel（例如 2003）插入，如屏幕截图所示。它也可以在较新版本中使用 VBA 插入，例如 Microsoft Excel 2016。

![待办事项：图片_替代_文本](DialogSheet.png)
## **查找工作表是否为对话框表**
Aspose.Cells for Python via Java 使您能够检查工作表是否为对话框表。为此，它提供了[工作表.类型](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type)财产。如果[工作表.类型](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type)返回枚举值[工作表类型.DIALOG](https://reference.aspose.com/cells/python/asposecells.api/sheettype#DIALOG)，那么这意味着，你正在处理一个对话框表。

以下代码片段显示了如何检查对话框表。代码生成的控制台输出如下，供参考。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}
## **控制台输出**
工作表是一个对话框表。
