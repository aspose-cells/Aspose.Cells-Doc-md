---
title: Modifier la direction de l étiquette de graduation avec Node.js via C++
linktitle: Modifier la direction des étiquettes de graduation
description: Apprenez comment changer la direction des étiquettes de graduation dans Aspose.Cells pour Node.js. Notre guide vous aidera à comprendre comment ajuster l orientation des étiquettes de graduation sur les axes, y compris l orientation horizontale, verticale et inclinée.
keywords: Aspose.Cells pour Node.js, étiquettes de graduation, direction, orientation, axes, horizontal, vertical, incliné.
type: docs
weight: 170
url: /fr/nodejs-cpp/change-tick-label-direction/
---

## **Changer la direction des étiquettes des graduations**

Aspose.Cells vous offre la possibilité de changer la direction des étiquettes de graduation du graphique en utilisant la propriété [**TickLabels.getDirectionType()**](https://reference.aspose.com/cells/nodejs-cpp/ticklabels/#getDirectionType--). La propriété [**TickLabels.getDirectionType()**](https://reference.aspose.com/cells/nodejs-cpp/ticklabels/#getDirectionType--) accepte la valeur d'énumération [**ChartTextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/charttextdirectiontype). L'énumération [**ChartTextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/charttextdirectiontype) fournit les membres suivants :

- Horizontale
- Verticale
- Rotation90
- Rotation270
- Empilée

L'image suivante compare les fichiers source et de sortie

### **Image du fichier source**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **Image du fichier de sortie**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

Le snippet de code suivant change la direction des étiquettes de graduation de Rotation90 à Horizontale.

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");
const filePath = path.join(sourceDir, "SampleChangeTickLabelDirection.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const worksheet = workbook.getWorksheets().get(0);

// Load the chart from source worksheet
const chart = worksheet.getCharts().get(0);

chart.getCategoryAxis().getTickLabels().setDirectionType(AsposeCells.ChartTextDirectionType.Horizontal);

// Output the file
workbook.save(path.join(outputDir, "outputChangeChartDataLableDirection.xlsx"));
```

Les fichiers source et de sortie peuvent être téléchargés à partir des liens suivants.

[Fichier source](105480221.xlsx)

[Fichier de sortie](105480223.xlsx)
