---
title: FAQ
type: docs
weight: 400
url: /it/net/grid-faq/
---
## **C'è qualche limitazione nella versione di valutazione di Aspose.Cells Grid Controls?**
 No, non ci sono limiti di funzionalità nella versione di valutazione di Aspose.Cells Grid Controls. La versione di valutazione fornisce tutte le funzionalità della versione con licenza, tranne per il fatto che aggiunge un foglio di lavoro aggiuntivo (contenente**Valutazione Avviso sul copyright** ) ai file di output.
## **Ci sono così tanti controlli Grid disponibili sul mercato. Perché dovrei acquistare Aspose.Cells Grid Controls?**
 Bene, Aspose.Cells Grid Control ha un prezzo molto conveniente per essere accessibile a tutti i tipi di utenti. A un prezzo molto ragionevole, ti offre una suite di due controlli per lavorare su Windows e applicazioni Web. Inoltre, non è solo una semplice Griglia, è la tua**Visualizzatore, editor e creatore di fogli di calcolo** allo stesso tempo. Non solo puoi associarlo a qualsiasi tipo di origine dati (come i normali controlli Grid), ma anche creare e gestire file Excel. Fornisce anche un forte e ricco**Motore di calcolo delle formule** per calcolare non solo funzioni integrate (supportate da Aspose.Cells Grid Controls) ma anche formule personalizzate definite dall'utente. Ci sono molte più funzionalità della suite Grid Aspose.Cells che non possono essere trattate qui, fare riferimento alla pagina dei tipi di edizione per un elenco più dettagliato delle funzionalità.
## **Recentemente ho acquistato la mia licenza per Aspose.Cells Grid Controls. Come posso utilizzare quella licenza nella mia applicazione con Aspose.Cells Grid Control?**
Si prega di fare riferimento al[Licenza](/cells/it/net/licensing/) pagina di Aspose.Cells Grid Controls. Fornisce dettagli completi su come utilizzare la licenza con Aspose.Cells Grid Controls nelle tue applicazioni.
## **I controlli griglia Aspose.Cells sono supportati in Visual Studio.NET 2005?**
Sì, i controlli griglia Aspose.Cells sono completamente supportati in Visual Studio.NET 2005 e versioni successive.
## **Sto usando il controllo Aspose.Cells.GridWeb nel mio sito web usando Visual Studio.NET 2005. Ma non funziona affatto. Qual è il problema?**
 Aspose.Cells.GridWeb supporta entrambi**Sistema di file** e**http** modalità di Visual Studio.NET 2005. Se sei ancora confuso, dai un'occhiata a una guida passo passo per Lavorare con Aspose.Cells.GridWeb usando Visual Studio.NET 2005.
## **Come posso distribuire il mio progetto/soluzione web basato su Aspose.Cells.GridWeb sul server?**
Se è necessario distribuire l'applicazione Web con il controllo GridWeb, copiare il file "acw_client" nella cartella del progetto almeno la tua applicazione web (distribuita sul server) non è riuscita a trovarlo. Puoi sempre specificare il percorso di scripting aggiungendo le seguenti righe di codice nella sezione di configurazione (ad esempio nel file web.config nel tuo Progetto VS.NET).Il progetto "acw_client" è una cartella che contiene file e Aspose.Cells.GridWeb usa questa cartella per gestire la sua configurazione interna, ha file di script, file immagine e altri file per specificare il comportamento di GridWeb e impostare altre operazioni. Il file config è usato per impedire al controllo di utilizzando le risorse client incorporate (immagini, script, ecc.) che sono utili in alcuni casi/scenari.

**XML**

{{< highlight "csharp" >}}

 <appSettings>

  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/>

  <add key="aspose.cells.gridweb.force_script_path" value="true"/>

  <add key="aspose.cells.gridweb.forcepath" value="true"/>

 </appSettings>

{{< /highlight >}}

{{% alert color="primary" %}} 

Il percorso è sempre correlato alla directory del progetto. Non dovresti usare alcuna directory che sia al di fuori della directory del progetto. Quindi è necessario copiare la directory "acw_client" (@ la cartella di installazione di GridWeb) nella directory del progetto.

{{% /alert %}} 
## **Esecuzione di Aspose.Cell.GridWeb in Internet Explorer 10 o 11**
 Attualmente Aspose.Cells.GridWeb non funziona molto bene su Internet Explorer 10 o 11, quindi è necessario utilizzare la modalità di compatibilità di IE8/9 per lavorare con il tipo di browser IE10/11. Dovresti aggiungere la seguente riga di**<meta>** tag nella sezione dell'intestazione in**.aspx** pagina:



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-FAQ-RunGridWebInIE-RunGridWebIE.aspx" >}}

