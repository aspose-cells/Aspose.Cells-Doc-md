---
title: 从单元格获取 HTML5 字符串
type: docs
weight: 40
url: /zh/python-java/get-html5-string-from-cell/
---

## **从单元格获取 HTML5 字符串**
使用Aspose.Cells for Python通过Java，您可以通过API提供的[getHtmlString(boolean html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\))方法从单元格获取HTML字符串。如果将**false**作为参数传递，则会返回普通HTML，如果将**true**作为参数传递，则会返回HTML5字符串。

以下示例代码创建一个工作簿对象，并向第一个工作表的A1单元格添加一些文本。然后，使用[getHtmlString(boolean html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\))方法从A1单元格中获取普通HTML和HTML5字符串，并打印它们。
## **示例代码**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-GetHTML5StringFromCell.py" >}}

以上提供的代码片段生成的输出如下。
## **输出**
{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
