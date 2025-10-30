---
title: Ändern Sie die Datenquelle des Diagramms auf das Ziel Arbeitsblatt, während Sie Zeilen oder Bereiche mit Node.js über C++ kopieren
linktitle: Ändern Sie die Datenquelle des Diagramms in das Zieltabellenblatt beim Kopieren von Zeilen oder Bereich
description: Lernen Sie, wie Sie in Aspose.Cells for Node.js via C++ die Datenquelle eines Diagramms auf ein Ziel Arbeitsblatt ändern, während Sie Zeilen oder einen Bereich kopieren. Dieser Leitfaden zeigt, wie Sie den Datenbereich des Diagramms aktualisieren und es mit dem Ziel Arbeitsblatt verknüpfen.
keywords: Aspose.Cells for Node.js via C++, Diagrammerstellung, Datenquelle, Ziel Arbeitsblatt, Zeilen, Bereich, Kopieren, Aktualisieren, Datenbereich, Verknüpfung.
type: docs
weight: 440
url: /de/nodejs-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Mögliche Verwendungsszenarien**

 Wenn Sie Zeilen oder Bereiche mit Diagrammen in ein neues Arbeitsblatt kopieren, ändert sich die Datenquelle des Diagramms nicht. Wenn die Datenquelle z.B. `=Sheet1!$A$1:$B$4` ist, bleibt sie nach dem Kopieren in ein neues Arbeitsblatt unverändert, also `=Sheet1!$A$1:$B$4`. Es verweist weiterhin auf das alte Arbeitsblatt, also Sheet1. Dies ist auch das Verhalten in Microsoft Excel. Wenn Sie möchten, dass es auf das neue Zielarbeitsblatt verweist, verwenden Sie bitte die Eigenschaft [**CopyOptions.getReferToDestinationSheet()**](https://reference.aspose.com/cells/nodejs-cpp/copyoptions/#getReferToDestinationSheet--) und setzen sie auf **true** beim Aufrufen der Methode [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-). Wenn Ihr Zielarbeitsblatt DestSheet ist, ändert sich die Datenquelle Ihres Diagramms von `=Sheet1!$A$1:$B$4` zu `=DestSheet!$A$1:$B$4`.

## **Ändern der Datenquelle des Diagramms zur Zieltabelle beim Kopieren von Zeilen oder Bereichen**

Der folgende Beispielcode erläutert die Verwendung der [**CopyOptions.getReferToDestinationSheet()**](https://reference.aspose.com/cells/nodejs-cpp/copyoptions/#getReferToDestinationSheet--)-Eigenschaft beim Kopieren von Zeilen oder Bereichen mit Diagrammen in ein neues Arbeitsblatt. Der Code nutzt die [Beispieldatei](5113699.xlsx) und erzeugt die [Ausgabedatei](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load sample excel file
const wb = new AsposeCells.Workbook(filePath);

// Access the first sheet which contains chart
const source = wb.getWorksheets().get(0);

// Add another sheet named DestSheet
const destination = wb.getWorksheets().add("DestSheet");

// Set CopyOptions.ReferToDestinationSheet to true
const options = new AsposeCells.CopyOptions();
options.setReferToDestinationSheet(true);

// Copy all the rows of source worksheet to destination worksheet which includes chart as well
// The chart data source will now refer to DestSheet
destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options);

// Save workbook in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
