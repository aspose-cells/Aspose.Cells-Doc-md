---
title: 从单元格获取HTML5字符串
type: docs
weight: 90
url: /zh/nodejs-cpp/get-html5-string-from-cell/
description: 了解如何通过Aspose.Cells for Node.js via C++ API从单元格获取HTML5字符串。
keywords: 通过C++从Node.js获取单元格的HTML5字符串，利用C++从Node.js获取单元格的HTML5字符串，管理Node.js中的单元格HTML5字符串（通过C++）
---

## **可能的使用场景**

Aspose.Cells 使用 [**Cell.getHtmlString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getHtmlString-boolean-) 方法返回单元格的HTML字符串，该方法接受一个布尔参数。如果传递 **false**，将返回普通HTML；如果传递 **true**，将返回HTML5字符串。

## **从单元格获取HTML5字符串**

以下示例代码创建一个工作簿对象，并在第一个工作表的A1单元格中添加一些文本。然后，它通过 [**Cell.getHtmlString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getHtmlString-boolean-) 方法获取A1单元格的普通HTML和HTML5字符串，并在控制台打印它们。

## **示例代码**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-HtmlStringValue-GetHtml5String.js" >}}


## **控制台输出**

{{< highlight javascript >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
