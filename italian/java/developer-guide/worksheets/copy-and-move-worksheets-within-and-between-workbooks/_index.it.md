---
title: Copiare e Spostare Fogli di Lavoro All interno e Tra Workbooks
type: docs
weight: 20
url: /it/java/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

A volte è necessario un numero di fogli di lavoro con formattazione comune e inserimento dati. Ad esempio, se lavori con i bilanci trimestrali, potresti voler creare un foglio con fogli che contengono gli stessi titoli di colonna, titoli di riga e formule. C'è un modo per farlo: creando un foglio e poi copiandolo tre volte.

Aspose.Cells supporta la copia o lo spostamento dei fogli di lavoro all'interno o tra i workbook. I fogli di lavoro, compresi dati, formattazione, tabelle, matrici, grafici, immagini e altri oggetti, vengono copiati con il massimo grado di precisione.

{{% /alert %}}

## **Copia e Sposta Fogli di Lavoro**

Questo articolo spiega come utilizzare Aspose.Cells per:

- [Copia di un foglio di lavoro all'interno di un libro di lavoro](/cells/it/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-within-a-workbook).
- [Sposta un foglio di lavoro all'interno di un libro di lavoro](/cells/it/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-with-in-a-workbook).
- [Copia di un foglio di lavoro tra i libri di lavoro](/cells/it/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-between-workbooks).
- [Sposta un foglio di lavoro tra i libri di lavoro](/cells/it/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-between-workbooks).

### **Copiare un foglio di lavoro all'interno di un libro di lavoro**

I passaggi iniziali sono gli stessi per tutti gli esempi.

1. Creare due libri di lavoro con alcuni dati in Microsoft Excel. A fini di questo esempio, abbiamo creato due nuovi libri di lavoro in Microsoft Excel e inserito alcuni dati nei fogli di lavoro.

- FirstWorkbook.xls (3 fogli di lavoro)
- SecondWorkbook.xls (1 foglio di lavoro).

  **FirstWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_1.png)

**SecondWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_2.png)

1. Scarica e installa Aspose.Cells:
   1. [Scarica Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
   1. Estrarlo sul tuo computer di sviluppo.
      Tutti i componenti [Aspose](http://www.aspose.com/), una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e inserisce solo filigrane nei documenti prodotti.
1. Crea un progetto:
   1. Crea un progetto utilizzando un editor Java come Eclipse o crea un programma semplice utilizzando un editor di testo.
1. Aggiungi un percorso di classe:
   1. Estrai Aspose.Cells.jar e dom4j_1.6.1.jar da Aspose.Cells.zip.
   1. Imposta il percorso di classe del progetto in Eclipse:
      1. Seleziona il tuo progetto in Eclipse e clicca su **Progetto**, poi su **Proprietà**.
      1. Seleziona **Percorso di build Java** nel lato sinistro della finestra di dialogo, poi seleziona la scheda Librerie.
      1. Clicca su **Aggiungi JAR** o **Aggiungi JAR Esterno** per selezionare Aspose.Cells.jar e dom4j_1.6.1.jar e aggiungerli ai percorsi di build.

{{% alert color="primary" %}}

Oppure puoi impostare il percorso di classe all'avvio in un prompt dei comandi su Windows.
Per esempio:

{{< highlight java >}}

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

{{% /alert %}}

1. Copia il foglio di lavoro all'interno di un workbook:
   Di seguito è riportato il codice utilizzato per completare il compito. Copia il foglio di lavoro Copia all'interno di FirstWorkbook.xls.

Eseguendo il codice sposta il foglio di lavoro chiamato Copia all'interno di FirstWorkbook.xls con il nuovo nome Ultimo Foglio.

**File di output**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWithinWorkbook-1.java" >}}

### **Spostare un Foglio di Lavoro all'interno di un Workbook**

Di seguito è riportato il codice utilizzato per completare il compito.

Eseguendo il codice sposta il foglio di lavoro Move dall'indice 1 all'indice 2 in FirstWorkbook.xls.

**File di output**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

### **Copia un Foglio di Lavoro tra i Workbooks**

Eseguendo il codice copia il foglio di lavoro Copia in SecondWorkbook.xls con il nuovo nome Foglio2.

**File di output**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.java" >}}

### **Spostare un foglio di lavoro tra i Workbooks**

Eseguendo il codice sposta il foglio di lavoro move da FirstWorkbook.xls a SecondWorkbook.xls con il nuovo nome Foglio3.

**PrimoWorkbook.xls di output**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_6.png)

**SecondoWorkbook.xls di output**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

## **Conclusioni**

{{% alert color="primary" %}}

Questo articolo spiega come copiare e spostare i fogli di lavoro all'interno e tra cartelle di lavoro utilizzando Aspose.Cells.

Aspose.Cells ha beneficiato di anni di ricerca, progettazione e attenta messa a punto. Accogliamo con favore le vostre domande, commenti e suggerimenti al [Forum Aspose.Cells](https://forum.aspose.com/c/cells/9). Garantiamo una risposta tempestiva.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
