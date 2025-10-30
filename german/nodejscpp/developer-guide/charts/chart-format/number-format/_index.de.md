---
title: Stellen Sie das Werteformat des Diagrammseriencodes mit Node.js über C++ ein
description: Lernen Sie, wie Sie den Werteformat Code der Diagrammserie in Aspose.Cells for Node.js via C++ setzen. Dieser Leitfaden hilft Ihnen zu verstehen, wie Sie Ihre Diagrammdaten mithilfe des passenden Format Codes formatieren, um Ihre Daten genau und professionell darzustellen.
keywords: Aspose.Cells für Node.js, Diagrammserie, Werteformatierung, Formatierung, Datenpräsentation, Genauigkeit, Professionalität.
linktitle: Zahlenformat
type: docs
weight: 100
url: /de/nodejs-cpp/set-the-values-format-code-of-chart-series/
---

## **Mögliche Verwendungsszenarien**
 Sie können den Werteformat-Code der Diagrammserie mit der Eigenschaften [Series.getValuesFormatCode()](https://reference.aspose.com/cells/nodejs-cpp/series/#getValuesFormatCode--) festlegen. Diese Eigenschaft ist nicht nur für Serien nützlich, die auf den Bereich innerhalb des Arbeitsblatts basieren, sondern funktioniert auch gut für Serien, die mit einem Wertearray erstellt wurden.

## **Setzen des Werteformatcodes der Diagrammserie**
 Der folgende Beispielcode fügt einer leeren Grafik, vorher ohne Serien, eine Serie hinzu. Es wird die Serie mit einem Wertearray hinzugefügt. Nach dem Hinzufügen wird sie mit dem Code $#,##0 formatiert, mithilfe der Eigenschaft [Series.getValuesFormatCode()](https://reference.aspose.com/cells/nodejs-cpp/series/#getValuesFormatCode--) und die Zahl 10000 wird zu $10.000. Die Aufnahme zeigt den Effekt des Codes auf die Beispiel-Excel-Datei (51740712.xlsx) und die Ausgabedatei (51740713.xlsx) nach der Ausführung.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Beispielcode**
```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "51740712.xlsx");

// Load the source Excel file 
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Add series using an array of values
chart.getNSeries().add("{10000, 20000, 30000, 40000}", true);

// Access the series and set its values format code
const series = chart.getNSeries().get(0);
series.setValuesFormatCode("$#,##0");

// Save the output Excel file
workbook.save(path.join(dataDir, "51740713.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
