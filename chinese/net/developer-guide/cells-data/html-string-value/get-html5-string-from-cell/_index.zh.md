---
title: 从 Cell 获取 HTML5 字符串
type: docs
weight: 90
url: /zh/net/get-html5-string-from-cell/
---
## **可能的使用场景**

Aspose.Cells 返回单元格的 HTML 字符串[**获取HTML字符串**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring)接受布尔参数的方法。如果你通过**错误的**作为参数，它将返回普通 HTML，但如果您通过**真的**作为参数，它将返回 HTML5 字符串。

## **从 Cell 获取 HTML5 字符串**

下面的示例代码创建一个工作簿对象并在第一个工作表的单元格 A1 中添加一些文本。然后它使用[**获取HTML字符串**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring)方法并将它们打印在控制台上。

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

## **控制台输出**

{{< highlight "java" >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
