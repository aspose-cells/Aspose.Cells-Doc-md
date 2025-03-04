---
title: Load Html to Excel with StreamProvider via Node.js and C++
linktitle: Load Html to Excel with StreamProvider
type: docs
weight: 80
url: /nodejs-cpp/convert-html-to-excel-with-streamprovider/
description: Learn how to load HTML files with external resources to Excel using a custom StreamProvider in Node.js via C++.
---

{{% alert color="primary" %}} 

When loading HTML files which contain external resources, we often face the following two issues:
1. When the HTML stream is loaded, the images and external resources referenced by the HTML file cannot be obtained through relative paths.
2. External resource paths referenced in HTML files need to be mapped.

This article explains how to implement a custom stream provider interface for setting the `HtmlLoadOptions.StreamProvider` property. By implementing this interface, you will be able to load external resources during loading HTML streams or when these external resources are relative.

{{% /alert %}} 

This is the main code showing the usage of `HtmlLoadOptions.StreamProvider` property

```javascript
const fs = require('fs');
const path = require('path');
const AsposeCells = require("aspose.cells.node");

class HtmlAttachedStreamProvider {
static isHRef(picPath) {
// This handles http://, https:// file:// and probably ftp://.
return picPath.startsWith("http://") ||
picPath.startsWith("https://") ||
picPath.startsWith("file://") ||
picPath.startsWith("ftp://");
}

static getStreamFromHref(href) {
try {
const request = require('http').get(href, (response) => {
const dstStream = [];
response.on('data', (chunk) => {
dstStream.push(chunk);
```
