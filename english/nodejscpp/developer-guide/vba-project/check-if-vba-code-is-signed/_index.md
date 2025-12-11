---
title: Check if VBA Code is Signed with Node.js via C++
linktitle: Check if VBA Code is Signed
type: docs
weight: 100
url: /nodejs-cpp/check-if-vba-code-is-signed/
description: Learn how to check if the VBA code project is signed using Aspose.Cells for Node.js via C++. 
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells allows the user to check whether the VBA code project is signed. Please use the [**VbaProject.isSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isSigned--) property to determine this.

{{% /alert %}}

The following code explains how to check if the VBA code is signed using the [**VbaProject.isSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isSigned--) property. You can use any of your Excel files to test this code. For testing purposes, you can use [this Excel file used in the code](5115032.xlsm).

## **Check if VBA Code is Signed in Node.js**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleVBAProjectSigned.xlsm");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

console.log("Is VBA Code Project Signed: " + workbook.getVbaProject().isSigned());
```

## Console Output

Below is the console output of the above code using the [sample Excel file](5115032.xlsm) provided in the link.

{{< highlight java >}}

Is VBA Code Project Signed: True

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
