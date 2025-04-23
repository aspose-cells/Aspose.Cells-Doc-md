---  
title: Добавление ссылки библиотеки в VBA проект в рабочей книге с Node.js через C++  
linktitle: Добавить ссылку на библиотеку в проект VBA в книге  
type: docs  
weight: 80  
url: /ru/nodejs-cpp/add-a-library-reference-to-vba-project-in-workbook/  
---  

{{% alert color="primary" %}}  

Иногда вам нужно добавить или зарегистрировать ссылку на библиотеку в проекте VBA через код. Вы можете сделать это с помощью метода Aspose.Cells [**VbaProjectReferenceCollection.addRegisteredReference(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-string-).  

{{% /alert %}}  

## **Добавить ссылку на библиотеку в проект VBA в Microsoft Excel**  

В Microsoft Excel вы можете добавить ссылку на библиотеку в проект VBA, нажав **Инструменты > Ссылки...** вручную.  

## **Добавьте ссылку библиотеки в VBA-проект рабочей книги с помощью Aspose.Cells for Node.js via C++**  

 Следующий пример кода добавляет или регистрирует две ссылки библиотеки в VBA-проекте рабочей книги с помощью метода [**VbaProjectReferenceCollection.addRegisteredReference(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-string-).  

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

