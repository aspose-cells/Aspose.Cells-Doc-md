---  
title: Vérifier le mot de passe pour modification avec Aspose.Cells for Node.js via C++  
linktitle: Vérifier le mot de passe pour modifier  
type: docs  
weight: 2400  
url: /fr/nodejs-cpp/check-password-to-modify-using-aspose-cells/  
description: Apprenez comment vérifier si un mot de passe pour modification correspond avec Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
 Parfois, vous avez besoin de vérifier si le mot de passe donné correspond avec le **mot de passe pour modification** de manière programmatique. Aspose.Cells fournit la méthode `WorkbookSettings.writeProtection.validatePassword()` que vous pouvez utiliser pour vérifier si le mot de passe pour modification est correct ou non.  
{{% /alert %}}  

## **Vérifiez le mot de passe pour modifier dans Microsoft Excel**  

Vous pouvez attribuer **Mot de passe pour ouvrir** et **Mot de passe pour modifier** lors de la création de vos classeurs dans Microsoft Excel. Veuillez consulter cette capture d'écran qui montre l'interface fournie par Microsoft Excel pour spécifier ces mots de passe.  

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|  
| :- |  

## ** Vérifier le mot de passe pour modification avec Aspose.Cells for Node.js via C++**  

 Les codes d'exemple suivants chargent le fichier [source Excel](5112232.xlsx). Il a un mot de passe pour ouvrir de 1234 et un mot de passe pour modifier de 5678. Le code vérifie d'abord si 567 est le bon mot de passe pour modifier et retourne false, puis il vérifie si 5678 est le mot de passe pour modifier et retourne true.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify password to open inside the load options
const opts = new AsposeCells.LoadOptions();
opts.setPassword("1234");

// Open the source Excel file with load options
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleBook.xlsx"), opts);

// Check if 567 is Password to modify
let ret = workbook.getSettings().getWriteProtection().validatePassword("567");
console.log("Is 567 correct Password to modify: " + ret);

// Check if 5678 is Password to modify
ret = workbook.getSettings().getWriteProtection().validatePassword("5678");
console.log("Is 5678 correct Password to modify: " + ret);
```  

### **Sortie console**  

Voici la sortie de la console du code d'exemple ci-dessus après le chargement du [fichier Excel source](5112232.xlsx).  

{{< highlight java >}}  
Is 567 correct Password to modify: False  
Is 5678 correct Password to modify: True  
{{< /highlight >}}  
