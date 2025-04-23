---  
title: Comment empêcher les utilisateurs d imprimer un fichier Excel avec Node.js via C++  
linktitle: Comment empêcher les utilisateurs d imprimer un fichier Excel  
type: docs  
weight: 600  
url: /fr/nodejs-cpp/how-to-prevent-printing-excel/  
description: Découvrez comment empêcher les utilisateurs d imprimer des fichiers Excel en utilisant Aspose.Cells for Node.js via C++.  
keywords: impression excel, empêcher l impression excel, comment empêcher les utilisateurs d imprimer excel, excel empêcher l impression, empêcher l impression d un classeur, Empêcher les utilisateurs d imprimer l ensemble du classeur avec VBA.  
---  

## **Scénarios d'utilisation possibles**  
Dans notre travail quotidien, il peut y avoir des informations importantes dans le fichier Excel; afin de protéger ces données internes de la diffusion, la société ne nous permettra pas de les imprimer. Ce document vous explique comment empêcher les autres d'imprimer des fichiers Excel.  

## **Comment empêcher les utilisateurs d'imprimer un fichier dans MS-Excel**  
Vous pouvez appliquer le code VBA suivant pour protéger votre fichier spécifique contre l'impression.  
1. Ouvrez votre classeur que vous ne permettez pas aux autres d'imprimer.  
1. Sélectionnez l'onglet "Développeur" dans le ruban Excel et cliquez sur le bouton "Afficher le code" dans la section "Contrôles". Alternativement, vous pouvez maintenir les touches ALT + F11 pour ouvrir la fenêtre **Visual Basic for Applications**.  
<br>  
<img src="1.png" width=70% />  
1. Ensuite, dans l'Explorateur de projets à gauche, double-cliquez sur ThisWorkbook pour ouvrir le module, et ajoutez des codes VBA.  
<br>  
<img src="2.png" width=70% />  
1. Ensuite, enregistrez et fermez ce code, revenez au classeur, et lorsque vous imprimez le fichier exemple, il ne sera pas autorisé à être imprimé, et une boîte d'avertissement apparaîtra :  
<br>  
<img src="3.png" width=70% />  

## **Comment empêcher les utilisateurs d'imprimer un fichier Excel avec Aspose.Cells for Node.js via C++**  

Le code d'exemple suivant illustre comment empêcher les utilisateurs d'imprimer un fichier Excel :  

1. Charger le [fichier d'exemple](sample.xlsx).  
1. Obtenez l'objet VbaModuleCollection à partir de la propriété VbaProject du classeur.  
1. Obtenez l'objet VbaModule via le nom "ThisWorkbook".  
1. Définissez la propriété codes de VbaModule.  
1. Enregistrez le fichier d'exemple au format [xlsm](out.xlsm).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample.xlsx");

// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);
const modules = wb.getVbaProject().getModules();
modules.get("ThisWorkbook").setCodes("Private Sub Workbook_BeforePrint(Cancel As Boolean)\r\n  Cancel = True\r\n  MsgBox \"Refusing to print in paperless office\"\r\nEnd Sub\r\n");

wb.save("out.xlsm");
```  

