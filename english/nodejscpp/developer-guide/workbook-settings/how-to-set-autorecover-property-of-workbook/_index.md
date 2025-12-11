---  
title: How to set AutoRecover property of Workbook with Node.js via C++  
linktitle: How to set AutoRecover property of Workbook  
type: docs  
weight: 220  
url: /nodejs-cpp/how-to-set-autorecover-property-of-workbook/  
description: Learn how to set the AutoRecover property of a workbook using Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  
You can use Aspose.Cells to set the AutoRecover property of the workbook. The default value of this property is **true**. When you set it to **false** for a workbook, Microsoft Excel disables AutoRecover (autosave) for that Excel file.  

Aspose.Cells provides the [**Workbook.getAutoRecover()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getAutoRecover--) and [**Workbook.setAutoRecover()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setAutoRecover--) methods to enable or disable this option.  
{{% /alert %}}  

The following code demonstrates how to use the Workbook.getAutoRecover() method. The code first reads the default value of this property, which is **true**; then it sets it to **false** and saves the workbook. Afterwards, it reads the workbook again and retrieves the value of this property, which is now **false**.  

## Node.js code to set the AutoRecover property of Workbook  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Read AutoRecover property
console.log("AutoRecover: " + workbook.getSettings().getAutoRecover());

// Set AutoRecover property to false
workbook.getSettings().setAutoRecover(false);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));

// Read the saved workbook again
const workbook2 = new AsposeCells.Workbook(path.join(dataDir, "output_out.xlsx"));

// Read AutoRecover property
console.log("AutoRecover: " + workbook2.getSettings().getAutoRecover());
```  

## **Output**  

Here is the console output of the above sample code.  

{{< highlight javascript >}}  
AutoRecover: True  
AutoRecover: False  
{{< /highlight >}}  
  
{{< app/cells/assistant language="nodejs-cpp" >}}
