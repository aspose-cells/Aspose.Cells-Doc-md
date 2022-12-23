---
title: GridDesktop 工作表的自定义行和自定义列标题
type: docs
weight: 120
url: /zh/net/custom-row-and-custom-column-caption-of-griddesktop-worksheet/
---
## **可能的使用场景**
您可以自定义 GridDesktop 工作表的行和列标题。通常，行从 1 开始，列从 A 开始。您可以更改此行为并为 GridDesktop 工作表的行和列使用您自己的标题。为了改变行和列的标题，请实现 ICustomRowCaption 和 ICustomColumnCaption 接口。
## **GridDesktop 工作表的自定义行和自定义列标题**
以下示例代码实现 ICustomRowCaption 和 ICustomColumnCaption 接口并更改行和列的标题。截图展示了该示例代码的执行结果，供参考。



![待办事项：图片_替代_文本](custom-row-and-custom-column-caption-of-griddesktop-worksheet_1.png)

## **示例代码**
{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples-GridDesktop-CSharp-WorkingWithRowsandColumns-Form_CustomRowAndCustomColumnCaptionOfGridDesktopWorksheet.cs" >}}
