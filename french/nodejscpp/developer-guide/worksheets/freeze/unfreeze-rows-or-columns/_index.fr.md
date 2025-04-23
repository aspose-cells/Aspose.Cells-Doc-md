---
title: Délier les lignes ou les colonnes avec Node.js via C++
linktitle: Décongeler les volets
type: docs
weight: 190
url: /fr/nodejs-cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: Dans cet article, vous apprendrez comment délier les lignes, colonnes ou volets des feuilles Excel de manière programmatique en utilisant l’API Node.js avec C++.
keywords: Délier les volets, délier les lignes, délier les colonnes, déverrouiller la fenêtre Node.js via C++.
---

## **Introduction**

Dans cet article, nous apprendrons comment délier les lignes, les colonnes et les volets. Si les feuilles de calcul dans les fichiers Excel sont gelées, il arrive que nous souhaitions déverrouiller la feuille ou ajuster les lignes, colonnes ou volets gelés.


## **Dans Excel**

1. Cliquez sur l'onglet Affichage > Immobiliser les volets > Débloquer les volets.

**![débloquer les volets dans Excel](Unfreeze-Panes.png)**




## **Délier les lignes, colonnes ou volets avec Aspose.Cells for Node.js via C++**
Il est simple de déverrouiller les volets avec Aspose.Cells for Node.js via C++. Veuillez utiliser la méthode [**Worksheet.unFreezePanes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unFreezePanes--) pour déverrouiller les volets.

1. Construisez le classeur pour ouvrir le fichier gelé.
2. Délier les volets avec la méthode Worksheet.unfreezePanes()
3. Enregistrez le fichier.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const frozenFilePath = path.join(dataDir, "Frozen.xlsx");

const workbook = new AsposeCells.Workbook(frozenFilePath); 
workbook.getWorksheets().get(0).unFreezePanes();
workbook.save("Unfrozen.xlsx");
```

Fichier Excel source joint (Frozen.xlsx).
