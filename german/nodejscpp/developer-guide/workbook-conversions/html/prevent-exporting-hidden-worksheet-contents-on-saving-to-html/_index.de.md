---
title: Verhindern Sie das Exportieren versteckter Arbeitsblatt Inhalte beim Speichern in HTML mit Node.js via C++
linktitle: Verhindern des Exports versteckter Arbeitsblattinhalte beim Speichern als HTML
type: docs
weight: 210
url: /de/nodejs-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Lernen Sie, wie Sie das Exportieren versteckter Arbeitsblatt Inhalte beim Speichern von Excel Dateien in HTML mit Aspose.Cells for Node.js via C++ verhindern.
---

{{% alert color="primary" %}}

Sie können Excel-Arbeitsmappen in HTML speichern. Wenn die Arbeitsmappe jedoch versteckte Arbeitsblätter enthält, exportiert Aspose.Cells standardmäßig die versteckten Inhalte des Arbeitsblatts in das HTML-Ausgabeverzeichnis (_files), das Dateien wie Arbeitsblätter, Bilder, tabstrip.htm, stylesheet.css usw. enthält. Manchmal ist es nicht angemessen, den Inhalt der versteckten Arbeitsblätter auf diese Weise zu exportieren. Zum Beispiel, wenn das versteckte Arbeitsblatt Bilder enthält, die nicht in das Verzeichnis _files exportiert werden sollen.

{{% /alert %}}

Aspose.Cells for Node.js via C++ bietet die [**HtmlSaveOptions.getExportHiddenWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportHiddenWorksheet--)-Eigenschaft. Standardmäßig ist sie auf **true** gesetzt, und versteckte Arbeitsblätter werden in HTML exportiert. Wenn Sie sie auf **false** setzen, exportiert Aspose.Cells keine versteckten Arbeitsblatt-Inhalte.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "WorkbookWithHiddenContent.xlsx"));

// Do not export hidden worksheet contents
const options = new AsposeCells.HtmlSaveOptions();
options.setExportHiddenWorksheet(false);

// Save the workbook
workbook.save(path.join(dataDir, "HtmlWithoutHiddenContent_out.html"), options);
```

{{< app/cells/assistant language="nodejs-cpp" >}}
