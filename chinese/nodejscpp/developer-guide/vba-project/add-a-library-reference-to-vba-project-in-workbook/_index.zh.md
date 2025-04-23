---  
title: 通过Node.js的C++在工作簿中添加VBA库引用  
linktitle: 在工作簿中为VBA项目添加库引用  
type: docs  
weight: 80  
url: /zh/nodejs-cpp/add-a-library-reference-to-vba-project-in-workbook/  
---  

{{% alert color="primary" %}}  

有时，您需要通过代码添加或注册VBA项目的库引用。您可以使用Aspose.Cells [**VbaProjectReferenceCollection.addRegisteredReference(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-string-)方法来实现。  

{{% /alert %}}  

## **在Microsoft Excel中为VBA项目添加库引用**  

在Microsoft Excel中，您可以通过手动点击**工具 > 引用...**来添加VBA项目的库引用。  

## **使用Aspose.Cells for Node.js via C++向工作簿中的VBA项目添加库引用**  

下列示例代码使用[**VbaProjectReferenceCollection.addRegisteredReference(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-string-)方法向工作簿的VBA项目添加或注册两个库引用。  

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

