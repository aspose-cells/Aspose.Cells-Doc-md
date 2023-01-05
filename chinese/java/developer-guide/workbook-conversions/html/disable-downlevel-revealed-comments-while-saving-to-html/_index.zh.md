---
title: 保存到 HTML 时禁用下层显示评论
type: docs
weight: 20
url: /zh/java/disable-downlevel-revealed-comments-while-saving-to-html/
---
## **可能的使用场景**

当您将 Excel 文件保存到 HTML 时，Aspose.Cells 会显示下层条件注释。这些条件注释主要与旧版本的 Internet Explorer 有关，与现代 Web 浏览器无关。您可以在以下链接中详细了解它们。

- [条件注释 - 下层显示的条件注释](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells 允许您通过设置[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments)财产给**真的**.

## **保存到 HTML 时禁用下层显示评论**

以下示例代码显示了[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments)财产。屏幕截图显示了此属性未设置为时的效果**真的**.请下载[示例 Excel 文件](50528267.xlsx)用于此代码和[输出 HTML](50528266.zip)它生成的文件供参考。

![待办事项：图片_替代_文本](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.java" >}}
