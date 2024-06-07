---
title: 查找工作表是否为对话框工作表
type: docs
weight: 90
url: /zh/net/find-if-the-worksheet-is-dialog-sheet/
description: 对话框工作表是表的旧格式。本文提供了使用C# API或.NET库来确定Excel工作表是否为对话框工作表的指令和示例代码。
keywords: 查找Excel工作表对话框类型C#，工作表对话框C#
---

## **可能的使用场景**

对话框工作表是表的旧格式，其中包含对话框框。例如，由较旧版本的Microsoft Excel（如2003）插入的此表如下图所示。它还可以在更新版本（如Microsoft Excel 2016）中使用VBA插入。

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

您可以使用Aspose.Cells提供的[**Worksheet.Type**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)属性找出表是对话框表还是其他类型的表。如果它返回枚举值[**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype)，则表示您正在处理对话框表。

## **查找工作表是否为对话框工作表**

以下示例代码加载了包含对话框工作表的示例Excel文件。它检查[**Worksheet.Type**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)属性并将其与[**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype)进行比较，然后输出消息。有关更多帮助，请参阅给出的示例代码的控制台输出。

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-FindIfWorksheetIsDialogSheet.cs" >}}

## **控制台输出**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
