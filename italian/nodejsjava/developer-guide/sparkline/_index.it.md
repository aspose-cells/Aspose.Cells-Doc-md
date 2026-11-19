---
title: Sparklines in Aspose.Cells for Node.js via Java
description: Aspose.Cells è una libreria Node.js via Java per lavorare con file di fogli elettronici che supporta la creazione di sparkline, ovvero grafici in miniatura inseriti nelle celle del foglio di lavoro. Questo articolo spiega come aggiungere e personalizzare sparkline a linee, a colonne e di tipo vincita/perdita utilizzando la libreria Aspose.Cells.
linktitle: Sparkline
keywords: Aspose.Cells, libreria Node.js via Java, foglio elettronico, sparkline, sparkline a linee, sparkline a colonne, sparkline vincita/perdita, SparklineGroup, SparklineType
type: docs
weight: 195
url: /it/nodejs-java/creating-sparklines/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta la creazione di sparkline all'interno delle celle del foglio di lavoro. Le sparkline sono grafici in miniatura che si adattano a una singola cella, offrendo una rapida rappresentazione visiva delle tendenze dei dati. Aspose.Cells supporta sparkline a linee, a colonne e di tipo vincita/perdita, ciascuna personalizzabile in termini di colore, spessore della linea, punti massimi/minimi e indicatori.
{{% /alert %}}

## **Introduzione**
Le sparkline sono piccoli grafici all'interno delle celle, utili quando si desidera visualizzare rapidamente una tendenza accanto a una riga o colonna di dati senza occupare lo spazio di un grafico completo. Excel supporta tre tipi di sparkline: **a linee**, **a colonne** e **vincita/perdita**. Aspose.Cells replica questa funzionalità tramite le API `SparklineGroup` e `SparklineGroupCollection` disponibili nel namespace `com.aspose.cells.Charts`.
In Aspose.Cells, ogni sparkline aggiunta viene creata tramite `worksheet.SparklineGroups.add(...)`, che restituisce un oggetto `SparklineGroup`. È quindi possibile utilizzare tale oggetto per impostare il tipo di sparkline, l'intervallo di dati, la cella di destinazione e le proprietà visive come colore della linea, spessore, indicatori e indicatori dei punti massimo/minimo.
Questo articolo illustra ciascuno dei tre tipi di sparkline supportati da Aspose.Cells — **Linee**, **Colonne** e **Vincita/Perdita** — e mostra come aggiungerli, personalizzarne i colori e salvare la cartella di lavoro risultante.

## **Sparkline a linee**
Una sparkline a linee disegna una linea continua attraverso i punti dati di una serie, risultando la scelta più naturale per mostrare tendenze nel tempo. In Aspose.Cells, una sparkline a linee viene creata passando `SparklineType.Line` al metodo `SparklineGroups.add`.
1. Creare un nuovo `Workbook` e accedere al primo foglio di lavoro.
2. Popolare una riga di dati di origine (ad esempio, riga 1, colonne da A a E) con i valori che si desidera visualizzare.
3. Costruire un `CellArea` che descriva la cella di destinazione in cui verrà disegnata la sparkline.
4. Chiamare `worksheet.SparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)`. Il terzo argomento, `false`, indica ad Aspose.Cells che l'intervallo di dati è orizzontale (una riga), non verticale (una colonna).
5. Opzionalmente personalizzare il `SparklineGroup` restituito. Per una sparkline a linee è possibile impostare il colore della linea tramite `group.Line.Color` (che richiede un `CellsColor` da `com.aspose.cells.Drawing`), regolare lo spessore della linea e attivare/disattivare gli indicatori dei punti massimo e minimo.
6. Salvare la cartella di lavoro.
L'esempio seguente crea una cartella di lavoro, scrive i valori 5, -3, 8, -2, 6 nelle celle da A1 a E1 e aggiunge una sparkline a linee nella cella F1 che traccia tali valori. Personalizza inoltre il colore della linea in rosso e attiva gli indicatori per i punti massimo e minimo.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();
// Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);
// Step 3: Build a CellArea pointing to destination cell F1
let dest = new AsposeCells.CellArea();
dest.StartColumn = 5;   // column F (0-indexed)
dest.EndColumn = 5;
dest.StartRow = 0;      // row 1 (0-indexed)
dest.EndRow = 0;
// Step 4: Add a Line sparkline from A1:E1 into F1
// SparklineGroups.Add returns the index of the newly added group
let index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.LINE, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(index);
// Step 5: Create a red CellsColor and assign it to the sparkline line color
let red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);
// Step 6: Enable high-point and low-point markers
group.setShowHighPoint(true);
group.setShowLowPoint(true);
// Step 7: Save the workbook
workbook.save("output_line.xlsx");
```

## **Sparkline a colonne**
Una sparkline a colonne rappresenta ciascun punto dati come una barra verticale. Ciò la rende particolarmente adatta a dati la cui magnitudine è significativa, ad esempio le cifre di vendita mensili o i conteggi. In Aspose.Cells, si crea una sparkline a colonne passando `SparklineType.Column` al metodo `SparklineGroups.add`.
La procedura rispecchia l'esempio della sparkline a linee:
1. Creare un nuovo `Workbook` e accedere al primo foglio di lavoro.
2. Popolare una riga di dati di origine con i valori da visualizzare.
3. Costruire un `CellArea` che descriva la cella di destinazione.
4. Chiamare `worksheet.SparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`.
5. Opzionalmente personalizzare il `SparklineGroup` risultante, impostando ad esempio `group.Type` per confermare il tipo oppure modificando il colore delle barre.
6. Salvare la cartella di lavoro in un file di output separato, in modo che non sovrascriva l'esempio della sparkline a linee.
L'esempio seguente scrive i valori 5, -3, 8, -2, 6 in A1:E1 e visualizza una sparkline a colonne in F1. I valori negativi vengono disegnati come barre rivolte verso il basso e i valori positivi come barre rivolte verso l'alto, il che rende facile individuare a colpo d'occhio i contributi positivi e negative.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Step 2: Write sample values into A1:E1
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}
// Step 3: Build a CellArea pointing to F1 (column index 5, row index 0)
let dest = new AsposeCells.CellArea();
dest.StartColumn = 5;
dest.EndColumn = 5;
dest.StartRow = 0;
dest.EndRow = 0;
// Step 4: Add a Column sparkline to the destination cell
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.COLUMN, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);
// Step 5: Confirm the sparkline type by reading group.Type
console.log("Sparkline Type added: " + group.getType());
// Step 6: Save the workbook
workbook.save("output_column.xlsx");
console.log("Workbook saved as output_column.xlsx");
```

## **Sparkline Vincita/Perdita**
Una sparkline vincita/perdita è una variante speciale della sparkline a colonne progettata per mostrare solo due esiti: un valore positivo viene disegnato come una barra "in alto" (una vittoria), mentre un valore zero o negativo viene disegnato come una barra "in basso" (una sconfitta). Le sparkline vincita/perdita sono comunemente utilizzate per visualizzare sequenze di vittorie e sconfitte, risultati di superamento/fallimento o qualsiasi esito binario nel tempo.
In Aspose.Cells, una sparkline vincita/perdita viene creata passando `SparklineType.Stacked` al metodo `SparklineGroups.add`. (Nonostante il nome, `SparklineType.Stacked` è il valore enum utilizzato per richiedere il rendering vincita/perdita.)
1. Creare un nuovo `Workbook` e accedere al primo foglio di lavoro.
2. Popolare l'intervallo di origine. Poiché le sparkline vincita/perdita trattano ogni valore come una vittoria o una sconfitta, la magnitudine del valore non conta, ma solo il suo segno. I valori positivi diventano barre verso l'alto e i valori non positivi diventano barre verso il basso.
3. Costruire un `CellArea` che descriva la cella di destinazione.
4. Chiamare `worksheet.SparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Opzionalmente personalizzare il `SparklineGroup` restituito, ad esempio impostando i colori accentati per le barre di vittoria e di sconfitta.
6. Salvare la cartella di lavoro con un nome file distinto, in modo che tutti e tre gli esempi possano coesistere su disco.

```javascript
const AsposeCells = require("aspose.cells");
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
dest.StartColumn = 5;   // F
dest.EndColumn = 5;
dest.StartRow = 0;      // row 1
dest.EndRow = 0;
// Step 4: Add a Win/Loss sparkline (SparklineType.STACKED)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.STACKED,
    "A1:E1",
    false,
    dest
);
let group = worksheet.getSparklineGroups().get(groupIndex);
// Step 5: Customize the sparkline group
// Enable high-point and low-point markers
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Set the high-point color to green
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.getGreen());
group.setHighPointColor(highColor);
// Set the low-point color to red
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.getRed());
group.setLowPointColor(lowColor);
// Set the negative-point color to orange
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.getOrange());
group.setNegativePointsColor(negColor);
// Set the default series color (used for positive bars)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.getSteelBlue());
group.setSeriesColor(seriesColor);
// Step 6: Save the workbook
workbook.save("output_winloss.xlsx");
console.log("Workbook saved successfully: output_winloss.xlsx");
```

## **Combinazione dei tre tipi di sparkline**
L'esempio combinato seguente crea una singola cartella di lavoro, popola la riga 1 con i valori 5, -3, 8, -2, 6 e quindi aggiunge tre gruppi di sparkline nelle celle F1, F2 e F3, uno per ciascun tipo, in modo che il file risultante dimostri simultaneamente tutti e tre gli stili di sparkline.

```javascript
const AsposeCells = require("aspose.cells");
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
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.LINE, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Customize the line sparkline color via CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);
// Step 4: Add a Column sparkline group at F2
let columnArea = new AsposeCells.CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.COLUMN, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Customize the column sparkline series color
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);
// Step 5: Add a Win/Loss (Stacked) sparkline group at F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.STACKED, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Customize the win/loss sparkline series color
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);
// Step 6: Save the workbook
workbook.save("output_all.xlsx");
```

## **Personalizzazione dell'aspetto delle sparkline**
Una volta che un `SparklineGroup` è stato creato e aggiunto a `worksheet.SparklineGroups`, è possibile leggere o modificare diverse proprietà visive prima di salvare la cartella di lavoro. Le proprietà più comunemente personalizzate sono:
- **`group.Type`** — il `SparklineType` (Line, Column o Stacked). Viene impostato quando il gruppo viene aggiunto, ma è possibile rileggerlo per confermarlo.
- **`group.Line.Color`** — il colore della linea, espresso come `CellsColor` creato tramite `workbook.createCellsColor()`. Questa è la proprietà da utilizzare per il colore del tratto della sparkline a linee.
- **`group.Line.Weight`** — lo spessore della linea in punti. Valori più alti producono linee più spesse.
- **Indicatori dei punti massimo/minimo** — flag che attivano piccoli indicatori sui punti dati più alti e più bassi, utili per evidenziare gli estremi.
- **Indicatori dei punti primo/ultimo/negativo** — flag che attivano/disattivano gli indicatori sui punti dati primo, ultimo e negativo.
Per modificare un colore, creare sempre un'istanza di `CellsColor` e assegnarla alla proprietà pertinente. Non assegnare un `java.awt.Color` direttamente alle proprietà di colore delle sparkline: esse tipo di un `CellsColor` da `com.aspose.cells.Drawing`. Il metodo `SparklineGroups.add` stesso restituisce un oggetto `SparklineGroup` completamente tipizzato, quindi è possibile concatenare le assegnazioni di proprietà sul valore restituito oppure memorizzarlo in una variabile locale e personalizzarlo prima di salvare.

{{< app/cells/assistant language="nodejs-java" >}}