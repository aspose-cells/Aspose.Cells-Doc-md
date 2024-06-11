---
title: 在保存为HTML时禁用旧版条件注释的显示
type: docs
weight: 20
url: /zh/net/disable-downlevel-revealed-comments-while-saving-to/
---

## **可能的使用场景**

当将Excel文件保存为HTML时，Aspose.Cells会显示下级条件注释。这些条件注释大多与较旧版本的Internet Explorer相关，与现代Web浏览器无关。您可以在以下链接详细了解它们。

- [条件注释 - Downlevel-revealed conditional comment](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells允许您通过将[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments)属性设置为**true**来消除这些下级条件注释。

## **在保存为HTML时禁用下级可见的批注**

以下示例代码展示了[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments)属性的用法。截图显示了在未将其设置为true时此属性的效果。请下载本代码中使用的[示例Excel文件](50528257.xlsx)以及它生成的[输出HTML](50528258.zip)作为参考。

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.cs" >}}
