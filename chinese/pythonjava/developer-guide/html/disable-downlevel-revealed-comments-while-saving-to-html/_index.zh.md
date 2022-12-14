---
title: 保存为 HTML 时禁用下层显示评论
type: docs
weight: 20
url: /zh/python-java/disable-downlevel-revealed-comments-while-saving-to/
---
## **保存为 HTML 时禁用下层显示评论**
当 Excel 文件转换为 HTML 时，Aspose.Cells 在输出的 HTML 文件中添加 Downlevel-revealed 条件注释。这些条件注释主要与旧版本的 Internet Explorer 有关，与现代浏览器无关。有关 Downlevel-revealed 条件注释的更多信息，请访问以下链接

[条件注释 - 下层显示的条件注释](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

要删除 Downlevel-revealed 条件注释，Aspose.Cells 提供了[HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments)财产。设定[HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments)财产给**真的**将删除输出 HTML 文件中的 Downlevel-revealed 条件注释。

下图显示了将在输出 HTML 文件中删除的 Downlevel-revealed 条件注释

![待办事项：图片_替代_文本](Disable-Downlevel-Revealed-Comments.png)
## **示例代码**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
