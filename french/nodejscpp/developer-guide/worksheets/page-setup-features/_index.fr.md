---
title: Fonctionnalités de configuration de la mise en page avec Node.js via C++
linktitle: Fonctionnalités de mise en page
type: docs
weight: 60
url: /fr/nodejs-cpp/page-setup-features/
description: Explorez les fonctionnalités de mise en page en utilisant Aspose.Cells for Node.js via C++. Apprenez comment configurer les dimensions de page, les orientations et les paramètres.
keywords: Fonctionnalités de mise en page Node.js via C++, configurez les dimensions de la page Node.js via C++, paramètres d orientation de la page Node.js via C++
---



## **Introduction**
Avec Aspose.Cells for Node.js via C++, vous pouvez manipuler diverses fonctionnalités de mise en page d'un classeur Excel. Ces fonctionnalités incluent la définition de la taille de la page, l'orientation, les marges, et plus encore. La configuration appropriée de ces fonctionnalités permet une meilleure impression et une meilleure visualisation.

## ** Définir la taille et l'orientation de la page**
Vous pouvez spécifier la taille de la page et l'orientation d'une feuille de calcul en utilisant la classe `PageSetup`. Elle offre diverses propriétés pour gérer les dimensions et la disposition de la page.

### **Code d'exemple**
Voici un exemple de code illustrant comment définir la taille et l'orientation de la page.

```javascript
const { Workbook } = require("aspose.cells");

// Create a new workbook
let workbook = new Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Set the page size
worksheet.getPageSetup().setPaperSize(0); // A4 size

// Set the page orientation
worksheet.getPageSetup().setOrientation(1); // Landscape orientation

// Save the workbook
workbook.save("PageSetupExample.xlsx");
```

## **Réglage des marges**
Vous pouvez également définir les marges de la page en utilisant la même classe `PageSetup`. Les marges peuvent être ajustées pour les côtés gauche, droit, haut et bas.

### **Code d'exemple**
Voici comment vous pouvez définir les marges d'une feuille de calcul.

```javascript
// Set the margins
worksheet.getPageSetup().setLeftMargin(0.5);
worksheet.getPageSetup().setRightMargin(0.5);
worksheet.getPageSetup().setTopMargin(1.0);
worksheet.getPageSetup().setBottomMargin(1.0);

// Save the workbook
workbook.save("PageMarginsExample.xlsx");
```

## **Conclusion**
Dans ce document, vous avez appris comment manipuler les fonctionnalités de configuration de page dans Excel en utilisant Aspose.Cells for Node.js via C++. En utilisant efficacement la classe `PageSetup`, vous pouvez contrôler la façon dont vos feuilles de calcul sont imprimées et affichées, améliorant ainsi la présentation globale des informations.

---
