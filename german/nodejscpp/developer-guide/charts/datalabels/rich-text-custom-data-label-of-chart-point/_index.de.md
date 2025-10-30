---
title: Rich Text Anpassung eines benutzerdefinierten Datenetiketts eines Diagrammpunkts mit Node.js über C++
description: Erfahren Sie, wie Sie mit Aspose.Cells for Node.js via C++ Rich Text Benutzerdefinierte Datenetiketten zu Diagrammpunkten hinzufügen. Unser Leitfaden zeigt, wie Sie die Etiketten mit verschiedenen Schriftarten, Farben und Ausrichtungsoptionen formatieren, um das Erscheinungsbild und die Lesbarkeit Ihrer Diagramme zu verbessern.
keywords: Aspose.Cells for Node.js via C++, Diagrammerstellung, Rich Text, benutzerdefinierte Datenetiketten, Schriftarten, Farben, Ausrichtung, Erscheinungsbild, Lesbarkeit.
type: docs
weight: 10
url: /de/nodejs-cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

Sie können Aspose.Cells verwenden, um Rich-Text-Benutzerdefinierte Datenetiketten für Diagrammpunkte zu erstellen. Aspose.Cells bietet die [**ChartTextFrame.characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#characters-number-number-)-Methode, um das [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting)-Objekt zurückzugeben, mit dem die Schriftarteigenschaften des Textes wie Farbe, Fettdruck usw. festgelegt werden können.

{{% /alert %}}

## Benutzerdefinierte Rich-Text-Datenbeschriftung des Diagrammpunkts

Der folgende Code greift auf den ersten Diagrammpunkt der ersten Serie zu, setzt seinen Text und legt dann die Schriftart der ersten 10 Zeichen fest, indem er die Farbe auf Rot setzt und die Fettdruck-Option auf **true** setzt.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample_custom_datalabel.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the sheet
const chart = worksheet.getCharts().get(0);

// Access the data label of first series first point
const dlbls = chart.getNSeries().get(0).getPoints().get(0).getDataLabels();

// Set data label text
dlbls.setText("Rich Text Label");

// Set the font setting of the first 10 characters
const fntSetting = dlbls.characters(0, 10);
fntSetting.getFont().setColor(AsposeCells.Color.Red);
fntSetting.getFont().setIsBold(true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
