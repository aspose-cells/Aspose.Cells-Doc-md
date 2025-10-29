---  
title: Protéger par mot de passe le projet VBA du classeur Excel avec Node.js via C++  
linktitle: Protégez le mot de passe du projet VBA de Classeur Excel  
type: docs  
weight: 10  
url: /fr/nodejs-cpp/password-protect-the-vba-project-of-excel-workbook/  
description: Découvrez comment protéger par mot de passe le projet VBA d un classeur Excel en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Protéger par mot de passe le projet VBA du classeur Excel dans Node.js**  

Vous pouvez protéger par mot de passe le projet VBA (Visual Basic for Applications) d'un classeur avec Aspose.Cells en utilisant la méthode [**VbaProject.protect(boolean, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#protect-boolean-string-).  

## **Code d'exemple**  

Le code exemple suivant charge le [fichier Excel d'exemple](43352067.xlsm), accède à son projet VBA et le protège par un mot de passe. Enfin, il le sauvegarde en tant que [fichier Excel de sortie](43352068.xlsm).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source Excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "samplePasswordProtectVBAProject.xlsm"));

// Access the VBA project of the workbook.
const vbaProject = workbook.getVbaProject();

// Lock the VBA project for viewing with password.
vbaProject.protect(true, "11");

// Save the output Excel file
workbook.save(path.join(dataDir, "outputPasswordProtectVBAProject.xlsm"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
