---
title: 用 Golang 通过 C++ 在保存为 HTML 时禁用向下显示的评论
linktitle: 禁用Downlevel Revealed Comments
type: docs
weight: 20
url: /zh/go-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: 使用 Golang 通过 C++ 结合 Aspose.Cells 在将 Excel 文件保存为 HTML 时消除向下显示的评论。
---

## **可能的使用场景**

将Excel文件保存为HTML时，Aspose.Cells显示了下层条件注释。这些条件注释主要与旧版本的Internet Explorer相关，与现代网页浏览器无关。你可以在以下链接详细了解它们。

- [条件注释 - Downlevel-revealed conditional comment](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells允许你通过将[**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisabledownlevelrevealedcomments/)属性设置为**true**来消除这些下层显示的注释。

## **在保存为HTML时禁用下级可见的批注**

以下示例代码展示了[**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisabledownlevelrevealedcomments/)属性的用法。截图显示了当未将此属性设置为true时的效果。请下载此代码中使用的[样本Excel文件](50528257.xlsx)以及它生成的[输出HTML](50528258.zip)作为参考。

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableDownlevelRevealedCommentsWhileSavingToHtml.go" >}}
