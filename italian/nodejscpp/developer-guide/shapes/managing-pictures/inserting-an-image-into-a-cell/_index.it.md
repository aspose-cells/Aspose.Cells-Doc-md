---
title: Inserimento di un'immagine in una cella
description: Aspose.Cells è una libreria Node.js via C++ per lavorare con file di fogli di calcolo. Questo articolo spiega come adattare un'immagine esattamente alla dimensione di una singola cella utilizzando due approcci diversi, posizionando un picture mobile sopra la cella oppure incorporando l'immagine direttamente nella cella.
keywords: Aspose.Cells, Node.js via C++ libreria, foglio di calcolo, inserire immagine, incorporare immagine, picture in cella, adattare immagine alla cella, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /it/nodejs-cpp/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells offre due modi distinti per associare un'immagine a una singola cella. Un picture mobile è una forma sul livello di disegno del foglio di lavoro che si sovrappone visivamente a un intervallo di celle, mentre un'immagine incorporata è memorizzata all'interno della cella stessa e si ridimensiona automaticamente all'area di visualizzazione della cella. Scegli l'approccio che meglio soddisfa le tue esigenze di layout.

{{% /alert %}}

## **Introduzione**

Adattare un'immagine esattamente a una singola cella è un requisito comune quando si progettano fogli di calcolo che fungono da report visivi, cataloghi di prodotti, elenchi di dipendenti, dashboard o inventari. Piuttosto che estendere un'immagine su più celle o posizionarla liberamente su un foglio di lavoro, potresti voler ottenere un'immagine pulita, legata alla cella, che rimane allineata con la cella che la possiede.

Aspose.Cells supporta questo scenario in due modi complementari:

- **Approccio 1 — Posizionare un picture mobile sopra una cella.** Aggiungi un `Picture` al foglio di lavoro, imposta il suo `placement` su `MoveAndSize` e regola le sue celle di ancoraggio (`upperLeftRow`, `upperLeftColumn`, `lowerRightRow`, `lowerRightColumn`) in modo che il picture copra esattamente una cella.
- **Approccio 2 — Incorporare un'immagine direttamente in una cella.** Assegna i byte dell'immagine alla proprietà `embeddedImage` della cella. L'immagine si ridimensiona automaticamente per adattarsi all'area di visualizzazione della cella e si sposta con essa.

Il resto di questo articolo illustra entrambi gli approcci, spiega le API rilevanti e mostra come utilizzarle nel codice.

## **Approccio 1: Posizionare un Picture Sopra una Cella**

Un picture mobile è un oggetto `Picture` che risiede sul livello di disegno del foglio di lavoro. Sebbene non faccia parte di alcuna singola cella, è ancorato a un intervallo di celle. Le celle di ancoraggio del picture — i suoi angoli in alto a sinistra e in basso a destra — ne determinano l'estensione visiva sul foglio di lavoro. Per impostazione predefinita, un picture appena aggiunto si estende su più celle.

Per fare in modo che un picture mobile copra **esattamente una cella**, è necessario:

1. Aggiungere il picture utilizzando `worksheet.pictures.add(row, column, stream)`, che ancora il nuovo picture alla cella specificata.
2. Impostare le quattro proprietà di ancoraggio in modo che il rettangolo di delimitazione del picture coincida con la cella di destinazione.
3. Impostare `picture.placement` su `PlacementType.MoveAndSize` in modo che il picture si sposti e si ridimensioni con la cella sottostante quando l'utente modifica la larghezza della colonna o l'altezza della riga.

### **Ancorare il Picture a una Singola Cella**

L'ancoraggio del picture è definito da quattro proprietà con indice a base zero:

- `picture.upperLeftRow` — l'indice di riga del bordo superiore del picture.
- `picture.upperLeftColumn` — l'indice di colonna del bordo sinistro del picture.
- `picture.lowerRightRow` — l'indice di riga del bordo inferiore del picture. Per fare in modo che il bordo inferiore del picture si trovi alla fine della riga `r`, imposta questo valore su `r + 1`.
- `picture.lowerRightColumn` — l'indice di colonna del bordo destro del picture. Per fare in modo che il bordo destro del picture si trovi alla fine della colonna `c`, imposta questo valore su `c + 1`.

Ad esempio, per adattare il picture esattamente alla cella **C6** (indice di riga `5`, indice di colonna `2`), imposta `upperLeftRow = 5`, `upperLeftColumn = 2`, `lowerRightRow = 6` e `lowerRightColumn = 3`.

{{% alert color="primary" %}}

Gli indici di riga e colonna in Aspose.Cells sono **a base zero**. La cella C6 ha indice di riga 5 e indice di colonna 2. Gli errori off-by-one sull'ancoraggio inferiore-destro sono la fonte più comune di picture che sembrano sovrapporsi a una cella adiacente.

{{% /alert %}}

### **Controllo del Comportamento di Posizionamento**

`picture.placement` è un'enumerazione di tipo `PlacementType` che controlla come si comporta il picture quando l'utente ridimensiona la riga o la colonna sottostante. Il valore consigliato per un picture a cella singola è `PlacementType.MoveAndSize`, che fa sì che il picture si sposti e si ridimensioni insieme alla cella sottostante, preservando l'adattamento esatto.

### **Istruzioni Passo per Passo**

1. Crea un nuovo `Workbook` (oppure aprine uno esistente).
2. Accedi al `Worksheet` di destinazione da `workbook.worksheets[0]`.
3. Apri il file immagine dal disco in uno stream, assicurandoti che lo stream venga chiuso correttamente dopo l'uso.
4. Chiama `worksheet.pictures.add(5, 2, stream)` per aggiungere un picture ancorato alla cella C6. Acquisisci il riferimento `Picture` restituito.
5. Imposta le quattro coordinate di ancoraggio in modo che il picture copra solo la cella C6: `upperLeftRow = 5`, `upperLeftColumn = 2`, `lowerRightRow = 6`, `lowerRightColumn = 3`.
6. Imposta `picture.placement = PlacementType.MoveAndSize` per mantenere il picture allineato con C6 quando la colonna o la riga viene ridimensionata.
7. Facoltativamente, aggiungi del testo di esempio alle celle circostanti per dimostrare che solo la cella C6 contiene il picture.
8. Salva la cartella di lavoro su disco come file `.xlsx`.

Il codice seguente dimostra l'approccio completo.

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

const fs_stream = fs.createReadStream("logo.png");
const picIndex = worksheet.getPictures().add(5, 2, fs_stream);
const picture = worksheet.getPictures().get(picIndex);
picture.setUpperLeftRow(5);
picture.setUpperLeftColumn(2);
picture.setLowerRightRow(6);
picture.setLowerRightColumn(3);
picture.setPlacement(AsposeCells.PlacementType.MoveAndSize);

workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Approccio 2: Incorporare un'Immagine Direttamente in una Cella**

Aspose.Cells espone anche un meccanismo più semplice per le immagini legate alle celle: la proprietà `cell.embeddedImage`. Assegnare i byte dell'immagine a questa proprietà collega l'immagine alla cella stessa, come se fosse contenuto inline.

### **Come Funzionano le Immagini Incorporate**

- L'immagine viene memorizzata come parte del contenuto della cella anziché come forma sul livello di disegno.
- L'immagine si ridimensiona automaticamente per adattarsi ai confini resi della cella. Non sono richieste coordinate di ancoraggio né impostazioni di posizionamento.
- La cella rimane una vera cella con un vero indirizzo che può essere referenziato da formule, ordinato come parte di una riga o utilizzato in altre operazioni a livello di cella.

Questo rende `cell.embeddedImage` l'opzione più concisa quando il tuo obiettivo è semplicemente "un'immagine che vive all'interno di questa cella".

### **Istruzioni Passo per Passo**

1. Crea un nuovo `Workbook` (oppure aprine uno esistente).
2. Accedi al `Worksheet` di destinazione da `workbook.worksheets[0]`.
3. Leggi il file immagine dal disco in un Buffer o array di byte utilizzando le API del file system di Node.js (ad esempio, `fs.readFileSync`).
4. Ottieni un riferimento alla cella di destinazione — tramite `worksheet.cells["C6"]` oppure `worksheet.cells[5, 2]`.
5. Assegna l'array di byte alla proprietà `embeddedImage` della cella.
6. Facoltativamente, regola l'altezza della riga e la larghezza della colonna della riga e colonna di destinazione per dare all'immagine incorporata un aspetto più prominente.
7. Salva la cartella di lavoro su disco come file `.xlsx`.

Il codice seguente dimostra l'approccio completo.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// Ottieni la cella di destinazione C6
var cell = worksheet.getCells().get("C6");

// Leggi il file immagine in un array di byte
var imageData = fs.readFileSync("logo.png");

// Incorpora l'immagine direttamente nella cella
cell.setEmbeddedImage(imageData);

// Opzionalmente regola l'altezza della riga e la larghezza della colonna per rendere l'immagine incorporata più visibile
worksheet.getCells().setColumnWidth(2, 30);   // Colonna C (indice 2)
worksheet.getCells().setRowHeight(5, 100);     // Riga 6 (indice 5)

// Salva la cartella di lavoro risultante come file .xlsx
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Scegliere l'Approccio Giusto**

Entrambi gli approcci producono un'immagine che si adatta all'interno di una singola cella, ma differiscono nel modo in cui l'immagine viene memorizzata e nel suo comportamento:

- **Usa un picture mobile (Approccio 1) quando:**
  - Hai bisogno di un controllo più fine sul posizionamento, sulla stratificazione o sull'allineamento con altri oggetti di disegno.
  - Vuoi che il picture si comporti come una forma che può essere selezionata, riordinata o raggruppata con altre forme.
  - Richiedi compatibilità legacy con codice che già funziona con la raccolta di picture.
  - Hai bisogno di calcolare le coordinate di ancoraggio dinamicamente in base al layout del foglio di lavoro.

- **Usa un'immagine incorporata (Approccio 2) quando:**
  - Vuoi l'inserimento più semplice possibile di un'immagine in una cella.
  - L'immagine deve viaggiare con la cella come qualsiasi altro contenuto della cella.
  - Non hai bisogno di manipolare l'immagine come una forma.

{{% alert color="primary" %}}

Entrambi gli approcci possono coesistere nella stessa cartella di lavoro. Puoi posizionare picture mobili sopra un insieme di celle e incorporare immagini direttamente in altre celle, poiché i due meccanismi utilizzano diversi livelli di memorizzazione nel file.

{{% /alert %}}

## **Articoli Correlati**

- [Come Inserire un Picture in una Cella](/cells/it/nodejs-cpp/how-to-place-image-to-cell/)
- [Aggiungere Hyperlink alle Immagini](/cells/it/nodejs-cpp/add-image-hyperlinks/)
- [Caricare un'Immagine Web da un URL in un Foglio di Lavoro Excel](/cells/it/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [Manipolare Posizione, Dimensione e Grafico del Designer](/cells/it/nodejs-cpp/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="javascript" >}}