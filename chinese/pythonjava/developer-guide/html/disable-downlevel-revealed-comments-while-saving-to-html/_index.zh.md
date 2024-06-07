---
title: 保存为HTML时禁用Downlevel Revealed Comments
type: docs
weight: 20
url: /zh/python-java/disable-downlevel-revealed-comments-while-saving-to/
---

## **在保存为HTML时禁用Downlevel Revealed Comments**
当将Excel文件转换为HTML时，Aspose.Cells会在输出的HTML文件中添加Downlevel-revealed条件注释。这些条件注释主要与旧版本的Internet Explorer相关，在现代浏览器中是无关紧要的。有关Downlevel-revealed条件注释的更多信息，请访问以下链接

[条件注释 - Downlevel-revealed条件注释](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

要删除Downlevel-revealed条件注释，Aspose.Cells提供了[HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments)属性。将[HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments)属性设置为**True**将在输出的HTML文件中删除Downlevel-revealed条件注释。

以下图片显示了将在输出的HTML文件中删除的Downlevel-revealed条件注释

![todo:image_alt_text](Disable-Downlevel-Revealed-Comments.png)
## **示例代码**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
