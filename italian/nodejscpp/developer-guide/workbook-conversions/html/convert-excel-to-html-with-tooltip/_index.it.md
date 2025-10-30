---  
title: Converti Excel in HTML con tooltip usando Node.js tramite C++  
linktitle: Convertire Excel in HTML con tooltip  
type: docs  
weight: 200  
url: /it/nodejs-cpp/convert-excel-to-html-with-tooltip/  
description: Scopri come convertire file Excel in formato HTML con tooltip per visualizzare il testo completo usando Aspose.Cells for Node.js via C++.  
---  

## **Convertire Excel in HTML con tooltip**

Potrebbero esserci casi in cui il testo viene tagliato nell'HTML generato e vuoi visualizzare il testo completo come tooltip al passaggio del mouse. Aspose.Cells for Node.js via C++ supporta questa funzionalità fornendo la proprietà [**HtmlSaveOptions.getAddTooltipText()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getAddTooltipText--). Impostare la proprietà [**HtmlSaveOptions.getAddTooltipText()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getAddTooltipText--) a **true** aggiungerà il testo completo come tooltip nell'HTML generato.

Nell'immagine seguente è mostrato il tooltip nel file HTML generato.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Il seguente esempio di codice carica il [file Excel sorgente](98107416.xlsx) e genera il [file HTML di output](98107417.zip) con il tooltip.

Codice di Esempio

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "AddTooltipToHtmlSample.xlsx"));

const options = new AsposeCells.HtmlSaveOptions();
options.setAddTooltipText(true);

// Save as Markdown
workbook.save(path.join(outputDir, "AddTooltipToHtmlSample_out.html"), options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
