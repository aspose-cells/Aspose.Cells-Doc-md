---
title: 查找工作表是否为对话框工作表
type: docs
weight: 100
url: /zh/java/find-if-the-worksheet-is-dialog-sheet/
---

## **可能的使用场景**

对话框工作表是一个包含对话框的旧格式工作表。如屏幕截图所示，这种表格可以由较旧版本的Microsoft Excel（例如2003）插入。也可以在较新版本中通过VBA插入，例如Microsoft Excel 2016。

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

您可以使用Aspose.Cells提供的[**Worksheet.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type)属性来查看工作表是否是对话框工作表或其他类型的工作表。如果它返回枚举值[**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG)，那么表示您正在处理对话框工作表。

## **查找工作表是否为对话框工作表**

以下示例代码加载包含对话框工作表的[示例Excel文件](64716841.xlsx)。它检查[**Worksheet.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type)属性，将其与[**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG)进行比较，然后打印消息。有关更多帮助，请参阅下面给出的示例代码的控制台输出。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-FindIfWorksheetIsDialogSheet.java" >}}

## **控制台输出**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
