---
title: 使用 Golang 通过 C++ 在保存为 HTML 时禁用 CSS
linktitle: 禁用CSS在保存为HTML时
type: docs
weight: 320
url: /zh/go-cpp/disable-css-while-saving-to-html/
description: 了解如何在使用Aspose.Cells for C++将Excel文件保存为HTML时禁用CSS。
---

## **可能的使用场景**

 当你将Excel文件保存为单页HTML时，CSS元素通常会嵌入到HTML文件中，并位于HEAD部分。如果将此文件作为内容/正文附加到电子邮件中，大多数电子邮件客户端会删除这些CSS元素，导致渲染不正确。Aspose.Cells的24.12版本引入了一个选项，允许你选择性禁用CSS，从而使样式直接应用于HTML元素本身。如果你希望将HTML用作电子邮件的内容/正文，请使用[**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisablecss/)属性并设置为**true**。

## ** 禁用CSS在保存为HTML时**

 下面的示例代码展示了[**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisablecss/)属性的用法。

## **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableCssWhileSavingToHtml.go" >}}
