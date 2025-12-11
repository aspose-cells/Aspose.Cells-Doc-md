---  
title: Convert Revision of XLSB to XLSM with Node.js via C++  
linktitle: Convert Revision of XLSB to XLSM  
type: docs  
weight: 290  
url: /nodejs-cpp/convert-revision-of-xlsb-to-xlsm/  
description: Learn how to fully convert revisions of XLSB files into XLSM format using Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  

Aspose.Cells now supports fully converting revisions of XLSB files into XLSM files. Revisions are found inside the path \xl\revisions. You can view them by changing the XLSB file's extension to .zip. The \xl\revisions path contains files ending with .bin extensions.  

When you convert your XLSB file into an XLSM file using Aspose.Cells, these .bin files successfully convert to .xml files as shown in these two screenshots.  

{{% /alert %}}  

The following code sample shows you how to convert the XLSB file into XLSM format using Aspose.Cells for Node.js via C++.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsb");

// Open workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save Workbook to XLSM format
workbook.save(path.join(dataDir, "output_out.xlsm"), AsposeCells.SaveFormat.Xlsm);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
