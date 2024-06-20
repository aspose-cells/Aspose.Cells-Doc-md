---
title: Applicare la formattazione condizionale nei fogli di lavoro
type: docs
weight: 40
url: /it/java/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Questo articolo è progettato per fornire una comprensione dettagliata di come aggiungere la formattazione condizionale a un intervallo di celle in un foglio di lavoro.

La formattazione condizionale è una funzionalità avanzata di Microsoft Excel che consente di applicare formati a un intervallo di celle e di far sì che la formattazione cambi a seconda del valore della cella o del valore di una formula. Ad esempio, lo sfondo di una cella può essere rosso per evidenziare un valore negativo, o il colore del testo potrebbe essere verde per un valore positivo. Quando il valore della cella soddisfa la condizione di formattazione, la formattazione viene applicata. Se il valore della cella non soddisfa la condizione di formattazione, viene utilizzata la formattazione predefinita della cella.

È possibile applicare la formattazione condizionale con la Automazione di Office di Microsoft ma ciò comporta alcuni svantaggi. Sono coinvolte diverse ragioni e problemi: ad esempio, sicurezza, stabilità, scalabilità e velocità. Il motivo principale per trovare un'altra soluzione è che Microsoft stessa sconsiglia vivamente l'Automazione di Office per le soluzioni software.

Questo articolo mostra come creare un'applicazione console, aggiungere la formattazione condizionale alle celle con poche semplici righe di codice utilizzando l'API di Aspose.Cells.

{{% /alert %}}

## **Lavorare con la formattazione condizionale**

Questo articolo affronta i seguenti compiti:

1. [Utilizzando Aspose.Cells per applicare formattazione condizionale basata sul valore della cella](/cells/it/java/apply-conditional-formatting-in-worksheets/#task-1-using-asposecells-to-apply-conditional-formatting-based-on-cell-value).
1. [Utilizzando Aspose.Cells per applicare formattazione condizionale basata su una formula](/cells/it/java/apply-conditional-formatting-in-worksheets/#task-2-using-asposecells-to-apply-conditional-formatting-based-on-a-formula).

### **Attività 1: Utilizzo di Aspose.Cells per Applicare la Formattazione Condizionale Basata sul Valore della Cella**

1. **Scarica e installa Aspose.Cells.zip**:
   1. [Download](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
   1. Estrarlo sul tuo computer di sviluppo.
      Tutti i componenti Aspose, una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e inserisce solo filigrane nei documenti prodotti.
1. **Crea un progetto**.
   Creare un progetto utilizzando un editor Java come Eclipse o creare un programma semplice utilizzando un editor di testo.
1. **Aggiungi il percorso della classe**.
   Per impostare un Percorso di Classe usando Eclipse, segui i seguenti passaggi:
   1. Estrai Aspose.Cells.jar e dom4j_1.6.1.jar da Aspose.Cells.zip.
   1. Imposta il percorso di classe del progetto in Eclipse:
      1. Seleziona il tuo progetto in Eclipse e seleziona **Proprietà** dal menu **Progetto**.
      1. Seleziona "Java Build Path" a sinistra della finestra di dialogo.
      1. Nella scheda **Librerie**, seleziona **Aggiungi JAR** o **Aggiungi JAR Esterno** per selezionare Aspose.Cells.jar e dom4j_1.6.1.jar e aggiungerli ai percorsi di compilazione.
   1. Scrivi un'applicazione per invocare le API dei componenti di Aspose.
      Oppure è possibile impostare il percorso in fase di esecuzione su un prompt DOS in Windows.

{{< highlight java >}}

  javac -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName  

{{< /highlight >}}

1. **Applicare formattazione condizionale basata sul valore della cella**.
   Di seguito è riportato il codice utilizzato dal componente per completare l'attività. Applica la formattazione condizionale su una cella.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingOnCellValue-ApplyConditionalFormattingOnCellValue.java" >}}

Quando il codice sopra viene eseguito, la formattazione condizionale viene applicata alla cella “A1” nel primo foglio di lavoro del file di output (output.xls). La formattazione condizionale applicata a A1 dipende dal valore della cella. Se il valore della cella di A1 è compreso tra 50 e 100 il colore di sfondo è rosso a causa della formattazione condizionale applicata. Si prega di vedere le seguenti immagini dello XLS generato.

**File Excel di Output con valore A1 inferiore a 50**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_1.png)

**File Excel di Output con A1 compreso tra 50 e 100**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_2.png)

### **Attività 2: Utilizzo di Aspose.Cells per Applicare la Formattazione Condizionale Basata su una Formula**

1. **Applicare formattazione condizionale in base a una formula**.
   Di seguito è riportato il codice effettivo utilizzato dal componente per completare il compito. Si applica la formattazione condizionale su “B3”.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingBasedOnFormula-ConditionalFormattingBasedOnFormula.java" >}}

Quando il codice sopra viene eseguito, la formattazione condizionale viene applicata alla cella “B3” nel primo foglio di lavoro del file di output (output.xls). La formattazione condizionale applicata dipende dalla formula che calcola il valore di “B3” come somma di B1 & B2. Si prega di consultare le seguenti schermate del file XLS generato.

**File Excel di output con valore di B3 inferiore a 100**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_3.png)

**File Excel di output con B3 maggiore di 100**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_4.png)

### **Conclusioni**

{{% alert color="primary" %}}

Questo articolo mostra come applicare la formattazione condizionale alle celle in un foglio di lavoro con l'API Aspose.Cells. Speriamo che ti dia un'idea in modo che tu possa utilizzare queste opzioni nei tuoi scenari.

Aspose.Cells offre grande flessibilità per le soluzioni e fornisce velocità, efficienza e affidabilità eccezionali per soddisfare specifici requisiti delle applicazioni aziendali. Aspose.Cells beneficia di anni di ricerca, progettazione e attenta messa a punto.

Accogliamo con piacere le vostre domande, commenti e suggerimenti nel [Forum Aspose.Cells](https://forum.aspose.com/c/cells/9). Garantiamo una risposta tempestiva.

{{% /alert %}}
