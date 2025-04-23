---  
title: Nicht verwendete Stile bei Excel zu HTML Konvertierung mit Node.js über C++ ausschließen  
linktitle: Nicht verwendete Styles bei der Excel zu HTML Konvertierung ausschließen  
type: docs  
weight: 30  
url: /de/nodejs-cpp/exclude-unused-styles-during-excel-to-html-conversion/  
description: Lernen Sie, wie Sie nicht verwendete Stile beim Konvertieren von Excel zu HTML mit Aspose.Cells for Node.js via C++ ausschließen.  
---  

## **Mögliche Verwendungsszenarien**  

Microsoft Excel-Dateien können viele ungenutzte Stile enthalten. Beim Export in das HTML-Format werden diese ungenutzten Stile ebenfalls exportiert, was die HTML-Größe vergrößern kann. Sie können die ungenutzten Stile beim Konvertieren von Excel in HTML mithilfe der Eigenschaft [**HtmlSaveOptions.getExcludeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExcludeUnusedStyles--) ausschließen. Ist sie auf **true** gesetzt, werden alle ungenutzten Stile vom HTML ausgeschlossen. Das folgende Beispiel zeigt einen Beispiel-ungenuzten Stil im Ausgab-HTML.  

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)  

## **Ausnutzen nicht verwendeter Stile während der Konvertierung von Excel in HTML ausschließen**  

Der folgende Beispielcode erstellt eine Arbeitsmappe und einen ungenutzten benannten Stil. Da [**HtmlSaveOptions.getExcludeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExcludeUnusedStyles--) auf **true** gesetzt ist, wird dieser ungenutzte benannte Stil nicht in [HTML-Ausgabe](61767778.zip) exportiert. Wenn Sie ihn auf **false** setzen, erscheint dieser ungenutzte Stil im Ausgabe-HTML, was im HTML-Markup sichtbar ist, wie im vorherigen Screenshot gezeigt.  

## **Beispielcode**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook
const wb = new AsposeCells.Workbook();

// Create an unused named style
wb.createStyle().setName("UnusedStyle_XXXXXXXXXXXXXX");

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Put some value in cell C7
ws.getCells().get("C7").putValue("This is sample text.");

// Specify html save options, we want to exclude unused styles
const opts = new AsposeCells.HtmlSaveOptions();

// Comment this line to include unused styles
opts.setExcludeUnusedStyles(true);

// Save the workbook in html format
wb.save("outputExcludeUnusedStylesInExcelToHTML.html", opts);
```  

