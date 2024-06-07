---
title: 保存为HTML时禁用Downlevel Revealed Comments
type: docs
weight: 20
url: /zh/java/disable-downlevel-revealed-comments-while-saving-to-html/
---

## **可能的使用场景**

当您将Excel文件保存为HTML时，Aspose.Cells会显示Downlevel Conditional Comments。这些条件注释大多与旧版本的Internet Explorer有关，对现代Web浏览器无关。您可以在以下链接中详细了解它们。

- [条件注释 - Downlevel-revealed conditional comment](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells允许您通过将[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments)属性设置为**true**来消除这些Downlevel Revealed Comments。

## **在保存为HTML时禁用Downlevel Revealed Comments**

以下示例代码显示了[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments)属性的用法。当未将此属性设置为**true**时，截图显示了此属性的效果。请下载在此代码中使用的[示例Excel文件](50528267.xlsx)和生成的[输出HTML](50528266.zip)文件以供参考。

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.java" >}}
