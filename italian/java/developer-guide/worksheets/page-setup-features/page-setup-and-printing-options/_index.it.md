---
title: Impostazioni di pagina e opzioni di stampa
type: docs
weight: 10
url: /it/java/page-setup-and-printing-options/
---
{{% alert color="primary" %}}

A volte, gli sviluppatori devono configurare l'impostazione della pagina e le impostazioni di stampa per controllare il processo di stampa. L'impostazione della pagina e le impostazioni di stampa offrono varie opzioni e sono completamente supportate in Aspose.Cells.

Questo articolo mostra come creare un'applicazione console e applicare le opzioni di impostazione della pagina e di stampa a un foglio di lavoro con poche semplici righe di codice utilizzando Aspose.Cells API.

{{% /alert %}}

## **Utilizzo delle impostazioni di pagina e stampa**

Per questo esempio, abbiamo creato una cartella di lavoro in Microsoft Excel e usiamo Aspose.Cells per impostare l'impostazione della pagina e le opzioni di stampa.

### **Impostazione delle opzioni di impostazione della pagina**

Per prima cosa crea un semplice foglio di lavoro in Microsoft Excel. Quindi applica le opzioni di impostazione della pagina. L'esecuzione del codice modifica le opzioni di Imposta pagina come nello screenshot qui sotto.

**File di uscita** 

![cose da fare:immagine_alt_testo](page-setup-and-printing-options_1.png)

1. Crea un foglio di lavoro con alcuni dati in Microsoft Excel:
 1. Apri una nuova cartella di lavoro in Microsoft Excel.
 1. Aggiungi alcuni dati.
 Di seguito è riportato uno screenshot del file.

      **File di input**

![cose da fare:immagine_alt_testo](page-setup-and-printing-options_2.png)

1. Imposta le opzioni di impostazione della pagina:
 Applicare le opzioni di impostazione della pagina al file. Di seguito è riportato uno screenshot delle opzioni predefinite, prima che vengano applicate le nuove opzioni.

   **Opzioni di impostazione della pagina predefinita**

![cose da fare:immagine_alt_testo](page-setup-and-printing-options_3.png)

1. Scarica e installa Aspose.Cells:
   1. [Scarica](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
 1. Decomprimilo sul tuo computer di sviluppo.
 Tutto[Aspose](http://www.aspose.com/) i componenti, una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e si limita a inserire filigrane nei documenti prodotti.
1. Crea un progetto.
 Crea un progetto utilizzando un editor Java, ad esempio Eclipse, oppure crea un semplice programma utilizzando un editor di testo.
1. Aggiungi un percorso di classe.
1. Estrarre Aspose.Cells.jar e dom4j_1.6.1.jar da Aspose.Cells.zip.
 1. Imposta il classpath del progetto in Eclipse:
 1. Seleziona il tuo progetto in Eclipse e poi clicca**Progetto** seguito da**Proprietà**.
 1. Selezionare**Java Costruisci Percorso** sinistra della finestra di dialogo.
 1. Selezionare la scheda Librerie, fare clic su**Aggiungi JAR** o**Aggiungi JAR esterni** per selezionare Aspose.Cells.jar e dom4j_1.6.1.jar e aggiungerli ai percorsi di build.
 Oppure puoi impostarlo in fase di esecuzione al prompt di DOS in Windows:

{{< highlight "java" >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

1. Scrivi l'applicazione che richiama le API:
 Di seguito è riportato il codice utilizzato dal componente in questo esempio.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPageSetupOptions-SettingPageSetupOptions.java" >}}

### **Impostazione delle opzioni di stampa**

Le impostazioni di impostazione della pagina forniscono anche diverse opzioni di stampa (chiamate anche opzioni del foglio) che consentono agli utenti di controllare come vengono stampate le pagine del foglio di lavoro. Consentono agli utenti di:

- Selezionare un'area di stampa specifica di un foglio di lavoro.
- Stampa titoli.
- Stampa griglia.
- Stampa le intestazioni di riga/colonna.
- Ottieni una bozza di qualità.
- Stampa commenti.
- Stampa gli errori della cella.
- Definire l'ordine delle pagine.

L'esempio che segue applica le opzioni di stampa al file creato nell'esempio precedente (PageSetup.xls). Lo screenshot seguente mostra le opzioni di stampa predefinite prima che vengano applicate le nuove opzioni.
**Documento di input**

![cose da fare:immagine_alt_testo](page-setup-and-printing-options_4.png)

L'esecuzione del codice modifica le opzioni di stampa.
**File di uscita**

![cose da fare:immagine_alt_testo](page-setup-and-printing-options_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPrintoptions-SettingPrintoptions.java" >}}

## **Riepilogo**

{{% alert color="primary" %}}

Questo articolo mostra come impostare l'impostazione della pagina e le opzioni di stampa del foglio utilizzando Aspose.Cells. Si spera che ti fornisca alcune informazioni e che tu possa utilizzare queste opzioni nei tuoi scenari.

 Aspose.Cells beneficia di anni di ricerca, progettazione e attenta messa a punto. Accogliamo con favore le vostre domande, commenti e suggerimenti a[Aspose.Cells Foro](https://forum.aspose.com/c/cells/9). Garantiamo una pronta risposta.

{{% /alert %}}
