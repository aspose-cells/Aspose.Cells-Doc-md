---
title: 保存为HTML时禁用Downlevel Revealed Comments
type: docs
weight: 20
url: /zh/net/disable-downlevel-revealed-comments-while-saving-to/
---

## **可能的使用场景**

当您将Excel文件保存为HTML时，Aspose.Cells会显示Downlevel Conditional Comments。 这些条件注释主要与较旧版本的Internet Explorer相关，并与现代Web浏览器无关。 您可以在以下链接详细了解它们。

- [条件注释 - Downlevel-revealed conditional comment](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

通过将[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments)属性设置为**true**，Aspose.Cells允许您消除这些Downlevel Revealed Comments。

## **在保存为HTML时禁用Downlevel Revealed Comments**

以下示例代码演示了[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments)属性的用法。截图显示了当未设置为**true**时该属性的效果。请下载此代码中使用的[示例Excel文件](50528257.xlsx)和生成的[输出HTML](50528258.zip)进行参考。

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.cs" >}}
