---
title: Formattare celle con Node.js tramite C++
description: Impara come formattare e stilizzare le celle in Aspose.Cells for Node.js via C++, inclusi formato numerico, formato data, stili di carattere e altre opzioni di stile delle celle. La nostra guida ti aiuterà a creare fogli di calcolo attraenti e dall aspetto professionale.
keywords: Aspose.Cells for Node.js via C++, formattazione celle, stile, formato numerico, formato data, stile carattere, opzioni di stile delle celle, foglio di calcolo, creare, aspetto professionale, formattare righe e colonne.
linktitle: Formattare celle
type: docs
weight: 120
url: /it/nodejs-cpp/cells-formatting/
---

## **Introduzione**

{{% alert color="primary" %}}

Aspose.Cells fornisce i metodi [**getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) e [**setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) della classe [Cell](https://reference.aspose.com/cells/nodejs-cpp/cell), usati per ottenere/impostare lo stile di formattazione di una cella. Aspose.Cells fornisce anche una classe [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style).

{{% /alert %}}

## **Come formattare le celle utilizzando i metodi GetStyle e SetStyle**

Applicare diversi tipi di stili di formattazione alle celle per impostare colori di sfondo o primo piano, bordi, caratteri, allineamenti orizzontali e verticali, livello di rientro, direzione del testo, angolo di rotazione e molto altro.

### **Come utilizzare i metodi GetStyle e SetStyle**

Se gli sviluppatori devono applicare stili di formattazione diversi a diverse celle, è meglio ottenere [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) della cella usando il metodo [**Cell.getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--), specificare gli attributi di stile e poi applicare la formattazione usando il metodo [**Cell.setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-). Un esempio viene mostrato di seguito per dimostrare questo approccio di applicazione di varie formattazioni su una cella.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Defining a Style object
let style;

// Get the style from A1 cell
style = cell.getStyle();

// Setting the vertical alignment
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text
style.getFont().setColor(AsposeCells.Color.Green);

// Setting to shrink according to the text contained in it
style.setShrinkToFit(true);

// Setting the bottom border color to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Applying the style to A1 cell
cell.setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Come utilizzare l'oggetto stile per formattare celle diverse**

Se gli sviluppatori devono applicare lo stesso stile di formattazione a celle diverse, possono utilizzare l'oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). Seguire i passaggi di seguito per usare l'oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style):

1. Aggiungere un oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) chiamando il metodo [**createStyle()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#createStyle--) della classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)
2. Accedere all'oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) appena aggiunto
3. Impostare le proprietà/attributi desiderati dell'oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) per applicare le impostazioni di formattazione desiderate
4. Assegnare l'oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) configurato alle celle desiderate

Questo approccio può migliorare notevolmente l'efficienza delle tue applicazioni e risparmiare memoria anche.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the first worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Adding a new Style
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Assigning the Style object to the "A1" cell
cell.setStyle(style);

// Apply the same style to some other cells
worksheet.getCells().get("B1").setStyle(style);
worksheet.getCells().get("C1").setStyle(style);
worksheet.getCells().get("D1").setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Come utilizzare gli stili predefiniti di Microsoft Excel 2007**

Se è necessario applicare stili di formattazione diversi per Microsoft Excel 2007, applicare gli stili utilizzando l'API Aspose.Cells. Di seguito viene fornito un esempio per dimostrare questo approccio per applicare uno stile predefinito su una cella.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");


// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Create a style object.
const style = workbook.createStyle();

// Input a value to A1 cell.
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Test");

// Apply the style to the cell.
workbook.getWorksheets().get(0).getCells().get("A1").setStyle(style);

// Save the Excel 2007 file.
workbook.save(path.join(dataDir, "book1.out.xlsx"));
```



## **Come formattare i caratteri selezionati in una cella**

Il trattamento delle impostazioni del carattere spiega come formattare il testo nelle celle, ma spiega solo come formattare tutto il contenuto della cella. E se si vuole formattare solo alcuni caratteri?

Anche Aspose.Cells supporta questa funzione. Questo argomento spiega come utilizzare questa funzione efficacemente.

### **Come formattare caratteri selezionati**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene la collezione [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che consente l'accesso a ogni foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) offre una collezione [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Ogni elemento della collezione [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).

La classe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) fornisce il metodo [**characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#characters-number-number-) che accetta i seguenti parametri per selezionare una gamma di caratteri all’interno di una cella:

- **Indice di inizio**, l'indice del carattere da cui inizia la selezione.
- **Numero di caratteri**, il numero di caratteri da selezionare.

Il metodo [**characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#characters-number-number-) restituisce un'istanza della classe [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting) che consente agli sviluppatori di formattare i caratteri nello stesso modo in cui si formattava una cella, come mostrato nell'esempio di codice sottostante. Nel file di output, nella cella A1, la parola 'Visit' sarà formattata con il font predefinito, mentre 'Aspose!' sarà in grassetto e blu.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first(default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Visit Aspose!");

// Setting the font of selected characters to bold
const font = cell.characters(6, 7).getFont();
font.isBold = true;

// Setting the font color of selected characters to blue
font.color = AsposeCells.Color.Blue;

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

{{% alert color="primary" %}}

Se si desidera formattare una parte del testo arricchito (Rich Text) in una cella, considerare l’uso dei metodi [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) e [**Cell.setCharacters(FontSetting[])**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-). Il metodo [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) viene utilizzato per accedere alle parti del testo e quindi apportare modifiche tramite il metodo [**Cell.setCharacters(FontSetting[])**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-), mentre il metodo **Get** restituisce un array di oggetti [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting) che possono essere manipolati per impostare varie proprietà come nome del font, colore del font, grassetto, ecc. e il metodo **Set** può essere usato per applicare le modifiche.

{{% /alert %}}

## **Come formattare righe e colonne**

A volte i developer devono applicare la stessa formattazione su righe o colonne. Applicare la formattazione alle celle una per una richiede spesso più tempo e non è una buona soluzione.
Per affrontare questo problema, Aspose.Cells fornisce un modo semplice e veloce discusso dettagliatamente in questo articolo.

### **Formattare Righe e Colonne**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una collezione [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) che consente l'accesso a ogni foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fornisce una collezione [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). La collezione [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) fornisce una collezione [**getRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRows--).

### **Come formattare una riga**

Ogni elemento della collezione [**getRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRows--) rappresenta un oggetto [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row). L'oggetto [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row) offre il metodo [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-) usato per impostare la formattazione della riga. Per applicare la stessa formattazione a una riga, utilizzare l’oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). I passaggi seguenti mostrano come utilizzarlo.

1. Aggiungere un oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) alla classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) chiamando il suo metodo [**createStyle()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#createStyle--).
2. Impostare le proprietà dell’oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) per applicare le impostazioni di formattazione.
3. Rendere attivi gli attributi rilevanti per l’oggetto [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag).
4. Assegnare l’oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) configurato all’oggetto [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first (default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Adding a new Style to the styles
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Creating StyleFlag
const styleFlag = new AsposeCells.StyleFlag();
styleFlag.setHorizontalAlignment(true);
styleFlag.setVerticalAlignment(true);
styleFlag.setShrinkToFit(true);
styleFlag.setBorders(true);
styleFlag.setFontColor(true);

// Accessing a row from the Rows collection
const row = worksheet.getCells().getRows().get(0);

// Assigning the Style object to the Style property of the row
row.applyStyle(style, styleFlag);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Come formattare una colonna**

La collezione [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) fornisce anche una collezione [**getColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getColumns--). Ogni elemento della collezione [**getColumns()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getColumns--) rappresenta un oggetto [**Column**](https://reference.aspose.com/cells/nodejs-cpp/column). Similmente a un oggetto [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row), anche l’oggetto [**Column**](https://reference.aspose.com/cells/nodejs-cpp/column) offre il metodo [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-) per formattare una colonna.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the first (default) worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(0);

// Adding a new Style to the styles
const style = workbook.createStyle();

// Setting the vertical alignment of the text in the "A1" cell
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the horizontal alignment of the text in the "A1" cell
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);

// Setting the font color of the text in the "A1" cell
style.getFont().setColor(AsposeCells.Color.Green);

// Shrinking the text to fit in the cell
style.setShrinkToFit(true);

// Setting the bottom border color of the cell to red
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Red);

// Setting the bottom border type of the cell to medium
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Medium);

// Creating StyleFlag
const styleFlag = new AsposeCells.StyleFlag();
styleFlag.setHorizontalAlignment(true);
styleFlag.setVerticalAlignment(true);
styleFlag.setShrinkToFit(true);
styleFlag.setBorders(true);
styleFlag.setFontColor(true);

// Accessing a column from the Columns collection
const column = worksheet.getCells().getColumns().get(0);

// Applying the style to the column
column.applyStyle(style, styleFlag);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Argomenti avanzati**
- [Impostazioni di Allineamento](/cells/it/nodejs-cpp/cells-alignment-settings/)
- [Impostazioni dei Bordi](/cells/it/nodejs-cpp/cells-border-settings/)
- [Imposta Formati Condizionali di file Excel e ODS.](/cells/it/nodejs-cpp/conditional-formatting/)
- [Temi e Colori di Excel](/cells/it/nodejs-cpp/excel-themes-and-colors/)
- [Impostazioni di Riempimento](/cells/it/nodejs-cpp/cells-fill-settings/)
- [Impostazioni dei Caratteri](/cells/it/nodejs-cpp/cells-font-settings/)
- [Formattare le Celle di un Foglio di Lavoro in un Documento di Lavoro](/cells/it/nodejs-cpp/format-worksheet-cells-in-a-workbook/)
- [Implementare il Sistema di Data 1904](/cells/it/nodejs-cpp/implement-1904-date-system/)
- [Unione e separazione di celle](/cells/it/nodejs-cpp/merging-and-unmerging-cells/)
- [Impostazioni dei numeri](/cells/it/nodejs-cpp/cells-number-settings/)
- [Ottenere e impostare lo stile delle celle](/cells/it/nodejs-cpp/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)

{{< app/cells/assistant language="nodejs-cpp" >}}
