---
title: Deaktivieren der Textumbruchfunktion für Datenetiketten des Diagramms mit Node.js über C++
description: Erfahren Sie, wie Sie den Textumbruch für Datenetiketten in Diagrammen mit Aspose.Cells for Node.js via C++ deaktivieren. Unser Leitfaden zeigt Ihnen, wie Sie verhindern können, dass lange Labels sich überlappen, und bietet lesbarere und klarere Diagrammanzeigen.
keywords: Aspose.Cells for Node.js via C++, Diagrammerstellung, Datenetiketten, Textumbruch, Überlappung, Lesbarkeit, Anzeigen.
type: docs
weight: 70
url: /de/nodejs-cpp/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013 ermöglicht es Benutzern, Texte in den Datenbeschriftungen des Diagramms umzubrechen oder nicht umzubrechen. Standardmäßig ist der Text in den Datenbeschriftungen des Diagramms umgebrochen.

Aspose.Cells bietet eine [**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#isTextWrapped--)-Eigenschaft, die Sie auf true oder false setzen können, um den Textumbruch von Datenetiketten entsprechend zu aktivieren oder zu deaktivieren.

{{% /alert %}}

Der folgende Codebeispiel zeigt, wie der Textumbruch für die Datenbeschriftungen des Diagramms deaktiviert wird.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample_wrap_label.xlsx");
// Load the sample Excel file inside the workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Disable the Text Wrapping of Data Labels in all Series
chart.getNSeries().get(0).getDataLabels().setIsTextWrapped(false);
chart.getNSeries().get(1).getDataLabels().setIsTextWrapped(false);
chart.getNSeries().get(2).getDataLabels().setIsTextWrapped(false);

// Save the workbook
workbook.save(path.join(dataDir, "Output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
