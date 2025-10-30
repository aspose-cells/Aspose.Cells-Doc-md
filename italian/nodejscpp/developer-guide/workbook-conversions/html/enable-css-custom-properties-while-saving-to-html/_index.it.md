---
title: Abilitare Proprietà Personalizzate CSS durante il salvataggio in HTML con Node.js tramite C++
linktitle: Abilita le Proprietà Personalizzate CSS durante il salvataggio in HTML
type: docs
weight: 320
url: /it/nodejs-cpp/enable-css-custom-properties-while-saving-to-html/
description: Impara come abilitare le proprietà CSS personalizzate durante il salvataggio dei file Excel in HTML usando Aspose.Cells for Node.js via C++. 
---

## **Possibili Scenari di Utilizzo**

Quando salvi il file Excel in HTML, per lo scenario in cui ci sono più occorrenze di un'immagine base64, con proprietà personalizzate i dati dell'immagine devono essere salvati una sola volta, migliorando così le prestazioni dell'HTML risultante. Usa la proprietà [**HtmlSaveOptions.getEnableCssCustomProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getEnableCssCustomProperties--) e impostala **true** durante il salvataggio in HTML.
![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg) 


## **Abilita le Proprietà CSS Personalizzate durante il salvataggio in HTML**

Il codice di esempio seguente mostra l'uso della proprietà [**HtmlSaveOptions.getEnableCssCustomProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getEnableCssCustomProperties--). La schermata mostra l'effetto di questa proprietà quando non è impostata su **true**. Scarica il [file Excel di esempio](50528260.xlsx) utilizzato in questo codice e l'[output HTML](50528261.zip) generato per riferimento.



## **Codice di Esempio**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleEnableCssCustomProperties.xlsx"));

const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportImagesAsBase64(true);

// Enable EnableCssCustomProperties
opts.setEnableCssCustomProperties(true);

// Save the workbook in HTML
workbook.save(path.join(dataDir, "outputEnableCssCustomProperties.html"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
