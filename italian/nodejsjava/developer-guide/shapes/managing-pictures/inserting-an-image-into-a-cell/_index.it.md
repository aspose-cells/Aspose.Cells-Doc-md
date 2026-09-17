---
title: Inserimento di un'immagine in una cella
linktitle: Inserimento di un'immagine in una cella
description: Aspose.Cells è una libreria Node.js tramite Java per lavorare con file di fogli di calcolo. Questo articolo spiega come adattare un'immagine esattamente a una singola cella, sia posizionando un'immagine mobile sopra la cella sia incorporando l'immagine direttamente nella cella.
keywords: Aspose.Cells, libreria Node.js tramite Java, foglio di calcolo, inserisci immagine, incorpora immagine, immagine nella cella, adatta immagine alla cella, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /it/nodejs-java/inserting-an-image-into-a-cell/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells fornisce due modi distinti per associare un'immagine a una singola cella. Un'immagine mobile è una forma sul livello di disegno del foglio di lavoro che si sovrappone visivamente a un intervallo di celle, mentre un'immagine incorporata è memorizzata all'interno della cella stessa e si ridimensiona automaticamente all'area di visualizzazione della cella. Scegli l'approccio che meglio soddisfa le tue esigenze di layout.
{{% /alert %}}

## **Introduzione**
Adattare un'immagine esattamente a una singola cella è un requisito comune quando si progettano fogli di calcolo che fungono da report visivi, cataloghi di prodotti, elenchi di dipendenti, dashboard o elenchi di inventario. Piuttosto che estendere un'immagine su molte celle o posizionarla liberamente su un foglio di lavoro, potresti voler ottenere un'immagine pulita e legata alla cella che rimane allineata alla cella che la possiede.
Aspose.Cells supporta questo scenario in due modi complementari:
- **Approccio 1 — Posizionare un'immagine mobile sopra una cella.** Aggiungi una `Picture` al foglio di lavoro, imposta il suo `Placement` su `MoveAndSize` e regola le celle di ancoraggio (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) in modo che l'immagine copra esattamente una cella.
- **Approccio 2 — Incorporare un'immagine direttamente in una cella.** Assegna i byte dell'immagine alla proprietà `EmbeddedImage` della cella. L'immagine si ridimensiona automaticamente per adattarsi all'area di visualizzazione della cella e viaggia con la cella.
Il resto di questo articolo illustra entrambi gli approcci, spiega le API pertinenti e mostra come utilizzarle nel codice.

## **Approccio 1: Posizionare un'immagine sopra una cella**
Un'immagine mobile è un oggetto `Picture` che risiede sul livello di disegno del foglio di lavoro. Sebbene non faccia parte di nessuna singola cella, è ancorato a un intervallo di celle. Le celle di ancoraggio dell'immagine — i suoi angoli in alto a sinistra e in basso a destra — determinano la sua estensione visiva sul foglio di lavoro. Per impostazione predefinita, un'immagine appena aggiunta si estende su più celle.
Per fare in modo che un'immagine mobile copra **esattamente una cella**, è necessario:
1. Aggiungere l'immagine utilizzando `worksheet.getPictures().add(int row, int column, InputStream stream)`, che ancora la nuova immagine alla cella specificata.
2. Impostare le quattro proprietà di ancoraggio in modo che il rettangolo di delimitazione dell'immagine coincida con la cella di destinazione.
3. Impostare `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` in modo che l'immagine si sposti e si ridimensioni con la cella sottostante quando l'utente modifica la larghezza della colonna o l'altezza della riga.

### **Ancoraggio dell'immagine a una singola cella**
L'ancoraggio dell'immagine è definito da quattro proprietà di indice a base zero:
- `picture.setUpperLeftRow(int)` — l'indice di riga del bordo superiore dell'immagine.
- `picture.setUpperLeftColumn(int)` — l'indice di colonna del bordo sinistro dell'immagine.
- `picture.setLowerRightRow(int)` — l'indice di riga del bordo inferiore dell'immagine. Per fare in modo che il bordo inferiore dell'immagine si trovi in fondo alla riga `r`, impostare questo valore su `r + 1`.
- `picture.setLowerRightColumn(int)` — l'indice di colonna del bordo destro dell'immagine. Per fare in modo che il bordo destro dell'immagine si trovi a destra della colonna `c`, impostare questo valore su `c + 1`.

{{% alert color="primary" %}}
Gli indici di riga e colonna in Aspose.Cells sono **a base zero**. La cella C6 ha indice di riga 5 e indice di colonna 2. Gli errori di una unità sull'ancoraggio in basso a destra sono la causa più comune di immagini che sembrano sovrapporsi a una cella adiacente.

### **Controllo del comportamento di posizionamento**
`Picture.Placement` è un'enumerazione di tipo `PlacementType` che controlla il comportamento dell'immagine quando l'utente ridimensiona la riga o la colonna sottostante. Il valore consigliato per un'immagine a cella singola è `PlacementType.MoveAndSize`, che fa sì che l'immagine si sposti e si ridimensioni insieme alla cella sottostante, preservando l'adattamento esatto.

### **Istruzioni passo per passo**
1. Creare un nuovo `Workbook` (o aprirne uno esistente).
2. Accedere al `Worksheet` di destinazione da `workbook.getWorksheets().get(0)`.
3. Aprire il file immagine dal disco in un `InputStream` (ad esempio, utilizzando `FileInputStream`) in modo che lo stream venga chiuso correttamente.
4. Chiamare `worksheet.getPictures().add(5, 2, stream)` per aggiungere un'immagine ancorata alla cella C6. Catturare il riferimento `Picture` restituito.
5. Impostare le quattro coordinate di ancoraggio in modo che l'immagine copra solo la cella C6: `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Impostare `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` per mantenere l'immagine allineata a C6 quando la colonna o la riga viene ridimensionata.
7. Facoltativamente, aggiungere testo di esempio alle celle circostanti per dimostrare che solo la cella C6 contiene l'immagine.
8. Salvare la cartella di lavoro su disco come file `.xlsx`.
Il codice seguente dimostra l'approccio completo.

```javascript
const AsposeCells = require("aspose.cells-node");
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
var picIndex = worksheet.getPictures().add(5, 2, "logo.png");
var picture = worksheet.getPictures().get(picIndex);
picture.setUpperLeftRow(5);
picture.setUpperLeftColumn(2);
picture.setLowerRightRow(6);
picture.setLowerRightColumn(3);
picture.setPlacement(AsposeCells.PlacementType.MoveAndSize);
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Approccio 2: Incorporare un'immagine direttamente in una cella**
Aspose.Cells espone anche un meccanismo più semplice per le immagini legate alle celle: la proprietà `Cell.EmbeddedImage`. L'assegnazione di byte immagine a questa proprietà collega l'immagine alla cella stessa, come se fosse contenuto inline.

### **Come funzionano le immagini incorporate**
- L'immagine viene memorizzata come parte del contenuto della cella anziché come forma sul livello di disegno.
- L'immagine si ridimensiona automaticamente per adattarsi ai confini renderizzati della cella. Non sono richieste coordinate di ancoraggio o impostazioni di posizionamento.
- La cella rimane una cella reale con un indirizzo reale che può essere referenziato da formule, ordinato come parte di una riga o utilizzato in altre operazioni a livello di cella.
Questo rende `Cell.EmbeddedImage` l'opzione più concisa quando il tuo obiettivo è semplicemente «un'immagine che vive all'interno di questa cella».

### **Istruzioni passo per passo**
1. Creare un nuovo `Workbook` (o aprirne uno esistente).
2. Accedere al `Worksheet` di destinazione da `workbook.getWorksheets().get(0)`.
3. Leggere il file immagine dal disco in un array di byte (ad esempio, utilizzando `Files.readAllBytes` da `java.nio.file.Files`).
4. Ottenere un riferimento alla cella di destinazione — tramite `worksheet.getCells().get("C6")` o `worksheet.getCells().get(5, 2)`.
5. Assegnare l'array di byte alla proprietà `EmbeddedImage` della cella tramite `cell.setEmbeddedImage(bytes)`.
6. Facoltativamente, regolare l'altezza della riga e la larghezza della colonna della riga e della colonna di destinazione per dare all'immagine incorporata un aspetto più prominente.
7. Salvare la cartella di lavoro su disco come file `.xlsx`.
Il codice seguente dimostra l'approccio completo.

```javascript
const AsposeCells = require("aspose.cells-node");
const fs = require("fs");
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// Ottieni la cella di destinazione C6
var cell = worksheet.getCells().get("C6");
// Leggi il file immagine in un array di byte
var imageData = fs.readFileSync("logo.png");
// Incorpora l'immagine direttamente nella cella
cell.setEmbeddedImage(imageData);
// Facoltativamente regola l'altezza della riga e la larghezza della colonna in modo che l'immagine incorporata sia più visibile
worksheet.getCells().setColumnWidth(2, 30);   // Colonna C (indice 2)
worksheet.getCells().setRowHeight(5, 100);     // Riga 6 (indice 5)
// Salva la cartella di lavoro risultante come file .xlsx
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Scegliere l'approccio giusto**
Entrambi gli approcci producono un'immagine che si adatta all'interno di una singola cella, ma differiscono nel modo in cui l'immagine viene memorizzata e nel suo comportamento:
- **Utilizzare un'immagine mobile (Approccio 1) quando:**
  - È necessario un controllo più preciso sul posizionamento, sulla disposizione a strati o sull'allineamento con altri oggetti di disegno.
  - Si desidera che l'immagine si comporti come una forma che può essere selezionata, riordinata o raggruppata con altre forme.
  - È richiesta la compatibilità legacy con codice che già funziona con `PictureCollection`.
  - È necessario calcolare dinamicamente le coordinate di ancoraggio in base al layout del foglio di lavoro.
- **Utilizzare un'immagine incorporata (Approccio 2) quando:**
  - Si desidera l'inserimento più semplice possibile di un'immagine in una cella.
  - L'immagine deve viaggiare con la cella come qualsiasi altro contenuto della cella.
{{% /alert %}}

{{< app/cells/assistant language="javascript" >}}