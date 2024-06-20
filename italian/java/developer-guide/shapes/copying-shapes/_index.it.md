---
title: Copia delle Forme tra Fogli di Lavoro
type: docs
weight: 250
url: /it/java/copy-shapes-between-worksheets/
---

{{% alert color="primary" %}}

A volte, è necessario copiare immagini, grafici e altri oggetti di disegno su fogli di lavoro diversi secondo le proprie esigenze. Aspose.Cells supporta la copia delle forme tra fogli di lavoro. I grafici, le immagini e altri oggetti vengono copiati con il massimo grado di precisione.

Potresti provare l'Automazione di Ufficio ma ha i suoi inconvenienti. Ci sono diverse ragioni e problemi coinvolti: ad esempio sicurezza, stabilità, scalabilità, velocità, prezzo e funzionalità. In breve, ci sono molte ragioni, con la principale che Microsoft stesso sconsiglia vivamente l'automazione di Office dalle soluzioni software.

In questo articolo, creiamo una applicazione console, eseguiamo la copia di immagini, grafici e altri oggetti di disegno tra i fogli di lavoro di un documento con poche e semplici righe di codice utilizzando Aspose.Cells.

Questo documento è progettato per fornire ai programmatori una comprensione dettagliata su come copiare forme (immagini, grafici, controlli e altri oggetti di disegno) tra fogli di lavoro.

{{% /alert %}}

## **Copia delle Forme**

Questo articolo spiega come:

- [Copia un'immagine da un foglio di lavoro a un altro](/cells/it/java/copy-shapes-between-worksheets/#copying-a-picture-from-one-worksheet-to-another).
- [Copia un grafico da un foglio di lavoro a un altro](/cells/it/java/copy-shapes-between-worksheets/#task-2-copying-a-chart-from-one-worksheet-to-another).
- [Copia controlli e altri oggetti di disegno da un foglio di lavoro a un altro](/cells/it/java/copy-shapes-between-worksheets/#task-3-copying-controls-and-other-drawing-objects-from-one-worksheet-to-another).

### **Copia di un'Immagine da un Foglio di Lavoro a un Altro**

#### **Passo 1: Creare un foglio di lavoro con immagine e grafico in Microsoft Excel**

1. Creato un nuovo foglio di lavoro in Microsoft Excel.
1. Aggiungi un'immagine sul primo foglio di lavoro e un grafico sul secondo foglio di lavoro.

   Le schermate seguenti mostrano i due modelli di fogli di lavoro creati in Microsoft Excel.

   **Foglio di lavoro “Grafico” con grafico**

![todo:image_alt_text](copy-shapes-between-worksheets_1.png)

**Foglio di lavoro “Immagine” con immagine**

![todo:image_alt_text](copy-shapes-between-worksheets_2.png)

Ora, copia l'immagine nel foglio di lavoro chiamato “Immagine” nell'ultimo foglio di lavoro “Risultato”.

#### **Passo 2: Scarica Aspose.Cells.Zip**

1. [Scarica Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. Estrarlo sul tuo computer di sviluppo.

   Tutti i componenti [Aspose](http://www.aspose.com/), una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e inserisce solo filigrane nei documenti prodotti.

#### **Passo 3: Crea un Progetto**

Puoi creare un progetto utilizzando un editor Java, ad esempio Eclipse, oppure creare un semplice programma con Notepad.

#### **Passo 4: Aggiungi Percorso di Classe**

Per impostare un Percorso di Classe usando Eclipse, segui i seguenti passaggi:

1. Estrai Aspose.Cells.jar e dom4j_1.6.1.jar da Aspose.Cells.zip.
1. Imposta il percorso di classe del progetto in Eclipse:
1. Seleziona il tuo progetto in Eclipse e poi clicca sui menu Progetto-Proprietà.
1. Seleziona "Percorso di compilazione Java" sul lato sinistro della finestra popup, poi seleziona la scheda "Librerie", clicca su "Aggiungi JAR" o "Aggiungi JAR Esterno" per selezionare Aspose.Cells.jar e dom4j_1.6.1.jar e aggiungerli ai percorsi di compilazione.
1. Scrivi un'applicazione per invocare le API dei componenti di Aspose.

Oppure puoi impostarlo in fase di esecuzione al prompt dei comandi DOS in Windows. Per esempio:

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

#### **Passo 5: Copia di un'immagine da un foglio di lavoro a un altro**

Di seguito è riportato il codice per completare il compito. Copia un'immagine dal foglio di lavoro chiamato “Immagine” al foglio di lavoro “Risultato”.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyPicturefromOneWorksheetToAnother-CopyPicturefromOneWorksheetToAnother.java" >}}

#### **Compito Risultato 1:**

Dopo aver eseguito il codice sopra, l'immagine dal foglio di lavoro “Immagine” è stata ora copiata nell'ultimo foglio di lavoro “Risultato”

**Foglio di lavoro “Risultato” con immagine copiata**

![todo:image_alt_text](copy-shapes-between-worksheets_3.png)

### **Compito 2: Copia di un Grafico da un Foglio di Lavoro a un Altro**

#### **Passo 1: Copia un grafico da un foglio di lavoro a un altro**

Di seguito è riportato il codice effettivo utilizzato dal componente per completare il compito.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyChartFromOneWorksheetToAnother-CopyChartFromOneWorksheetToAnother.java" >}}

#### **Risultato Compito 2**

Dopo aver eseguito il codice sopra, il grafico dal foglio di lavoro 'Grafico' è copiato nel foglio di lavoro 'Risultato'. Si prega di consultare lo snapshot seguente del foglio di lavoro risultante.

**Foglio di lavoro 'Risultato' con immagine e grafico copiati**

![todo:image_alt_text](copy-shapes-between-worksheets_4.png)

### **Compito 3: Copiare Controlli e Altri Oggetti Disegnati da un Foglio di Lavoro a un Altro**

**Foglio di lavoro 'Controllo' con casella di testo e ovale**

![todo:image_alt_text](copy-shapes-between-worksheets_5.png)

Si prega di seguire i seguenti semplici passaggi che è necessario eseguire per ottenere i risultati desiderati.

#### **Passo 1: Copiare un foglio di lavoro tra cartelle di lavoro**

Di seguito è riportato il codice utilizzato dal componente per completare il compito.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyWorksheetBetweenWorkbooks-CopyWorksheetBetweenWorkbooks.java" >}}

#### **Risultato Compito 3**

Dopo aver eseguito il codice sopra, i controlli dal foglio di lavoro 'Controllo' sono ora copiati nel foglio di lavoro 'Risultato'. Si prega di consultare lo snapshot seguente di 'Risultato'.

**Foglio di lavoro 'Risultato' con casella di testo e ovale copiati**

![todo:image_alt_text](copy-shapes-between-worksheets_6.png)

## **Conclusioni**

Questo articolo ha mostrato come copiare diverse forme come immagini, grafici e altri oggetti disegnati tra utilizzando Aspose.Cells. Speriamo che ti darà qualche spunto e sarai in grado di utilizzare queste opzioni in base a diversi scenari.

Aspose.Cells può offrire maggiore flessibilità rispetto ad altri per soluzioni e fornisce velocità, efficienza e affidabilità eccezionali per soddisfare specifiche esigenze dell'applicazione aziendale. I risultati dimostrano che Aspose.Cells ha beneficiato di anni di ricerca, progettazione e attenta sintonizzazione.

Accogliamo con favore le tue domande, commenti e suggerimenti nel [Forum Aspose.Cells](https://forum.aspose.com/c/cells/9).
