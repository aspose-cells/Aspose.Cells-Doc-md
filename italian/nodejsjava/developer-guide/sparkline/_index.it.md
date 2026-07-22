---
title: Sparkline in Aspose.Cells for Node.js via Java
linktitle: Sparkline
description: Aspose.Cells è una libreria Node.js via Java per lavorare con file di fogli di calcolo che supporta la creazione di sparkline — grafici in miniatura inseriti all'interno delle celle del foglio di lavoro. Questo articolo spiega come aggiungere e personalizzare sparkline a linee, a colonne e win/loss utilizzando la libreria Aspose.Cells.
keywords: Aspose.Cells, libreria Node.js via Java, foglio di calcolo, sparkline, sparkline a linee, sparkline a colonne, sparkline win/loss, SparklineGroup, SparklineType
type: docs
weight: 195
url: /it/nodejs-java/creating-sparklines/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supporta la creazione di sparkline all'interno delle celle del foglio di lavoro. Le sparkline sono grafici in miniatura che si adattano a una singola cella, fornendo una rapida rappresentazione visiva delle tendenze dei dati. Aspose.Cells supporta sparkline a linee, a colonne e win/loss, e ognuna può essere personalizzata per quanto riguarda colore, spessore della linea, punti massimo/minimo e indicatori.

{{% /alert %}}

## **Introduzione**

Le sparkline sono piccoli grafici all'interno delle celle utili quando si desidera visualizzare una rapida tendenza accanto a una riga o colonna di dati senza occupare lo spazio di un grafico completo. Excel supporta tre tipi di sparkline: **a linee**, **a colonne** e **win/loss**. Aspose.Cells rispecchia questa capacità attraverso le API `SparklineGroup` e `SparklineGroupCollection` presenti nel namespace `com.aspose.cells.Charts`.

In Aspose.Cells, ogni sparkline che aggiungi viene creata tramite `worksheet.SparklineGroups.add(...)`, che restituisce un oggetto `SparklineGroup`. È quindi possibile utilizzare tale oggetto per impostare il tipo di sparkline, l'intervallo di dati, la cella di destinazione e le proprietà visive come il colore della linea, lo spessore della linea, gli indicatori e gli indicatori dei punti massimo/minimo.

{{% alert color="primary" %}}

Un singolo `SparklineGroup` può contenere una o più sparkline che condividono lo stesso stile. Quando si chiama `add` e si passa una riga di dati più una singola cella di destinazione, si ottiene una sparkline all'interno di quella cella. Se l'intervallo di destinazione è più ampio di una cella, viene disegnata una sparkline separata in ciascuna cella di destinazione, tutte utilizzando lo stesso stile e intervallo di dati.

{{% /alert %}}

Questo articolo illustra ciascuno dei tre tipi di sparkline supportati da Aspose.Cells — **Linee**, **Colonne** e **Win/Loss** — e mostra come aggiungerli, personalizzare i loro colori e salvare la cartella di lavoro risultante.

## **Sparkline a linee**

Una sparkline a linee disegna una linea continua attraverso i punti dati di una serie, rendendola la scelta più naturale per mostrare le tendenze nel tempo. In Aspose.Cells, una sparkline a linee viene creata passando `SparklineType.Line` al metodo `SparklineGroups.add`.

Il flusso di lavoro è lo stesso di qualsiasi altro tipo di sparkline:

1. Crea un nuovo `Workbook` e accedi al primo foglio di lavoro.
2. Popola una riga di dati di origine (ad esempio, riga 1, colonne da A a E) con i valori che desideri visualizzare.
3. Costruisci un `CellArea` che descriva la cella di destinazione in cui verrà disegnata la sparkline.
4. Chiama `worksheet.SparklineGroups.add(SparklineType.Line, "A1:E1", false, dest)`. Il terzo argomento — `false` — indica ad Aspose.Cells che l'intervallo di dati è orizzontale (una riga), non verticale (una colonna).
5. Facoltativamente, personalizza il `SparklineGroup` restituito. Per una sparkline a linee puoi impostare il colore della linea utilizzando `group.Line.Color` (che si aspetta un `CellsColor` da `com.aspose.cells.Drawing`), regolare lo spessore della linea e attivare/disattivare gli indicatori dei punti massimo/minimo.
6. Salva la cartella di lavoro.

L'esempio seguente crea una cartella di lavoro, scrive i valori 5, -3, 8, -2, 6 nelle celle da A1 a E1 e aggiunge una sparkline a linee nella cella F1 che traccia tali valori. Personalizza inoltre il colore della linea in rosso e abilita gli indicatori per i punti massimo e minimo.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();

// Passo 2: Scrivi i valori di esempio 5, -3, 8, -2, 6 nelle celle A1:E1
cells.get("A1").putValue(5);
cells.get("B1").putValue(-3);
cells.get("C1").putValue(8);
cells.get("D1").putValue(-2);
cells.get("E1").putValue(6);

// Passo 3: Costruisci un CellArea che punti alla cella di destinazione F1
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);   // colonna F (indicizzata a 0)
dest.setEndColumn(5);
dest.setStartRow(0);      // riga 1 (indicizzata a 0)
dest.setEndRow(0);

// Passo 4: Aggiungi una sparkline di tipo Linea da A1:E1 in F1
// SparklineGroups.Add restituisce l'indice del gruppo appena aggiunto
let index = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(index);

// Passo 5: Crea un CellsColor rosso e assegnalo al colore della linea della sparkline
let red = workbook.createCellsColor();
red.setColor(AsposeCells.Color.fromArgb(255, 0, 0));
group.setSeriesColor(red);

// Passo 6: Abilita i marcatori dei punti alti e bassi
group.setShowHighPoint(true);
group.setShowLowPoint(true);

// Passo 7: Salva la cartella di lavoro
workbook.save("output_line.xlsx");
```

## **Sparkline a colonne**

Una sparkline a colonne rende ciascun punto dati come una barra verticale. Ciò la rende particolarmente adatta a dati la cui magnitudine è significativa — ad esempio, cifre di vendite mensili o conteggi. In Aspose.Cells, crei una sparkline a colonne passando `SparklineType.Column` al metodo `SparklineGroups.add`.

La procedura rispecchia l'esempio della sparkline a linee:

1. Crea un nuovo `Workbook` e accedi al primo foglio di lavoro.
2. Popola lo stesso intervallo di origine (A1:E1) con i valori che desideri visualizzare.
3. Costruisci un `CellArea` che descriva la cella di destinazione.
4. Chiama `worksheet.SparklineGroups.add(SparklineType.Column, "A1:E1", false, dest)`.
5. Facoltativamente, personalizza il `SparklineGroup` risultante — ad esempio, impostando `group.Type` per confermare il tipo, o modificando il colore delle barre.
6. Salva la cartella di lavoro in un file di output separato in modo che non sovrascriva l'esempio della sparkline a linee.

L'esempio seguente scrive i valori 5, -3, 8, -2, 6 in A1:E1 e rende una sparkline a colonne in F1. I valori negativi sono disegnati come barre rivolte verso il basso e i valori positivi come barre rivolte verso l'alto, il che rende facile individuare a colpo d'occhio i contributi positivi e negativi.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Passo 2: Scrivere valori di esempio in A1:E1
let values = [5, -3, 8, -2, 6];
for (let i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}

// Passo 3: Creare un CellArea che punta a F1 (indice colonna 5, indice riga 0)
let dest = new AsposeCells.CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// Passo 4: Aggiungere una sparkline a colonne alla cella di destinazione
let idx = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Column, "A1:E1", false, dest);
let group = worksheet.getSparklineGroups().get(idx);

// Passo 5: Confermare il tipo di sparkline leggendo group.Type
console.log("Sparkline Type added: " + group.getType());

// Passo 6: Salvare la cartella di lavoro
workbook.save("output_column.xlsx");

console.log("Workbook saved as output_column.xlsx");
```

## **Sparkline Win/Loss**

Una sparkline win/loss è una variante speciale della sparkline a colonne progettata per mostrare solo due esiti: un valore positivo è disegnato come una barra "su" (una vittoria) e un valore zero o negativo è disegnato come una barra "giù" (una sconfitta). Le sparkline win/loss sono comunemente utilizzate per visualizzare sequenze di vittorie e sconfitte, risultati di superamento/fallimento o qualsiasi esito binario nel tempo.

In Aspose.Cells, una sparkline win/loss viene creata passando `SparklineType.Stacked` al metodo `SparklineGroups.add`. (Nonostante il nome, `SparklineType.Stacked` è il valore enum utilizzato per richiedere il rendering win/loss.)

La procedura è la stessa degli altri due tipi:

1. Crea un nuovo `Workbook` e accedi al primo foglio di lavoro.
2. Popola l'intervallo di origine. Poiché le sparkline win/loss trattano ogni valore come una vittoria o una sconfitta, la magnitudine del valore non conta — conta solo il suo segno. I valori positivi diventano barre verso l'alto e i valori non positivi diventano barre verso il basso.
3. Costruisci un `CellArea` che descriva la cella di destinazione.
4. Chiama `worksheet.SparklineGroups.add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Facoltativamente, personalizza il `SparklineGroup` restituito, ad esempio impostando i colori accent per le barre di vittoria e sconfitta.
6. Salva la cartella di lavoro con un nome file distinto in modo che tutti e tre gli esempi possano coesistere su disco.

L'esempio seguente utilizza gli stessi dati di input delle due sezioni precedenti. I valori 5, -3, 8, -2, 6 sono interpretati come vittoria, sconfitta, vittoria, sconfitta, vittoria — e la sparkline disegnata in F1 riflette esattamente quel pattern.

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

// Passo 4: Aggiungi uno sparkline Win/Loss (SparklineType.Stacked)
let groupIndex = worksheet.getSparklineGroups().add(
    AsposeCells.SparklineType.Stacked,
    "A1:E1",
    false,
    dest
);
let group = worksheet.getSparklineGroups().get(groupIndex);

// Passo 5: Personalizza il gruppo di sparkline
// Abilita i marcatori dei punti alti e bassi
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// Imposta il colore del punto alto a verde
let highColor = workbook.createCellsColor();
highColor.setColor(AsposeCells.Color.getGreen());
group.setHighPointColor(highColor);

// Imposta il colore del punto basso a rosso
let lowColor = workbook.createCellsColor();
lowColor.setColor(AsposeCells.Color.getRed());
group.setLowPointColor(lowColor);

// Imposta il colore dei punti negativi a arancione
let negColor = workbook.createCellsColor();
negColor.setColor(AsposeCells.Color.getOrange());
group.setNegativePointsColor(negColor);

// Imposta il colore predefinito della serie (usato per le barre positive)
let seriesColor = workbook.createCellsColor();
seriesColor.setColor(AsposeCells.Color.getSteelBlue());
group.setSeriesColor(seriesColor);

// Passo 6: Salva la cartella di lavoro
workbook.save("output_winloss.xlsx");

console.log("Workbook salvato con successo: output_winloss.xlsx");
```

## **Combinazione di tutti e tre i tipi di sparkline**

I tre esempi precedenti producono ciascuno la propria cartella di lavoro in modo che i file di output siano facili da ispezionare in isolamento. In uno scenario reale, tuttavia, si vorrà spesso confrontare più serie di dati fianco a fianco. Il modo più pulito per farlo è inserire più di un gruppo di sparkline nello stesso foglio di lavoro, con ciascun gruppo che rende uno stile diverso.

È possibile aggiungere più oggetti `SparklineGroup` alla stessa `SparklineGroupCollection`, e ciascun gruppo può avere come target una cella di destinazione diversa o un intervallo diverso. Ad esempio, potresti inserire una sparkline a linee in F1, una sparkline a colonne in F2 e una sparkline win/loss in F3 — tutte leggendo dagli stessi dati di origine nella riga 1 — in modo che il lettore possa vedere tre diversi trattamenti visivi degli stessi numeri.

L'esempio combinato seguente crea una singola cartella di lavoro, popola la riga 1 con i valori 5, -3, 8, -2, 6, e poi aggiunge tre gruppi di sparkline nelle celle F1, F2 e F3 — uno per ciascun tipo — in modo che il file risultante dimostri tutti e tre gli stili di sparkline contemporaneamente.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Passo 2: Popola i dati di esempio nella riga 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Passo 3: Aggiungi un gruppo di sparkline Linea in F1
let lineArea = new AsposeCells.CellArea();
lineArea.setStartColumn(5);
lineArea.setEndColumn(5);
lineArea.setStartRow(0);
lineArea.setEndRow(0);
let lineIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, "A1:E1", false, lineArea);
let lineGroup = worksheet.getSparklineGroups().get(lineIdx);

// Personalizza il colore della sparkline Linea tramite CellsColor
let lineColor = workbook.createCellsColor();
lineColor.setColor(AsposeCells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);

// Passo 4: Aggiungi un gruppo di sparkline Colonna in F2
let columnArea = new AsposeCells.CellArea();
columnArea.setStartColumn(5);
columnArea.setEndColumn(5);
columnArea.setStartRow(1);
columnArea.setEndRow(1);
let columnIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "A1:E1", false, columnArea);
let columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// Personalizza il colore della serie di sparkline Colonna
let columnColor = workbook.createCellsColor();
columnColor.setColor(AsposeCells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);

// Passo 5: Aggiungi un gruppo di sparkline Vittoria/Perdita (In pila) in F3
let stackedArea = new AsposeCells.CellArea();
stackedArea.setStartColumn(5);
stackedArea.setEndColumn(5);
stackedArea.setStartRow(2);
stackedArea.setEndRow(2);
let stackedIdx = worksheet.getSparklineGroups().add(AsposeCells.SparklineType.Stacked, "A1:E1", false, stackedArea);
let stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// Personalizza il colore della serie di sparkline Vittoria/Perdita
let stackedColor = workbook.createCellsColor();
stackedColor.setColor(AsposeCells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);

// Passo 6: Salva la cartella di lavoro
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

Quando combini più gruppi di sparkline in un singolo foglio di lavoro, ciascun gruppo è indipendente. Possono condividere lo stesso intervallo di origine o utilizzare intervalli di origine diversi, e possono essere stilizzati indipendentemente. Ciò rende facile costruire un piccolo "dashboard" di visualizzazioni all'interno delle celle direttamente in un foglio di lavoro esistente.

{{% /alert %}}

## **Personalizzazione dell'aspetto delle sparkline**

Una volta che un `SparklineGroup` è stato creato e aggiunto a `worksheet.SparklineGroups`, è possibile leggere o modificare diverse delle sue proprietà visive prima di salvare la cartella di lavoro. Le proprietà più comunemente personalizzate sono:

- **`group.Type`** — il `SparklineType` (Line, Column o Stacked). Viene impostato quando il gruppo viene aggiunto, ma è possibile rileggerlo per confermarlo.
- **`group.Line.Color`** — il colore della linea, espresso come `CellsColor` creato tramite `workbook.createCellsColor()`. Questa è la proprietà da utilizzare per il colore del tratto della sparkline a linee.
- **`group.Line.Weight`** — lo spessore della linea in punti. Valori più alti producono linee più spesse.
- **Indicatori dei punti massimo/minimo** — flag che attivano piccoli indicatori sui punti dati più alti e più bassi, utili per enfatizzare gli estremi.
- **Indicatori dei punti primo/ultimo/negativo** — flag che attivano/disattivano gli indicatori sui punti dati primo, ultimo e negativo.

Per modificare un colore, crea sempre un'istanza di `CellsColor` e assegnala alla proprietà pertinente. Non assegnare un `java.awt.Color` direttamente alle proprietà di colore delle sparkline — si aspettano il tipo `CellsColor` da `com.aspose.cells.Drawing`. Il metodo `SparklineGroups.add` stesso restituisce un oggetto `SparklineGroup` completamente tipizzato, quindi è possibile concatenare le assegnazioni di proprietà sul valore restituito o memorizzarlo in una variabile locale e personalizzarlo prima del salvataggio.



{{< app/cells/assistant language="javascript" >}}