---
title: Aspose.Cells Java per Jython
type: docs
weight: 70
url: /it/java/aspose-cells-java-for-jython/
---
## **introduzione**

### **Cos'è Jython?**

Jython è un'implementazione Java di Python che unisce potenza espressiva e chiarezza. Jython è disponibile gratuitamente sia per uso commerciale che non commerciale ed è distribuito con il codice sorgente. Jython è complementare a Java ed è particolarmente adatto per le seguenti attività:

- **Script incorporato** Java i programmatori possono aggiungere le librerie Jython al proprio sistema per consentire agli utenti finali di scrivere script semplici o complicati che aggiungono funzionalità all'applicazione.
- **Sperimentazione interattiva** - Jython fornisce un interprete interattivo che può essere utilizzato per interagire con i pacchetti Java o con le applicazioni Java in esecuzione. Ciò consente ai programmatori di sperimentare ed eseguire il debug di qualsiasi sistema Java utilizzando Jython.
- **Sviluppo rapido di applicazioni** - I programmi Python sono in genere 2-10 volte più brevi del programma Java equivalente. Ciò si traduce direttamente in una maggiore produttività del programmatore. La perfetta interazione tra Python e Java consente agli sviluppatori di combinare liberamente le due lingue sia durante lo sviluppo che nella spedizione dei prodotti.

### **Aspose.Cells for Java**

Aspose.Cells for Java è una libreria di classi avanzata for Java che ti consente di eseguire una vasta gamma di attività di elaborazione dei documenti direttamente all'interno del tuo Java
applicazioni.

Aspose.Cells for Java supporta l'elaborazione Cells (DOC, DOCX, OOXML, RTF) HTML, OpenDocument, PDF, EPUB, XPS, SWF e tutti i formati immagine. Con Aspose.Cells puoi
generare, modificare e convertire documenti senza utilizzare Microsoft Cells.

### **Aspose.Cells Java per Jython**

Aspose.Cells Java per Jython è un progetto che dimostra/fornisce gli esempi di utilizzo Aspose.Cells for Java API in Jython.

## **Requisiti di sistema e piattaforme supportate**

### **Requisiti di sistema**

**Di seguito sono riportati i requisiti di sistema per utilizzare Aspose.Cells Java per Jython:**

- Java 1.5 o superiore installato
- Componente Aspose.Cells scaricato
- Jyton 2.7.0

### **Piattaforme supportate**

**Di seguito le piattaforme supportate:**

- Aspose.Cells 15.4 e superiori.
- Java IDE (Eclipse, NetBeans...)

## **Scarica Installazione e utilizzo**

### **Download**

**Scarica esempi da siti Web di social coding**

Le seguenti versioni di esempi in esecuzione sono disponibili per il download su tutti i siti di social coding sotto indicati:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)

**Scarica il componente Aspose.Cells for Java**

- [Aspose.Cells for Java](https://releases.aspose.com/cells/java/)

### **Installazione**

- Posiziona il file jar Aspose.Cells for Java scaricato nella directory "lib".
- Sostituisci "your-lib" con il nome del file jar scaricato nel file _*init*_.py.

### **Usando**

Puoi creare un documento HelloWorld utilizzando il seguente codice di esempio:

{{< highlight "java" >}}

 from aspose-cells  import Settings

from com.aspose.Cells import Document

from com.aspose.Cells import DocumentBuilder

class HelloWorld:

    def __init__(self):

        dataDir = Settings.dataDir + 'quickstart/'



        workbook = Workbook()



        sheet = workbook.getWorksheets().get(0)



        cell = sheet.getCells().get("A1")



        cell.setValue("Hello World!")



        file_format_type = FileFormatType



        workbook.save(dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )



        print "Document has been saved, please check the output file.";

if __name__ == '__main__':

    HelloWorld()

{{< /highlight >}}

## **Supporto, estensione e contributo**

### **Supporto**

Fin dai primi giorni di Aspose, sapevamo che solo dare ai nostri clienti buoni prodotti non sarebbe bastato. Avevamo anche bisogno di fornire un buon servizio. Siamo sviluppatori noi stessi e comprendiamo quanto sia frustrante quando un problema tecnico o una stranezza nel software ti impedisce di fare ciò che devi fare. Siamo qui per risolvere i problemi, non per crearli.

Per questo offriamo assistenza gratuita. Chiunque utilizzi il nostro prodotto, sia che lo abbia acquistato o che stia utilizzando una valutazione, merita la nostra piena attenzione e rispetto.

Puoi registrare eventuali problemi o suggerimenti relativi a Aspose.Cells Java per Jython utilizzando una delle seguenti piattaforme:

- [Github](https://github.com/aspose-words/Aspose.Words-for-Java/issues)

### **Estendi e contribuisci**

Aspose.Cells Java per Jython è open source e il suo codice sorgente è disponibile sui principali siti Web di social coding elencati di seguito. Gli sviluppatori sono incoraggiati a scaricare il codice sorgente ea contribuire suggerendo o aggiungendo nuove funzionalità o migliorando quelle esistenti, in modo che anche altri possano trarne vantaggio.

### **Codice sorgente**

È possibile ottenere il codice sorgente più recente da una delle seguenti posizioni

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)
