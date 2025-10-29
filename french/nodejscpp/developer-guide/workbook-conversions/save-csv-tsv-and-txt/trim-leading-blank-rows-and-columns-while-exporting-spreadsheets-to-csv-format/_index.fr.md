---
title: Trimer les lignes et colonnes vides en tête lors de l exportation de feuilles de calcul en format CSV avec Node.js via C++
linktitle: Supprimer les lignes et colonnes vides initiales lors de l exportation de feuilles de calcul au format CSV
type: docs
weight: 100
url: /fr/nodejs-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Apprenez comment tronquer les lignes et colonnes vides en tête lors de l exportation de feuilles de calcul en format CSV en utilisant Aspose.Cells for Node.js via C++.
---

## **Scénarios d'utilisation possibles**

Parfois, votre fichier Excel ou CSV contient des colonnes ou des lignes vides initiales. Par exemple, considérez cette ligne

{{< highlight javascript >}}

 ,,,data1,data2

{{< /highlight >}}

Ici, les trois premières cellules ou colonnes sont vides. Lorsque vous ouvrez un tel fichier CSV dans Microsoft Excel, Microsoft Excel ignore ces lignes et colonnes vides initiales.

Par défaut, Aspose.Cells for Node.js via C++ ne supprime pas les colonnes et lignes vides en tête lors de la sauvegarde, mais si vous souhaitez les supprimer comme le fait Microsoft Excel, Aspose.Cells fournit la propriété [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--). Veuillez la définir à **true** et toutes les lignes et colonnes vides en tête seront supprimées lors de la sauvegarde.

{{% alert color="primary" %}}

Avant la sortie de Aspose.Cells for Node.js via C++ 20.4, la valeur par défaut de [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) était **false**. Depuis la version 20.4, la valeur par défaut de [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) est **true**.

{{% /alert %}}

## **Supprimer les lignes et colonnes vides en tête lors de l'exportation de feuilles de calcul au format CSV**

Le code suivant charge le [fichier Excel source](sampleTrimBlankColumns.xlsx) qui possède deux colonnes vides en tête. Il sauvegarde d'abord le fichier Excel au format CSV sans modification, puis définit la propriété [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) à **true** et le sauvegarde à nouveau. La capture d'écran montre le [fichier Excel source](sampleTrimBlankColumns.xlsx), le fichier CSV de sortie sans troncature, et le fichier CSV de sortie avec troncature.

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load source workbook
const wb = new AsposeCells.Workbook(path.join(dataDir, "sampleTrimBlankColumns.xlsx"));

// Save in csv format
wb.save(path.join(dataDir, "outputWithoutTrimBlankColumns.csv"), AsposeCells.SaveFormat.Csv);

// Now save again with TrimLeadingBlankRowAndColumn as true
const opts = new AsposeCells.TxtSaveOptions();
opts.setTrimLeadingBlankRowAndColumn(true);

// Save in csv format
wb.save(path.join(dataDir, "outputTrimBlankColumns.csv"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
