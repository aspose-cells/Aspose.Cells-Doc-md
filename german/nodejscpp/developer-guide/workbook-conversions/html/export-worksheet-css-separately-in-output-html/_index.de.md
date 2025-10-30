---  
title: Exportiere Arbeitsblatt CSS separat im Ausgab HTML mit Node.js via C++  
linktitle: Arbeitsblatt CSS separat im ausgegebenen HTML exportieren  
type: docs  
weight: 80  
url: /de/nodejs-cpp/export-worksheet-css-separately-in-output/  
description: Lernen Sie, wie Sie Arbeitsblatt CSS separat exportieren, wenn Sie eine Excel Datei mit Aspose.Cells for Node.js via C++ in HTML konvertieren.  
---  

## **Mögliche Verwendungsszenarien**

Aspose.Cells for Node.js via C++ bietet die Funktion, Arbeitsblatt-CSS separat zu exportieren, wenn Sie Ihre Excel-Datei in HTML umwandeln. Bitte verwenden Sie die [**HtmlSaveOptions.getExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetCSSSeparately--)-Eigenschaft hierfür und setzen Sie sie beim Speichern der Excel-Datei im HTML-Format auf **true**.

## **Arbeitsblatt-CSS separat im ausgegebenen HTML exportieren**

Der folgende Beispielcode erstellt eine Excel-Datei, fügt Text in Zelle **B5** in **Rot** farbe hinzu und speichert sie dann im HTML-Format mit [**HtmlSaveOptions.getExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetCSSSeparately--)-Eigenschaft. Bitte sehen Sie die [Ausgab-HTML](60489766.zip), die vom Code generiert wurde, zur Referenz. Im Archiv finden Sie **stylesheet.css** als Ergebnis des Beispielcodes.

## **Beispielcode**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and put value inside it
const cell = ws.getCells().get("B5");
cell.putValue("This is some text.");

// Set the style of the cell - font color is Red
const st = cell.getStyle();
st.getFont().setColor(AsposeCells.Color.Red);
cell.setStyle(st);

// Specify html save options - export worksheet css separately
const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportWorksheetCSSSeparately(true);

// Save the workbook in html 
wb.save("outputExportWorksheetCSSSeparately.html", opts);
```

## **Einzelarbeitsblatt-Arbeitsmappe in HTML exportieren**

Wenn eine Arbeitsmappe mit mehreren Blättern mit Aspose.Cells for Node.js via C++ in HTML konvertiert wird, erstellt sie eine HTML-Datei zusammen mit einem Ordner, der CSS und mehrere HTML-Dateien enthält. Wenn diese HTML-Datei im Browser geöffnet wird, sind die Registerkarten sichtbar. Das gleiche Verhalten ist bei einer Arbeitsmappe mit nur einem Arbeitsblatt erforderlich, wenn sie in HTML umgewandelt wird. Früher wurde für Arbeitsmappen mit nur einem Blatt kein separater Ordner erstellt, sondern nur eine HTML-Datei. Eine solche HTML-Datei zeigt beim Öffnen im Browser keine Registerkarten. MS Excel erstellt auch für ein einzelnes Arbeitsblatt einen passenden Ordner und HTML, daher wurde dasselbe Verhalten mit Aspose.Cells APIs implementiert. Die Beispieldatei kann unter folgendem Link für den Einsatz im untenstehenden Beispielcode heruntergeladen werden:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Beispielcode**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleSingleSheet.xlsx");
// Load the sample Excel file containing single sheet only
const wb = new AsposeCells.Workbook(sourceFilePath);

// Specify HTML save options
const options = new AsposeCells.HtmlSaveOptions();

// Set optional settings if required
options.setEncoding(AsposeCells.EncodingType.UTF8);
options.setExportImagesAsBase64(true);
options.setExportGridLines(true);
options.setExportSimilarBorderStyle(true);
options.setExportBogusRowData(true);
options.setExcludeUnusedStyles(true);
options.setExportHiddenWorksheet(true);

// Save the workbook in Html format with specified Html Save Options
wb.save(path.join(dataDir, "outputSampleSingleSheet.htm"), options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
