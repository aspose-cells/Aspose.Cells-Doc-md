---
title: Sparkline in Aspose.Cells for Java
description: Aspose.Cells è una libreria Java per lavorare con file di fogli di calcolo che supporta la creazione di sparkline, ovvero grafici in miniatura inseriti nelle celle del foglio di lavoro. Questo articolo spiega come aggiungere e personalizzare sparkline a linea, a colonna e di tipo win/loss utilizzando la libreria Aspose.Cells.
linktitle: Sparkline
keywords: Aspose.Cells, libreria Java, foglio di calcolo, sparkline, sparkline a linea, sparkline a colonna, sparkline win/loss, SparklineGroup, SparklineType
type: docs
weight: 195
url: /it/java/creating-sparklines/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta la creazione di sparkline all'interno delle celle del foglio di lavoro. Le sparkline sono grafici in miniatura che si adattano a una singola cella, offrendo una rappresentazione visiva rapida delle tendenze dei dati. Aspose.Cells supporta sparkline a linea, a colonna e di tipo win/loss, e ciascuna può essere personalizzata per quanto riguarda colore, spessore della linea, punti massimo/minimo e marcatori.

## **Introduzione**
Le sparkline sono piccoli grafici all'interno delle celle, utili quando si desidera visualizzare rapidamente una tendenza accanto a una riga o colonna di dati senza occupare lo spazio di un grafico completo. Excel supporta tre tipi di sparkline: **a linea**, **a colonna** e **win/loss**. Aspose.Cells replica questa funzionalità tramite le API `SparklineGroup` e `SparklineGroupCollection` presenti nel namespace `Aspose.Cells.Charts`.
In Aspose.Cells, ogni sparkline che aggiungi viene creata tramite `worksheet.getSparklineGroups().add(...)`, che restituisce un oggetto `SparklineGroup`. Puoi quindi usare tale oggetto per impostare il tipo di sparkline, l'intervallo di dati, la cella di destinazione e le proprietà visive come il colore della linea, lo spessore, i marcatori e gli indicatori dei punti massimo/minimo.
Questo articolo illustra ciascuno dei tre tipi di sparkline supportati da Aspose.Cells — **Linea**, **Colonna** e **Win/Loss** — e mostra come aggiungerli, personalizzarne i colori e salvare la cartella di lavoro risultante.

## **Sparkline a Linea**
Una sparkline a linea disegna una linea continua attraverso i punti dati di una serie, risultando la scelta più naturale per mostrare tendenze nel tempo. In Aspose.Cells, una sparkline a linea viene creata passando `SparklineType.LINE` al metodo `add`.
1. Crea una nuova `Workbook` e accedi al primo foglio di lavoro.
2. Popola una riga di dati di origine (ad esempio, riga 1, colonne da A a E) con i valori che desideri visualizzare.
3. Costruisci una `CellArea` che descriva la cella di destinazione in cui verrà disegnata la sparkline.
4. Chiama `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`. Il terzo argomento — `false` — indica ad Aspose.Cells che l'intervallo di dati è orizzontale (una riga), non verticale (una colonna).
5. Facoltativamente, personalizza il `SparklineGroup` restituito. Per una sparkline a linea puoi impostare il colore della linea usando `group.getLine().setColor(...)` (che si aspetta un `CellsColor` da `Aspose.Cells.Drawing`), regolare lo spessore della linea e attivare/disattivare i marcatori dei punti massimo/minimo.
6. Salva la cartella di lavoro.
L'esempio seguente crea una cartella di lavoro, scrive i valori 5, -3, 8, -2, 6 nelle celle da A1 a E1 e aggiunge una sparkline a linea nella cella F1 che traccia tali valori. Personalizza inoltre il colore della linea in rosso e abilita i marcatori per i punti massimo e minimo.

```java
public class CodeRunner {
    public static void main(String[] args) {
        try {
            // Passo 1: Crea un Workbook e ottieni il primo foglio di lavoro
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.getWorksheets().get(0);
            Cells cells = worksheet.getCells();
            // Passo 2: Scrivi i valori di esempio 5, -3, 8, -2, 6 nelle celle A1:E1
            cells.get("A1").putValue(5);
            cells.get("B1").putValue(-3);
            cells.get("C1").putValue(8);
            cells.get("D1").putValue(-2);
            cells.get("E1").putValue(6);
            // Passo 3: Costruisci un CellArea che punta alla cella di destinazione F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // colonna F (indicizzata a 0)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // riga 1 (indicizzata a 0)
            dest.EndRow = 0;
            // Passo 4: Aggiungi una sparkline Line da A1:E1 in F1
            // SparklineGroups.add restituisce l'indice del gruppo appena aggiunto
            int index = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest);
            SparklineGroup group = worksheet.getSparklineGroups().get(index);
            // Passo 5: Crea un CellsColor rosso e assegnalo al colore della linea della sparkline
            CellsColor red = workbook.createCellsColor();
            red.setColor(com.aspose.cells.Color.getRed());
            group.setSeriesColor(red);
            // Passo 6: Abilita i marcatori dei punti alti e bassi
            group.setShowHighPoint(true);
            group.setShowLowPoint(true);
            // Passo 7: Salva il workbook
            workbook.save("output_line.xlsx");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

## **Sparkline a Colonna**
Una sparkline a colonna rende ogni punto dati come una barra verticale. Ciò la rende particolarmente adatta a dati la cui magnitudine è significativa — ad esempio, cifre di vendite mensili o conteggi. In Aspose.Cells, crei una sparkline a colonna passando `SparklineType.COLUMN` al metodo `add`.
La procedura rispecchia l'esempio della sparkline a linea:
1. Crea una nuova `Workbook` e accedi al primo foglio di lavoro.
2. Popola una riga di dati di origine (ad esempio, riga 1, colonne da A a E) con i valori che desideri visualizzare.
3. Costruisci una `CellArea` che descriva la cella di destinazione.
4. Chiama `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`.
5. Facoltativamente, personalizza il `SparklineGroup` risultante — ad esempio, impostando `group.getType()` per confermare il tipo, oppure modificando il colore delle barre.
6. Salva la cartella di lavoro in un file di output separato, in modo che non sovrascriva l'esempio della sparkline a linea.
L'esempio seguente scrive i valori 5, -3, 8, -2, 6 in A1:E1 e rende una sparkline a colonna in F1. I valori negativi sono disegnati come barre rivolte verso il basso e i valori positivi come barre rivolte verso l'alto, il che rende facile individuare a colpo d'occhio i contributi positivi e negativi.

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
// Aggiungi uno sparkline a colonne alla cella di destinazione
int idx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(idx);
// Conferma il tipo di sparkline leggendo group.Type
System.out.println("Sparkline Type added: " + group.getType());
// Salva la cartella di lavoro
workbook.save("output_column.xlsx");
System.out.println("Workbook saved as output_column.xlsx");
```

## **Sparkline Win/Loss**
Una sparkline win/loss è una variante speciale della sparkline a colonna progettata per mostrare solo due esiti: un valore positivo viene disegnato come una barra "in su" (una vittoria) e un valore pari a zero o negativo come una barra "in giù" (una sconfitta). Le sparkline win/loss sono comunemente usate per visualizzare sequenze di vittorie e sconfitte, risultati di superamento/fallimento o qualsiasi esito binario nel tempo.
In Aspose.Cells, una sparkline win/loss viene creata passando `SparklineType.STACKED` al metodo `add`. (Nonostante il nome, `SparklineType.STACKED` è il valore enum utilizzato per richiedere il rendering win/loss.)
1. Crea una nuova `Workbook` e accedi al primo foglio di lavoro.
2. Popola l'intervallo di origine. Poiché le sparkline win/loss trattano ogni valore come una vittoria o una sconfitta, la magnitudine del valore non è rilevante — conta solo il suo segno. I valori positivi diventano barre in su e i valori non positivi diventano barre in giù.
3. Costruisci una `CellArea` che descriva la cella di destinazione.
4. Chiama `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`.
5. Facoltativamente, personalizza il `SparklineGroup` restituito, ad esempio impostando i colori principali per le barre di vittoria e sconfitta.
6. Salva la cartella di lavoro con un nome file distinto, in modo che tutti e tre gli esempi possano coesistere su disco.

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
// Costruisci un CellArea che punta a F1 (colonna 5, riga 0)
CellArea dest = new CellArea();
dest.setStartColumn(5);
dest.setEndColumn(5);
dest.setStartRow(0);
dest.setEndRow(0);
// Aggiungi uno sparkline Win/Loss (SparklineType.Stacked)
int groupIndex = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest);
SparklineGroup group = worksheet.getSparklineGroups().get(groupIndex);
// Personalizza il gruppo di sparkline
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.setShowNegativePoints(true);
// Imposta il colore del punto massimo a verde
CellsColor highColor = workbook.createCellsColor();
highColor.setColor(Color.GREEN);
group.setHighPointColor(highColor);
// Imposta il colore del punto minimo a rosso
CellsColor lowColor = workbook.createCellsColor();
lowColor.setColor(Color.RED);
group.setLowPointColor(lowColor);
// Imposta il colore del punto negativo ad arancione
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

## **Combinazione di tutti e tre i tipi di Sparkline**
L'esempio combinato seguente crea una singola cartella di lavoro, popola la riga 1 con i valori 5, -3, 8, -2, 6 e quindi aggiunge tre gruppi di sparkline nelle celle F1, F2 e F3 — uno per ciascun tipo — in modo che il file risultante dimostri tutti e tre gli stili di sparkline contemporaneamente.

```java
import com.aspose.cells.*;
// Passo 1: Creare una Workbook e ottenere il primo foglio di lavoro
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Passo 2: Popolare i dati di esempio nella riga 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5);
worksheet.getCells().get("B1").putValue(-3);
worksheet.getCells().get("C1").putValue(8);
worksheet.getCells().get("D1").putValue(-2);
worksheet.getCells().get("E1").putValue(6);
// Passo 3: Aggiungere un gruppo di sparkline Linea in F1
CellArea lineArea = CellArea.createCellArea(0, 5, 0, 5); // Correzione: Usare il metodo factory statico
int lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.getSparklineGroups().get(lineIdx);
// Personalizzare il colore della sparkline linea tramite CellsColor
CellsColor lineColor = workbook.createCellsColor();
lineColor.setColor(com.aspose.cells.Color.getBlue());
lineGroup.setSeriesColor(lineColor);
// Passo 4: Aggiungere un gruppo di sparkline Colonna in F2
CellArea columnArea = CellArea.createCellArea(1, 5, 1, 5); // Correzione: Usare il metodo factory statico
int columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.getSparklineGroups().get(columnIdx);
// Personalizzare il colore della serie della sparkline colonna
CellsColor columnColor = workbook.createCellsColor();
columnColor.setColor(com.aspose.cells.Color.getGreen());
columnGroup.setSeriesColor(columnColor);
// Passo 5: Aggiungere un gruppo di sparkline Win/Loss (Stacked) in F3
CellArea stackedArea = CellArea.createCellArea(2, 5, 2, 5); // Correzione: Usare il metodo factory statico
int stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.getSparklineGroups().get(stackedIdx);
// Personalizzare il colore della serie della sparkline win/loss
CellsColor stackedColor = workbook.createCellsColor();
stackedColor.setColor(com.aspose.cells.Color.getDarkOrange());
stackedGroup.setSeriesColor(stackedColor);
// Passo 6: Salvare la workbook
workbook.save("output_all.xlsx");
```

## **Personalizzazione dell'aspetto delle Sparkline**
Una volta creato e aggiunto un `SparklineGroup` a `worksheet.getSparklineGroups()`, è possibile leggere o modificare diverse delle sue proprietà visive prima di salvare la cartella di lavoro. Le proprietà più comunemente personalizzate sono:
- **`group.getType()`** — lo `SparklineType` (LINE, COLUMN o STACKED). Viene impostato quando il gruppo viene aggiunto, ma è possibile rileggerlo per confermarlo.
- **`group.getLine().setColor(...)`** — il colore della linea, espresso come `CellsColor` creato tramite `workbook.createCellsColor()`. Questa è la proprietà da usare per il colore del tratto della sparkline a linea.
- **`group.getLine().setWeight(...)`** — lo spessore della linea in punti. Valori più alti producono linee più spesse.
- **Marcatori dei punti massimo/minimo** — flag che attivano piccoli marcatori sui punti dati più alti e più bassi, utili per evidenziare gli estremi.
- **Marcatori dei punti primo/ultimo/negativo** — flag che attivano/disattivano i marcatori sui punti dati primo, ultimo e negativo.
Per cambiare un colore, crea sempre un'istanza di `CellsColor` e assegnala alla proprietà pertinente. Non assegnare direttamente un `java.awt.Color` alle proprietà di colore delle sparkline — si aspettano il tipo `CellsColor` di `Aspose.Cells.Drawing`. Il metodo `add` stesso restituisce un oggetto `SparklineGroup` completamente tipizzato, quindi puoi concatenare le assegnazioni di proprietà sul valore restituito oppure memorizzarlo in una variabile locale e personalizzarlo prima del salvataggio.
{{% /alert %}}

{{< app/cells/assistant language="java" >}}