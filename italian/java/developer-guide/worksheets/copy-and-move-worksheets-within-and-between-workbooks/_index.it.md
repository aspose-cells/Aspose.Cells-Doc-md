---
title: Copia e sposta i fogli di lavoro all'interno e tra le cartelle di lavoro
type: docs
weight: 20
url: /it/java/copy-and-move-worksheets-within-and-between-workbooks/
---
{{% alert color="primary" %}}

volte, hai bisogno di un numero di fogli di lavoro con formattazione e immissione dati comuni. Ad esempio, se lavori con budget trimestrali, potresti voler creare una cartella di lavoro con fogli che contengono le stesse intestazioni di colonna, intestazioni di riga e formule. C'è un modo per farlo: creando un foglio e poi copiandolo tre volte.

Aspose.Cells supporta la copia o lo spostamento di fogli di lavoro all'interno o tra cartelle di lavoro. Fogli di lavoro inclusi dati, formattazione, tabelle, matrici, grafici, immagini e altri oggetti vengono copiati con il massimo grado di precisione.

{{% /alert %}}

## **Copiare e spostare fogli di lavoro**

Questo articolo spiega come utilizzare Aspose.Cells per:

- [Copiare un foglio di lavoro all'interno di una cartella di lavoro](/cells/it/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-within-a-workbook).
- [Sposta un foglio di lavoro all'interno di una cartella di lavoro](/cells/it/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-with-in-a-workbook).
- [Copia un foglio di lavoro tra le cartelle di lavoro](/cells/it/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-between-workbooks).
- [Sposta un foglio di lavoro tra le cartelle di lavoro](/cells/it/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-between-workbooks).

### **Copia di un foglio di lavoro all'interno di una cartella di lavoro**

I passaggi iniziali sono gli stessi per tutti gli esempi.

1. Crea due cartelle di lavoro con alcuni dati in Microsoft Excel. Ai fini di questo esempio, abbiamo creato due nuove cartelle di lavoro in Microsoft Excel e inserito alcuni dati nei fogli di lavoro.

- FirstWorkbook.xls (3 fogli di lavoro)
- SecondWorkbook.xls (1 foglio di lavoro).

  **FirstWorkbook.xls**

![cose da fare:immagine_alt_testo](copy-and-move-worksheets-within-and-between-workbooks_1.png)

**SecondWorkbook.xls**

![cose da fare:immagine_alt_testo](copy-and-move-worksheets-within-and-between-workbooks_2.png)

1. Scarica e installa Aspose.Cells:
   1. [Scarica Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
 1. Decomprimilo sul tuo computer di sviluppo.
 Tutto[Aspose](http://www.aspose.com/) i componenti, una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e si limita a inserire filigrane nei documenti prodotti.
1. Crea un progetto:
 1. Creare un progetto utilizzando un editor Java come Eclipse o creare un semplice programma utilizzando un editor di testo.
1. Aggiungi un percorso di classe:
1. Estrarre Aspose.Cells.jar e dom4j_1.6.1.jar da Aspose.Cells.zip.
 1. Imposta il classpath del progetto in Eclipse:
 1. Seleziona il tuo progetto in Eclipse e fai clic sui menu**Progetto** , poi**Proprietà**.
 1. Selezionare**Percorso di compilazione Java** nella parte sinistra della finestra di dialogo, quindi seleziona la scheda Librerie,
 1. Fare clic**Aggiungi JAR** o**Aggiungi JAR esterni** per selezionare Aspose.Cells.jar e dom4j_1.6.1.jar e aggiungerli nei percorsi di compilazione.

{{% alert color="primary" %}}

Oppure puoi impostare il classpath in fase di esecuzione in un prompt di DOS su Windows.
Per esempio:

{{< highlight "java" >}}

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

{{% /alert %}}

1. Copia il foglio di lavoro all'interno di una cartella di lavoro:
 Di seguito è riportato il codice utilizzato da per eseguire l'attività. Copia il foglio di lavoro Copia all'interno di FirstWorkbook.xls.

L'esecuzione del codice sposta il foglio di lavoro denominato Copia all'interno di FirstWorkbook.xls con il nuovo nome Last Sheet.

**File di uscita**

![cose da fare:immagine_alt_testo](copy-and-move-worksheets-within-and-between-workbooks_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWithinWorkbook-1.java" >}}

### **Spostare un foglio di lavoro con in una cartella di lavoro**

Di seguito è riportato il codice utilizzato per eseguire l'attività.

L'esecuzione del codice sposta il foglio di lavoro Sposta dall'indice 1 all'indice 2 in FirstWorkbook.xls.

**File di uscita**

![cose da fare:immagine_alt_testo](copy-and-move-worksheets-within-and-between-workbooks_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

### **Copia di un foglio di lavoro tra cartelle di lavoro**

L'esecuzione del codice copia il foglio di lavoro Copy in SecondWorkbook.xls con il nuovo nome Sheet2.

**File di uscita**

![cose da fare:immagine_alt_testo](copy-and-move-worksheets-within-and-between-workbooks_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.java" >}}

### **Spostare un foglio di lavoro tra cartelle di lavoro**

L'esecuzione del codice sposta il foglio di lavoro di spostamento da FirstWorkbook.xls a SecondWorkbook.xls con il nuovo nome Sheet3.

**Output FirstWorkbook.xls**

![cose da fare:immagine_alt_testo](copy-and-move-worksheets-within-and-between-workbooks_6.png)

**Output SecondWorkbook.xls**

![cose da fare:immagine_alt_testo](copy-and-move-worksheets-within-and-between-workbooks_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

## **Conclusione**

{{% alert color="primary" %}}

Questo articolo spiega come copiare e spostare i fogli di lavoro all'interno e tra le cartelle di lavoro utilizzando Aspose.Cells.

 Aspose.Cells ha beneficiato di anni di ricerca, progettazione e attenta messa a punto. Accogliamo con favore le vostre domande, commenti e suggerimenti a[Aspose.Cells Foro](https://forum.aspose.com/c/cells/9). Garantiamo una pronta risposta.

{{% /alert %}}
