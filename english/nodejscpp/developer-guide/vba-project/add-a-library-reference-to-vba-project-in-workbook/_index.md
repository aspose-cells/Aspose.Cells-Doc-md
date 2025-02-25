---  
title: Add a library reference to VBA project in workbook with Node.js via C++  
linktitle: Add a library reference to VBA project in workbook  
type: docs  
weight: 80  
url: /nodejs-cpp/add-a-library-reference-to-vba-project-in-workbook/  
---  

{{% alert color="primary" %}}  

Sometimes, you need to add or register the library reference to the VBA project through code. You can do it using Aspose.Cells [**VbaProject.References.AddRegisteredReference()**](https://reference.aspose.com/cells/nodejs-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-) method.  

{{% /alert %}}  

## **Add a library reference to VBA project in Microsoft Excel**  

In Microsoft Excel, you can add a library reference to the VBA project by clicking the **Tools > References...** manually.  

## **Add a library reference to the VBA project in a workbook using Aspose.Cells for Node.js via C++**  

The following sample code adds or registers two library references to the VBA project of the workbook using [**VbaProject.References.AddRegisteredReference()**](https://reference.aspose.com/cells/nodejs-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-) method.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputPath = path.join(dataDir, "Output_out.xlsm");

const workbook = new AsposeCells.Workbook();

const vbaProj = workbook.getVbaProject();
vbaProj.getReferences().addRegisteredReference("stdole", "*\\G{00020430-0000-0000-C000-000000000046}#2.0#0#C:\\Windows\\system32\\stdole2.tlb#OLE Automation");
vbaProj.getReferences().addRegisteredReference("Office", "*\\G{2DF8D04C-5BFA-101B-BDE5-00AA0044DE52}#2.0#0#C:\\Program Files\\Common Files\\Microsoft Shared\\OFFICE14\\MSO.DLL#Microsoft Office 14.0 Object Library");

workbook.save(outputPath);
```  
  