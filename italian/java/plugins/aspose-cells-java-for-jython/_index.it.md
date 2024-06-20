---
title: Aspose.Cells Java for Jython
type: docs
weight: 70
url: /it/java/aspose-cells-java-for-jython/
---

## **Introduzione**

### **Cos'è Jython?**

Jython è un'implementazione di Python in Java che combina potenza espressiva con chiarezza. Jython è liberamente disponibile sia per uso commerciale che non commerciale ed è distribuito con il codice sorgente. Jython è complementare a Java ed è particolarmente adatto per i seguenti compiti:

- **Scripting integrato** - I programmatori Java possono aggiungere le librerie Jython al proprio sistema per consentire agli utenti finali di scrivere script semplici o complessi che aggiungono funzionalità all'applicazione.
- **Sperimentazione interattiva** - Jython fornisce un interprete interattivo che può essere utilizzato per interagire con i pacchetti Java o con le applicazioni Java in esecuzione. Ciò consente ai programmatori di sperimentare e debuggare qualsiasi sistema Java utilizzando Jython.
- **Sviluppo rapido dell'applicazione** - I programmi Python sono tipicamente 2-10 volte più brevi del programma Java equivalente. Questo si traduce direttamente in un aumento della produttività del programmatore. L'interazione senza soluzione di continuità tra Python e Java consente agli sviluppatori di mescolare liberamente i due linguaggi sia durante lo sviluppo che nella distribuzione dei prodotti.

### **Aspose.Cells for Java**

Aspose.Cells for Java è una libreria di classi avanzata per Java che consente di eseguire una vasta gamma di attività di elaborazione documenti direttamente all'interno del tuo Java
applicazioni.

Aspose.Cells for Java supporta l'elaborazione di Cells (DOC, DOCX, OOXML, RTF) HTML, OpenDocument, PDF, EPUB, XPS, SWF e tutti i formati di immagine. Con Aspose.Cells è possibile
generare, modificare e convertire documenti senza utilizzare Microsoft Cells.

### **Aspose.Cells Java for Jython**

Aspose.Cells Java per Jython è un progetto che dimostra / fornisce esempi di utilizzo dell'API Aspose.Cells for Java in Jython.

## **Requisiti di sistema e piattaforme supportate**

### **Requisiti di sistema**

**Di seguito sono riportati i requisiti di sistema per utilizzare Aspose.Cells Java per Jython:**

- Java 1.5 o versione successiva installata
- Componente Aspose.Cells scaricato
- Jython 2.7.0

### **Piattaforme Supportate**

**Di seguito sono indicate le piattaforme supportate:**

- Aspose.Cells 15.4 e successivi.
- IDE Java (Eclipse, NetBeans ...)

## **Download Installazione e Utilizzo**

### **Download**

**Scarica Esempi da siti di codice sociale**

Le release degli esempi in esecuzione sono disponibili per il download su tutti i siti di codice sociale menzionati di seguito:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)

**Scarica componente Aspose.Cells for Java**

- [Aspose.Cells for Java](https://releases.aspose.com/cells/java/)

### **Installazione**

- Posiziona il file jar Aspose.Cells for Java scaricato nella directory "lib".
- Sostituisci "your-lib" con il nome del file jar scaricato nel file _*init*_.py.

### **Utilizzo**

È possibile creare il documento HelloWorld utilizzando il seguente esempio di codice:

{{< highlight java >}}

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

## **Supporto, Estendi e Contribuisci**

### **Supporto**

Fin dai primi giorni di Aspose, sapevamo che fornire ai nostri clienti solo buoni prodotti non sarebbe stato sufficiente. Dovevamo anche offrire un buon servizio. Siamo anche sviluppatori e comprendiamo quanto sia frustrante quando un problema tecnico o una stranezza nel software ti impedisce di fare ciò che devi fare. Siamo qui per risolvere i problemi, non per crearli.

Ecco perché offriamo un supporto gratuito. Chiunque utilizzi il nostro prodotto, che li abbia acquistati o li stia usando in valutazione, merita la nostra piena attenzione e rispetto.

È possibile registrare eventuali problemi o suggerimenti relativi ad Aspose.Cells Java per Jython utilizzando una delle seguenti piattaforme:

- [Github](https://github.com/aspose-words/Aspose.Words-for-Java/issues)

### **Estensione e Contribuzione**

Aspose.Cells Java per Jython è open source e il suo codice sorgente è disponibile sui principali siti di codifica sociale elencati di seguito. Gli sviluppatori sono incoraggiati a scaricare il codice sorgente e contribuire suggerendo o aggiungendo nuove funzionalità o migliorando quelle esistenti, in modo che anche altri possano beneficiarne.

### **Codice Sorgente**

Puoi ottenere l'ultimo codice sorgente da uno dei seguenti siti

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)
