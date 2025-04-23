---
title: Gérer les paramètres des fichiers de feuille de calcul Excel avec Node.js via C++
linktitle: Paramètres du classeur
type: docs
weight: 185
url: /fr/nodejs-cpp/workbook-settings/
description: Gérer les paramètres des fichiers Excel à l aide de Aspose.Cells for Node.js via C++.
---


## **Vue d'ensemble des paramètres du classeur**
Travailler avec des fichiers Excel implique divers réglages qui peuvent être manipulés de manière programmatique à l'aide de Aspose.Cells for Node.js via C++. Ce document décrit comment gérer efficacement ces paramètres.

## **Scénarios d'utilisation possibles**
Les scénarios suivants illustrent quand vous pourriez avoir besoin de gérer les paramètres du classeur :
- Ajustement des options d'affichage
- Définir le mode de calcul
- Configuration des paramètres de mise en page

## **Gérer les paramètres du classeur avec Aspose.Cells for Node.js via C++**
Cet exemple démontre comment gérer les paramètres du classeur tels que les options de calcul et d'affichage.

1. Créez un nouveau classeur ou chargez-en un existant.
2. Modifiez les paramètres du classeur selon vos besoins.
3. Enregistrez le classeur pour conserver les changements.

### **Code d'exemple**

```javascript
const { Workbook, SaveFormat } = require('aspose.cells');

// Create a new workbook
let workbook = new Workbook();

// Access the settings of the workbook
let settings = workbook.getSettings();
settings.setCalculationMode(1); // Manual calculation

// Display options
settings.setShowGridLines(false); // Disable gridlines

// Save the workbook
workbook.save('WorkbookSettingsExample.xlsx', SaveFormat.XLSX);
```

## **Propriétés et méthodes clés des paramètres du classeur**
Aspose.Cells pour Node.js offre un certain nombre de propriétés et de méthodes pour ajuster les paramètres du classeur :
- **Workbook.getSettings()** : Accède aux paramètres du classeur.
- **Settings.setCalculationMode(mode)** : Définit le mode de calcul pour le classeur.
- **Settings.setShowGridLines(value)** : Active ou désactive les lignes de grille à l'écran.

## **Conclusion**
Gérer les paramètres du classeur dans Aspose.Cells for Node.js via C++ est simple et offre de nombreuses options pour personnaliser le comportement des fichiers Excel. En utilisant les réglages disponibles, vous pouvez adapter le classeur à vos besoins spécifiques.

