---
title: 查找工作表是否为对话框工作表
type: docs
weight: 100
url: /zh/java/find-if-the-worksheet-is-dialog-sheet/
---

## **可能的使用场景**

对话框工作表是包含对话框的旧格式的工作表。此类工作表可以由较旧版本的 Microsoft Excel（如2003年）插入，如下图所示。它也可以在较新版本（如 Microsoft Excel 2016）中使用 VBA 插入。

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

您可以使用 Aspose.Cells 提供的 [**Worksheet.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type) 属性来查找工作表是否为对话框工作表或其他类型的工作表。如果它返回枚举值 [**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG)，则表示您正在处理对话框工作表。

## **查找工作表是否为对话框工作表**

以下示例代码加载包含对话框工作表的 [示例 Excel 文件](64716841.xlsx)。它会检查 [**Worksheet.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type) 属性并将其与 [**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG) 进行比较，然后打印消息。有关更多帮助，请参阅下面给出的示例代码的控制台输出。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-FindIfWorksheetIsDialogSheet.java" >}}

## **控制台输出**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
