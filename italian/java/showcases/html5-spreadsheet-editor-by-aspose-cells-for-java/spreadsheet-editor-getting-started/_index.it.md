---
title: Introduzione all Editor di Fogli di Calcolo
type: docs
weight: 10
url: /it/java/spreadsheet-editor-getting-started/
---

**Tabella dei contenuti**

- [Introduzione](#SpreadsheetEditorGettingStarted-Introduction)
- [Requisiti di sistema](#SpreadsheetEditorGettingStarted-SystemRequirements)
- [Download e Installazione](#SpreadsheetEditorGettingStarted-DownloadandInstallation)
- [Supporto](#SpreadsheetEditorGettingStarted-Support)
- [Contribuisci](#SpreadsheetEditorGettingStarted-Contribute)
- [Licenza](#SpreadsheetEditorGettingStarted-License)
### **Introduzione**
Html5 Spreadsheet Editor è un'applicazione web che può visualizzare e modificare documenti di fogli di calcolo in un browser web. Supporta Excel, SpreadsheetML, CVS, OpenDocument e molti altri formati supportati da Microsoft Excel. Sono supportate tutte le funzionalità di base, incluso l'editing delle celle, la formattazione, l'editing delle formule, la gestione delle righe e delle colonne, ecc.

![todo:image_alt_text](aowcrc1.png)

L'editor di fogli di calcolo HTML5 utilizza molte funzionalità di [Aspose.Cells for Java](https://products.aspose.com/cells/java/) e mostra come utilizzarle per creare, manipolare e visualizzare un foglio di calcolo nella tua applicazione Java.

**Caratteristiche**

- Lavorare con i file 
  - Formati supportati
  - Aprire file locali
  - Aprire da Dropbox
  - Aprire da un URL
  - Creare un nuovo foglio di calcolo
  - Esportare in vari formati
- Lavorare con le schede 
  - Aggiungere e rimuovere schede
  - Rinominare le schede
  - Passare tra le schede
- Lavorare con righe e colonne 
  - Aggiungere una riga
  - Aggiungere una colonna
  - Rimuovere una riga
  - Rimuovere una colonna
  - Larghezza della colonna e altezza della riga
- Lavorare con le celle 
  - Selezione di una cella
  - Modifica di una cella
  - Modifica della formula
  - Allineamento della cella
  - Cancella Cellula
  - Aggiungi una cella
  - Rimuovi una cella
- Lavorare con la formattazione del testo 
  - Grassetto, corsivo, sottolineato
  - Stile del carattere e dimensione
  - Cancella la formattazione
### **Requisiti di sistema**
**Requisiti del Software**

- Server applicazioni supportato da CDI
- [Aspose.Cells for Java](https://products.aspose.com/cells/java/)
- [JavaServer Faces 2.0](https://javaee.github.io/javaserverfaces-spec/)
- [Primefaces 5.1](https://www.primefaces.org/)

**Requisiti Hardware**

I requisiti hardware variano in base al server dell'applicazione Java scelto per distribuire HTML5 Spreadsheet Editor e al numero di fogli elettronici aperti simultaneamente. Di seguito è riportata una stima che aiuterà a configurare l'ambiente inizialmente.

- 2 GHz CPU
- 2 GB RAM
- 500 MB di Disco
### **Download e Installazione**
L'editor di fogli elettronici HTML5 è un'applicazione Java EE e può essere distribuita su qualsiasi server di applicazioni Java con supporto CDI. È stato testato con [Glassfish](https://javaee.github.io/glassfish/).

**Codice Sorgente**

Il codice sorgente del progetto è disponibile su [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/). Stiamo anche mantenendo mirror Git nei seguenti siti:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [Google Code](https://code.google.com/archive/p/html5-spreadsheet-editor/)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

Usa uno dei seguenti comandi per scaricare il codice sorgente tramite riga di comando:

**Github**

{{< highlight bash >}}

 git clone https://github.com/aspose-cells/Aspose.Cells-for-Java.git

{{< /highlight >}}

**Bitbucket**

{{< highlight bash >}}

 git clone https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java.git

{{< /highlight >}}

**Google Code**

{{< highlight bash >}}

 git clone https://code.google.com/p/html5-spreadsheet-editor/

{{< /highlight >}}

**SourceForge**

{{< highlight bash >}}

 git clone git://git.code.sf.net/p/html5-spreadsheet-editor/code html5-spreadsheet-editor-code

{{< /highlight >}}

**Build con Maven**

Il processo di build del progetto è gestito utilizzando Maven. Quindi puoi preparare un file WAR da riga di comando senza alcuna IDE. Usa il seguente comando per generare un WAR per la distribuzione. La documentazione del server di applicazione corrispondente ti aiuterà a come distribuire il WAR generato e le sue dipendenze.

{{< highlight java >}}

 mvn clean install

{{< /highlight >}}

**Utilizzando NetBeans**

È molto facile gestire il progetto utilizzando [NetBeans IDE](https://netbeans.apache.org/). NetBeans è uno degli IDE più popolari tra i programmatori Java e è sponsorizzato da Oracle.

- Scarica il codice sorgente del progetto.
- Apri il progetto in NetBeans IDE.
- Clicca sul pulsante ***Esegui*** sulla barra degli strumenti.
- Seleziona il server ***Glassfish*** come Server di Applicazioni.

**Utilizzando Eclipse**

[Eclipse IDE](http://www.eclipse.org/ide/) fornisce un'integrazione ufficiale per importare progetti Maven chiamata [M2Eclipse](http://www.eclipse.org/m2e/):

1. Installa M2Eclipse nel tuo Eclipse IDE. La procedura di installazione è descritta sul loro sito web.
1. Scarica il codice sorgente del progetto.
1. Apri il dialogo ***Importa*** dal menu File.
1. Seleziona ***Progetto Maven*** dal dialogo di importazione.
1. Fai clic su ***Avanti***.
1. Fai clic su ***Sfoglia*** per selezionare la posizione del codice sorgente.
1. Seleziona ***pom.xml*** dalla lista sottostante.
1. Fai clic su ***Fine***.

L'Eclipse IDE dovrebbe importare e caricare il progetto.
### **Supporto**
**Segnalazione di bug**

Per inviare una segnalazione di bug, crea un nuovo problema sulla [pagina del progetto GitHub](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) e applica l'etichetta ***bug***.

**Richiesta di funzionalità**

Apprezziamo molto il tuo feedback e le funzionalità che richiedi. Per richiedere una nuova funzionalità o un miglioramento esistente, crea un nuovo problema sulla [pagina del progetto GitHub](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) e applica l'etichetta ***enhancement***.

**Domande e Aiuto**

Puoi fare qualsiasi tipo di domanda relativa all'HTML5 Spreadsheet Editor utilizzando il [problema di Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues). Crea semplicemente un nuovo problema e applica l'etichetta ***question***.

**Forum Aspose.Cells for Java**

I forum dei prodotti Aspose offrono pieno supporto sia per i clienti in prova che per quelli pagati. Gli esperti sono a disposizione 24/7 per fornire assistenza e rispondere alle domande. Visita i [forum del prodotto qui](https://forum.aspose.com/c/cells/9).

**Blog Aspose**

Entrate in contatto con noi e rimanete aggiornati sulle ultime notizie sui nostri prodotti e offerte. Iscriviti al [nostro blog qui](http://blog.aspose.com).
### **Contribuisci**
[](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)

[!\[todo:image_alt_text\](https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png)](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)


HTML5 Spreadsheet Editor è un progetto open source che offre massime opzioni a tutti per contribuire al progetto.

**Codice Sorgente**

Il codice sorgente del progetto è disponibile su [Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java). Manteniamo anche specchi Git ai seguenti siti:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

**Richieste di estrazione**

Per contribuire al codice sorgente del progetto, invia una pull request tramite Github. Leggi ulteriori informazioni nell'articolo di Github su [Creare una pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).
### **Licenza**
**Licenza MIT**

Utilizziamo una delle licenze open source più liberali per ridurre al minimo le responsabilità sui contributori. HTML5 Spreadsheet Editor è rilasciato sotto [Licenza MIT](https://opensource.org/licenses/mit-license.php).

**Licenza Aspose**

Il prodotto funziona senza licenza Aspose, [con limitazioni](/cells/it/java/licensing/). Per rimuovere le limitazioni, puoi acquisire una [licenza temporanea gratuita](https://purchase.aspose.com/temporary-license) o [acquistare una licenza completa](https://purchase.aspose.com/buy).

Per impostazione predefinita, l'editor cercherà di caricare il file **Aspose.Total.Java.lic** dalla directory **src/main/resources/com/aspose/spreadsheeteditor**. Basta copiare il file della licenza in questa directory. Il comportamento predefinito può essere modificato modificando la classe **AsposeLicense**.
