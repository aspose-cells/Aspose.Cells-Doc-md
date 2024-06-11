---
title: 从单元格获取HTML5字符串
type: docs
weight: 90
url: /zh/python-net/get-html5-string-from-cell/
description: 通过Aspose.Cells for Python via .NET API了解如何从单元格获取HTML5字符串。
keywords: Python Excel库，Python从单元格获取HTML5字符串，使用Python获取单元格的HTML5字符串，使用Python管理单元格的HTML5字符串。
---

## **可能的使用场景**

Aspose.Cells for Python via .NET使用[**get_html_string(html5)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_html_string/#bool)方法返回单元格的HTML字符串，该方法接受一个布尔参数。如果将**false**作为参数传递，它将返回普通的HTML，但如果将**true**作为参数传递，它将返回HTML5字符串。

## **从单元格获取HTML5字符串**

以下示例代码创建一个工作簿对象，并在第一个工作表的A1单元格中添加一些文本。然后使用[**get_html_string(html5)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_html_string/#bool)方法从A1单元格获取普通的HTML和HTML5字符串，并将它们打印在控制台上。

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-HtmlStringValue-GetHTML5StringFromCell.py" >}}

## **控制台输出**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
