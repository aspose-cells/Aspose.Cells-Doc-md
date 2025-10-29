---  
title: 如何使用Node.js通过C++设置工作簿的AutoRecover属性  
linktitle: 如何设置工作簿的AutoRecover属性  
type: docs  
weight: 220  
url: /zh/nodejs-cpp/how-to-set-autorecover-property-of-workbook/  
description: 学习如何使用Aspose.Cells for Node.js via C++设置工作簿的AutoRecover属性。  
---  

{{% alert color="primary" %}}  
你可以使用Aspose.Cells设置工作簿的AutoRecover属性。该属性的默认值为**true**。当你将其设置为**false**时，Microsoft Excel会禁用该Excel文件的自动恢复（自动保存）功能。  

Aspose.Cells提供了[**Workbook.getAutoRecover()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getAutoRecover--)属性来启用或禁用此选项。  
{{% /alert %}}  

以下代码说明了如何使用工作簿的[**Workbook.getAutoRecover()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getAutoRecover--)属性。代码先读取该属性的默认值（为**true**），然后将其设置为**false**并保存工作簿。再一次读取工作簿时，该属性的值为**false**。  

## 在Node.js中设置工作簿的AutoRecover属性的代码示例  

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

## **输出**  

这是上面示例代码的控制台输出。  

{{< highlight java >}}  
AutoRecover: True  
AutoRecover: False  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
