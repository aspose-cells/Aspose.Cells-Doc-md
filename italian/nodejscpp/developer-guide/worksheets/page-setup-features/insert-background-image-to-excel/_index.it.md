---
title: Inserisci immagine di sfondo in Excel con Node.js tramite C++
linktitle: Inserire un immagine di sfondo in Excel
type: docs
weight: 90
url: /it/nodejs-cpp/insert-background-image-to-excel/
description: Come inserire immagine di sfondo in Excel usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}} 

Puoi rendere un foglio di lavoro più accattivante aggiungendo un'immagine come sfondo del foglio. Questa funzionalità può essere molto efficace se hai una grafica aziendale speciale che aggiunge un tocco di sfondo senza oscurare i dati nel foglio. Puoi impostare l'immagine di sfondo per un foglio utilizzando l'API Aspose.Cells.

{{% /alert %}} 

## **Impostare lo sfondo del foglio in Microsoft Excel**

Impostare un'immagine di sfondo di un foglio in Microsoft Excel (ad esempio, Microsoft Excel 2019):

1. Dal menu **Layout di pagina**, individuare l'opzione **Imposta pagina** e fare clic sull'opzione **Sfondo**.
1. Seleziona un'immagine da impostare come sfondo del foglio.

   **Impostazione di uno sfondo del foglio**

![todo:image_alt_text](insert-background-to-excel.jpg)

## **Impostare lo sfondo del foglio con Aspose.Cells for Node.js via C++**

Il codice di seguito imposta un'immagine di sfondo utilizzando un'immagine da un flusso.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const backgroundImagePath = path.join(dataDir, "background.jpg");

// Create a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Set the background image for the worksheet.
sheet.setBackgroundImage(fs.readFileSync(backgroundImagePath).buffer);

// Save the Excel file
workbook.save("outputBackImageSheet.xlsx");

// Save the HTML file
workbook.save("outputBackImageSheet.html", AsposeCells.SaveFormat.Html);
```

## Articoli correlati

- [Lavorare con lo sfondo nei file ODS](/cells/it/nodejs-cpp/working-with-background-in-ods-files/)

