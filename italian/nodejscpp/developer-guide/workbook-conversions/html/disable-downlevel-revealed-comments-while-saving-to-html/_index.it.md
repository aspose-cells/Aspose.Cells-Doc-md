---
title: Disabilitare Commenti Downlevel Revealed durante il salvataggio in HTML con Node.js tramite C++
linktitle: Disabilitare i commenti rivelati di livello inferiore durante il salvataggio in formato HTML
type: docs
weight: 20
url: /it/nodejs-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: Impara come disabilitare i commenti Downlevel Revealed quando si salva un file Excel come HTML usando Aspose.Cells for Node.js via C++.
---

## **Possibili Scenari di Utilizzo**

Quando salvi il file Excel in HTML, Aspose.Cells rivela i Commenti Condizionali Downlevel. Questi commenti condizionali sono rilevanti principalmente per le vecchie versioni di Internet Explorer e irrilevanti per i browser moderni. Puoi leggere i dettagli al seguente link.

- [Commento condizionale - Commento condizionale rivelato di livello inferiore](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells for Node.js via C++ ti permette di eliminare questi Commenti Downlevel Revealed impostando la proprietà [**HtmlSaveOptions.getDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableDownlevelRevealedComments--) su **true**.

## **Disabilita i Commenti Rivelati di Basso Livello durante il Salvataggio in HTML**

Il seguente esempio di codice mostra l'uso della proprietà [**HtmlSaveOptions.getDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableDownlevelRevealedComments--). La schermata mostra l'effetto di questa proprietà quando non è impostata su true. Per favore scarica il [file Excel di esempio](50528257.xlsx) usato in questo codice e l'[output HTML](50528258.zip) generato per riferimento.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Codice di Esempio**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleDisableDownlevelRevealedComments.xlsx"));

// Disable DisableDownlevelRevealedComments
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDisableDownlevelRevealedComments(true);

// Save the workbook in html
workbook.save(path.join(outputDir, "outputDisableDownlevelRevealedComments_true.html"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
