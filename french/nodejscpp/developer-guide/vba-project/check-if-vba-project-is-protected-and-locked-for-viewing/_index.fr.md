---
title: Vérifier si le projet VBA est protégé et verrouillé en lecture seule avec Node.js via C++
linktitle: Vérifier si le projet VBA est protégé et verrouillé pour consultation
type: docs
weight: 30
url: /fr/nodejs-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: Apprenez comment vérifier si un projet VBA dans un fichier Excel est protégé et verrouillé en utilisant Aspose.Cells for Node.js via C++.
---

## Vérifier si le projet VBA est protégé et verrouillé en lecture seule dans Node.js

Aspose.Cells vous permet de vérifier si le projet VBA (Visual Basic for Applications) d'un fichier Excel est protégé et verrouillé pour la visualisation. Pour cela, l'API fournit la propriété [**VbaProject.getIslockedForViewing()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getIslockedForViewing--). S'il est verrouillé pour la visualisation, alors la propriété [**VbaProject.getIslockedForViewing()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getIslockedForViewing--) retourne **true**.

## **Code d'exemple**

Le code d'exemple suivant charge le [fichier Excel exemple](43352065.xlsm) et vérifie si le projet VBA (Visual Basic for Applications) du fichier Excel est protégé et verrouillé en lecture seule. Veuillez également voir sa sortie Console pour référence.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source Excel file.
const filePath = path.join(dataDir, "sampleCheckifVBAProjectisProtected.xlsm");
const workbook = new AsposeCells.Workbook(filePath);

// Access the VBA project of the workbook.
const vbaProject = workbook.getVbaProject();

// Whether "Lock project for viewing" is true or not.
console.log("Is VBA Project Locked for Viewing: " + vbaProject.getIslockedForViewing());
```

## **Sortie console**

Il s'agit de la sortie de la console du code d'exemple ci-dessus lorsqu'il est exécuté avec le [fichier Excel d'exemple](43352065.xlsm) fourni.

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
