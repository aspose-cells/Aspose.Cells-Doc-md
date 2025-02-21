---  
title: Editing Hyperlinks of Worksheet with Node.js via C++  
type: docs  
weight: 330  
url: /nodejs-cpp/editing-hyperlinks-of-worksheet/  
description: Learn how to edit hyperlinks of Worksheet through the Aspose.Cells for Node.js via C++ API.  
keywords: Edit Hyperlinks, Edit Hyperlinks of Worksheet, Edit hyperlink of Cell, Access all the hyperlinks of the worksheet  
---  

{{% alert color="primary" %}}  
Aspose.Cells allows you to access all the hyperlinks of the worksheet using the [**Worksheet.hyperlinks**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#hyperlinks) collection. You can access each hyperlink from this collection one by one and edit its properties.  
{{% /alert %}}  

The following sample code accesses all the hyperlinks of the worksheet and changes their [**Hyperlink.address**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink/#address) property to the Aspose website.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

const workbook = new AsposeCells.Workbook(dataDir + "Sample.xlsx");
const worksheet = workbook.getWorksheets().get(0);

for (let i = 0; i < worksheet.getHyperlinks().getCount(); i++) {
    const hl = worksheet.getHyperlinks().get(i);
    hl.setAddress("http://www.aspose.com");
}

workbook.save(dataDir + "output_out.xlsx");
```  
  