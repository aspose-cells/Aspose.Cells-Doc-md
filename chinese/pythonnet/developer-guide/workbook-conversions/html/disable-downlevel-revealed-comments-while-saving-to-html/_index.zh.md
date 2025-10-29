---
title: 在保存为HTML时禁用旧版条件注释的显示
type: docs
weight: 20
url: /zh/python-net/disable-downlevel-revealed-comments-while-saving-to/
---

## **可能的使用场景**

当你将Excel文件保存为HTML时，Aspose.Cells for Python via .NET 会显示向下兼容条件注释。这些条件注释主要与较旧版本的Internet Explorer相关，与现代浏览器无关。你可以在以下链接中详细了解它们。

- [条件注释 - Downlevel-revealed conditional comment](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells for Python via .NET 允许你通过设置 [**HtmlSaveOptions.disable_downlevel_revealed_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_downlevel_revealed_comments) 属性为 **true** 来消除这些向下兼容的揭示性注释。

## **在保存为HTML时禁用下级可见的批注**

以下示例代码展示了[**HtmlSaveOptions.disable_downlevel_revealed_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_downlevel_revealed_comments)属性的用法。截图显示了在未将其设置为true时此属性的效果。请下载本代码中使用的[示例Excel文件](50528257.xlsx)以及它生成的[输出HTML](50528258.zip)作为参考。

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
{{< app/cells/assistant language="python-net" >}}
