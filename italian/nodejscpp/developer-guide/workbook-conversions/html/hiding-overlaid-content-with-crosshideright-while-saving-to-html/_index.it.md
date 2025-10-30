---
title: Nascondere contenuto sovrapposto con CrossHideRight durante il salvataggio in HTML con Node.js tramite C++
linktitle: Nascondere il contenuto sovrapposto con CrossHideRight durante il salvataggio in HTML
type: docs
weight: 100
url: /it/nodejs-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
---


## **Possibili Scenari di Utilizzo**

Quando salvi il tuo file Excel in HTML, puoi specificare diversi tipi di incrocio per le stringhe delle celle. Per default, Aspose.Cells genera HTML secondo Microsoft Excel, ma quando cambi il tipo di incrocio in [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype), nasconde tutte le stringhe sul lato destro della cella che sono sovrapposte o si sovrappongono con la stringa della cella.

## **Nascondere il contenuto sovrapposto con CrossHideRight durante il salvataggio in HTML**

Il seguente esempio di codice carica il [file Excel di esempio](64716894.xlsx) e lo salva in [HTML di output](64716893.zip) dopo aver impostato [**HtmlSaveOptions.getHtmlCrossStringType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getHtmlCrossStringType--) come [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype). La schermata spiega come [**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) influenzi l'HTML di output rispetto a quello di default.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Codice di Esempio**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample Excel file
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
const opts = new AsposeCells.HtmlSaveOptions();
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.CrossHideRight);

// Save to HTML with HtmlSaveOptions
workbook.save(path.join(dataDir, "outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html"), opts);
``` 
{{< app/cells/assistant language="nodejs-cpp" >}}
