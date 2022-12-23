---
title: Applicare la formattazione condizionale nei fogli di lavoro
type: docs
weight: 40
url: /it/java/apply-conditional-formatting-in-worksheets/
---
{{% alert color="primary" %}}

Questo articolo è progettato per fornire informazioni dettagliate su come aggiungere la formattazione condizionale a un intervallo di celle in un foglio di lavoro.

La formattazione condizionale è una funzionalità avanzata in Microsoft Excel che consente di applicare formati a un intervallo di celle e di modificare la formattazione in base al valore della cella o al valore di una formula. Ad esempio, lo sfondo di una cella potrebbe essere rosso per evidenziare un valore negativo oppure il colore del testo potrebbe essere verde per un valore positivo. Quando il valore della cella soddisfa la condizione del formato, viene applicato il formato. Se il valore della cella non soddisfa la condizione del formato, viene utilizzata la formattazione predefinita della cella.

È possibile applicare la formattazione condizionale con Microsoft Office Automation ma questo ha i suoi svantaggi. Ci sono diversi motivi e problemi coinvolti: ad esempio, sicurezza, stabilità, scalabilità e velocità. Il motivo principale per trovare un'altra soluzione è che lo stesso Microsoft sconsiglia vivamente Office Automation per le soluzioni software.

Questo articolo mostra come creare un'applicazione console, aggiungere la formattazione condizionale alle celle con poche semplici righe di codice utilizzando Aspose.Cells API.

{{% /alert %}}

## **Lavorare con la formattazione condizionale**

Questo articolo funziona attraverso le seguenti attività:

1. [Utilizzo di Aspose.Cells per applicare la formattazione condizionale in base al valore della cella](/cells/it/java/apply-conditional-formatting-in-worksheets/#task-1-using-asposecells-to-apply-conditional-formatting-based-on-cell-value).
1. [Utilizzo di Aspose.Cells per applicare la formattazione condizionale basata su una formula](/cells/it/java/apply-conditional-formatting-in-worksheets/#task-2-using-asposecells-to-apply-conditional-formatting-based-on-a-formula).

### **Attività 1: utilizzo di Aspose.Cells per applicare la formattazione condizionale in base al valore Cell**

1. **Scaricare e installare Aspose.Cells.zip**:
   1. [Scaricamento](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
 1. Decomprimilo sul tuo computer di sviluppo.
 Tutti i componenti Aspose, una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e inserisce solo filigrane nei documenti prodotti.
1. **Crea un progetto**.
 Crea un progetto utilizzando un editor Java come Eclipse o crea un semplice programma utilizzando un editor di testo.
1. **Aggiungi percorso di classe**.
 Per impostare un Class Path utilizzando Eclipse, eseguire i seguenti passaggi:
1. Estrarre Aspose.Cells.jar e dom4j_1.6.1.jar da Aspose.Cells.zip.
 1. Imposta il classpath del progetto in Eclipse:
 1. Seleziona il tuo progetto in Eclipse e poi seleziona**Proprietà** dal**Progetto** menù.
 1. Selezionare "Java Build Path" a sinistra della finestra di dialogo.
 1. Sul**Biblioteche** scheda, selezionare**Aggiungi JAR** o**Aggiungi JAR esterni** per selezionare Aspose.Cells.jar e dom4j_1.6.1.jar e aggiungerli nei percorsi di compilazione.
 1. Scrivere un'applicazione per richiamare le API dei componenti di Aspose.
 Oppure puoi impostare il percorso in fase di esecuzione su un prompt di DOS in Windows.

{{< highlight "java" >}}

  javac -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName  

{{< /highlight >}}

1. **Applicare la formattazione condizionale in base al valore della cella**.
 Di seguito è riportato il codice utilizzato dal componente per eseguire l'attività. Applica la formattazione condizionale su una cella.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingOnCellValue-ApplyConditionalFormattingOnCellValue.java" >}}

Quando viene eseguito il codice precedente, la formattazione condizionale viene applicata alla cella "A1" nel primo foglio di lavoro del file di output (output.xls). La formattazione condizionale applicata ad A1 dipende dal valore della cella. Se il valore della cella di A1 è compreso tra 50 e 100, il colore di sfondo è rosso a causa della formattazione condizionale applicata. Si prega di vedere i seguenti screenshot del file XLS generato.

**File Excel di output con valore A1 inferiore a 50**

![cose da fare:immagine_alt_testo](apply-conditional-formatting-in-worksheets_1.png)

**File di output Excel con A1 tra 50 e 100**

![cose da fare:immagine_alt_testo](apply-conditional-formatting-in-worksheets_2.png)

### **Attività 2: utilizzo di Aspose.Cells per applicare la formattazione condizionale basata su una formula**

1. **Applicare la formattazione condizionale in base alla formula**.
 Di seguito è riportato il codice effettivo utilizzato dal componente per eseguire l'attività. Applica la formattazione condizionale su "B3".

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingBasedOnFormula-ConditionalFormattingBasedOnFormula.java" >}}

Quando viene eseguito il codice precedente, la formattazione condizionale viene applicata alla cella "B3" nel primo foglio di lavoro del file di output (output.xls). La formattazione condizionale applicata dipende dalla formula che calcola il valore di "B3" come somma di B1 e B2. Si prega di vedere i seguenti screenshot del file XLS generato.

**File di output Excel con valore B3 inferiore a 100**

![cose da fare:immagine_alt_testo](apply-conditional-formatting-in-worksheets_3.png)

**File Excel di output con B3 maggiore di 100**

![cose da fare:immagine_alt_testo](apply-conditional-formatting-in-worksheets_4.png)

### **Conclusione**

{{% alert color="primary" %}}

Questo articolo mostra come applicare la formattazione condizionale alle celle in un foglio di lavoro con Aspose.Cells API. Si spera che ti fornisca alcune informazioni in modo da poter utilizzare queste opzioni nei tuoi scenari.

Aspose.Cells offre una grande flessibilità per le soluzioni e fornisce velocità, efficienza e affidabilità eccezionali per soddisfare specifici requisiti applicativi aziendali. Aspose.Cells beneficia di anni di ricerca, progettazione e attenta messa a punto.

 Accogliamo con favore le vostre domande, commenti e suggerimenti nel[Aspose.Cells Foro](https://forum.aspose.com/c/cells/9). Garantiamo una pronta risposta.

{{% /alert %}}
