---
title: Come cambiare lo sfondo del commento in Excel con Node.js tramite C++
linktitle: Sfondo del commento
type: docs
weight: 190
url: /it/nodejs-cpp/how-to-set-comment-background/
description: Come cambiare il colore del commento e inserire un’immagine o foto in un commento in Excel utilizzando Aspose.Cells for Node.js via C++.
keywords: Aggiungi un’immagine inserita nel commento con colore di sfondo in Excel Node.js tramite C++
---

{{% alert color="primary" %}}
I commenti sono aggiunti alle celle per registrare commenti, siano essi dettagli su come funziona una formula, da dove proviene un valore o domande dei revisori. I commenti svolgono un ruolo estremamente importante quando più persone discutono o revisionano lo stesso documento in momenti diversi. Come distinguere i commenti di persone diverse? Sì, possiamo impostare un colore di sfondo diverso per ogni commento. Ma quando dobbiamo elaborare molti documenti e molti commenti, farlo manualmente è un disastro. Fortunatamente [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) fornisce un’API che permette di farlo nel codice.
{{% /alert %}}

## **Come cambiare il colore nel commento in Excel**

Se non hai bisogno del colore di sfondo predefinito per i commenti, potresti volerlo sostituire con un colore di tuo interesse. Come posso cambiare il colore di sfondo della casella dei Commenti in Excel?

Il codice seguente ti guiderà su come utilizzare [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) per aggiungere il tuo colore di sfondo preferito ai commenti da scegliere.

Qui abbiamo preparato un [file di esempio](exmaple.xlsx) per te. Questo file viene usato per inizializzare l’oggetto Workbook nel codice sottostante.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Initialize a new workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "example.xlsx"));

// Accessing the newly added comment
const comment = workbook.getWorksheets().get(0).getComments().get(0);

// change background color
const shape = comment.getCommentShape();
shape.getFill().getSolidFill().setColor(AsposeCells.Color.Red);

// Save the Excel file
workbook.save(path.join(dataDir, "result.xlsx"));
```

Esegui il codice sopra e otterrai un file di output (result.xlsx).

## **Come inserire un'immagine o una foto nel commento in Excel**

Microsoft Excel permette agli utenti di personalizzare molto l’aspetto dei fogli di lavoro. È anche possibile aggiungere immagini di sfondo ai commenti. Aggiungere un’immagine di sfondo può essere una scelta estetica o utile per rafforzare il branding.

Il codice di esempio seguente crea un file XLSX da zero usando le API [**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) e aggiunge un commento con uno sfondo di immagine alla cella A1.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook
const workbook = new AsposeCells.Workbook();

// Get a reference of comments collection with the first sheet
const comments = workbook.getWorksheets().get(0).getComments();

// Add a comment to cell A1
const commentIndex = comments.add(0, 0);
const comment = comments.get(commentIndex);
comment.setNote("First note.");
comment.getFont().setName("Times New Roman");

// Load an image into stream
const fs = require("fs");
const bmp = fs.readFileSync(path.join(dataDir, "image2.jpg"));
const ms = Buffer.from(bmp);

// Set image data to the shape associated with the comment
comment.getCommentShape().getFill().setImageData(ms);

// Save the workbook
const outputFilePath = path.join(dataDir, "commentwithpicture1.out.xlsx");
workbook.save(outputFilePath, AsposeCells.SaveFormat.Xlsx);
```

