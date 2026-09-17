---
title: Inserimento di un'immagine in una cella
linktitle: Inserimento di un'immagine in una cella
description: Aspose.Cells è una libreria Node.js via C++ per lavorare con i file di fogli di calcolo. Questo articolo spiega come adattare un'immagine esattamente a una singola cella, posizionando un'immagine mobile sopra la cella o incorporando l'immagine direttamente nella cella.
keywords: Aspose.Cells, libreria Node.js via C++, foglio di calcolo, inserisci immagine, incorpora immagine, immagine in cella, adatta immagine alla cella, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /it/nodejs-cpp/inserting-an-image-into-a-cell/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells offre due modi distinti per associare un'immagine a una singola cella. Un'immagine mobile è una forma sul livello di disegno del foglio di lavoro che si sovrappone visivamente a un intervallo di celle, mentre un'immagine incorporata è memorizzata all'interno della cella stessa e si adatta automaticamente all'area di visualizzazione della cella. Scegli l'approccio che meglio soddisfa i tuoi requisiti di layout.

## **Introduzione**
Adattare un'immagine esattamente a una singola cella è un requisito comune quando si progettano fogli di calcolo che fungono da report visivi, cataloghi di prodotti, rubriche del personale, dashboard o elenchi di inventario. Piuttosto che allungare un'immagine su più celle o posizionarla liberamente su un foglio di lavoro, potresti volere un'immagine pulita, legata alla cella, che rimanga allineata con la cella che la possiede.
Aspose.Cells supporta questo scenario in due modi complementari:
- **Approccio 1 — Posizionare un'immagine mobile sopra una cella.** Aggiungi un `Picture` al foglio di lavoro, imposta il suo `placement` su `MoveAndSize` e regola le sue celle di ancoraggio (`upperLeftRow`, `upperLeftColumn`, `lowerRightRow`, `lowerRightColumn`) in modo che l'immagine copra esattamente una cella.
- **Approccio 2 — Incorporare un'immagine direttamente in una cella.** Assegna i byte dell'immagine alla proprietà `embeddedImage` della cella. L'immagine si ridimensiona automaticamente per adattarsi all'area di visualizzazione della cella e segue la cella.
Il resto di questo articolo esamina entrambi gli approcci, spiega le API pertinenti e mostra come usarle nel codice.

## **Approccio 1: Posizionare un'immagine sopra una cella**
Un'immagine mobile è un oggetto `Picture` che risiede sul livello di disegno del foglio di lavoro. Sebbene non faccia parte di nessuna singola cella, è ancorata a un intervallo di celle. Le celle di ancoraggio dell'immagine — i suoi angoli in alto a sinistra e in basso a destra — ne determinano l'estensione visiva sul foglio di lavoro. Per impostazione predefinita, un'immagine appena aggiunta copre più celle.
Per fare in modo che un'immagine mobile copra **esattamente una cella**, devi:
1. Aggiungi l'immagine usando `worksheet.pictures.add(row, column, stream)`, che ancora la nuova immagine alla cella specificata.
2. Imposta le quattro proprietà di ancoraggio in modo che il rettangolo delimitatore dell'immagine coincida con la cella di destinazione.
3. Imposta `picture.placement` su `PlacementType.MoveAndSize` in modo che l'immagine si sposti e si ridimensioni con la cella sottostante quando l'utente modifica la larghezza della colonna o l'altezza della riga.

### **Ancorare l'immagine a una singola cella**
L'ancoraggio dell'immagine è definito da quattro proprietà di indice a base zero:
- `picture.upperLeftRow` — l'indice di riga del bordo superiore dell'immagine.
- `picture.upperLeftColumn` — l'indice di colonna del bordo sinistro dell'immagine.
- `picture.lowerRightRow` — l'indice di riga del bordo inferiore dell'immagine. Per fare in modo che il bordo inferiore dell'immagine si trovi in fondo alla riga `r`, imposta questo su `r + 1`.
- `picture.lowerRightColumn` — l'indice di colonna del bordo destro dell'immagine. Per fare in modo che il bordo destro dell'immagine si trovi a destra della colonna `c`, imposta questo su `c + 1`.

{{% alert color="primary" %}}
Gli indici di riga e colonna in Aspose.Cells sono **a base zero**. La cella C6 ha indice di riga 5 e indice di colonna 2. Gli errori di off-by-one sull'ancoraggio in basso a destra sono la causa più comune di immagini che sembrano sovrapporsi a una cella adiacente.

### **Controllo del comportamento di posizionamento**
`picture.placement` è un'enumerazione di tipo `PlacementType` che controlla come si comporta l'immagine quando l'utente ridimensiona la riga o la colonna sottostante. Il valore consigliato per un'immagine a cella singola è `PlacementType.MoveAndSize`, che fa sì che l'immagine si sposti e si ridimensioni insieme alla cella sottostante, preservando l'adattamento esatto.

### **Istruzioni passo per passo**
1. Crea una nuova `Workbook` (o aprine una esistente).
2. Accedi al `Worksheet` di destinazione da `workbook.worksheets[0]`.
3. Apri il file immagine dal disco in uno stream, assicurandoti che lo stream venga chiuso correttamente dopo l'uso.
4. Chiama `worksheet.pictures.add(5, 2, stream)` per aggiungere un'immagine ancorata alla cella C6. Acquisisci il riferimento al `Picture` restituito.
5. Imposta le quattro coordinate di ancoraggio in modo che l'immagine copra solo la cella C6: `upperLeftRow = 5`, `upperLeftColumn = 2`, `lowerRightRow = 6`, `lowerRightColumn = 3`.
6. Imposta `picture.placement = PlacementType.MoveAndSize` per mantenere l'immagine allineata con C6 quando la colonna o la riga viene ridimensionata.
7. Facoltativamente aggiungi testo di esempio alle celle circostanti per dimostrare che solo la cella C6 contiene l'immagine.
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

## **Approccio 2: Incorporare un'immagine direttamente in una cella**
Aspose.Cells espone anche un meccanismo più semplice per le immagini legate alle celle: la proprietà `cell.embeddedImage`. Assegnare i byte dell'immagine a questa proprietà collega l'immagine alla cella stessa, come se fosse contenuto in linea.

### **Come funzionano le immagini incorporate**
- L'immagine è memorizzata come parte del contenuto della cella piuttosto che come una forma sul livello di disegno.
- L'immagine si ridimensiona automaticamente per adattarsi ai confini resi della cella. Non sono richieste coordinate di ancoraggio o impostazioni di posizionamento.
- La cella rimane una vera cella con un vero indirizzo che può essere referenziato dalle formule, ordinato come parte di una riga o utilizzato in altre operazioni a livello di cella.
Questo rende `cell.embeddedImage` l'opzione più concisa quando il tuo obiettivo è semplicemente "un'immagine che vive all'interno di questa cella".

### **Istruzioni passo per passo**
1. Crea una nuova `Workbook` (o aprine una esistente).
2. Accedi al `Worksheet` di destinazione da `workbook.worksheets[0]`.
3. Leggi il file immagine dal disco in un Buffer o array di byte usando le API del file system di Node.js (ad esempio, `fs.readFileSync`).
4. Ottieni un riferimento alla cella di destinazione — tramite `worksheet.cells["C6"]` o `worksheet.cells[5, 2]`.
5. Assegna l'array di byte alla proprietà `embeddedImage` della cella.
6. Facoltativamente regola l'altezza della riga e la larghezza della colonna di destinazione per dare all'immagine incorporata un aspetto più prominente.
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
// Facoltativamente regola l'altezza della riga e la larghezza della colonna per rendere più visibile l'immagine incorporata
worksheet.getCells().setColumnWidth(2, 30);   // Colonna C (indice 2)
worksheet.getCells().setRowHeight(5, 100);     // Riga 6 (indice 5)
// Salva il workbook risultante come file .xlsx
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Scegliere l'approccio giusto**
Entrambi gli approcci producono un'immagine che si adatta all'interno di una singola cella, ma differiscono nel modo in cui l'immagine è memorizzata e nel suo comportamento:
- **Usa un'immagine mobile (Approccio 1) quando:**
  - Hai bisogno di un controllo più fine sul posizionamento, la stratificazione o l'allineamento con altri oggetti di disegno.
  - Vuoi che l'immagine si comporti come una forma che può essere selezionata, riordinata o raggruppata con altre forme.
  - Richiedi compatibilità legacy con codice che già funziona con la raccolta di immagini.
  - Hai bisogno di calcolare le coordinate di ancoraggio dinamicamente in base al layout del foglio di lavoro.
- **Usa un'immagine incorporata (Approccio 2) quando:**
  - Vuoi l'inserimento più semplice possibile di un'immagine in una cella.
  - L'immagine deve seguire la cella come qualsiasi altro contenuto della cella.
  - Non hai bisogno di manipolare l'immagine come una forma.
{{% /alert %}}

{{% /alert %}}

## Related Articles
- [Excel Camera in Aspose.Cells for Node.js via C++](/cells/it/nodejs-cpp/excel-camera/)
- [Aggiungi campi filtro a una tabella pivot in Aspose.Cells for Node.js via C++](/cells/it/nodejs-cpp/add-page-field-in-pivot-table/)
- [Applica stili alle tabelle pivot in Aspose.Cells for Node.js via C++](/cells/it/nodejs-cpp/apply-style-to-pivot-table/)
- [Modifica layout dei campi pagina nella tabella pivot](/cells/it/nodejs-cpp/change-page-field-layout/)
- [Converti Sparkline in immagine e HTML in Aspose.Cells for Node.js via C++](/cells/it/nodejs-cpp/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="javascript" >}}