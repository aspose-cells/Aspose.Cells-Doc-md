---  
title: Agregar una referencia de biblioteca al proyecto VBA en el libro de trabajo con Node.js mediante C++  
linktitle: Agregar una referencia de biblioteca al proyecto VBA en el libro  
type: docs  
weight: 80  
url: /es/nodejs-cpp/add-a-library-reference-to-vba-project-in-workbook/  
---  

{{% alert color="primary" %}}  

A veces, es necesario agregar o registrar la referencia de la biblioteca en el proyecto VBA a través del código. Puedes hacerlo usando el método [**VbaProjectReferenceCollection.addRegisteredReference(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-string-) de Aspose.Cells.  

{{% /alert %}}  

## **Agrega una referencia de la biblioteca al proyecto VBA en Microsoft Excel**  

En Microsoft Excel, puedes agregar una referencia de la biblioteca al proyecto VBA haciendo clic en **Herramientas > Referencias...** manualmente.  

## **Agregar una referencia de biblioteca al proyecto VBA en un libro de trabajo usando Aspose.Cells for Node.js via C++**  

El siguiente ejemplo de código añade o registra dos referencias de biblioteca en el proyecto VBA del libro de trabajo usando el método [**VbaProjectReferenceCollection.addRegisteredReference(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-string-).  

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

