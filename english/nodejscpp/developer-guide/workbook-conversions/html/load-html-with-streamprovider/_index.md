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
                });
                response.on('end', () => {
                    return Buffer.concat(dstStream);
                });
            });
            request.on('error', (err) => {
                // ignored
            });
            return null; // Placeholder; needs proper async handling
        } catch {
            return null;
        }
    }

    initStream(options) {
        let absolutePath = null;
        switch (options.defaultPath) {
            case "/Files/Image1.png":
                absolutePath = path.join("D:/filetemp/G1.png");
                break;
            case "/Files/Image2.png":
                absolutePath = path.join("D:/filetemp/E1.png");
                break;
            case "https://www.aspose.com/templates/aspose/img/products/cells/aspose_cells-for-net.svg":
                absolutePath = path.join("D:/filetemp/F1.png");
                break;
            default:
                break;
        }
        if (absolutePath === null) {
            if (HtmlAttachedStreamProvider.isHRef(options.defaultPath)) {
                options.stream = HtmlAttachedStreamProvider.getStreamFromHref(options.defaultPath);
            } else if (fs.existsSync(options.defaultPath)) {
                options.stream = fs.createReadStream(options.defaultPath);
            }
            return;
        }
        options.stream = fs.createReadStream(absolutePath);
    }

    closeStream(options) {
        if (options.stream != null) {
            options.stream.close();
        }
    }
}

async function main() {
    const attachedStreamProvider = new HtmlAttachedStreamProvider();
    const options = new AsposeCells.HtmlLoadOptions();
    options.streamProvider = attachedStreamProvider;
    const workbook = new AsposeCells.Workbook("html1.html", options);
    await workbook.saveAsync("dest.xlsx");
}

main().catch(console.error);
```
