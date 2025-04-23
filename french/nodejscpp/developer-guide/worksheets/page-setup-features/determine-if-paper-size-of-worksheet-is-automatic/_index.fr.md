---
title: Déterminer si la taille du papier de la feuille est automatique avec Node.js via C++
linktitle: Déterminer si la taille du papier de la feuille de calcul est automatique
type: docs
weight: 90
url: /fr/nodejs-cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: Cet article explique comment utiliser l’API Node.js avec C++ addons pour déterminer si la taille du papier d’une feuille est réglée sur automatique de manière programmatique.
keywords: déterminer si la taille du papier de la feuille est automatique avec Node.js via C++
---

## **Scénarios d'utilisation possibles**

La plupart du temps, la taille du papier de la feuille est automatique. Lorsqu’elle est automatique, elle est souvent réglée sur *Letter*. Parfois, l’utilisateur configure la taille du papier selon ses besoins. Dans ce cas, la taille n’est pas automatique. Vous pouvez vérifier si la taille du papier de la feuille est automatique ou non en utilisant la propriété [**Worksheet.isAutomaticPaperSize()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#isAutomaticPaperSize--).

## **Déterminer si la taille du papier de la feuille de calcul est automatique**

Le code d'exemple ci-dessous charge les deux fichiers Excel suivants

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

et détermine si la taille du papier de leur première feuille de calcul est automatique ou non. Dans Microsoft Excel, vous pouvez vérifier si la taille du papier est automatique ou non via la fenêtre de configuration de la page comme indiqué dans cette capture d'écran.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const wb1 = new AsposeCells.Workbook(path.join(dataDir, "samplePageSetupIsAutomaticPaperSize-False.xlsx"));
const wb2 = new AsposeCells.Workbook(path.join(dataDir, "samplePageSetupIsAutomaticPaperSize-True.xlsx"));

// Access first worksheet of both workbooks
const ws11 = wb1.getWorksheets().get(0);
const ws12 = wb2.getWorksheets().get(0);

// Print the PageSetup.IsAutomaticPaperSize property of both worksheets
console.log("First Worksheet of First Workbook - IsAutomaticPaperSize: " + ws11.getPageSetup().isAutomaticPaperSize());
console.log("First Worksheet of Second Workbook - IsAutomaticPaperSize: " + ws12.getPageSetup().isAutomaticPaperSize());
```

## **Sortie console**

Voici la sortie console du code d'exemple ci-dessus lorsqu'il est exécuté avec les fichiers Excel d'exemple donnés.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
