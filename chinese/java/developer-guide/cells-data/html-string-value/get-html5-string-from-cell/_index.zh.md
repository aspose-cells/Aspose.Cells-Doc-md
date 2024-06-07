---
title: 从单元格获取 HTML5 字符串
type: docs
weight: 90
url: /zh/java/get-html5-string-from-cell/
---

## **可能的使用场景**

Aspose.Cells使用[**getHtmlString(boolean html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString)方法返回单元格的HTML字符串。 如果将**false**作为参数传递，它将返回普通的HTML，但如果将**true**作为参数传递，它将返回HTML5字符串。

## **从单元格获取 HTML5 字符串**

以下示例代码创建一个工作簿对象，并将一些文本添加到第一个工作表的单元格A1中。 然后使用[**getHtmlString(boolean html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString)方法从单元格A1获取普通的HTML和HTML5字符串，并在控制台上打印它们。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-GetHTML5StringFromCell.java" >}}

## **控制台输出**

{{< highlight java >}}

Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
