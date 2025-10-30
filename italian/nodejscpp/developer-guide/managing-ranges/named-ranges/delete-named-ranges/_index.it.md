---
title: Elimina intervalli denominati con Node.js tramite C++
linktitle: Eliminare i Nomi Definiti
type: docs
weight: 90
url: /it/nodejs-cpp/Delete-named-ranges/
description: Puoi imparare come rimuovere nomi definiti o intervalli denominati da file Excel o OpenOffice con Aspose.Cells for Node.js via C++.
---

## **Introduzione**
Se ci sono troppi nomi definiti o intervalli nominati nei file Excel, dobbiamo eliminarne alcuni perché non vengono più referenziati.

## **Rimuovere Intervallo Nominato in MS Excel**

Per rimuovere un intervallo nominato da Excel, segui questi passaggi:
1. Apri Microsoft Excel e apri il libro di lavoro che contiene l'intervallo nominato.
2. Vai alla scheda "Formule" nella barra multifunzione di Excel.
3. Fai clic sul pulsante "Gestione nomi" nel gruppo "Nomi definiti". Si aprirà la finestra di dialogo Gestione nomi.
4. Nella finestra di dialogo Gestione nomi, seleziona l'intervallo nominato che desideri rimuovere.
5. Fai clic sul pulsante "Elimina". Conferma l'eliminazione quando richiesto.
6. Fai clic sul pulsante "Chiudi" per chiudere la finestra di dialogo Gestione nomi.
7. Salva il libro di lavoro per mantenere le modifiche.

## **Elimina intervallo denominato usando Aspose.Cells for Node.js via C++**
Con Aspose.Cells for Node.js via C++, puoi rimuovere intervalli denominati o nomi definiti tramite [testo](https://reference.aspose.com/cells/nodejs-cpp/namecollection/#remove-string-) o [indice](https://reference.aspose.com/cells/nodejs-cpp/namecollection/#removeAt-number-) in l'elenco.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted a named range by text.
worksheets.getNames().remove("NamedRange");

// Deleted a defined name by index. Ensure to check the count before removal.
if (worksheets.getNames().getCount() > 0) {
worksheets.getNames().removeAt(0);
}

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```

Nota: se il nome definito è referenziato da formule, non può essere rimosso. Possiamo rimuovere solo la formula del nome definito.

## **Rimuove alcuni intervalli nominati**
Quando rimuoviamo un nome definito, dobbiamo verificare se è referenziato da tutte le formule nel file.
Per migliorare le prestazioni nella rimozione di intervalli denominati, possiamo rimuoverne alcuni insieme.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted some defined names.
worksheets.getNames().remove(["NamedRange1", "NamedRange2"]);

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```

## **Rimuovere Nomi Definiti Duplicati**
Alcuni file Excel si corrompono perché alcuni nomi definiti sono duplicati. Quindi possiamo rimuovere questi nomi duplicati per riparare il file.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Deleted some defined names.
worksheets.getNames().removeDuplicateNames();

// Save the workbook to retain the changes.
workbook.save("Book2.xlsx");
```



{{< app/cells/assistant language="nodejs-cpp" >}}
