---
title: 查找工作表是否为对话框工作表
type: docs
weight: 90
url: /zh/net/find-if-the-worksheet-is-dialog-sheet/
description: 对话工作表是工作表的旧格式。本文提供了利用C# API或.NET库来确定Excel工作表是否为对话工作表的指令和示例代码。
keywords: 查找Excel工作表对话类型C#，工作表对话C#
---

## **可能的使用场景**

对话工作表是一种包含对话框的工作表的旧格式。这样的工作表可能是由Microsoft Excel的旧版本（如2003）插入的，就像这张截图中所显示的一样。它也可以在较新版本的Microsoft Excel（如2016）中使用VBA插入。

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

您可以使用Aspose.Cells提供的[**Worksheet.Type**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)属性来查找工作表是否是对话框工作表或其他类型的工作表。如果它返回枚举值[**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype)，那么表示您正在处理对话框工作表。

## **查找工作表是否为对话框工作表**

以下示例代码加载包含对话框工作表的[示例Excel文件](64716820.xlsx)。它检查[**Worksheet.Type**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)属性并将其与[**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype)进行比较，然后打印消息。请参阅下面给出的示例代码的控制台输出以获取更多帮助。

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-FindIfWorksheetIsDialogSheet.cs" >}}

## **控制台输出**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
