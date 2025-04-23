---
title: 从单元格获取HTML5字符串
type: docs
weight: 90
url: /zh/java/get-html5-string-from-cell/
---

## **可能的使用场景**

Aspose.Cells使用[**getHtmlString(boolean html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString)方法返回单元格的HTML字符串。如果您将false作为参数传递，它将返回普通HTML，但如果您将true作为参数传递，它将返回HTML5字符串。

## **从单元格获取HTML5字符串**

以下示例代码创建一个工作簿对象，并在第一个工作表的A1单元格中添加一些文本。然后使用[**getHtmlString(boolean html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString)方法从A1单元格获取普通HTML和HTML5字符串，并将它们打印在控制台上。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-GetHTML5StringFromCell.java" >}}

## **控制台输出**

{{< highlight java >}}

Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
