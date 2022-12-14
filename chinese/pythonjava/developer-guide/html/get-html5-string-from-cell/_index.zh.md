---
title: 从 Cell 获取 HTML5 字符串
type: docs
weight: 40
url: /zh/python-java/get-html5-string-from-cell/
---
## **从 Cell 获取 HTML5 字符串**
通过 Java 将 Aspose.Cells 用于 Python，您可以从单元格中获取 HTML 字符串。这可以通过使用[getHtmlString（布尔值 html5）](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)API提供的方法。如果你通过**错误的**作为参数，它会返回给你普通的 HTML 但如果你通过**真的**作为参数，它将返回 HTML5 字符串。

下面的示例代码创建一个工作簿对象并在第一个工作表的单元格 A1 中添加一些文本。然后它使用[getHtmlString（布尔值 html5）](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)方法并打印它们。
## **示例代码**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-GetHTML5StringFromCell.py" >}}

以下是上面提供的代码片段生成的输出。
## **输出**
{{< highlight "java" >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
