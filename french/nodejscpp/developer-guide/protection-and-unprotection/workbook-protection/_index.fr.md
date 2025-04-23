---  
title: Protéger et Déprotéger la Structure du Classeur avec Node.js via C++  
linktitle: Protéger et déprotéger la structure du classeur  
type: docs  
weight: 40  
url: /fr/nodejs-cpp/protect-and-unprotect-workbook-structure/  
description: Protéger et déprotéger la structure du classeur dans les fichiers Excel en utilisant Node.js via C++.  
---  


{{% alert color="primary" %}}  
Pour empêcher les autres utilisateurs de voir des feuilles de calcul cachées, d'ajouter, de déplacer, de supprimer ou de masquer des feuilles de calcul, et de renommer des feuilles de calcul, vous pouvez protéger la structure de votre classeur Excel avec un mot de passe.  
{{% /alert %}}  


## **Protéger et déprotéger la structure du classeur dans MS Excel**  

**![Protéger et déprotéger la structure du classeur](protect-and-unprotect-workbook-structure.png)**  

1. Cliquez sur **Relecture > Protéger le classeur**.  
1. Entrez un mot de passe dans **la boîte de mot de passe**.  
1. Sélectionnez **OK**, saisissez à nouveau le mot de passe pour le confirmer, puis sélectionnez à nouveau **OK**.  


## **Protéger la structure du classeur en utilisant Aspose.Cells for Node.js via C++**  
Il suffit d'utiliser les lignes de code suivantes pour implémenter la protection de la structure du classeur Excel.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Create a new file.
const workbook = new AsposeCells.Workbook();
// Protect workbook structure.
workbook.protect(AsposeCells.ProtectionType.Structure, "password");
// Save Excel file.
workbook.save(filePath);
```  

## **Déprotéger la structure du classeur en utilisant Aspose.Cells for Node.js via C++**  
La déprotection de la structure du classeur est facile avec l'API Aspose.Cells.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open an Excel file which workbook structure is protected.
const workbook = new AsposeCells.Workbook(filePath);
// Unprotect workbook structure.
workbook.unprotect("password");
// Save Excel file.
workbook.save(filePath);
```  

{{% alert color="primary" %}}  
Remarque : un mot de passe correct est requis.  
{{% /alert %}}  

