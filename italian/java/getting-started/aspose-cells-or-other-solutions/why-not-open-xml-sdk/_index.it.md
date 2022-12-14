---
title: Perché non aprire XML SDK
type: docs
weight: 20
url: /it/java/why-not-open-xml-sdk/
---
{{% alert color="primary" %}} 

A volte sentiamo questa domanda:

**Perché dovremmo utilizzare i prodotti Aspose anziché l'SDK Open XML gratuito?**

 È facile rispondere a questa domanda:**caratteristiche e funzionalità**.

{{% /alert %}} 
## ** Cos'è Open XML SDK?**
Secondo MSDN Library, Open XML SDK è definito come: Open XML SDK 2.0 semplifica l'attività di manipolazione dei pacchetti Open XML e degli elementi dello schema Open XML sottostanti all'interno di un pacchetto. Open XML SDK 2.0 incapsula molte attività comuni che gli sviluppatori eseguono su pacchetti Open XML, in modo da poter eseguire operazioni complesse con poche righe di codice. I documenti OOXML sono essenzialmente file XML compressi e Open XML SDK è una raccolta di classi che consente di lavorare con il contenuto dei documenti OOXML in modo fortemente tipizzato. Cioè invece di decomprimere un file per estrarre XML, caricare quell'XML in un albero DOM e lavorare direttamente con elementi e attributi XML, Open XML SDK fornisce classi per farlo.
## ** Cos'è Aspose.Cells?**
Aspose.Cells è una libreria di classi che consente all'applicazione di eseguire le seguenti attività di elaborazione dei fogli di calcolo: Conversioni di alta qualità tra tutti i formati Excel più diffusi, inclusa la conversione in PDF, HTML, TIFF e la stampa. Programmazione con un modello a oggetti della cartella di lavoro. Capacità di costruire documenti da frammenti, da uno o più documenti, unendo automaticamente i dati mediante formattazione stilistica, grafici e grafici. Funzioni di alto livello, come l'importazione di dati da diverse origini dati tra cui Array, ArrayList, DataTable / ResultSet. Robusto motore di calcolo delle formule che supporta quasi tutte le funzioni Excel Microsoft standard e avanzate.

{{% alert color="primary" %}}
## ** Confronta Open XML SDK e Aspose.Cells**
 La tabella seguente confronta le funzionalità di Open XML SDK e Aspose.Cells.{{% /alert %}}

|**Funzionalità o categoria di funzionalità**|**Apri l'SDK XML**|**Aspose.Cells**|
|:- |:- |:- |
|Excel o altri formati supportati|XLSX|XLS, CSV, SpreadsheetML 2003, XLSX, HTML, delimitato da tabulazioni, ODS, testo normale (TXT), PDF, XPS|
|Conversione tra formati Excel|No|sì|
|<p>Programmazione di alto livello con un modello a oggetti della cartella di lavoro:</p><p>- Trova e sostituisci.</p><p>- Assemblare fogli di calcolo.</p><p>- Copia frammenti e fogli di lavoro tra cartelle di lavoro.</p>|No|sì|
|Programmazione dettagliata con un modello di oggetto del documento, accesso ai singoli elementi e proprietà di formattazione di tutti gli elementi del foglio di calcolo.|sì|sì|
|Accesso diretto e completo di basso livello agli elementi e attributi XML sottostanti come identificatori di relazione, identificatori di elenco di un documento OOXML.|sì|No|
|<p>Genera report, popola documenti con dati:</p><p>- Importa/Esporta dati da/a a*Tabella dati /*Set di risultati.</p><p>- Funzione marcatori intelligenti.</p><p>- Inserisci/Elimina righe/colonne/intervalli.</p><p>- Fonti di dati personalizzate.</p>|No|sì|
|<p>Rendering e stampa:* Renderizza le pagine del foglio di lavoro in immagini raster (TIFF, TIFF multipagina, PNG, JPEG, BMP).*Renderizza le pagine del foglio di calcolo in immagini vettoriali (EMF).* Converti i grafici in immagini (TIFF, TIFF multipagina, PNG, JPEG, BMP, EMF ecc.)</p><p>- Specifica la risoluzione dell'immagine, la qualità, la compressione e altre opzioni. </p><p>- Stampa fogli di calcolo utilizzando l'infrastruttura di stampa .NET. Il componente ha un metodo di stampa integrato per stampare i fogli di lavoro come mostrato nell'anteprima di stampa di MS Excel.</p>|No|sì|
|Calcola/Ricalcola le formule in modo dinamico| No| sì|
|Piattaforme supportate|Windows, .NET|Windows, Linux, Java, .NET, Mono|
## **Conclusione**
  {{% alert color="primary" %}}Open XML SDK e Aspose.Cells non competono testa a testa perché si rivolgono a esigenze e pubblici molto diversi. Open XML SDK è una libreria di classi che fornisce un modo fortemente tipizzato per lavorare con i documenti OOXML. Aspose.Cells è una libreria di elaborazione di fogli di calcolo molto utile che fornisce un ottimo supporto per tutti i Microsoft Excel e altri formati di file. Se tutto ciò che devi fare è un'operazione di programmazione abbastanza semplice su un documento XLSX, allora Open XML SDK potrebbe essere una scelta adatta. Con Open XML SDK ti sentirai abbastanza a tuo agio nel fare compiti semplici come generare un semplice documento XLSX o rimuovere commenti, intestazioni/piè di pagina, estrarre immagini o altro. Alcune attività possono essere eseguite con Open XML SDK, ma non con Aspose.Cells. Ad esempio, se è necessario accedere direttamente agli elementi e agli attributi XML di un documento OOXML, è necessario utilizzare Open XML SDK. Tuttavia, se è necessario eseguire operazioni complesse sui documenti, ad esempio alcune delle seguenti attività, quindi utilizzare Aspose.Cells è l'opzione migliore: Supporta altri formati di file oltre a XLSX. Copia frammenti e fogli di lavoro tra cartelle di lavoro o unisci cartelle di lavoro in un modo che combini oggetti, stili e altra formattazione in modo appropriato. Sostituisci testo formattato o non formattato. Funzioni di alto livello, come l'importazione di dati da diverse origini dati tra cui Array, ArrayList, DataTable / ResultSet. Generare un documento commerciale, ad esempio un ordine con i dettagli dell'ordine da un'origine dati. Converti un documento in PDF o XPS in modo che appaia esattamente come Microsoft Excel lo avrebbe convertito. Sviluppare un'applicazione .NET o Java.{{% /alert %}}
