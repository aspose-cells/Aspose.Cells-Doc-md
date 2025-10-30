---
title: Crea e gestisci tabelle di file Microsoft Excel con Node.js tramite C++
linktitle: Tabelle
type: docs
weight: 150
url: /it/nodejs-cpp/create-and-format-table/
description: Inserisci, ridimensiona, modifica, elimina e formatta tabelle di file Excel usando Aspose.Cells for Node.js via C++.
---

## **Creare una tabella**

Uno dei vantaggi dei fogli di calcolo è che consentono di creare diversi tipi di elenchi, ad esempio elenchi telefonici, elenchi delle attività, elenchi di transazioni, attivi o passivi. Diversi utenti possono lavorare insieme per utilizzare, creare e mantenere vari elenchi.

Aspose.Cells supporta la creazione e la gestione di elenchi.

### **Vantaggi di un oggetto elenco**

Ci sono diversi vantaggi quando si converte un elenco di dati in un vero oggetto elenco

- Nuove righe e colonne vengono automaticamente incluse.
- Una riga di totale in fondo al tuo elenco può essere facilmente aggiunta per visualizzare SOMMA, MEDIA, CONTEGGIO, ecc.
- Le colonne aggiunte a destra vengono automaticamente incorporate nell'oggetto Elenco.
- I grafici basati su righe e colonne verranno espansi automaticamente.
- I nomi definiti assegnati a righe e colonne verranno espansi automaticamente.
- L'elenco è protetto dalla cancellazione accidentale di righe e colonne.

### **Creazione di un oggetto elenco utilizzando Microsoft Excel**

- Selezionare l'intervallo di dati per creare un oggetto Lista
- Questo visualizza il dialogo Crea elenco.
- Implementare l'oggetto Lista per i dati e specificare la riga totale (Seleziona **Dati**, poi **Lista**, seguito da **Riga Totale**).

### **Utilizzando l'API di Aspose.Cells**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una collezione [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che consente di accedere a ciascun foglio di lavoro in un file Excel.

Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fornisce un'ampia gamma di proprietà e metodi per la gestione di un foglio di lavoro. Per creare un [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) in un foglio di lavoro, usa la proprietà di raccolta [**getListObjects()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getListObjects--) della classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Ogni [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) è, infatti, un oggetto della classe [**ListObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/), che ulteriormente fornisce il metodo [**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/#add-number-number-number-number-boolean-) per aggiungere un oggetto Lista e specificare un intervallo di celle per la lista.

In base all'intervallo di celle specificato, l'oggetto Lista viene creato da Aspose.Cells. Usa gli attributi (ad esempio, [**getShowTotals()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getShowTotals--), [**getListColumns()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getListColumns--), ecc.) della classe [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) per controllare la lista.

Nell'esempio seguente, abbiamo creato lo stesso [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) usando l'API di Aspose.Cells come abbiamo fatto con Microsoft Excel nella sezione sopra.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Create a Workbook object.
// Open a template excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Get the List objects collection in the first worksheet.
const listObjects = workbook.getWorksheets().get(0).getListObjects();

// Add a List based on the data source range with headers on.
listObjects.add(1, 1, 7, 5, true);

// Show the total row for the List.
listObjects.get(0).setShowTotals(true);

// Calculate the total of the last (5th) list column.
listObjects.get(0).getListColumns().get(4).setTotalsCalculation(AsposeCells.TotalsCalculation.Sum);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```

## **Formattare una tabella**

Per gestire e analizzare un gruppo di dati correlati, è possibile trasformare un intervallo di celle in un oggetto elenco (noto anche come tabella di Excel). Una tabella è una serie di righe e colonne che contengono dati correlati gestiti indipendentemente dai dati in altre righe e colonne. Per impostazione predefinita, ogni colonna nella tabella ha abilitata la funzione di filtro nella riga di intestazione in modo da poter filtrare o ordinare rapidamente i dati dell'oggetto elenco. È possibile aggiungere una riga totale (una riga speciale in un elenco che fornisce una selezione di funzioni aggregate utili per lavorare con dati numerici) all'oggetto elenco che fornisce un elenco a discesa di funzioni aggregate per ogni cella di riga totale. Aspose.Cells fornisce opzioni per la creazione e la gestione di elenchi (o tabelle).

### **Formattazione di un oggetto elenco**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una collezione [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che consente di accedere a ciascun foglio di lavoro in un file Excel.

Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) offre una vasta gamma di proprietà e metodi per la gestione dei fogli di lavoro. Per creare un [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) in un foglio di lavoro, usa la proprietà di raccolta [**getListObjects()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getListObjects--) della classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Ogni [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) è, infatti, un oggetto della classe [**ListObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/), che fornisce ulteriormente il metodo [**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/#add-number-number-number-number-boolean-) per aggiungere un oggetto Lista e specificare l'intervallo di celle che dovrebbe abbracciare. In base all'intervallo di celle specificato, viene creato nel foglio di lavoro un [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) da Aspose.Cells. Usa gli attributi (ad esempio, [**TableStyleType**](https://reference.aspose.com/cells/nodejs-cpp/tablestyletype/)) della classe [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) per formattare il tavolo secondo i tuoi requisiti.

L'esempio seguente aggiunge dati di esempio a un foglio di lavoro, aggiunge un [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) e applica stili predefiniti. Gli stili [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) sono supportati da Microsoft Excel 2007/2010.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook.
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the default(first) worksheet
const sheet = workbook.getWorksheets().get(0);

// Obtaining Worksheet's cells collection
const cells = sheet.getCells();

// Setting the value to the cells
cells.get(1, 1).putValue("Employee");
cells.get(1, 2).putValue("Quarter");
cells.get(1, 3).putValue("Product");
cells.get(1, 4).putValue("Continent");
cells.get(1, 5).putValue("Country");
cells.get(1, 6).putValue("Sale");

cells.get(2, 1).putValue("David");
cells.get(3, 1).putValue("David");
cells.get(4, 1).putValue("David");
cells.get(5, 1).putValue("David");
cells.get(6, 1).putValue("James");
cells.get(7, 1).putValue("James");
cells.get(8, 1).putValue("James");
cells.get(9, 1).putValue("James");
cells.get(10, 1).putValue("James");
cells.get(11, 1).putValue("Miya");
cells.get(12, 1).putValue("Miya");
cells.get(13, 1).putValue("Miya");
cells.get(14, 1).putValue("Miya");
cells.get(15, 1).putValue("Miya");
cells.get(2, 2).putValue(1);
cells.get(3, 2).putValue(2);
cells.get(4, 2).putValue(3);
cells.get(5, 2).putValue(4);
cells.get(6, 2).putValue(1);
cells.get(7, 2).putValue(2);
cells.get(8, 2).putValue(3);
cells.get(9, 2).putValue(4);
cells.get(10, 2).putValue(4);
cells.get(11, 2).putValue(1);
cells.get(12, 2).putValue(1);
cells.get(13, 2).putValue(2);
cells.get(14, 2).putValue(2);
cells.get(15, 2).putValue(2);

cells.get(2, 3).putValue("Maxilaku");
cells.get(3, 3).putValue("Maxilaku");
cells.get(4, 3).putValue("Chai");
cells.get(5, 3).putValue("Maxilaku");
cells.get(6, 3).putValue("Chang");
cells.get(7, 3).putValue("Chang");
cells.get(8, 3).putValue("Chang");
cells.get(9, 3).putValue("Chang");
cells.get(10, 3).putValue("Chang");
cells.get(11, 3).putValue("Geitost");
cells.get(12, 3).putValue("Chai");
cells.get(13, 3).putValue("Geitost");
cells.get(14, 3).putValue("Geitost");
cells.get(15, 3).putValue("Geitost");

cells.get(2, 4).putValue("Asia");
cells.get(3, 4).putValue("Asia");
cells.get(4, 4).putValue("Asia");
cells.get(5, 4).putValue("Asia");
cells.get(6, 4).putValue("Europe");
cells.get(7, 4).putValue("Europe");
cells.get(8, 4).putValue("Europe");
cells.get(9, 4).putValue("Europe");
cells.get(10, 4).putValue("Europe");
cells.get(11, 4).putValue("America");
cells.get(12, 4).putValue("America");
cells.get(13, 4).putValue("America");
cells.get(14, 4).putValue("America");
cells.get(15, 4).putValue("America");

cells.get(2, 5).putValue("China");
cells.get(3, 5).putValue("India");
cells.get(4, 5).putValue("Korea");
cells.get(5, 5).putValue("India");
cells.get(6, 5).putValue("France");
cells.get(7, 5).putValue("France");
cells.get(8, 5).putValue("Germany");
cells.get(9, 5).putValue("Italy");
cells.get(10, 5).putValue("France");
cells.get(11, 5).putValue("U.S.");
cells.get(12, 5).putValue("U.S.");
cells.get(13, 5).putValue("Brazil");
cells.get(14, 5).putValue("U.S.");
cells.get(15, 5).putValue("U.S.");

cells.get(2, 6).putValue(2000);
cells.get(3, 6).putValue(500);
cells.get(4, 6).putValue(1200);
cells.get(5, 6).putValue(1500);
cells.get(6, 6).putValue(500);
cells.get(7, 6).putValue(1500);
cells.get(8, 6).putValue(800);
cells.get(9, 6).putValue(900);
cells.get(10, 6).putValue(500);
cells.get(11, 6).putValue(1600);
cells.get(12, 6).putValue(600);
cells.get(13, 6).putValue(2000);
cells.get(14, 6).putValue(500);
cells.get(15, 6).putValue(900);

// Adding a new List Object to the worksheet
const index = sheet.getListObjects().add("A1", "F15", true);

const listObject = sheet.getListObjects().get(index);

// Adding Default Style to the table
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium10);

// Show Total
listObject.setShowTotals(true);

// Set the Quarter field's calculation type
listObject.getListColumns().get(1).setTotalsCalculation(AsposeCells.TotalsCalculation.Count);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```

## **Argomenti avanzati**
- [Convertire la tabella in ODS](/cells/it/nodejs-cpp/convert-table-to-ods/)
- [Trova query tabelle e oggetti elenco relativi alle connessioni esterne dei dati](/cells/it/nodejs-cpp/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Leggere e scrivere una tabella con dati della tabella di query](/cells/it/nodejs-cpp/read-and-write-table-with-query-table-data-source/)
- [Imposta il commento della tabella o dell'oggetto lista all'interno del foglio di lavoro](/cells/it/nodejs-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Tabelle e intervalli](/cells/it/nodejs-cpp/tables-and-ranges/)

{{< app/cells/assistant language="nodejs-cpp" >}}
