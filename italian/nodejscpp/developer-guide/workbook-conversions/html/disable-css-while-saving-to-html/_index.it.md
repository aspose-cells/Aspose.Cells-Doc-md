---
title: Disabilitare CSS durante il salvataggio in HTML tramite Node.js tramite C++
linktitle: Disabilitare CSS durante il salvataggio in HTML
type: docs
weight: 320
url: /it/nodejs-cpp/disable-css-while-saving-to-html/
description: Impara come disabilitare il CSS durante il salvataggio di file Excel in HTML usando Aspose.Cells for Node.js via C++. 
---

## **Possibili Scenari di Utilizzo**

Quando salvi il file Excel come HTML a pagina singola, di solito gli elementi CSS saranno incorporati nel file HTML e collocati nella sezione HEAD. Se allegi questo file come contenuto/corpo di un'email, la maggior parte dei client di posta eliminerà gli elementi CSS, risultando in una visualizzazione non corretta. La versione 24.12 di Aspose.Cells introduce un'opzione che permette di disabilitare opzionalmente il CSS, consentendo di applicare gli stili direttamente agli elementi HTML stessi. Se vuoi impostare l'HTML come contenuto/corpo dell'email, usa la proprietà [**HtmlSaveOptions.getDisableCss()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableCss--) e impostala su **true**.

## **Disabilita CSS durante il salvataggio in HTML**

Il seguente esempio di codice mostra l'uso della proprietà [**HtmlSaveOptions.getDisableCss()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableCss--). 

## **Codice di Esempio**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleDisableCss.xlsx"));

// Disable CSS
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDisableCss(true);

// Save the workbook in HTML
workbook.save(path.join(outputDir, "outputDisable.html"), opts);
```
