---
title: 从单元格获取 HTML5 字符串
type: docs
weight: 90
url: /zh/net/get-html5-string-from-cell/
description: 学习如何通过 Aspose.Cells for .NET API 从单元格获取 HTML5 字符串。
keywords: 从单元格获取 HTML5 字符串，获取单元格的 HTML5 字符串，管理单元格的 HTML5 字符串
---

## **可能的使用场景**

Aspose.Cells 使用 [**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) 方法返回单元格的 HTML 字符串，该方法接受一个布尔参数。如果将 **false** 作为参数传递，它将返回正常的 HTML，但如果将 **true** 作为参数传递，将返回 HTML5 字符串。

## **从单元格获取 HTML5 字符串**

以下示例代码创建一个工作簿对象，并在第一个工作表的 A1 单元格中添加一些文本。然后，使用 [**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) 方法从 A1 单元格获取正常 HTML 和 HTML5 字符串，并将它们打印在控制台上。

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

## **控制台输出**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
