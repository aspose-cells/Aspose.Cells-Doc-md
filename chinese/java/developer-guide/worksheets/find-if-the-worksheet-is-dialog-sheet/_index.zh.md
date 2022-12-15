---
title: 查找工作表是否为对话框表
type: docs
weight: 100
url: /zh/java/find-if-the-worksheet-is-dialog-sheet/
---
## **可能的使用场景**

对话框工作表是一种包含对话框的工作表的旧格式。这样的工作表可以由旧版本的 Microsoft Excel（例如 2003）插入，如屏幕截图所示。它也可以在较新版本中使用 VBA 插入，例如 Microsoft Excel 2016。

![待办事项：图像_替代_文本](find-if-the-worksheet-is-dialog-sheet_1.png)

您可以找到工作表是对话框工作表还是其他类型的工作表[**工作表.类型**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type)Aspose.Cells提供的属性，如果返回枚举值[**工作表类型.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG)，那么这意味着，你正在处理一个对话框表。

## **查找工作表是否为对话框表**

下面的示例代码加载[示例 Excel 文件](64716841.xlsx)包含一个对话框表。它检查[**工作表.类型**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type)财产将其与[**工作表类型.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG)然后打印消息。请查看下面给出的示例代码的控制台输出以获得更多帮助。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-FindIfWorksheetIsDialogSheet.java" >}}

## **控制台输出**

{{< highlight "java" >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
