---
title: 在保存为HTML时禁用旧版条件注释的显示
type: docs
weight: 20
url: /zh/java/disable-downlevel-revealed-comments-while-saving-to-html/
---

## **可能的使用场景**

当将Excel文件保存为HTML时，Aspose.Cells会显示Downlevel Conditional Comments。这些条件注释大多与旧版本的Internet Explorer相关，并与现代Web浏览器无关。您可以在以下链接中详细了解它们。

- [条件注释 - Downlevel-revealed conditional comment](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells允许您通过将[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments)属性设置为**true**来消除这些Downlevel Revealed Comments。

## **在保存为HTML时禁用下级可见的批注**

以下示例代码显示了[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments)属性的用法。当其未设置为**true**时，截图显示了此属性的效果。请下载此代码中使用的[sample Excel file](50528267.xlsx)和由其生成的[output HTML](50528266.zip)文件以供参考。

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.java" >}}
