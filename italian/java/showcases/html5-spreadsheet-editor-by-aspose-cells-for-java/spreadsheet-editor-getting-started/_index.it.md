---
title: Introduzione all'editor di fogli di calcolo
type: docs
weight: 10
url: /it/java/spreadsheet-editor-getting-started/
---
**Sommario**

- [introduzione](#SpreadsheetEditorGettingStarted-Introduction)
- [Requisiti di sistema](#SpreadsheetEditorGettingStarted-SystemRequirements)
- [Download e installazione](#SpreadsheetEditorGettingStarted-DownloadandInstallation)
- [Supporto](#SpreadsheetEditorGettingStarted-Support)
- [Contribuire](#SpreadsheetEditorGettingStarted-Contribute)
- [Licenza](#SpreadsheetEditorGettingStarted-License)
### **introduzione**
Html5 Spreadsheet Editor è un'applicazione Web in grado di visualizzare e modificare documenti di fogli di calcolo in un browser Web. Supporta Excel, SpreadsheetML, CVS, OpenDocument e molti altri formati supportati da Microsoft Excel. Sono supportate tutte le funzionalità di base tra cui la modifica delle celle, la formattazione, la modifica delle formule, la gestione di righe e colonne, ecc.

![cose da fare:immagine_alt_testo](aowcrc1.png)

 HTML5 Spreadsheet Editor utilizza molte funzionalità di[Aspose.Cells for Java](https://products.aspose.com/cells/java/) mostra come usarli per creare, manipolare e rendere un foglio di calcolo nella tua applicazione Java.

**Caratteristiche**

-  Lavorare con i file
 - Formati supportati
 - Apri file locali
 - Apri da Dropbox
 - Apri dall'URL
 - Crea un nuovo foglio di calcolo
 - Esporta in vari formati
-  Lavorare con Fogli
 - Aggiungi e rimuovi fogli
 - Rinominare i fogli
 - Passa da un foglio all'altro
-  Lavorare con righe e colonne
 - Aggiungi una riga
 - Aggiungi una colonna
 - Rimuovi una riga
 - Rimuovi una colonna
 - Larghezza colonna e altezza riga
-  Funzionante con Cells
 - Selezione di una cella
 - Modifica di una cella
 - Formula di modifica
 - Allineamento Cell
 - Chiaro Cell
 - Aggiungi una cella
 - Rimuovere una cella
-  Lavorare con la formattazione del testo
 - Grassetto, corsivo, sottolineato
 - Stile e dimensione del carattere
 - Chiara formattazione
### **Requisiti di sistema**
**Requisiti software**

- CDI ha supportato il server delle applicazioni Java
- [Aspose.Cells for Java](https://products.aspose.com/cells/java/)
- [JavaServer Faces 2.0](https://javaee.github.io/javaserverfaces-spec/)
- [Prime facce 5.1](https://www.primefaces.org/)

**Requisiti hardware**

I requisiti hardware variano in base all'application server Java che scegliamo di distribuire HTML5 Spreadsheet Editor e al numero di fogli di calcolo che apriamo contemporaneamente. Di seguito è riportato un preventivo, che aiuterà inizialmente a configurare l'ambiente.

- Processore da 2 GHz
- RAM da 2GB
- Disco da 500MB
### **Download e installazione**
 L'editor di fogli di calcolo HTML5 è un'applicazione EE Java e può essere distribuito a qualsiasi profilo Web del server delle applicazioni Java con supporto CDI. È stato testato con[Pesce vetro](https://javaee.github.io/glassfish/).

**Codice sorgente**

 La fonte del progetto è disponibile su[Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/). Stiamo anche mantenendo i mirror Git nei seguenti siti:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [Google Cod](https://code.google.com/archive/p/html5-spreadsheet-editor/)
- [FonteForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

Utilizzare uno dei seguenti comandi per scaricare il codice sorgente tramite la riga di comando:

**Github**

{{< highlight "bash" >}}

 git clone https://github.com/aspose-cells/Aspose.Cells-for-Java.git

{{< /highlight >}}

**Bitbucket**

{{< highlight "bash" >}}

 git clone https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java.git

{{< /highlight >}}

**Google Cod**

{{< highlight "bash" >}}

 git clone https://code.google.com/p/html5-spreadsheet-editor/

{{< /highlight >}}

**FonteForge**

{{< highlight "bash" >}}

 git clone git://git.code.sf.net/p/html5-spreadsheet-editor/code html5-spreadsheet-editor-code

{{< /highlight >}}

**Costruisci utilizzando Maven**

Il processo di compilazione del progetto è gestito utilizzando Maven. Quindi puoi preparare un file WAR dalla riga di comando senza alcun IDE. Utilizzare il seguente comando per generare un WAR per la distribuzione. La documentazione del server delle applicazioni corrispondente ti aiuterà a distribuire il WAR generato e le sue dipendenze.

{{< highlight "java" >}}

 mvn clean install

{{< /highlight >}}

**Utilizzo di NetBeans**

 È molto facile gestire il progetto utilizzando[IDE di NetBeans](https://netbeans.apache.org/). NetBeans è uno degli IDE popolari tra gli sviluppatori Java ed è sponsorizzato da Oracle.

- Scarica il codice sorgente del progetto.
- Apri il progetto in NetBeans IDE.
-  Clic***Correre*** pulsante sulla barra degli strumenti.
-  Selezionare***Pesce vetro*** server come server delle applicazioni.

**Usando Eclipse**

[Eclipse IDE](http://www.eclipse.org/ide/) fornisce l'integrazione ufficiale per importare Maven progetti chiamati[M2Eclipse](http://www.eclipse.org/m2e/):

1. Installa M2Eclipse nel tuo IDE Eclipse. La procedura di installazione è descritta sul loro sito web.
1. Scarica il codice sorgente del progetto.
1. Apri il***Importare*** dialogo dal menu File.
1.  Selezionare***Maven Progetto*** dalla finestra di dialogo di importazione.
1.  Clic***Prossimo***.
1.  Clic***Navigare*** per selezionare la posizione del codice sorgente.
1.  Selezionare***pom.xml*** dall'elenco sottostante.
1.  Clic***Fine***.

L'IDE Eclipse dovrebbe importare e caricare il progetto.
### **Supporto**
**Riportare un errore**

 Per inviare una segnalazione di bug, crea un nuovo problema all'indirizzo[Pagina del progetto Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) e applicare l'etichetta***insetto***.

**Richiesta di funzionalità**

 Apprezziamo molto il tuo feedback e le funzionalità che richiedi. Per richiedere una nuova funzionalità o un miglioramento esistente, creare un nuovo numero all'indirizzo[Pagina del progetto Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) e applicare l'etichetta***aumento***.

**Domande e aiuto**

 Puoi porre qualsiasi tipo di domanda relativa all'editor di fogli di calcolo HTML5 utilizzando[Problema Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) . Basta creare un nuovo problema e applicare il***domanda*** etichetta.

**Aspose.Cells for Java Forum**

 I forum dei prodotti Aspose forniscono supporto completo sia per i clienti di prova che per quelli a pagamento. Gli esperti sono seduti 24 ore su 24, 7 giorni su 7, per fornire assistenza e rispondere alle domande. Visitare[forum sui prodotti qui](https://forum.aspose.com/c/cells/9).

**Aspose Blog**

 Mettiti in contatto con noi e rimani aggiornato sulle ultime novità sui nostri prodotti e offerte. Iscriviti a[il nostro blog qui](http://blog.aspose.com).
### **Contribuire**
[](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)

[!\[tutto:image_alt_text\]](https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png)](https://github.com/AsposeShowcase/Html5_Foglio di calcolo_Editore_di_Aspose.Cells_per_Java)


HTML5 Spreadsheet Editor è un progetto open source che consente a tutti le massime opzioni di contribuire al progetto.

**Codice sorgente**

 La fonte del progetto è disponibile su[Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java). Stiamo anche mantenendo i mirror Git nei seguenti siti:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [FonteForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

**Richieste pull**

 Per contribuire al progetto con il codice sorgente è sufficiente inviare una richiesta pull tramite Github. Leggi ulteriori informazioni nell'articolo di Github su[Crea una richiesta pull](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).
### **Licenza**
**Licenza MIT**

 Stiamo utilizzando una delle licenze open source più liberali per le responsabilità minime sui contributori. HTML5 Spreadsheet Editor è rilasciato sotto[Licenza MIT](https://opensource.org/licenses/mit-license.php).

**Aspose Licenza**

 Il prodotto funziona senza licenza Aspose,[con limitazioni](/cells/it/java/licensing/) . Per rimuovere le limitazioni, puoi acquisire un file[licenza temporanea gratuita](https://purchase.aspose.com/temporary-license) o[acquista la licenza completa](https://purchase.aspose.com/buy).

 Per impostazione predefinita, l'editor tenterà di caricare**Aspose.Total.Java.lic** file da**src/main/resources/com/aspose/spreadsheeteditor** directory. Basta copiare il file di licenza in questa directory. Il comportamento predefinito può essere modificato modificando il file**Aspose Licenza** classe.
