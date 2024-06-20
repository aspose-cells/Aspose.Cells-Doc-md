---
title: Opzioni di Impostazione Pagina e di Stampa
type: docs
weight: 10
url: /it/java/page-setup-and-printing-options/
---

{{% alert color="primary" %}}

A volte, gli sviluppatori devono configurare l'impostazione della pagina e le impostazioni di stampa per controllare il processo di stampa. Le impostazioni di configurazione della pagina e di stampa offrono varie opzioni e sono completamente supportate in Aspose.Cells.

Questo articolo mostra come creare un'applicazione console e applicare l'impostazione della pagina e le opzioni di stampa a un foglio di lavoro con poche righe di codice utilizzando le API di Aspose.Cells.

{{% /alert %}}

## **Lavorare con Impostazioni Pagina e di Stampa**

Per questo esempio, abbiamo creato un libro in Microsoft Excel e utilizzato Aspose.Cells per impostare le opzioni di impostazione pagina e di stampa.

### **Impostazione Opzioni di Impostazione Pagina**

Prima creare un foglio di lavoro semplice in Microsoft Excel. Quindi applicare le opzioni dell'impostazione pagina ad esso. Eseguendo il codice cambia le opzioni dell'impostazione pagina come nello screenshot sottostante.

**File di output** 

![todo:image_alt_text](page-setup-and-printing-options_1.png)

1. Creare un foglio di lavoro con alcuni dati in Microsoft Excel:
   1. Apri un nuovo foglio di lavoro in Microsoft Excel.
   1. Aggiungi alcuni dati.
      Di seguito è riportato uno screenshot del file.

      **File di input**

![todo:image_alt_text](page-setup-and-printing-options_2.png)

1. Imposta opzioni dell'impostazione pagina:
   Applicare le opzioni di impostazione pagina al file. Di seguito è riportata una schermata delle opzioni predefinite, prima che vengano applicate le nuove opzioni.

   **Opzioni predefinite di impostazione pagina**

![todo:image_alt_text](page-setup-and-printing-options_3.png)

1. Scarica e installa Aspose.Cells:
   1. [Download](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
   1. Estrarlo sul tuo computer di sviluppo.
      Tutti i componenti [Aspose](http://www.aspose.com/), una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e inserisce solo filigrane nei documenti prodotti.
1. Creare un progetto.
   Creare un progetto utilizzando un editor Java, ad esempio Eclipse, oppure creare un programma semplice utilizzando un editor di testo.
1. Aggiungere un percorso della classe.
   1. Estrai Aspose.Cells.jar e dom4j_1.6.1.jar da Aspose.Cells.zip.
   1. Imposta il percorso di classe del progetto in Eclipse:
   1. Selezionare il proprio progetto in Eclipse e fare clic su **Progetto** seguito da **Proprietà**.
   1. Selezionare **Percorso Build Java** a sinistra della finestra di dialogo.
   1. Selezionare la scheda Librerie, fare clic su **Aggiungi JAR** o **Aggiungi JAR Esterni** per selezionare Aspose.Cells.jar e dom4j_1.6.1.jar e aggiungerli ai percorsi di build.
      Oppure è possibile impostarlo all'avvio da un prompt dei comandi in Windows:

{{< highlight java >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

1. Scrivere l'applicazione che invoca le API:
   Di seguito è riportato il codice utilizzato dal componente in questo esempio.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPageSetupOptions-SettingPageSetupOptions.java" >}}

### **Impostazione delle opzioni di stampa**

Le impostazioni di impostazione pagina forniscono anche diverse opzioni di stampa (chiamate anche opzioni di foglio) che consentono agli utenti di controllare come vengono stampate le pagine del foglio di lavoro. Consentono agli utenti di:

- Selezionare un'area di stampa specifica di un foglio di lavoro.
- Stampare i titoli.
- Stampare le linee di griglia.
- Stampare gli intitoli di riga/colonna.
- Ottenere una qualità di bozza.
- Stampare commenti.
- Stampare errori di cella.
Definire l'ordinamento delle pagine.

L'esempio che segue applica le opzioni di stampa al file creato nell'esempio precedente (PageSetup.xls). La schermata di seguito mostra le opzioni di stampa predefinite prima che vengano applicate nuove opzioni.
**Documento di input**

![todo:image_alt_text](page-setup-and-printing-options_4.png)

Eseguendo il codice si modificano le opzioni di stampa.
**File di output**

![todo:image_alt_text](page-setup-and-printing-options_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPrintoptions-SettingPrintoptions.java" >}}

## **Sommario**

{{% alert color="primary" %}}

Questo articolo mostra come impostare le opzioni di impostazione pagina e di stampa del foglio utilizzando Aspose.Cells. Si spera che possa fornire delle informazioni utili e che si possano utilizzare queste opzioni nei propri scenari.

Aspose.Cells beneficia di anni di ricerca, design e accordatura attenta. Accogliamo con piacere le vostre richieste, commenti e suggerimenti su [Aspose.Cells Forum](https://forum.aspose.com/c/cells/9). Garantiamo una risposta tempestiva.

{{% /alert %}}
