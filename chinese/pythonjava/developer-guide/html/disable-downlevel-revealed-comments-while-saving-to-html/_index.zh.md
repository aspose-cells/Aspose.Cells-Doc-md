---
title: 在保存为HTML时禁用旧版条件注释的显示
type: docs
weight: 20
url: /zh/python-java/disable-downlevel-revealed-comments-while-saving-to/
---

## **在保存为HTML时禁用下级可见的批注**
当将Excel文件转换为HTML时，Aspose.Cells会在输出HTML文件中添加Downlevel-revealed条件注释。这些条件注释大多与旧版本的Internet Explorer有关，在现代浏览器中不相关。有关Downlevel-revealed条件注释的更多信息，请访问以下链接

[条件注释 - Downlevel-revealed条件注释](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

为了删除Downlevel-revealed条件注释，Aspose.Cells提供了HtmlSaveOptions.DisableDownlevelRevealedComments属性。将HtmlSaveOptions.DisableDownlevelRevealedComments属性设置为True将会删除输出HTML文件中的Downlevel-revealed条件注释。

以下图片显示了将在输出HTML文件中删除的Downlevel-revealed条件注释

![todo:image_alt_text](Disable-Downlevel-Revealed-Comments.png)
## **示例代码**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
