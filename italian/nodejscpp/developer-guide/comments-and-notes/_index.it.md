---
title: Gestisci commenti e note con Node.js tramite C++
linktitle: Commenti e note
type: docs
weight: 128
url: /it/nodejs-cpp/comments-and-notes/
description: Inserisci e gestisci commenti o note con Aspose.Cells for Node.js via C++.
keywords: Inserisci commenti, inserisci note con Node.js tramite C++
---

## **Introduzione**

I commenti vengono usati per aggiungere informazioni supplementari alle celle. Aspose.Cells for Node.js via C++ fornisce due metodi per aggiungere commenti alle celle. Il primo è creare commenti in un file di progettazione manualmente. Questi commenti vengono poi importati usando Aspose.Cells. Il secondo è aggiungere commenti usando l'API Aspose.Cells durante l'esecuzione. Questo argomento discute l'aggiunta di commenti alle celle usando l'API Aspose.Cells. Verrà anche spiegato come formattare i commenti.

## **Aggiungere un commento**

Aggiungi un commento a una cella chiamando il metodo [**CommentCollection.add(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#add-number-number-) della collezione [**Comments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection) (incapsulato nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)). Il nuovo oggetto [**Comment**](https://reference.aspose.com/cells/nodejs-cpp/comment) può essere accessibile dalla collezione [**Comments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection) passando l'indice del commento. Dopo aver accesso all'oggetto [**Comment**](https://reference.aspose.com/cells/nodejs-cpp/comment), personalizza la nota del commento usando la proprietà [**getNote()**](https://reference.aspose.com/cells/nodejs-cpp/comment/#getNote--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a comment to "F5" cell
const commentIndex = worksheet.getComments().add("F5");

// Accessing the newly added comment
const comment = worksheet.getComments().get(commentIndex);

// Setting the comment note
comment.setNote("Hello Aspose!");

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Formattazione del commento**

È anche possibile formattare l'aspetto dei commenti configurando la loro altezza, larghezza e impostazioni del carattere.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a comment to "F5" cell
const commentIndex = worksheet.getComments().add("F5");

// Accessing the newly added comment
const comment = worksheet.getComments().get(commentIndex);

// Setting the comment note
comment.setNote("Hello Aspose!");

// Setting the font size of a comment to 14
comment.getFont().setSize(14);

// Setting the font of a comment to bold
comment.getFont().setIsBold(true);

// Setting the height of the font to 10
comment.setHeightCM(10);

// Setting the width of the font to 2
comment.setWidthCM(2);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Aggiungi un'immagine al commento**

Con Microsoft Excel 2007, è anche possibile avere un'immagine come sfondo di un commento di cella. In Excel 2007 questo si realizza seguendo i seguenti passaggi. (Si suppone che tu abbia già aggiunto un commento alla cella.)

1. Fare clic con il pulsante destro del mouse sulla cella che contiene il commento.
1. Selezionare **Mostra/Nascondi commenti**, e cancellare eventuali testi dal commento.
1. Fare clic sul bordo del commento per selezionarlo.
1. Selezionare **Formato**, quindi **Commento**.
1. Nella scheda **Colori e linee**, espandere l'elenco **Colore**.
1. Fare clic su **Effetti di riempimento**.
1. Nella scheda **Immagine**, fare clic su **Seleziona immagine**.
1. Trovare e selezionare l'immagine.
1. Fare clic su **OK** finché tutte le finestre di dialogo non si sono chiuse.

Aspose.Cells fornisce anche questa funzionalità. Di seguito è riportato un esempio di codice che crea un file XLSX da zero, aggiungendo un commento alla cella "A1" con un'immagine impostata come sfondo.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

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
const bmpPath = path.join(dataDir, "logo.jpg");
const bmpData = fs.readFileSync(bmpPath);

// Set image data to the shape associated with the comment
comment.getCommentShape().getFill().setImageData(bmpData);

// Save the workbook
workbook.save(path.join(dataDir, "book1.out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **Argomenti avanzati**
- [Cambia la Direzione del Testo del Commento](/cells/it/nodejs-cpp/change-text-direction-of-the-comment/)
- [Come cambiare il Colore del Testo del Commento](/cells/it/nodejs-cpp/how-to-change-the-comment-font-color/)
- [Come impostare lo sfondo del commento](/cells/it/nodejs-cpp/how-to-set-comment-background/)
- [Commenti in discussione](/cells/it/nodejs-cpp/threaded-comments/)

{{< app/cells/assistant language="nodejs-cpp" >}}
