---
title: Länge führender Leerzeilen und spalten beim Exportieren von Tabellenkalkulationen in CSV Format mit Node.js durch C++ kürzen
linktitle: Abschneiden führender Leerzeilen und spalten beim Exportieren von Tabellenkalkulationen in das CSV Format
type: docs
weight: 100
url: /de/nodejs-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Lernen Sie, wie Sie führende leere Zeilen und Spalten beim Exportieren von Tabellenkalkulationen in CSV Format mit Aspose.Cells for Node.js via C++ kürzen.
---

## **Mögliche Verwendungsszenarien**

Manchmal enthält Ihre Excel- oder CSV-Datei führende leere Spalten oder Zeilen. Beispielweise betrachten Sie diese Zeile

{{< highlight javascript >}}

 ,,,data1,data2

{{< /highlight >}}

Hier sind die ersten drei Zellen oder Spalten leer. Wenn Sie eine solche CSV-Datei in Microsoft Excel öffnen, verwirft Microsoft Excel diese führenden leeren Zeilen und Spalten.

Standardmäßig entfernt Aspose.Cells for Node.js via C++ beim Speichern keine führenden leeren Spalten und Zeilen, aber wenn Sie sie entfernen möchten, wie es Microsoft Excel macht, bietet Aspose.Cells die [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--)-Eigenschaft. Setzen Sie sie auf **true**, und alle führenden leeren Zeilen und Spalten werden beim Speichern verworfen.

{{% alert color="primary" %}}

Vor der Veröffentlichung von Aspose.Cells for Node.js via C++ 20.4 war der Standardwert von [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) **false**. Seit der Version 20.4 ist der Standardwert von [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--) **true**.

{{% /alert %}}

## **Führende leere Zeilen und Spalten beim Export von Tabellenkalkulationen in das CSV-Format abschneiden**

Der folgende Beispielcode lädt die [Quellexcel-Datei](sampleTrimBlankColumns.xlsx), die zwei führende leere Spalten enthält. Er speichert die Excel-Datei zuerst im CSV-Format ohne Änderungen und setzt dann die [**TxtSaveOptions.getTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getTrimLeadingBlankRowAndColumn--)-Eigenschaft auf **true**, um sie erneut zu speichern. Der Screenshot zeigt die [Quellexcel-Datei](sampleTrimBlankColumns.xlsx), die [CSV-Ausgabedatei ohne Kürzung](outputWithoutTrimBlankColumns.csv) und die [CSV-Ausgabedatei mit Kürzung](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

## **Beispielcode**

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
