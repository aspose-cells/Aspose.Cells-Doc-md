---
title: Définir des en têtes et pieds de page différents pour des pages différentes avec Node.js via C++
linktitle: Définir des en têtes et des pieds de page différents pour différentes pages
type: docs
weight: 35
url: /fr/nodejs-cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: Cet article fournit un exemple de code montrant comment définir de manière programmatique les en têtes et pieds de page de la configuration de la page de la feuille Excel en utilisant Aspose.Cells for Node.js via C++. Définissez les en têtes et pieds de page pour la première, les pages impaires et paires.
keywords: définir l en tête et le pied de page Excel pour la première page Node.js via C++, définir l en tête et le pied de page Excel pour les pages impaires Node.js via C++, définir l en tête et le pied de page Excel pour les pages paires Node.js via C++
---

{{% alert color="primary" %}}

MS Excel supporte la définition d'en-têtes et pieds de page différents pour la première page, les pages impaires et les pages paires depuis Excel 2007.
 Aspose.Cells for Node.js via C++ supporte la même fonctionnalité.

{{% /alert %}}

## **Définir des en-têtes et des pieds de page différents dans MS Excel**

**![Définir des en-têtes et des pieds de page différents](difpage.png)**

1. Cliquez sur **Mise en page > Titres et en-têtes > En-tête/pied de page**.
1. Cochez **Différentes pages impaires et paires** ou **Première page différente**.
1. Entrez des en-têtes et pieds de page différents.

## **Configurer différents en-têtes et pieds de page avec Aspose.Cells for Node.js via C++**

Aspose.Cells se comporte de la même manière qu'Excel.
1. Activez les drapeaux [PageSetup.isHFDiffOddEven()](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isHFDiffOddEven--) et [PageSetup.isHFDiffFirst()](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isHFDiffFirst--) 
1. Entrez des en-têtes et pieds de page différents.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Gets the setting of page setup.
const pageSetup = wb.getWorksheets().get(0).getPageSetup();
// Sets different odd and even pages
pageSetup.setIsHFDiffOddEven(true);
pageSetup.setHeader(1, "I am the header of the Odd page.");
pageSetup.setEvenHeader(1, "I am the header of the Even page.");
// Sets different first page
pageSetup.setIsHFDiffFirst(true);
pageSetup.setFirstPageHeader(1, "I am the header of the First page.");
```
