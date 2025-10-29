---  
title: Optimisation de l’utilisation de la mémoire lors de la manipulation de gros fichiers contenant de grands ensembles de données avec Node.js en C++  
linktitle: Optimisation de l utilisation de la mémoire lors du travail avec de gros fichiers contenant de grands ensembles de données  
type: docs  
weight: 180  
url: /fr/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/  
---  

{{% alert color="primary" %}}  

Lors de la création d’un classeur avec de grands ensembles de données, ou la lecture d’un grand fichier Microsoft Excel, la quantité totale de RAM que le processus consommera est toujours une préoccupation. Il existe des mesures qui peuvent être adaptées pour faire face à ce défi. Aspose.Cells for Node.js via C++ offre des options et des appels API pertinents pour réduire, optimiser et gérer la mémoire. Cela peut également aider le processus à fonctionner plus efficacement et plus rapidement.  

Utilisez l'option [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) pour optimiser l'utilisation de la mémoire pour les données des cellules et réduire le coût total de la mémoire. Lors de la création d'un grand ensemble de données pour les cellules, cela peut économiser une certaine quantité de mémoire par rapport à l'utilisation du paramètre par défaut ([**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)).  

{{% /alert %}}  

## **Optimisation de la mémoire**  

### **Lecture de gros fichiers Excel**  

L'exemple suivant montre comment lire un gros fichier Microsoft Excel en mode optimisé.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the LoadOptions
const opt = new AsposeCells.LoadOptions();
// Set the memory preferences
opt.setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Instantiate the Workbook
// Load the Big Excel file having large Data set in it
const wb = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"), opt);
```  

### **Écriture de gros fichiers Excel**  

L'exemple suivant montre comment écrire un grand ensemble de données dans une feuille de calcul en mode optimisé.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook();

// Set the memory preferences
wb.getSettings().setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Note: The memory settings also would not work for the default sheet i.e., "Sheet1" etc. automatically created by the Workbook

// To change the memory setting of existing sheets, please change memory setting for them manually:
let cells = wb.getWorksheets().get(0).getCells();
cells.setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Input large dataset into the cells of the worksheet.
// Your code goes here.
// .........

// Get cells of the newly created Worksheet "Sheet2" whose memory setting is same with the one defined in WorkbookSettings:
cells = wb.getWorksheets().add("Sheet2").getCells();
// .........
// Input large dataset into the cells of the worksheet.
// Your code goes here.
// .........
```  

## **Attention**  

L’option par défaut, [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/), s’applique à toutes les versions. Dans certains cas, comme la création d’un classeur avec un grand ensemble de cellules, l’option [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) peut optimiser l’utilisation de la mémoire et diminuer le coût en mémoire pour l’application. Cependant, cette option peut dégrader la performance dans certains cas particuliers, comme suit.  

1. **Accéder aux cellules de manière aléatoire et répétée** : La séquence la plus efficace pour accéder à la collection de cellules est d’abord par cellule dans une ligne, puis ligne par ligne. Surtout si vous accédez aux lignes/cellules par l’énumérateur obtenu à partir de [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells), [**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection), et [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row), la performance sera maximisée avec [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/).  
2. **Insérer & supprimer des cellules et des lignes** : Notez que si il y a beaucoup d’opérations d’insertion/suppression pour les cellules/lignes, la dégradation des performances sera notable en mode *MemoryPreference* par rapport au mode *Normal*.  
3. **Travailler avec différents types de cellules** : Si la majorité des cellules contiennent des valeurs string ou des formules, le coût mémoire sera le même que le mode *Normal*, mais s’il y a beaucoup de cellules vides, ou si les valeurs sont numériques, booléennes, etc., l’option [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) offrira une meilleure performance.  

{{< app/cells/assistant language="nodejs-cpp" >}}
