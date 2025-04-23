---
title: Ändern Sie die Richtung der Tick Beschriftung mit Node.js über C++
linktitle: Ändern Sie die Ausrichtung der Tickbeschriftung
description: Erfahren Sie, wie Sie die Richtung der Tick Beschriftungen in Aspose.Cells für Node.js ändern. Unser Leitfaden hilft Ihnen, die Ausrichtung der Tick Beschriftungen auf den Achsen anzupassen, einschließlich horizontaler, vertikaler und geneigter Ausrichtungen.
keywords: Aspose.Cells für Node.js, Tick Beschriftungen, Richtung, Orientierung, Achsen, horizontal, vertikal, geneigt.
type: docs
weight: 170
url: /de/nodejs-cpp/change-tick-label-direction/
---

## **Ändern der Richtung der Markierungstexte**

Aspose.Cells bietet die Möglichkeit, die Richtung der Diagramm-Tick-Labels mit der [**TickLabels.getDirectionType()**](https://reference.aspose.com/cells/nodejs-cpp/ticklabels/#getDirectionType--) Eigenschaft zu ändern. Die [**TickLabels.getDirectionType()**](https://reference.aspose.com/cells/nodejs-cpp/ticklabels/#getDirectionType--) Eigenschaft akzeptiert den [**ChartTextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/charttextdirectiontype) Enumeration-Wert. Das [**ChartTextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/charttextdirectiontype) Enumeration bietet die folgenden Mitglieder:

- Horizontal
- Vertikal
- Drehen90
- Drehen270
- Gestapelt

Das folgende Bild vergleicht die Quell- und Ausgabedateien

### **Quelldateibild**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **Ausgabedateibild**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

Der folgende Code-Schnipsel ändert die Richtung der Tickbeschriftung von Rotate90 auf Horizontal.

## **Beispielcode**

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

Die Quell- und Ausgabedateien können von den folgenden Links heruntergeladen werden.

[Quelldatei](105480221.xlsx)

[Ausgabedatei](105480223.xlsx)
