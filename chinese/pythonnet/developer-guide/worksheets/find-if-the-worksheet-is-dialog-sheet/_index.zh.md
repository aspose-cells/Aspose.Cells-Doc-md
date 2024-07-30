---
title: 查找工作表是否为对话框工作表
type: docs
weight: 90
url: /zh/python-net/find-if-the-worksheet-is-dialog-sheet/
description: 对话表是一种旧的表格格式。本文提供了使用Aspose.Cells for Python via .NET库编程确定Excel工作表是否为对话表的说明和示例代码。
keywords: Python Excel库，Python查找Excel工作表对话框类型，在Python中查找工作表对话框。
---

## **可能的使用场景**

对话工作表是一种包含对话框的工作表的旧格式。这样的工作表可能是由Microsoft Excel的旧版本（如2003）插入的，就像这张截图中所显示的一样。它也可以在较新版本的Microsoft Excel（如2016）中使用VBA插入。

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

您可以使用Aspose.Cells for Python via .NET提供的[**Worksheet.type**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/type/)属性来查看工作表是否是对话表或其他类型的表。如果返回枚举值[**SheetType.DIALOG**](https://reference.aspose.com/cells/python-net/aspose.cells/sheettype/)，那么表示您正在处理对话表。

## **查找工作表是否为对话框工作表**

以下示例代码加载包含对话框工作表的[示例Excel文件](64716820.xlsx)。它检查[**Worksheet.type**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/type/)属性并将其与[**SheetType.DIALOG**](https://reference.aspose.com/cells/python-net/aspose.cells/sheettype/)进行比较，然后打印消息。请参阅下面给出的示例代码的控制台输出以获取更多帮助。

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}

## **控制台输出**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
