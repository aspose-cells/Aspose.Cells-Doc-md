---  
title: Gestione delle immagini con Node.js tramite C++  
linktitle: Gestione delle immagini  
type: docs  
weight: 10  
url: /it/nodejs-cpp/managing-pictures/  
description: Scopri come aggiungere e posizionare le immagini nei fogli di calcolo usando Aspose.Cells for Node.js via C++.  
---  

Aspose.Cells consente ai programmatori di aggiungere immagini ai fogli di calcolo in fase di esecuzione. Inoltre, la posizione di queste immagini può essere controllata in fase di esecuzione, come discusso più in dettaglio nelle sezioni successive.

Questo articolo spiega come aggiungere immagini e come inserire un’immagine che mostra il contenuto di alcune celle.

## **Aggiunta di immagini**

Aggiungere immagini a un foglio di calcolo è molto facile. Bastano poche righe di codice:  
Basta chiamare il metodo [**Add**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-string-) della raccolta [**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection) (incapsulato nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)). Il metodo [**Add**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection/#add-number-number-string-) accetta i seguenti parametri:

- **Indice della riga in alto a sinistra**, l'indice della riga in alto a sinistra.
- **Indice della colonna in alto a sinistra**, l'indice della colonna in alto a sinistra.
- **Nome del file immagine**, il nome del file immagine, completo di percorso.

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

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
worksheet.getPictures().add(5, 5, path.join(dataDir, "logo.jpg"));

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Posizionamento delle immagini**

Ci sono due possibili modi per controllare il posizionamento delle immagini utilizzando Aspose.Cells:

- Posizionamento proporzionale: definire una posizione proporzionale all'altezza e alla larghezza della riga.
- Posizionamento assoluto: definisce la posizione esatta sulla pagina in cui verrà inserita l'immagine, ad esempio 40 pixel a sinistra e 20 pixel sotto il bordo della cella.

### **Posizionamento proporzionale**

Gli sviluppatori possono posizionare le immagini proportionatamente all'altezza delle righe e alla larghezza delle colonne usando le proprietà [**getUpperDeltaX()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getUpperDeltaX--) e [**getUpperDeltaY()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getUpperDeltaY--) dell'oggetto [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/). Un oggetto [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/) può essere ottenuto dalla collezione [**Pictures**](https://reference.aspose.com/cells/nodejs-cpp/picturecollection) passando il suo indice dell’immagine. Questo esempio posiziona un’immagine nella cella F6.

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

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
const pictureIndex = worksheet.getPictures().add(5, 5, path.join(dataDir, "logo.jpg"));

// Accessing the newly added picture
const picture = worksheet.getPictures().get(pictureIndex);

// Positioning the picture proportional to row height and column width
picture.setUpperDeltaX(200);
picture.setUpperDeltaY(200);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

### **Posizionamento Assoluto**

Gli sviluppatori possono anche posizionare le immagini in modo assoluto usando le proprietà [**getLeft()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getLeft--) e [**getTop()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTop--) dell'oggetto [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/). Questo esempio posiziona un'immagine nella cella F6, a 60 pixel da sinistra e a 10 pixel dall'alto della cella.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "logo.jpg");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a picture at the location of a cell whose row and column indices
// Are 5 in the worksheet. It is "F6" cell
const pictureIndex = worksheet.getPictures().add(5, 5, filePath);

// Accessing the newly added picture
const picture = worksheet.getPictures().get(pictureIndex);

// Absolute positioning of the picture in unit of pixels
picture.setLeft(60);
picture.setTop(10);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Inserimento di un'immagine in base al riferimento della cella**

Aspose.Cells consente di visualizzare i contenuti di una cella del foglio di lavoro in una forma di immagine. È possibile collegare l'immagine alla cella che contiene i dati che si desidera visualizzare. Poiché la cella, o il range di celle, è collegata all'oggetto grafico, le modifiche apportate ai dati in quella cella o in quel range di celle appaiono automaticamente nell'oggetto grafico.

Aggiungi un’immagine al foglio di lavoro chiamando il metodo [**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-) della raccolta [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection) (incapsulato nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)). Specifica l'intervallo di celle usando l'attributo [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getFormula--) dell'oggetto [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture/).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();
// Get the first worksheet's cells collection
const cells = workbook.getWorksheets().get(0).getCells();

// Add string values to the cells
cells.get("A1").putValue("A1");
cells.get("C10").putValue("C10");

const picts = workbook.getWorksheets().get(0).getPictures();
// Add a blank picture to the D1 cell
const picIndex = picts.add(0, 3, 10, 6, null);
const pic = picts.get(picIndex);

// Specify the formula that refers to the source range of cells

pic.setFormula("A1:C10");

// Update the shapes selected value in the worksheet
workbook.getWorksheets().get(0).getShapes().updateSelectedValue();

// Save the Excel file.
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **Argomenti avanzati**
- [Aggiungi Impostazioni Icona Condizionale con il Testo della Cella](/cells/it/nodejs-cpp/add-conditional-icons-set-with-the-cell-text/)
- [Inserisci un'immagine collegata dall'indirizzo web](/cells/it/nodejs-cpp/insert-a-linked-picture-from-web-address/)
- [Inserisci un'immagine basata sul riferimento della cella](/cells/it/nodejs-cpp/insert-a-picture-based-on-cell-reference/)
- [Caricare un'immagine Web da un URL in un foglio di lavoro Excel](/cells/it/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)

{{< app/cells/assistant language="nodejs-cpp" >}}
