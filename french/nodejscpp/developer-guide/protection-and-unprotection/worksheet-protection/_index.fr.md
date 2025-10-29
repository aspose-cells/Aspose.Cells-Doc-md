---  
title: Protéger et Déprotéger la feuille de calcul avec Node.js via C++  
linktitle: Protéger et déprotéger la feuille de calcul  
type: docs  
weight: 40  
url: /fr/nodejs-cpp/protect-and-unprotect-worksheets/  
description: Protéger et déprotéger la feuille de calcul des fichiers Excel avec Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Pour empêcher d'autres utilisateurs de modifier, déplacer ou supprimer accidentellement ou délibérément des données dans une feuille de calcul, vous pouvez verrouiller les cellules de votre feuille de calcul Excel, puis protéger la feuille avec un mot de passe.  
{{% /alert %}}  

## **Protéger et déprotéger une feuille de calcul dans MS Excel**  

**![Protéger et déprotéger la feuille de calcul](protéger-et-déprotéger-la-feuille-de-calcul.png)**  

1. Cliquez sur **Révision > Protéger la feuille**.  
1. Entrez un mot de passe dans **la boîte de mot de passe**.  
1. Sélectionnez les options **autoriser**.  
1. Sélectionnez **OK**, saisissez à nouveau le mot de passe pour le confirmer, puis sélectionnez à nouveau **OK**.  

## **Protéger la feuille de calcul en utilisant Aspose.Cells for Node.js via C++**  
Il suffit d'utiliser les lignes de code suivantes pour implémenter la protection de la structure du classeur Excel.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a new file.
const workbook = new AsposeCells.Workbook();
// Gets the first worksheet.
const sheet = workbook.getWorksheets().get(0);
// Protect contents of the worksheet.
sheet.protect(AsposeCells.ProtectionType.Contents);
// Protect worksheet with password.
sheet.getProtection().setPassword("test");
// Save as Excel file.
workbook.save("Book1.xlsx");
```  

## **Déprotéger la feuille de calcul en utilisant Aspose.Cells for Node.js via C++**  
La déprotection de la feuille de calcul est facile avec l'API Aspose.Cells. Si la feuille est protégée par mot de passe, un mot de passe correct est requis.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Create a new file.
const workbook = new AsposeCells.Workbook(filePath);
// Gets the first worksheet.
const sheet = workbook.getWorksheets().get(0);
// Protect contents of the worksheet.
sheet.unprotect("password");
// Save Excel file.
workbook.save("Book1.xlsx");
```  

## **Sujets avancés**  
- [Paramètres de protection avancés depuis Excel XP](/cells/fr/nodejs-cpp/advanced-protection-settings-since-excel-xp/)  
- [Détecter si la feuille de calcul est protégée par mot de passe](/cells/fr/nodejs-cpp/detect-if-worksheet-is-password-protected/)  
- [Protection des feuilles de calcul](/cells/fr/nodejs-cpp/protecting-worksheets/)  
- [Déprotéger une feuille de calcul](/cells/fr/nodejs-cpp/unprotect-a-worksheet/)  
- [Vérifier le mot de passe utilisé pour protéger la feuille de calcul](/cells/fr/nodejs-cpp/verify-password-used-to-protect-the-worksheet/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
