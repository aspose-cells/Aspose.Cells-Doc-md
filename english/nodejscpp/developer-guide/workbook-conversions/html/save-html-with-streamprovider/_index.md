---  
title: Save Html With StreamProvider using Node.js via C++  
linktitle: Save Html With StreamProvider  
type: docs  
weight: 80  
url: /nodejs-cpp/convert-excel-to-html-with-streamprovider/  
description: Learn how to convert Excel files with images and shapes to HTML using StreamProvider in Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

When converting Excel files which contain images and shapes to HTML files, we often face the following two issues:  
1. Where should we save the images and shapes when saving an Excel file to HTML stream.  
2. Replace the default path with the expected path.  

This article explains how to implement [IStreamProvider](https://reference.aspose.com/cells/nodejs-cpp/istreamprovider) interface for setting the [HtmlSaveOptions.streamProvider](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#streamProvider) property. By implementing this interface, you will be able to save the created resources during HTML generation to your specific locations or memory streams.  

{{% /alert %}}  

This is the main code showing the usage of [HtmlSaveOptions.streamProvider](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#streamProvider) property  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(dataDir, 'out');

// Create workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

const options = new AsposeCells.HtmlSaveOptions();
options.setStreamProvider(new ExportStreamProvider(outputDir));

// Save into .html using HtmlSaveOptions
await workbook.saveAsync(path.join(dataDir, "output_out.html"), options);
```  

Here is the code for *ExportStreamProvider* class which implements [IStreamProvider](https://reference.aspose.com/cells/nodejs-cpp/istreamprovider) interface used inside the above code.  

```javascript
const fs = require("fs");
const path = require("path");

class ExportStreamProvider {
    constructor(dir) {
        this.outputDir = dir;
    }

    initStream(options) {
        const filePath = path.join(this.outputDir, path.basename(options.defaultPath));
        options.customPath = filePath;
        fs.mkdirSync(path.dirname(filePath), { recursive: true });
        options.stream = fs.createWriteStream(filePath);
    }

    closeStream(options) {
        if (options && options.stream) {
            options.stream.end();
        }
    }
}
```  

  