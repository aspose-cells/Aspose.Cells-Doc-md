---
title: Obtenir l adresse, le nombre de cellules, le décalage, la colonne entière et la ligne entière de la plage avec Node.js via C++
linktitle: Obtenir le décalage du nombre de cellules d adresse de la colonne entière et de la ligne entière de la plage
type: docs
weight: 330
url: /fr/nodejs-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
---

## **Scénarios d'utilisation possibles**
Aspose.Cells for Node.js via C++ fournit l'objet Range qui possède diverses méthodes utilitaires facilitant le travail avec les plages Excel. Cet article illustre l'utilisation des méthodes ou propriétés suivantes de l'objet Range.

- **Adresse**

Obtient l'adresse de la plage.

- **Nombre de cellules**

Obtient le nombre de cellules dans la plage.

- **Décalage**

Obtient la plage par décalage.

- **Colonne entière**

Obtient un objet Range qui représente la colonne entière (ou les colonnes) contenant la plage spécifiée.

- **Ligne entière**

Obtient un objet Range qui représente la ligne entière (ou les lignes) contenant la plage spécifiée.

## **Obtenez l'adresse, le nombre de cellules, le décalage, la colonne entière et la ligne entière de la plage.**
Le code d'exemple suivant explique l'utilisation des méthodes et propriétés comme discuté ci-dessus. Veuillez consulter la sortie de la console du code ci-dessous pour référence.

## **Code d'exemple**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create empty workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Create range A1:B3.
console.log("Creating Range A1:B3\n");
let rng = ws.getCells().createRange("A1:B3");

// Print range address and cell count.
console.log("Range Address: " + rng.getAddress());
console.log("Range row Count: " + rng.getRowCount());
console.log("Range column Count: " + rng.getColumnCount());

// Formatting console output.
console.log("----------------------");
console.log("");

// Create range A1.
console.log("Creating Range A1\n");
rng = ws.getCells().createRange("A1");

// Print range offset, entire column and entire row.
console.log("Offset: " + rng.getOffset(2, 2).getAddress());
console.log("Entire Column: " + rng.getEntireColumn().getAddress());
console.log("Entire Row: " + rng.getEntireRow().getAddress());

// Formatting console output.
console.log("----------------------");
console.log("");
```

## **Sortie console**
{{< highlight javascript >}}
 Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
