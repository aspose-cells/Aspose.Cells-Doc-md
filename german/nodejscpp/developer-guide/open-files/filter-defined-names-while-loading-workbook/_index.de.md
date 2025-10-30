---
title: Gefilterte definierte Namen beim Laden der Arbeitsmappe mit Node.js über C++
linktitle: Definierte Namen filtern beim Laden einer Arbeitsmappe
type: docs
weight: 50
url: /de/nodejs-cpp/filter-defined-names-while-loading-workbook/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells ermöglicht es Ihnen, definierte Namen innerhalb der Arbeitsmappe zu filtern oder zu entfernen. Bitte verwenden Sie [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/), um definierte Namen zu laden, und [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/), um sie beim Laden der Arbeitsmappe zu entfernen. Bitte beachten Sie, dass das Entfernen definierter Namen dazu führen kann, dass Formeln innerhalb der Arbeitsmappe nicht mehr funktionieren.

## **Definierte Namen filtern beim Laden der Arbeitsmappe**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](61767860.xlsx), die eine Formel in Zelle **C1** enthält, die die definierten Namen enthält, d.h. *=SUM(MyName1, MyName2)*. Da wir [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions/) verwenden, um die definierten Namen beim Laden der Arbeitsmappe zu entfernen, wird die Formel in Zelle C1 in der [Ausgabe-Excel-Datei](61767861.xlsx) unterbrochen und stattdessen *#NAME?* angezeigt. Bitte sehen Sie sich den folgenden Screenshot an, der die Auswirkungen des Codes auf die Beispiel-Excel-Datei zeigt.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFilterDefinedNamesWhileLoadingWorkbook.xlsx");
// Specify the load options
let opts = new AsposeCells.LoadOptions();
// We do not want to load defined names
opts.setLoadFilter(new AsposeCells.LoadFilter(~AsposeCells.LoadDataFilterOptions.DefinedNames));

// Load the workbook
const workbook = new AsposeCells.Workbook(filePath, opts);

// Save the output Excel file, it will break the formula in C1
workbook.save(path.join(dataDir, "outputFilterDefinedNamesWhileLoadingWorkbook.xlsx"));

console.log("FilterDefinedNamesWhileLoadingWorkbook executed successfully.");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
