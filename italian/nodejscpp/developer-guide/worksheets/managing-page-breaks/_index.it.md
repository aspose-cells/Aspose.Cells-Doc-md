---
title: Gestione delle interruzioni di pagina con Node.js tramite C++
linktitle: Gestione dei salti di pagina
type: docs
weight: 30
url: /it/nodejs-cpp/managing-page-breaks/
description: Questo articolo fornisce codice di esempio e spiega come aggiungere, cancellare o eliminare interruzioni di pagina specifiche nei fogli di lavoro Excel programmaticamente usando Aspose.Cells for Node.js via C++.
keywords: interruzioni di pagina Node.js tramite C++, interruzioni di pagina excel Node.js tramite C++, cancella interruzione di pagina Node.js tramite C++, elimina interruzione di pagina specifica Node.js tramite C++
---

{{% alert color="primary" %}}

Secondo la definizione, un'interruzione di pagina è un punto in un flusso di testo in cui termina una pagina e inizia la successiva. Microsoft Excel consente agli utenti di aggiungere interruzioni di pagina in qualsiasi cella selezionata di un foglio di lavoro.

La posizione della cella in cui viene aggiunta l'interruzione di pagina, la pagina termina e il resto dei dati dopo l'interruzione di pagina viene stampato sulla pagina successiva durante la stampa. In parole semplici, le interruzioni di pagina dividono il foglio di lavoro in più pagine in base alle specifiche. È inoltre possibile aggiungere interruzioni di pagina ai fogli di lavoro durante l'esecuzione utilizzando Aspose.Cells. Aspose.Cells consente agli sviluppatori di aggiungere due tipi di interruzioni di pagina:

- Interruzione di pagina orizzontale
- Interruzione di pagina verticale

Nel resto della discussione, descriveremo come è possibile aggiungere interruzioni di pagina orizzontali o verticali ai fogli di lavoro utilizzando Aspose.Cells.

{{% /alert %}}

## **Interruzioni di pagina**

Aspose.Cells fornisce una classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una collezione di [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che consente l'accesso a ciascun foglio di lavoro nel file Excel.

Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fornisce una vasta gamma di proprietà e metodi utilizzati per gestire un foglio di lavoro.

Per aggiungere le interruzioni di pagina, utilizzare le proprietà [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) e [**Worksheet.getHorizontalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHorizontalPageBreaks--) della classe [**Worksheet.getVerticalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getVerticalPageBreaks--).

Le proprietà [**Worksheet.getHorizontalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHorizontalPageBreaks--) e [**Worksheet.getVerticalPageBreaks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getVerticalPageBreaks--) sono collezioni che possono contenere diverse interruzioni di pagina. Ogni collezione contiene diversi metodi per gestire interruzioni di pagina orizzontali e verticali.

### **Aggiunta dei salti di pagina**

Per aggiungere un'interruzione di pagina in un foglio di lavoro, inserisci interruzioni di pagina verticali e orizzontali alla cella specificata chiamando i metodi [**HorizontalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/horizontalpagebreakcollection/#add-number-number-number-) e [**VerticalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/verticalpagebreakcollection/#add-number-number-number-). Ogni metodo **add** prende il nome della cella in cui deve essere aggiunta l'interruzione.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Add a page break at cell Y30
workbook.getWorksheets().get(0).getHorizontalPageBreaks().add("Y30");
workbook.getWorksheets().get(0).getVerticalPageBreaks().add("Y30");

// Save the Excel file.
workbook.save(path.join(dataDir, "AddingPageBreaks_out.xls"));
```

{{% alert color="primary" %}}

In modalità anteprima interruzione di pagina o anteprima di stampa, è possibile vedere come funzionano queste interruzioni di pagina.

{{% /alert %}}

### **Rimozione di specifiche interruzioni di pagina**

Per rimuovere un’interruzione di pagina specifica, chiama i metodi [**HorizontalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/nodejs-cpp/horizontalpagebreakcollection/#removeAt-number-) e [**VerticalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/nodejs-cpp/verticalpagebreakcollection/#removeAt-number-). Ogni metodo **removeAt** prende come input l’indice dell’interruzione di pagina da rimuovere.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "PageBreaks.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Removing a specific page break
workbook.getWorksheets().get(0).getHorizontalPageBreaks().removeAt(0);
workbook.getWorksheets().get(0).getVerticalPageBreaks().removeAt(0);

// Save the Excel file.
workbook.save(path.join(dataDir, "RemoveSpecificPageBreak_out.xls"));
```

## **Importante sapere**

Quando imposti le proprietà **fitToPages** (cioè [**PageSetup.getFitToPagesTall()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesTall--) e [**PageSetup.getFitToPagesWide()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFitToPagesWide--)) nelle impostazioni di configurazione della pagina, le impostazioni di interruzione di pagina sono influenzate, quindi, se stampi il foglio di lavoro, le impostazioni di interruzione di pagina non vengono considerate, anche se sono ancora impostate.
