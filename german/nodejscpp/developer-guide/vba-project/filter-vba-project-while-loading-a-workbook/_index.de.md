---
title: VBA Projekt beim Laden einer Arbeitsmappe mit Node.js via C++ filtern
linktitle: Filtern des VBA Projekts beim Laden einer Arbeitsmappe
type: docs
weight: 140
url: /de/nodejs-cpp/filter-vba-project-while-loading-a-workbook/
description: Erfahren Sie, wie man VBA Projekte beim Laden von Excel Arbeitsmappen mit Aspose.Cells for Node.js via C++ filtert.
---

## **VBA-Projekt beim Laden einer Excel-Arbeitsmappe in Node.js via C++ filtern**

Einige .xlsm/.xslb-Dateien enthalten eine extrem große Anzahl von Makros (oder sehr, sehr lange Makros). Aspose.Cells for Node.js via C++ lädt diese (Meta-)Daten beim Öffnen solcher Arbeitsmappen bedingungslos. Sie müssen dies möglicherweise kontrollieren, [**LoadDataFilterOptions**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions), wenn Sie nur Sheet-Namen für eine große Anzahl von Arbeitsmappen extrahieren möchten und somit unbrauchbare Inhalte überspringen. Dieser Filter wird durch die Einführung einer neuen Option, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions), bereitgestellt.

## **Beispielcode**

Der folgende Beispielscode lädt eine Arbeitsmappe so, dass nur das VBA gefiltert wird. Eine Testdatei für dieses Feature können Sie über den folgenden Link herunterladen:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Set the load options, we do not want to load VBA
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Auto);
const loadFilter = new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.VBA);
loadOptions.setLoadFilter(loadFilter);

// Create workbook object from sample excel file using load options
const book = new AsposeCells.Workbook(path.join(sourceDir, "sampleMacroEnabledWorkbook.xlsm"), loadOptions);

// Save the output in pdf format
book.save(outputDir + "OutputSampleMacroEnabledWorkbook.xlsm", AsposeCells.SaveFormat.Xlsm);
```
