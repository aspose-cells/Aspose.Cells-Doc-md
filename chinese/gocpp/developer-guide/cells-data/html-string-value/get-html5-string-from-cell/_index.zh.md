---
title: 用Golang via C++从单元格获取HTML5字符串
linktitle: 从单元格获取HTML5字符串
type: docs
weight: 90
url: /zh/go-cpp/get-html5-string-from-cell/
description: 通过Aspose.Cells for C++ API学习如何从单元格获取HTML5字符串。
keywords: 从单元格获取 HTML5 字符串，从单元格获取 HTML5 字符串，管理单元的 HTML5 字符串
---

## **可能的使用场景**

 Aspose.Cells使用接受布尔参数的[**GetHtmlString**](https://reference.aspose.com/cells/go-cpp/cell/gethtmlstring/)方法返回单元格的HTML字符串。传入**false**作为参数，将返回普通HTML；传入**true**，将返回HTML5字符串。

## ** 从单元格获取HTML5字符串**

以下示例代码创建一个工作簿对象，并在第一个工作表的A1单元格中添加一些文本。然后使用[**GetHtmlString**](https://reference.aspose.com/cells/go-cpp/cell/gethtmlstring/)方法从A1单元格获取普通的HTML和HTML5字符串，并将它们打印在控制台上。

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetHtml5StringFromCell.go" >}}
## **控制台输出**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
