---  
title: Ajouter une référence de bibliothèque au projet VBA dans le classeur avec Node.js via C++  
linktitle: Ajoutez une référence de bibliothèque au projet VBA dans le classeur  
type: docs  
weight: 80  
url: /fr/nodejs-cpp/add-a-library-reference-to-vba-project-in-workbook/  
---  

{{% alert color="primary" %}}  

Parfois, vous devez ajouter ou enregistrer la référence de la bibliothèque dans le projet VBA par le biais du code. Vous pouvez le faire en utilisant la méthode Aspose.Cells [**VbaProjectReferenceCollection.addRegisteredReference(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-string-).  

{{% /alert %}}  

## **Ajouter une référence de bibliothèque au projet VBA dans Microsoft Excel**  

Dans Microsoft Excel, vous pouvez ajouter une référence de bibliothèque au projet VBA en cliquant sur **Outils > Références...** manuellement.  

## **Ajouter une référence de bibliothèque au projet VBA dans un classeur en utilisant Aspose.Cells for Node.js via C++**  

Le code d'exemple suivant ajoute ou enregistre deux références de bibliothèque au projet VBA du classeur en utilisant la méthode [**VbaProjectReferenceCollection.addRegisteredReference(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaprojectreferencecollection/#addRegisteredReference-string-string-).  

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

