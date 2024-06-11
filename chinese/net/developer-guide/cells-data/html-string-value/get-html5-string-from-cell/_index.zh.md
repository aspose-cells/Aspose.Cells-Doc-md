---
title: 从单元格获取HTML5字符串
type: docs
weight: 90
url: /zh/net/get-html5-string-from-cell/
description: 使用Aspose.Cells for .NET API学习如何从单元格获取HTML5字符串。
keywords: 从单元格获取 HTML5 字符串，从单元格获取 HTML5 字符串，管理单元的 HTML5 字符串
---

## **可能的使用场景**

Aspose.Cells返回单元格的HTML字符串，使用[**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring)方法接受一个布尔型参数。如果你传递**false**作为参数，它将返回标准的HTML，但如果你传递**true**作为参数，它将返回HTML5字符串。

## **从单元格获取HTML5字符串**

以下示例代码创建一个工作簿对象，并在第一个工作表的A1单元格中添加一些文本。然后使用[**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring)方法从A1单元格获取普通的HTML和HTML5字符串，并将它们打印在控制台上。

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

## **控制台输出**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
