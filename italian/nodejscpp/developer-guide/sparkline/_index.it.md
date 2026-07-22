---
title: Sparklines in Aspose.Cells for Node.js via C++
linktitle: Sparkline
description: Aspose.Cells è una libreria Node.js per lavorare con file di fogli di calcolo che supporta la creazione di sparkline — mini grafici inseriti all'interno delle celle del foglio di lavoro. Questo articolo spiega come aggiungere e personalizzare sparkline a linee, colonne e vittoria/sconfitta utilizzando la libreria Aspose.Cells.
keywords: Aspose.Cells, libreria Node.js, foglio di calcolo, sparkline, sparkline a linee, sparkline a colonne, sparkline vittoria/sconfitta, SparklineGroup, SparklineType
type: docs
weight: 195
url: /it/nodejs-cpp/creating-sparklines/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supporta la creazione di sparkline all'interno delle celle del foglio di lavoro. Le sparkline sono mini grafici che si adattano a una singola cella, fornendo una rapida rappresentazione visiva dell'andamento dei dati. Aspose.Cells supporta sparkline a linee, colonne e vittoria/sconfitta, e ciascuna può essere personalizzata per quanto riguarda colore, spessore della linea, punti massimi/minimi e indicatori.

{{% /alert %}}

## **Introduzione**

Le sparkline sono piccoli grafici all'interno delle celle utili quando si desidera visualizzare un rapido andamento accanto a una riga o colonna di dati senza occupare lo spazio di un grafico completo. Excel supporta tre tipi di sparkline: **linea**, **colonna** e **vittoria/sconfitta**. Aspose.Cells rispecchia questa funzionalità attraverso le API `SparklineGroup` e `SparklineGroupCollection` presenti nel namespace `Aspose.Cells.Charts`.

In Aspose.Cells, ogni sparkline aggiunta viene creata tramite `worksheet.sparklineGroups.add(...)`, che restituisce un oggetto `SparklineGroup`. È quindi possibile utilizzare tale oggetto per impostare il tipo di sparkline, l'intervallo di dati, la cella di destinazione e le proprietà visive come il colore della linea, lo spessore, gli indicatori e gli indicatori dei punti massimi/minimi.

{{% alert color="primary" %}}

Un singolo `SparklineGroup` può contenere una o più sparkline che condividono lo stesso stile. Quando si chiama `add` e si passa una riga di dati più una singola cella di destinazione, si ottiene una sparkline all'interno di tale cella. Se l'intervallo di destinazione è più ampio di una cella, viene disegnata una sparkline separata in ciascuna cella di destinazione, tutte utilizzando lo stesso stile e intervallo di dati.

{{% /alert %}}

Questo articolo illustra ciascuno dei tre tipi di sparkline supportati da Aspose.Cells — **Linea**, **Colonna** e **Vittoria/Sconfitta** — e mostra come aggiungerli, personalizzare i loro colori e salvare la cartella di lavoro risultante.

## **Sparkline a Linee**

Una sparkline a linee disegna una linea continua attraverso i punti dati di una serie, rendendola la scelta più naturale per mostrare l'andamento nel tempo. In Aspose.Cells, una sparkline a linee viene creata passando `SparklineType.Line` al metodo `sparklineGroups.add`.

Il flusso di lavoro è lo stesso di qualsiasi altro tipo di sparkline:

1. Creare un nuovo `Workbook` e accedere al primo foglio di lavoro.
2. Popolare una riga di dati di origine (ad esempio, riga 1, colonne da A a E) con i valori che si desidera visualizzare.
3. Costruire un `CellArea` che descriva la cella di destinazione in cui verrà disegnata la sparkline.
4. Chiamare `worksheet.sparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)`. Il terzo argomento — `false` — indica ad Aspose.Cells che l'intervallo di dati è orizzontale (una riga), non verticale (una colonna).
5. Facoltativamente personalizzare il `SparklineGroup` restituito. Per una sparkline a linee è possibile impostare il colore della linea utilizzando `group.line.color` (che si aspetta un `CellsColor` da `Aspose.Cells.Drawing`), regolare lo spessore della linea e attivare/disattivare gli indicatori dei punti massimi/minimi.
6. Salvare la cartella di lavoro.

Il seguente esempio crea una cartella di lavoro, scrive i valori 5, -3, 8, -2, 6 nelle celle da A1 a E1 e aggiunge una sparkline a linee nella cella F1 che traccia tali valori. Personalizza inoltre il colore della linea in rosso e abilita gli indicatori per i punti massimi e minimi.

```javascript
const AsposeCells = require("aspose.cells");

// Passo 1: Crea una cartella di lavoro e ottieni il primo foglio di lavoro
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

// Passo 2: Scrivi i valori di esempio 5, -3, 8, -2, 6 nelle celle A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);

// Passo 3: Costruisci una CellArea che punta alla cella di destinazione F1
const dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // colonna F (indicizzata a 0)
dest.setEndColumn(5);
dest.setStartRow(0);      // riga 1 (indicizzata a 0)
dest.setEndRow(0);

// Passo 4: Aggiungi una sparkline a linea da A1:E1 in F1
// SparklineGroups.Add restituisce l'indice del gruppo appena aggiunto
const index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
const group = worksheet.getSparklineGroups().get(index);

// Passo 5: Crea un CellsColor rosso e assegnalo al colore della linea della sparkline
const red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);

// Passo 6: Abilita i marcatori del punto massimo e del punto minimo
group.setShowHighPoint(true);
group.setShowLowPoint(true);

// Passo 7: Salva la cartella di lavoro
workbook.save("output_line.xlsx");
```

## **Sparkline a Colonne**

Una sparkline a colonne rappresenta ciascun punto dati come una barra verticale. Ciò la rende particolarmente adatta a dati la cui magnitudine è significativa — ad esempio, cifre di vendita mensili o conteggi. In Aspose.Cells, si crea una sparkline a colonne passando `SparklineType.Column` al metodo `sparklineGroups.add`.

La procedura rispecchia l'esempio della sparkline a linee:

1. Creare un nuovo `Workbook` e accedere al primo foglio di lavoro.
2. Popolare lo stesso intervallo di origine (A1:E1) con i valori che si desidera visualizzare.
3. Costruire un `CellArea` che descriva la cella di destinazione.
4. Chiamare `worksheet.sparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`.
5. Facoltativamente personalizzare il `SparklineGroup` risultante — ad esempio, impostando `group.type` per confermare il tipo, oppure modificando il colore delle barre.
6. Salvare la cartella di lavoro in un file di output separato in modo che non sovrascriva l'esempio della sparkline a linee.

L'esempio seguente scrive i valori 5, -3, 8, -2, 6 in A1:E1 e rende una sparkline a colonne in F1. I valori negativi vengono disegnati come barre verso il basso e i valori positivi come barre verso l'alto, il che rende facile individuare a colpo d'occhio i contributi positivi e negativi.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Passo 2: Scrivi valori di esempio in A1:E1
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}

// Passo 3: Crea un CellArea che punta a F1 (indice colonna 5, indice riga 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// Passo 4: Aggiungi una sparkline di tipo Colonna alla cella di destinazione
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);

// Passo 5: Conferma il tipo di sparkline leggendo group.Type
console.log("Sparkline Type added: " + group.getType());

// Passo 6: Salva la cartella di lavoro
workbook.save("output_column.xlsx");

console.log("Workbook saved as output_column.xlsx");
```

## **Sparkline Vittoria/Sconfitta**

Una sparkline vittoria/sconfitta è una variante speciale della sparkline a colonne progettata per mostrare solo due esiti: un valore positivo viene disegnato come una barra "in alto" (una vittoria) e un valore zero o negativo viene disegnato come una barra "in basso" (una sconfitta). Le sparkline vittoria/sconfitta sono comunemente utilizzate per visualizzare sequenze di vittorie e sconfitte, risultati di superamento/fallimento, o qualsiasi esito binario nel tempo.

In Aspose.Cells, una sparkline vittoria/sconfitta viene creata passando `SparklineType.Stacked` al metodo `sparklineGroups.add`. (Nonostante il nome, `SparklineType.Stacked` è il valore enum utilizzato per richiedere il rendering vittoria/sconfitta.)

La procedura è la stessa degli altri due tipi:

1. Creare un nuovo `Workbook` e accedere al primo foglio di lavoro.
2. Popolare l'intervallo di origine. Poiché le sparkline vittoria/sconfitta trattano ogni valore come una vittoria o una sconfitta, la magnitudine del valore non conta — conta solo il suo segno. I valori positivi diventano barre in alto e i valori non positivi diventano barre in basso.
3. Costruire un `CellArea` che descriva la cella di destinazione.
4. Chiamare `worksheet.sparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Facoltativamente personalizzare il `SparklineGroup` restituito, ad esempio impostando colori di accento per le barre di vittoria e sconfitta.
6. Salvare la cartella di lavoro con un nome file distinto in modo che tutti e tre gli esempi possano coesistere sul disco.

L'esempio seguente utilizza gli stessi dati di input delle due sezioni precedenti. I valori 5, -3, 8, -2, 6 vengono interpretati come vittoria, sconfitta, vittoria, sconfitta, vittoria — e la sparkline disegnata in F1 riflette esattamente tale schema.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");

// Passo 2: Popola i dati di esempio nella riga 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Passo 3: Crea un CellArea che punta a F1 (colonna 5, riga 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // F
dest.setEndColumn(5);
dest.setStartRow(0);      // riga 1
dest.setEndRow(0);

// Passo 4: Aggiungi una sparkline Win/Loss (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest);
let group = worksheet.getSparklineGroups().get(groupIndex);

// Passo 5: Personalizza il gruppo di sparkline
// Abilita i marcatori dei punti alti e bassi
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// Imposta il colore dei punti alti su verde
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.Green);
group.setHighPointColor(highColor);

// Imposta il colore dei punti bassi su rosso
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.Red);
group.setLowPointColor(lowColor);

// Imposta il colore dei punti negativi su arancione
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.Orange);
group.setNegativePointsColor(negColor);

// Imposta il colore predefinito della serie (usato per le barre positive)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.SteelBlue);
group.setSeriesColor(seriesColor);

// Passo 6: Salva la cartella di lavoro
workbook.save("output_winloss.xlsx");

console.log("Cartella di lavoro salvata con successo: output_winloss.xlsx");
```

## **Combinazione dei Tre Tipi di Sparkline**

I tre esempi precedenti producono ciascuno la propria cartella di lavoro in modo che i file di output siano facili da ispezionare in isolamento. In uno scenario reale, tuttavia, si vorrà spesso confrontare più serie di dati affiancate. Il modo più pulito per farlo è inserire più di un gruppo di sparkline nello stesso foglio di lavoro, con ciascun gruppo che rende uno stile diverso.

È possibile aggiungere più oggetti `SparklineGroup` alla stessa `SparklineGroupCollection`, e ciascun gruppo può avere come destinazione una cella diversa o un intervallo diverso. Ad esempio, si potrebbe posizionare una sparkline a linee in F1, una sparkline a colonne in F2 e una sparkline vittoria/sconfitta in F3 — tutte leggendo dagli stessi dati di origine nella riga 1 — in modo che il lettore possa vedere tre diversi trattamenti visivi degli stessi numeri.

L'esempio combinato seguente crea una singola cartella di lavoro, popola la riga 1 con i valori 5, -3, 8, -2, 6 e quindi aggiunge tre gruppi di sparkline nelle celle F1, F2 e F3 — uno per ciascun tipo — in modo che il file risultante dimostri tutti e tre gli stili di sparkline contemporaneamente.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Passo 2: Popola i dati di esempio nella riga 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Passo 3: Aggiungi un gruppo di sparkline di tipo Linea in F1
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);

// Personalizza il colore della sparkline di tipo Linea tramite CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.Blue);
lineGroup.setSeriesColor(lineColor);

// Passo 4: Aggiungi un gruppo di sparkline di tipo Colonna in F2
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// Personalizza il colore della serie della sparkline di tipo Colonna
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.Green);
columnGroup.setSeriesColor(columnColor);

// Passo 5: Aggiungi un gruppo di sparkline Win/Loss (Stacked) in F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// Personalizza il colore della serie della sparkline Win/Loss
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.DarkOrange);
stackedGroup.setSeriesColor(stackedColor);

// Passo 6: Salva la cartella di lavoro
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

Quando si combinano più gruppi di sparkline in un singolo foglio di lavoro, ciascun gruppo è indipendente. Possono condividere lo stesso intervallo di origine o utilizzare intervalli di origine diversi, e possono essere stilizzati indipendentemente. Ciò rende facile costruire un piccolo "cruscotto" di visualizzazioni in-cell direttamente all'interno di un foglio di lavoro esistente.

{{% /alert %}}

## **Personalizzazione dell'Aspetto delle Sparkline**

Una volta che un `SparklineGroup` è stato creato e aggiunto a `worksheet.sparklineGroups`, è possibile leggere o modificare diverse delle sue proprietà visive prima di salvare la cartella di lavoro. Le proprietà più comunemente personalizzate sono:

- **`group.type`** — il `SparklineType` (Linea, Colonna o Stacked). Viene impostato quando il gruppo viene aggiunto, ma è possibile rileggerlo per confermare.
- **`group.line.color`** — il colore della linea, espresso come un `CellsColor` creato tramite `workbook.createCellsColor()`. Questa è la proprietà da utilizzare per il colore del tratto delle sparkline a linee.
- **`group.line.weight`** — lo spessore della linea in punti. Valori più alti producono linee più spesse.
- **Indicatori dei punti massimi/minimi** — flag che attivano piccoli indicatori sui punti dati più alti e più bassi, utili per enfatizzare gli estremi.
- **Indicatori dei punti primo/ultimo/negativo** — flag che attivano/disattivano gli indicatori sui punti dati primo, ultimo e negativo.

Per modificare un colore, creare sempre un'istanza di `CellsColor` e assegnarla alla proprietà pertinente. Non assegnare direttamente un `System.Drawing.Color` alle proprietà di colore delle sparkline — si aspettano il tipo `CellsColor` da `Aspose.Cells.Drawing`. Il metodo `sparklineGroups.add` stesso restituisce un oggetto `SparklineGroup` completamente tipizzato, quindi è possibile concatenare le assegnazioni delle proprietà sul valore restituito o memorizzarlo in una variabile locale e personalizzarlo prima di salvare.



{{< app/cells/assistant language="javascript" >}}