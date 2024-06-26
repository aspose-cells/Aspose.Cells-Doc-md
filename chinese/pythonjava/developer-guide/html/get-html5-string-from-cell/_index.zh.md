---
title: 从单元格获取HTML5字符串
type: docs
weight: 40
url: /zh/python-java/get-html5-string-from-cell/
---

## **从单元格获取HTML5字符串**
使用Aspose.Cells for Python via Java，您可以从单元格获取HTML字符串。这可以通过使用API提供的[getHtmlString(boolean html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\))方法实现。如果将**false**作为参数传递，它将返回普通HTML，但如果将**true**作为参数传递，它将返回HTML5字符串。

以下示例代码创建一个工作簿对象，并在第一个工作表的单元格A1中添加一些文本。然后使用[getHtmlString(boolean html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\))方法从单元格A1获取普通HTML和HTML5字符串，并打印它们。
## **示例代码**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-GetHTML5StringFromCell.py" >}}

以下是上述代码片段生成的输出。
## **输出**
{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
