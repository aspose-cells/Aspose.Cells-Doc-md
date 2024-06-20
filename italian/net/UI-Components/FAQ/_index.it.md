---
title: Domande frequenti
type: docs
weight: 400
url: /it/net/grid-faq/
---

## **Ci sono limitazioni nella versione di valutazione dei controlli Grid di Aspose.Cells?**
No, non ci sono limitazioni delle funzionalità nella versione di valutazione di quei controlli.

La versione di valutazione fornisce tutte le funzionalità della versione con licenza tranne che aggiunge un foglio di lavoro extra (contenente **Avviso di Copyright di Valutazione**) ai file di output.


## **Ci sono così tanti controlli di griglia disponibili sul mercato. Perché dovrei comprare i Controlli di Griglia Aspose.Cells?**
Beh, i Controlli di Griglia Aspose.Cells hanno un prezzo molto conveniente per essere accessibili a tutti i tipi di utenti. In un prezzo molto ragionevole,

ti fornisce una suite di due controlli per lavorare su Applicazioni Windows & Web. 

Inoltre, non è solo una semplice griglia, è il **Visualizzatore, Editore & Creatore di Fogli Elettronici** nello stesso momento. 

Non solo puoi associarlo a qualsiasi tipo di Sorgente Dati (come i normali controlli di griglia) ma anche creare e gestire file Excel. Fornisce anche un **Motore di Calcolo delle Formule** forte e ricco per calcolare non solo le funzioni integrate (supportate dai Controlli di Griglia Aspose.Cells) ma anche formule personalizzate definite da te. Ci sono molte più funzionalità della suite di griglie Aspose.Cells che non possono essere trattate qui, consulta la pagina dei Tipi di Edizione per un elenco più dettagliato delle funzionalità.

## **Di recente ho acquistato la mia licenza per i Controlli di Griglia Aspose.Cells. Come posso utilizzare quella licenza nella mia applicazione con il Controllo di Griglia Aspose.Cells?**
Consulta la pagina [Licensing](/cells/it/net/licensing/) dei Controlli di Griglia Aspose.Cells. 

Fornisce dettagli completi su come utilizzare la licenza con i Controlli di Griglia Aspose.Cells nelle tue applicazioni.



## **Come posso distribuire il mio progetto/soluzione web basato su Aspose.Cells.GridWeb sul Server?**
Se hai bisogno di distribuire l'applicazione web con il controllo GridWeb, dovresti copiare la directory "acw_client" nella cartella del tuo progetto almeno la tua applicazione web (distribuita sul server) non potrebbe trovarla.

Puoi sempre specificare il percorso dello script aggiungendo le seguenti righe di codice nella sezione di configurazione (ad es. nel file web.config del tuo progetto VS.NET). Il "acw_client" è una cartella che contiene file e Aspose.Cells.GridWeb utilizza questa cartella per gestire la sua configurazione interna, contiene file di script, file di immagine e altri file per specificare il comportamento di GridWeb e impostare altre operazioni. Il file di configurazione è utilizzato per impedire al controllo di utilizzare le risorse client incorporate (immagini, script, ecc.) che è utile in alcuni casi/scenari.

**XML**

{{< highlight csharp >}}

 <appSettings>

  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/>

  <add key="aspose.cells.gridweb.force_script_path" value="true"/>

  <add key="aspose.cells.gridweb.forcepath" value="true"/>

 </appSettings>

{{< /highlight >}}

{{% alert color="primary" %}} 

Il percorso è sempre relativo alla directory del progetto. Non dovresti utilizzare alcuna directory che si trovi al di fuori della directory del progetto. Quindi è necessario copiare la directory "acw_client" (@ la tua cartella di installazione GridWeb) nella directory del progetto.

{{% /alert %}} 
## **Esecuzione di Aspose.Cell.GridWeb in Internet Explorer **
Attualmente Aspose.Cells.GridWeb non supporta più Internet Explorer, è un browser troppo vecchio. 
Supportiamo Chrome, Edge, Firefox, Safari, Opera



