---
title: Sparkline in Aspose.Cells for Node.js via C++
description: Aspose.Cells è una libreria Node.js per lavorare con file di fogli di calcolo che supporta la creazione di sparkline, ovvero grafici in miniatura posizionati all'interno delle celle del foglio di lavoro. Questo articolo spiega come aggiungere e personalizzare sparkline a linea, a colonne e win/loss utilizzando la libreria Aspose.Cells.
linktitle: Sparkline
keywords: Aspose.Cells, libreria Node.js, foglio di calcolo, sparkline, sparkline a linea, sparkline a colonne, sparkline win/loss, SparklineGroup, SparklineType
type: docs
weight: 195
url: /it/nodejs-cpp/creating-sparklines/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta la creazione di sparkline all'interno delle celle del foglio di lavoro. Le sparkline sono grafici in miniatura che si adattano a una singola cella, fornendo una rapida rappresentazione visiva delle tendenze dei dati. Aspose.Cells supporta sparkline a linea, a colonne e win/loss, e ciascuna può essere personalizzata per colore, spessore della linea, punti massimi/minimi e marcatori.
{{% /alert %}}

## **Introduzione**
Le sparkline sono piccoli grafici all'interno delle celle, utili quando si desidera visualizzare rapidamente una tendenza accanto a una riga o colonna di dati senza occupare lo spazio di un grafico completo. Excel supporta tre tipi di sparkline: **a linea**, **a colonne** e **win/loss**. Aspose.Cells replica questa funzionalità attraverso le API `SparklineGroup` e `SparklineGroupCollection` presenti nel namespace `Aspose.Cells.Charts`.
In Aspose.Cells, ogni sparkline che si aggiunge viene creata tramite `worksheet.sparklineGroups.add(...)`, che restituisce un oggetto `SparklineGroup`. È quindi possibile utilizzare tale oggetto per impostare il tipo di sparkline, l'intervallo di dati, la cella di destinazione e le proprietà visive come il colore della linea, lo spessore della linea, i marcatori e gli indicatori dei punti massimi/minimi.
Questo articolo esamina ciascuno dei tre tipi di sparkline supportati da Aspose.Cells — **Linea**, **Colonne** e **Win/Loss** — e mostra come aggiungerli, personalizzare i loro colori e salvare la cartella di lavoro risultante.

## **Sparkline a linea**
Una sparkline a linea traccia una linea continua attraverso i punti dati di una serie, rendendola la scelta più naturale per mostrare le tendenze nel tempo. In Aspose.Cells, una sparkline a linea viene creata passando `SparklineType.Line` al metodo `sparklineGroups.add`.
1. Creare un nuovo `Workbook` e accedere al primo foglio di lavoro.
2. Popolare una riga di dati di origine (ad esempio, riga 1, colonne da A a E) con i valori che si desidera visualizzare.
3. Creare un `CellArea` che descriva la cella di destinazione in cui verrà disegnata la sparkline.
4. Chiamare `worksheet.sparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)`. Il terzo argomento — `false` — indica ad Aspose.Cells che l'intervallo di dati è orizzontale (una riga), non verticale (una colonna).
5. Facoltativamente, personalizzare l'oggetto `SparklineGroup` restituito. Per una sparkline a linea è possibile impostare il colore della linea tramite `group.line.color` (che si aspetta un `CellsColor` da `Aspose.Cells.Drawing`), regolare lo spessore della linea e attivare/disattivare i marcatori dei punti massimi/minimi.
6. Salvare la cartella di lavoro.
L'esempio seguente crea una cartella di lavoro, scrive i valori 5, -3, 8, -2, 6 nelle celle da A1 a E1 e aggiunge una sparkline a linea nella cella F1 che traccia tali valori. Personalizza inoltre il colore della linea in rosso e abilita i marcatori per i punti massimi e minimi.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Step 2: Populate sample data in row 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Step 3: Add a Line sparkline group at F1
let lineArea = new AsposeCells.CellArea();
lineArea.startColumn = 5;
lineArea.endColumn = 5;
lineArea.startRow = 0;
lineArea.endRow = 0;
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Customize the line sparkline color via CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.Blue);
lineGroup.setSeriesColor(lineColor);
// Step 4: Add a Column sparkline group at F2
let columnArea = new AsposeCells.CellArea();
columnArea.startColumn = 5;
columnArea.endColumn = 5;
columnArea.startRow = 1;
columnArea.endRow = 1;
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Customize the column sparkline series color
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.Green);
columnGroup.setSeriesColor(columnColor);
// Step 5: Add a Win/Loss (Stacked) sparkline group at F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.startColumn = 5;
stackedArea.endColumn = 5;
stackedArea.startRow = 2;
stackedArea.endRow = 2;
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Customize the win/loss sparkline series color
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.DarkOrange);
stackedGroup.setSeriesColor(stackedColor);
// Step 6: Save the workbook
workbook.save("output_all.xlsx");
```

## **Sparkline a colonne**
Una sparkline a colonne rappresenta ciascun punto dati come una barra verticale. Ciò la rende particolarmente adatta a dati la cui magnitudine è significativa, ad esempio le cifre delle vendite mensili o i conteggi. In Aspose.Cells, una sparkline a colonne viene creata passando `SparklineType.Column` al metodo `sparklineGroups.add`.
La procedura rispecchia l'esempio della sparkline a linea:
1. Creare un nuovo `Workbook` e accedere al primo foglio di lavoro.
3. Creare un `CellArea` che descriva la cella di destinazione.
4. Chiamare `worksheet.sparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`.
5. Facoltativamente, personalizzare l'oggetto `SparklineGroup` risultante, ad esempio impostando `group.type` per confermare il tipo, oppure modificando il colore delle barre.
6. Salvare la cartella di lavoro in un file di output separato, in modo che non sovrascriva l'esempio della sparkline a linea.
L'esempio seguente scrive i valori 5, -3, 8, -2, 6 in A1:E1 e rende una sparkline a colonne in F1. I valori negativi sono disegnati come barre verso il basso e i valori positivi come barre verso l'alto, il che rende facile individuare a colpo d'occhio i contributi positivi e negativi.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");
// Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Step 3: Build a CellArea pointing to F1 (column 5, row 0)
let dest = new AsposeCells.CellArea();
dest.startColumn = 5;   // F
dest.endColumn = 5;
dest.startRow = 0;      // row 1
dest.endRow = 0;
// Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest);
let group = worksheet.getSparklineGroups().get(groupIndex);
// Step 5: Customize the sparkline group
// Enable high-point and low-point markers
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Set the high-point color to green
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.Green);
group.setHighPointColor(highColor);
// Set the low-point color to red
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.Red);
group.setLowPointColor(lowColor);
// Set the negative-point color to orange
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.Orange);
group.setNegativePointsColor(negColor);
// Set the default series color (used for positive bars)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.SteelBlue);
group.setSeriesColor(seriesColor);
// Step 6: Save the workbook
workbook.save("output_winloss.xlsx");
console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **Sparkline Win/Loss**
Una sparkline win/loss è una variante speciale della sparkline a colonne, progettata per mostrare solo due esiti: un valore positivo viene disegnato come una barra "in alto" (una vittoria) e un valore zero o negativo viene disegnato come una barra "in basso" (una sconfitta). Le sparkline win/loss sono comunemente utilizzate per visualizzare sequenze di vittorie e sconfitte, risultati di successo/fallimento o qualsiasi esito binario nel tempo.
In Aspose.Cells, una sparkline win/loss viene creata passando `SparklineType.Stacked` al metodo `sparklineGroups.add`. (Nonostante il nome, `SparklineType.Stacked` è il valore enum utilizzato per richiedere il rendering win/loss.)
1. Creare un nuovo `Workbook` e accedere al primo foglio di lavoro.
2. Popolare l'intervallo di origine. Poiché le sparkline win/loss trattano ogni valore come una vittoria o una sconfitta, la magnitudine del valore non è rilevante, ma lo è solo il suo segno. I valori positivi diventano barre verso l'alto e i valori non positivi diventano barre verso il basso.
3. Creare un `CellArea` che descriva la cella di destinazione.
4. Chiamare `worksheet.sparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Facoltativamente, personalizzare l'oggetto `SparklineGroup` restituito, ad esempio impostando colori d'accento per le barre di vittoria e sconfitta.
6. Salvare la cartella di lavoro con un nome file distinto, in modo che tutti e tre gli esempi possano coesistere sul disco.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Step 2: Write sample values into A1:E1
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// Step 3: Build a CellArea pointing to F1 (column index 5, row index 0)
let dest = new AsposeCells.CellArea();
dest.startColumn = 5;
dest.endColumn = 5;
dest.startRow = 0;
dest.endRow = 0;
// Step 4: Add a Column sparkline to the destination cell
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);
// Step 5: Confirm the sparkline type by reading group.Type
console.log("Sparkline Type added: " + group.getType());
// Step 6: Save the workbook
workbook.save("output_column.xlsx");
console.log("Workbook saved as output_column.xlsx");
```

## **Combinazione di tutti e tre i tipi di sparkline**
L'esempio combinato seguente crea un'unica cartella di lavoro, popola la riga 1 con i valori 5, -3, 8, -2, 6 e quindi aggiunge tre gruppi di sparkline nelle celle F1, F2 e F3 — uno di ciascun tipo — in modo che il file risultante dimostri tutti e tre gli stili di sparkline contemporaneamente.

```javascript
const AsposeCells = require("aspose.cells.node");
// Step 1: Create a Workbook and get the first worksheet
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
// Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);
// Step 3: Build a CellArea pointing to destination cell F1
const dest = new AsposeCells.CellArea();
dest.startColumn = 5;   // column F (0-indexed)
dest.endColumn = 5;
dest.startRow = 0;      // row 1 (0-indexed)
dest.endRow = 0;
// Step 4: Add a Line sparkline from A1:E1 into F1
// SparklineGroups.Add returns the index of the newly added group
const index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
const group = worksheet.getSparklineGroups().get(index);
// Step 5: Create a red CellsColor and assign it to the sparkline line color
const red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.Red);
group.setSeriesColor(red);
// Step 6: Enable high-point and low-point markers
group.setShowHighPoint(true);
group.setShowLowPoint(true);
// Step 7: Save the workbook
workbook.save("output_line.xlsx");
```

## **Personalizzazione dell'aspetto delle sparkline**
Una volta che un `SparklineGroup` è stato creato e aggiunto a `worksheet.sparklineGroups`, è possibile leggere o modificare diverse delle sue proprietà visive prima di salvare la cartella di lavoro. Le proprietà più comunemente personalizzate sono:
- **`group.type`** — il `SparklineType` (Line, Column o Stacked). Viene impostato quando il gruppo viene aggiunto, ma è possibile rileggerlo per confermarlo.
- **`group.line.color`** — il colore della linea, espresso come un `CellsColor` creato tramite `workbook.createCellsColor()`. Questa è la proprietà da utilizzare per il colore del tratto della sparkline a linea.
- **`group.line.weight`** — lo spessore della linea in punti. Valori più elevati producono linee più spesse.
- **Marcatori dei punti massimo/minimo** — flag che attivano piccoli marcatori sui punti dati più alti e più bassi, utili per evidenziare gli estremi.
- **Marcatori dei punti primo/ultimo/negativo** — flag che attivano/disattivano i marcatori sui punti dati primo, ultimo e negativi.
Per modificare un colore, creare sempre un'istanza di `CellsColor` e assegnarla alla proprietà pertinente. Non assegnare un `System.Drawing.Color` direttamente alle proprietà del colore delle sparkline: queste si aspettano il tipo `CellsColor` di `Aspose.Cells.Drawing`. Il metodo `sparklineGroups.add` stesso restituisce un oggetto `SparklineGroup` completamente tipizzato, quindi è possibile concatenare le assegnazioni di proprietà sul valore restituito oppure memorizzarlo in una variabile locale e personalizzarlo prima di salvare.

{{< app/cells/assistant language="nodejs-cpp" >}}