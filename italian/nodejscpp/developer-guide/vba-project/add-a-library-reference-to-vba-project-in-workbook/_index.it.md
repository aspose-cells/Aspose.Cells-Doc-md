---  
title: Aggiungere un riferimento di libreria al progetto VBA nel workbook con Node.js via C++  
linktitle: Aggiungi un riferimento di libreria al progetto VBA nel workbook  
type: docs  
weight: 80  
url: /it/nodejs-cpp/add-a-library-reference-to-vba-project-in-workbook/  
---  

{{% alert color="primary" %}}  

A volte è necessario aggiungere o registrare il riferimento della libreria al progetto VBA tramite codice. Puoi farlo utilizzando il metodo Aspose.Cells [**VbaProjectReferenceCollection.addRegisteredReference(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-string-).  

{{% /alert %}}  

## **Aggiungi un riferimento della libreria al progetto VBA in Microsoft Excel**  

In Microsoft Excel, puoi aggiungere un riferimento della libreria al progetto VBA cliccando manualmente su **Strumenti > Riferimenti...**  

## **Aggiungi un riferimento di libreria al progetto VBA in un workbook usando Aspose.Cells for Node.js via C++**  

Il seguente esempio di codice aggiunge o registra due riferimenti di libreria al progetto VBA del workbook usando il metodo [**VbaProjectReferenceCollection.addRegisteredReference(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-string-).  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
