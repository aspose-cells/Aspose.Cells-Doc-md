---
title: Sparklines in Aspose.Cells per Aspose.Cells per Java
linktitle: Sparkline
description: Aspose.Cells è una libreria Java per lavorare con file di fogli di calcolo che supporta la creazione di sparkline — mini grafici inseriti all'interno delle celle del foglio di lavoro. Questo articolo spiega come aggiungere e personalizzare sparkline a linea, colonna e win/loss utilizzando la libreria Aspose.Cells.
keywords: Aspose.Cells, libreria Java, foglio di calcolo, sparkline, sparkline a linea, sparkline a colonna, sparkline win/loss, SparklineGroup, SparklineType
type: docs
weight: 195
url: /it/java/creating-sparklines/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supporta la creazione di sparkline all'interno delle celle del foglio di lavoro. Le sparkline sono mini grafici che si adattano a una singola cella, fornendo una rapida rappresentazione visiva dell'andamento dei dati. Aspose.Cells supporta sparkline a linea, colonna e win/loss, e ciascuna può essere personalizzata in termini di colore, spessore della linea, punti massimo/minimo e indicatori.

{{% /alert %}}

## **Introduzione**

Le sparkline sono piccoli grafici all'interno delle celle che sono utili quando si desidera visualizzare una rapida tendenza accanto a una riga o colonna di dati senza occupare lo spazio di un grafico completo. Excel supporta tre tipi di sparkline: **linea**, **colonna** e **win/loss**. Aspose.Cells rispecchia questa funzionalità attraverso le API `SparklineGroup` e `SparklineGroupCollection` presenti nel namespace `Aspose.Cells.Charts`.

In Aspose.Cells, ogni sparkline che si aggiunge viene creata tramite `worksheet.getSparklineGroups().add(...)`, che restituisce un oggetto `SparklineGroup`. È quindi possibile utilizzare tale oggetto per impostare il tipo di sparkline, l'intervallo di dati, la cella di destinazione e le proprietà visive come il colore della linea, lo spessore della linea, gli indicatori e gli indicatori dei punti massimo/minimo.

{{% alert color="primary" %}}

Un singolo `SparklineGroup` può contenere una o più sparkline che condividono lo stesso stile. Quando si chiama `add` e si passa una riga di dati più una singola cella di destinazione, si ottiene una sparkline all'interno di tale cella. Se l'intervallo di destinazione è più ampio di una cella, viene disegnata una sparkline separata in ciascuna cella di destinazione, tutte utilizzando lo stesso stile e intervallo di dati.

{{% /alert %}}

Questo articolo illustra ciascuno dei tre tipi di sparkline supportati da Aspose.Cells — **Linea**, **Colonna** e **Win/Loss** — e mostra come aggiungerli, personalizzare i loro colori e salvare la cartella di lavoro risultante.

## **Sparkline a Linea**

Una sparkline a linea disegna una linea continua attraverso i punti dati di una serie, rendendola la scelta più naturale per mostrare tendenze nel tempo. In Aspose.Cells, una sparkline a linea viene creata passando `SparklineType.LINE` al metodo `add`.

Il flusso di lavoro è lo stesso di qualsiasi altro tipo di sparkline:

1. Creare un nuovo `Workbook` e accedere al primo foglio di lavoro.
2. Popolare una riga di dati di origine (ad esempio, riga 1, colonne da A a E) con i valori che si desidera visualizzare.
3. Costruire un `CellArea` che descriva la cella di destinazione in cui verrà disegnata la sparkline.
4. Chiamare `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`. Il terzo argomento — `false` — indica ad Aspose.Cells che l'intervallo di dati è orizzontale (una riga), non verticale (una colonna).
5. Facoltativamente, personalizzare il `SparklineGroup` restituito. Per una sparkline a linea è possibile impostare il colore della linea utilizzando `group.getLine().setColor(...)` (che si aspetta un `CellsColor` da `Aspose.Cells.Drawing`), regolare lo spessore della linea e attivare/disattivare gli indicatori dei punti massimo/minimo.
6. Salvare la cartella di lavoro.

Il seguente esempio crea una cartella di lavoro, scrive i valori 5, -3, 8, -2, 6 nelle celle da A1 a E1 e aggiunge una sparkline a linea nella cella F1 che traccia tali valori. Personalizza inoltre il colore della linea in rosso e abilita gli indicatori per i punti massimo e minimo.

```java
public class CodeRunner {
    public static void main(String[] args) {
        try {
            // Passaggio 1: Crea una cartella di lavoro e ottieni il primo foglio di lavoro
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.getWorksheets().get(0);
            Cells cells = worksheet.getCells();

            // Passaggio 2: Scrivi i valori di esempio 5, -3, 8, -2, 6 nelle celle A1:E1
            cells.get("A1").putValue(5);
            cells.get("B1").putValue(-3);
            cells.get("C1").putValue(8);
            cells.get("D1").putValue(-2);
            cells.get("E1").putValue(6);

            // Passaggio 3: Crea un'area di celle che punti alla cella di destinazione F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // colonna F (indicizzata a 0)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // riga 1 (indicizzata a 0)
            dest.EndRow = 0;

            // Passaggio 4: Aggiungi una sparkline a linea da A1:E1 in F1
            // SparklineGroups.add restituisce l'indice del gruppo appena aggiunto
            int index = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest);
            SparklineGroup group = worksheet.getSparklineGroups().get(index);

            // Passaggio 5: Crea un CellsColor rosso e assegnalo al colore della linea della sparkline
            CellsColor red = workbook.createCellsColor();
            red.setColor(com.aspose.cells.Color.getRed());
            group.setSeriesColor(red);

            // Passaggio 6: Abilita i marcatori dei punti alti e bassi
            group.setShowHighPoint(true);
            group.setShowLowPoint(true);

            // Passaggio 7: Salva la cartella di lavoro
            workbook.save("output_line.xlsx");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

## **Sparkline a Colonna**

Una sparkline a colonna rende ogni punto dati come una barra verticale. Questo la rende particolarmente adatta per dati la cui grandezza è significativa — ad esempio, cifre di vendite mensili o conteggi. In Aspose.Cells, si crea una sparkline a colonna passando `SparklineType.COLUMN` al metodo `add`.

La procedura rispecchia l'esempio della sparkline a linea:

1. Creare un nuovo `Workbook` e accedere al primo foglio di lavoro.
2. Popolare lo stesso intervallo di origine (A1:E1) con i valori che si desidera visualizzare.
3. Costruire un `CellArea` che descriva la cella di destinazione.
4. Chiamare `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`.
5. Facoltativamente, personalizzare il `SparklineGroup` risultante — ad esempio, impostando `group.getType()` per confermare il tipo, oppure modificando il colore delle barre.
6. Salvare la cartella di lavoro in un file di output separato in modo che non sovrascriva l'esempio della sparkline a linea.

L'esempio seguente scrive i valori 5, -3, 8, -2, 6 in A1:E1 e rende una sparkline a colonna in F1. I valori negativi sono disegnati come barre rivolte verso il basso e i valori positivi come barre rivolte verso l'alto, il che rende i contributi positivi e negativi facili da individuare a colpo d'occhio.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Scrivi valori di esempio in A1:E1
int[] values = new int[] { 5, -3, 8, -2, 6 };
for (int i = 0; i < values.length; i++) {
    worksheet.getCells().get(0, i).putValue(values[i]);
}

// Costruisci un CellArea che punta a F1 (indice colonna 5, indice riga 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// Aggiungi una sparkline di tipo Column alla cella di destinazione
int idx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(idx);

// Conferma il tipo di sparkline leggendo group.Type
System.out.println("Sparkline Type added: " + group.getType());

// Salva la cartella di lavoro
workbook.save("output_column.xlsx");

System.out.println("Workbook saved as output_column.xlsx");
```

## **Sparkline Win/Loss**

Una sparkline win/loss è una variante speciale della sparkline a colonna progettata per mostrare solo due esiti: un valore positivo viene disegnato come una barra "su" (una vittoria) e un valore zero o negativo viene disegnato come una barra "giù" (una sconfitta). Le sparkline win/loss sono comunemente utilizzate per visualizzare sequenze di vittorie e sconfitte, risultati pass/fail o qualsiasi esito binario nel tempo.

In Aspose.Cells, una sparkline win/loss viene creata passando `SparklineType.STACKED` al metodo `add`. (Nonostante il nome, `SparklineType.STACKED` è il valore enum utilizzato per richiedere il rendering win/loss.)

La procedura è la stessa degli altri due tipi:

1. Creare un nuovo `Workbook` e accedere al primo foglio di lavoro.
2. Popolare l'intervallo di origine. Poiché le sparkline win/loss trattano ogni valore come una vittoria o una sconfitta, la grandezza del valore non è rilevante — solo il suo segno. I valori positivi diventano barre su e i valori non positivi diventano barre giù.
3. Costruire un `CellArea` che descriva la cella di destinazione.
4. Chiamare `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`.
5. Facoltativamente, personalizzare il `SparklineGroup` restituito, ad esempio impostando i colori di accento per le barre di vittoria e sconfitta.
6. Salvare la cartella di lavoro con un nome file distinto in modo che tutti e tre gli esempi possano coesistere su disco.

L'esempio seguente utilizza gli stessi dati di input delle due sezioni precedenti. I valori 5, -3, 8, -2, 6 sono interpretati come vittoria, sconfitta, vittoria, sconfitta, vittoria — e la sparkline disegnata in F1 riflette esattamente tale schema.

```java
import com.aspose.cells.*;
import com.aspose.cells.charts.*;
import com.aspose.cells.drawing.*;
import java.awt.Color;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("WinLoss");

// Popola dati di esempio
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Crea un CellArea che punta a F1 (colonna 5, riga 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);

// Aggiungi una sparkline Win/Loss (SparklineType.Stacked)
int groupIndex = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(groupIndex);

// Personalizza il gruppo di sparkline
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);

// Imposta il colore del punto massimo su verde
CellsColor highColor = workbook.createCellsColor();
highColor.setColor(Color.GREEN);
group.setHighPointColor(highColor);

// Imposta il colore del punto minimo su rosso
CellsColor lowColor = workbook.createCellsColor();
lowColor.setColor(Color.RED);
group.setLowPointColor(lowColor);

// Imposta il colore dei punti negativi su arancione
CellsColor negColor = workbook.createCellsColor();
negColor.setColor(Color.ORANGE);
group.setNegativePointsColor(negColor);

// Imposta il colore predefinito della serie (usato per le barre positive)
CellsColor seriesColor = workbook.createCellsColor();
seriesColor.setColor(new Color(70, 130, 180)); // Approssimazione di SteelBlue
group.setSeriesColor(seriesColor);

// Salva la cartella di lavoro
workbook.save("output_winloss.xlsx");

System.out.println("Workbook saved successfully: output_winloss.xlsx");
```

## **Combinazione di Tutti e Tre i Tipi di Sparkline**

I tre esempi precedenti producono ciascuno la propria cartella di lavoro in modo che i file di output siano facili da ispezionare in isolamento. In uno scenario reale, tuttavia, si vorrà spesso confrontare più serie di dati affiancate. Il modo più pulito per farlo è inserire più di un gruppo di sparkline nello stesso foglio di lavoro, con ciascun gruppo che rende uno stile diverso.

È possibile aggiungere più oggetti `SparklineGroup` alla stessa `SparklineGroupCollection`, e ciascun gruppo può puntare a una cella di destinazione diversa o a un intervallo diverso. Ad esempio, si potrebbe inserire una sparkline a linea in F1, una sparkline a colonna in F2 e una sparkline win/loss in F3 — leggendo tutte dagli stessi dati di origine nella riga 1 — in modo che il lettore possa vedere tre diversi trattamenti visivi degli stessi numeri.

L'esempio combinato seguente crea una singola cartella di lavoro, popola la riga 1 con i valori 5, -3, 8, -2, 6, e poi aggiunge tre gruppi di sparkline nelle celle F1, F2 e F3 — uno per ciascun tipo — in modo che il file risultante dimostri tutti e tre gli stili di sparkline contemporaneamente.

```java
import com.aspose.cells.*;

// Passo 1: Crea una cartella di lavoro e ottieni il primo foglio di lavoro
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Passo 2: Popola i dati di esempio nella riga 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);

// Passo 3: Aggiungi un gruppo di sparkline a linee in F1
CellArea lineArea = CellArea.createCellArea(0, 5, 0, 5); // Fix: Usa il metodo factory statico
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.getSparklineGroups().get(lineIdx);

// Personalizza il colore della sparkline a linee tramite CellsColor
CellsColor lineColor = workbook.createCellsColor();
lineColor.setColor(com.aspose.cells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);

// Passo 4: Aggiungi un gruppo di sparkline a colonne in F2
CellArea columnArea = CellArea.createCellArea(1, 5, 1, 5); // Fix: Usa il metodo factory statico
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.getSparklineGroups().get(columnIdx);

// Personalizza il colore della serie della sparkline a colonne
CellsColor columnColor = workbook.createCellsColor();
columnColor.setColor(com.aspose.cells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);

// Passo 5: Aggiungi un gruppo di sparkline Win/Loss (Stacked) in F3
CellArea stackedArea = CellArea.createCellArea(2, 5, 2, 5); // Fix: Usa il metodo factory statico
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);

// Personalizza il colore della serie della sparkline win/loss
CellsColor stackedColor = workbook.createCellsColor();
stackedColor.setColor(com.aspose.cells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);

// Passo 6: Salva la cartella di lavoro
workbook.save("output_all.xlsx");
```

{{% alert color="primary" %}}

Quando si combinano più gruppi di sparkline in un singolo foglio di lavoro, ciascun gruppo è indipendente. Possono condividere lo stesso intervallo di origine o utilizzare intervalli di origine diversi, e possono essere stilizzati indipendentemente. Questo rende facile costruire un piccolo "dashboard" di visualizzazioni all'interno delle celle direttamente all'interno di un foglio di lavoro esistente.

{{% /alert %}}

## **Personalizzazione dell'Aspetto delle Sparkline**

Una volta che un `SparklineGroup` è stato creato e aggiunto a `worksheet.getSparklineGroups()`, è possibile leggere o modificare diverse delle sue proprietà visive prima di salvare la cartella di lavoro. Le proprietà più comunemente personalizzate sono:

- **`group.getType()`** — lo `SparklineType` (LINE, COLUMN, o STACKED). Viene impostato quando il gruppo viene aggiunto, ma è possibile rileggerlo per confermarlo.
- **`group.getLine().setColor(...)`** — il colore della linea, espresso come `CellsColor` creato tramite `workbook.createCellsColor()`. Questa è la proprietà da utilizzare per il colore del tratto della sparkline a linea.
- **`group.getLine().setWeight(...)`** — lo spessore della linea in punti. Valori più alti producono linee più spesse.
- **Indicatori dei punti massimo/minimo** — flag che attivano piccoli indicatori sui punti dati più alti e più bassi, utili per enfatizzare gli estremi.
- **Indicatori dei punti primo/ultimo/negativo** — flag che attivano/disattivano gli indicatori sui punti dati primo, ultimo e negativo.

Per modificare un colore, creare sempre un'istanza di `CellsColor` e assegnarla alla proprietà pertinente. Non assegnare un `java.awt.Color` direttamente alle proprietà di colore delle sparkline — si aspettano il tipo `CellsColor` da `Aspose.Cells.Drawing`. Il metodo `add` stesso restituisce un oggetto `SparklineGroup` completamente tipizzato, quindi è possibile concatenare le assegnazioni di proprietà sul valore restituito o memorizzarlo in una variabile locale e personalizzarlo prima di salvare.



{{< app/cells/assistant language="java" >}}