---
title: Disable CSS while saving to HTML with Golang via C++
linktitle: Disable CSS while saving to HTML
type: docs
weight: 320
url: /go-cpp/disable-css-while-saving-to-html/
description: Learn how to disable CSS while saving Excel files to HTML using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**

When you save your Excel file to a single‑page HTML, usually the CSS elements will be embedded within the HTML file and will be located in the HEAD section. If you attach this file as the content/body of an email, the CSS elements will be stripped out by most email clients, resulting in improper rendering. The 24.12 version of Aspose.Cells introduces an option that allows you to optionally disable CSS, letting styles be applied directly within the HTML elements themselves. If you want to set the HTML as the content/body of the email, please use the [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisablecss/) property and set it to **true**.

## **Disable CSS while saving to HTML**

The following sample code shows how to use the [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisablecss/) property.

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableCssWhileSavingToHtml.go" >}}