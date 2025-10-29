---
title: Rendre des compléments Office lors de la conversion d Excel en PDF avec Node.js via C++
linktitle: Rendre les Compléments Office lors de la conversion d Excel en PDF
type: docs
weight: 100
url: /fr/nodejs-cpp/render-office-add-ins-while-converting-excel-to-pdf/
---

## **Scénarios d'utilisation possibles**

Auparavant, Aspose.Cells ne pouvait pas rendre les compléments Office lors de la sauvegarde d'un fichier Excel en format PDF. Maintenant, Aspose.Cells le rend correctement. Vous n'avez pas besoin d'utiliser une méthode ou propriété spéciale pour rendre les compléments Office dans le PDF de sortie. Il suffit d'enregistrer votre fichier Excel en format PDF, et il rendra les compléments Office.

## **Rendre les compléments Office lors de la conversion Excel en PDF**

Le code d'exemple suivant enregistre le [fichier Excel d'exemple](60489769.xlsx) qui contient les compléments Office. Veuillez voir le [PDF de sortie généré avec la version précédente, c’est-à-dire 17.11](60489770.pdf) et le [PDF de sortie généré avec la version plus récente, c’est-à-dire 17.12 et suivantes](60489771.pdf). Le PDF de la version précédente est vide, mais le PDF de la version plus récente montre le complément Office.

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleRenderOfficeAdd-Ins.xlsx");
// Load the sample Excel file containing Office Add-Ins
const wb = new AsposeCells.Workbook(filePath);

// Save it to Pdf format
wb.save(`output-${AsposeCells.CellsHelper.getVersion()}.pdf`);
``` 
{{< app/cells/assistant language="nodejs-cpp" >}}
