---  
title: Fügen Sie in einer Arbeitsmappe eine Bibliotheksreferenz im VBA Projekt mit Node.js via C++ hinzu  
linktitle: Fügen Sie eine Bibliotheksreferenz zum VBA Projekt in der Arbeitsmappe hinzu  
type: docs  
weight: 80  
url: /de/nodejs-cpp/add-a-library-reference-to-vba-project-in-workbook/  
---  

{{% alert color="primary" %}}  

Manchmal müssen Sie den Bibliotheksverweis in das VBA-Projekt durch Code hinzufügen oder registrieren. Sie können dies mit der Methode [**VbaProjectReferenceCollection.addRegisteredReference(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-string-) von Aspose.Cells tun.  

{{% /alert %}}  

## **Fügen Sie einem VBA-Projekt in Microsoft Excel einen Bibliotheksverweis hinzu.**  

In Microsoft Excel können Sie manuell durch Klicken auf **Extras > Verweise...** einen Bibliotheksverweis auf das VBA-Projekt hinzufügen.  

## **Fügen Sie eine Bibliotheksreferenz zum VBA-Projekt in einer Arbeitsmappe mit Aspose.Cells for Node.js via C++ hinzu**  

Das folgende Beispielcode fügt zwei Bibliotheksreferenzen zum VBA-Projekt der Arbeitsmappe mit der [**VbaProjectReferenceCollection.addRegisteredReference(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-string-)-Methode hinzu oder registriert sie.  

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
