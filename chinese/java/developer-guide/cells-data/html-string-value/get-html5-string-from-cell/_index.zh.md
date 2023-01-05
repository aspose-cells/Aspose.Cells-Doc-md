---
title: 从 Cell 获取 HTML5 字符串
type: docs
weight: 90
url: /zh/java/get-html5-string-from-cell/
---
## **可能的使用场景**

Aspose.Cells 返回单元格的 HTML 字符串[**getHtmlString（布尔值 html5）**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString)方法。如果你通过**错误的**作为参数，它将返回 Normal HTML 但如果你通过**真的**作为参数，它将返回 HTML5 字符串。

## **从 Cell 获取 HTML5 字符串**

下面的示例代码创建一个工作簿对象并在第一个工作表的单元格 A1 中添加一些文本。然后它使用[**getHtmlString（布尔值 html5）**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString)方法并将它们打印在控制台上。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-GetHTML5StringFromCell.java" >}}

## **控制台输出**

{{< highlight "java" >}}

Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
