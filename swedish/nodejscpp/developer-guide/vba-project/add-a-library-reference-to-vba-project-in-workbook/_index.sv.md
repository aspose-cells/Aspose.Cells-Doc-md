---  
title: Lägg till en bibliotekreferens till VBA projekt i arbetsboken med Node.js via C++  
linktitle: Lägg till en biblioteksreferens till VBA projekt i arbetsbok  
type: docs  
weight: 80  
url: /sv/nodejs-cpp/add-a-library-reference-to-vba-project-in-workbook/  
---  

{{% alert color="primary" %}}  

Ibland behöver du lägga till eller registrera biblioteksreferensen till VBA-projektet via kod. Du kan göra det med hjälp av Aspose.Cells [**VbaProjectReferenceCollection.addRegisteredReference(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-string-) -metoden.  

{{% /alert %}}  

## **Lägg till en biblioteksreferens till VBA-projekt i Microsoft Excel**  

I Microsoft Excel kan du lägga till en biblioteksreferens till VBA-projektet genom att klicka på **Verktyg > Referenser...** manuellt.  

## **Lägg till en bibliotekreferens till VBA-projektet i en arbetsbok med Aspose.Cells for Node.js via C++**  

Följande kodexempel lägger till eller registrerar två bibliotekreferenser till VBA-projektet i arbetsboken med hjälp av [**VbaProjectReferenceCollection.addRegisteredReference(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-string-)-metoden.  

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

