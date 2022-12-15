---
title: Copia forme tra fogli di lavoro
type: docs
weight: 250
url: /it/java/copy-shapes-between-worksheets/
---
{{% alert color="primary" %}}

volte, è necessario copiare immagini, grafici e altri oggetti di disegno diversi in fogli di lavoro diversi secondo le proprie esigenze. Aspose.Cells supporta la copia di forme tra fogli di lavoro. I grafici, le immagini e altri oggetti vengono copiati con il massimo grado di precisione.

Potresti provare Office Automation, ma questo ha i suoi svantaggi. Ci sono diversi motivi e problemi coinvolti: ad esempio sicurezza, stabilità, scalabilità, velocità, prezzo e funzionalità. In breve, ci sono molte ragioni, la prima delle quali è che la stessa Microsoft sconsiglia vivamente l'automazione dell'ufficio dalle soluzioni software.

In questo articolo, creiamo un'applicazione console, eseguiamo la copia di immagini, grafici e altri oggetti di disegno tra fogli di lavoro di una cartella di lavoro con poche e semplici righe di codice utilizzando Aspose.Cells.

Questo documento è progettato per fornire agli sviluppatori una comprensione dettagliata su come copiare forme (immagini, grafici, controlli e altri oggetti di disegno) tra fogli di lavoro.

{{% /alert %}}

## **Copia di forme**

Questo articolo spiega come:

- [Copia un'immagine da un foglio di lavoro a un altro](/cells/it/java/copy-shapes-between-worksheets/#copying-a-picture-from-one-worksheet-to-another).
- [Copia un grafico da un foglio di lavoro a un altro](/cells/it/java/copy-shapes-between-worksheets/#task-2-copying-a-chart-from-one-worksheet-to-another).
- [Copia controlli e altri oggetti di disegno da un foglio di lavoro a un altro](/cells/it/java/copy-shapes-between-worksheets/#task-3-copying-controls-and-other-drawing-objects-from-one-worksheet-to-another).

### **Copiare un'immagine da un foglio di lavoro a un altro**

#### **Passaggio 1: creazione di una cartella di lavoro con immagine e grafico in Microsoft Excel**

1. Creata una nuova cartella di lavoro in Microsoft Excel.
1. Aggiungi un'immagine sul primo foglio di lavoro e un grafico sul secondo foglio di lavoro.

 Gli screenshot seguenti mostrano i due fogli di lavoro modello creati in Microsoft Excel.

   **Foglio di lavoro "Grafico" con grafico**

![cose da fare:immagine_alt_testo](copy-shapes-between-worksheets_1.png)

**Foglio di lavoro "Immagine" con immagine**

![cose da fare:immagine_alt_testo](copy-shapes-between-worksheets_2.png)

Ora, copia l'immagine nel foglio di lavoro denominato "Immagine" nell'ultimo foglio di lavoro "Risultato".

#### **Passo 2: Scarica Aspose.Cells.Zip**

1. [Scarica Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. Decomprimilo sul tuo computer di sviluppo.

 Tutto[Aspose](http://www.aspose.com/) i componenti, una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e si limita a inserire filigrane nei documenti prodotti.

#### **Passaggio 3: creare un progetto**

Puoi creare un progetto utilizzando un editor Java, ad esempio Eclipse o creare un semplice programma utilizzando un Blocco note.

#### **Passaggio 4: aggiungi Class Path**

Per impostare un Class Path utilizzando Eclipse, eseguire i seguenti passaggi:

1. Estrai Aspose.Cells.jar e dom4j_1.6.1.jar da Aspose.Cells.zip.
1. Imposta il classpath del progetto in Eclipse:
1. Seleziona il tuo progetto in Eclipse, quindi fai clic sui menu Project-Properties.
1. Selezionare "Java Build Path" nella parte sinistra della finestra popup, quindi selezionare la scheda "Librerie", fare clic su "Aggiungi JAR" o "Aggiungi JAR esterni" per selezionare Aspose.Cells.jar e dom4j_1.6.1.jar e aggiungerli alla build percorsi.
1. Scrivere un'applicazione per richiamare le API dei componenti di Aspose.

Oppure puoi impostarlo in fase di esecuzione al prompt di DOS in Windows. Per esempio:

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; Nome della classe

#### **Passaggio 5: copia di un'immagine da un foglio di lavoro a un altro**

Di seguito è riportato il codice per eseguire l'operazione. Copia un'immagine dal foglio di lavoro denominato "Immagine" al foglio di lavoro "Risultato".

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyPicturefromOneWorksheetToAnother-CopyPicturefromOneWorksheetToAnother.java" >}}

#### **Risultato Compito 1:**

Dopo aver eseguito il codice precedente, l'immagine dal foglio di lavoro "Immagine" viene ora copiata nell'ultimo foglio di lavoro "Risultato"

**Foglio di lavoro "Risultato" con immagine copiata**

![cose da fare:immagine_alt_testo](copy-shapes-between-worksheets_3.png)

### **Attività 2: copiare un grafico da un foglio di lavoro a un altro**

#### **Passaggio 1: copia un grafico da un foglio di lavoro a un altro**

Di seguito è riportato il codice effettivo utilizzato dal componente per eseguire l'attività.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyChartFromOneWorksheetToAnother-CopyChartFromOneWorksheetToAnother.java" >}}

#### **Risultato Compito 2**

Dopo aver eseguito il codice precedente, il grafico dal foglio di lavoro "Grafico" viene copiato nel foglio di lavoro "Risultato". Si prega di vedere la seguente istantanea del foglio di lavoro risultante.

**Foglio di lavoro "Risultato" con immagine e grafico copiati**

![cose da fare:immagine_alt_testo](copy-shapes-between-worksheets_4.png)

### **Attività 3: Copia di controlli e altri oggetti di disegno da un foglio di lavoro a un altro**

**Foglio di lavoro "Controllo" con casella di testo e ovale**

![cose da fare:immagine_alt_testo](copy-shapes-between-worksheets_5.png)

Si prega di consultare i seguenti semplici passaggi che è necessario eseguire per ottenere i risultati desiderati.

#### **Passaggio 1: copia di un foglio di lavoro tra cartelle di lavoro**

Di seguito è riportato il codice utilizzato dal componente per eseguire l'attività.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyWorksheetBetweenWorkbooks-CopyWorksheetBetweenWorkbooks.java" >}}

#### **Risultato Compito 3**

Dopo aver eseguito il codice precedente, i controlli dal foglio di lavoro "Controllo" vengono ora copiati nel foglio di lavoro "Risultato". Si prega di vedere la seguente istantanea di "Risultato".

**Foglio di lavoro "Risultato" con casella di testo copiata e ovale**

![cose da fare:immagine_alt_testo](copy-shapes-between-worksheets_6.png)

## **Conclusione**

Questo articolo ha mostrato come copiare forme diverse come immagini, grafici e altri oggetti di disegno tra l'utilizzo di Aspose.Cells. Si spera che ti dia un'idea e sarai in grado di utilizzare queste opzioni in base ai tuoi diversi scenari.

Aspose.Cells è in grado di offrire maggiore flessibilità rispetto ad altri per le soluzioni e fornisce velocità, efficienza e affidabilità eccezionali per soddisfare specifici requisiti applicativi aziendali. I risultati mostrano che Aspose.Cells ha beneficiato di anni di ricerca, progettazione e attenta messa a punto.

 Accogliamo con favore le vostre domande, commenti e suggerimenti nel[Aspose.Cells Foro](https://forum.aspose.com/c/cells/9).
