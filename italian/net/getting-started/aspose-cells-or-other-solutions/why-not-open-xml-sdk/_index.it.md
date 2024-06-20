---
title: Perché non usare Open XML SDK
type: docs
weight: 90
url: /it/net/why-not-open-xml-sdk/
---

{{% alert color="primary" %}}

A volte ci capita di sentire questa domanda:

**Perché dovremmo usare i prodotti Aspose anziché il gratuito Open XML SDK?**

Questa domanda è facile da rispondere: funzionalità e capacità.

{{% /alert %}}

## **Cos'è Open XML SDK?**

Secondo la [MSDN Library](https://docs.microsoft.com/en-us/office/open-xml/open-xml-sdk?redirectedfrom=MSDN), l'Open XML SDK è definito come:

"L'Open XML SDK 2.5 semplifica il compito di manipolare pacchetti Open XML e gli elementi di schema Open XML sottostanti all'interno del pacchetto. L'Open XML SDK 2.5 incapsula molte attività comuni che i programmatori eseguono su pacchetti Open XML, in modo che tu possa eseguire operazioni complesse con poche linee di codice."

I documenti OOXML sono essenzialmente file XML compressi e l'Open XML SDK è una raccolta di classi che ti consente di lavorare con il contenuto dei documenti OOXML in modo fortemente tipizzato. Invece di decomprimere un file per estrarre XML, caricare quel XML in un albero DOM e lavorare direttamente con elementi e attributi XML, l'Open XML SDK fornisce classi per farlo.

## **Cos'è Aspose.Cells?**

Aspose.Cells è una libreria di classi che consente alle applicazioni di eseguire le seguenti attività di elaborazione dei fogli di calcolo:

- Conversioni di alta qualità tra tutti i popolari formati di Microsoft Excel, inclusa la conversione in PDF, HTML, TIFF e la stampa.
- Programmazione con un modello di oggetto di foglio di lavoro.
- Capacità di creare documenti da frammenti, da uno o più documenti, mentre si fondono automaticamente i dati tramite formattazione stilistica, grafici e grafici.
- Funzioni di alto livello, come importare dati da diverse fonti di dati, inclusi Array, ArrayList, DataTable / ResultSet.
- Robusto motore di calcolo delle formule che supporta quasi tutte le funzioni standard e avanzate di Microsoft Excel.

## **Confronta Open XML SDK e Aspose.Cells**

La seguente tabella confronta le funzionalità di Open XML SDK e Aspose.Cells.

|**Funzionalità o Categoria di funzionalità**|**Open XML SDK**|**Aspose.Cells**|
| :- | :- | :- |
|Formati Excel o altri supportati|XLSX|XLS, CSV, SpreadsheetML 2003, XLSX, HTML, Tabella delimitata, ODS, Testo semplice (TXT), PDF, XPS|
|Convertire tra formati Excel|No|Sì|
|<p>Programmazione di alto livello con un modello di oggetto di cartelle di lavoro:</p><p>- Trova e sostituisci.</p><p>- Assembla fogli di calcolo.</p><p>- Copia frammenti e fogli di lavoro tra cartelle di lavoro.</p>|No|Sì|
|Programmazione dettagliata con un modello di oggetto documento, accesso agli elementi individuali e alle proprietà di formattazione di tutti gli elementi del foglio di calcolo.|Sì|Sì|
|Accesso diretto e completo a basso livello agli elementi XML sottostanti e ai relativi attributi come identificatori di relazione, identificatori di elenchi di un documento OOXML.|Sì|No|
|<p>Generare report, popolare documenti con dati:</p><p>- Importazione/Esportazione di dati da/a un DataTable / ResultSet.</p><p>- Funzionalità Smart Markers.</p><p>- Inserimento/Eliminazione righe/colonne/intervallo.</p><p>- Fonti di dati personalizzate.</p>|No|Sì|
|<p>Rendering e Stampa:* Renderizzare pagine di fogli di calcolo in immagini raster (TIFF, TIFF multipagina, PNG, JPEG, BMP).* Renderizzare pagine di fogli di calcolo in immagini vettoriali (EMF).</p><p>- Convertire grafici in immagini (TIFF, TIFF multipagina, PNG, JPEG, BMP, EMF, ecc.)</p><p>- Specificare risoluzione dell'immagine, qualità, compressione e altre opzioni.</p><p>- Stampare fogli di calcolo utilizzando l'infrastruttura di stampa .NET. Il componente ha un metodo di stampa incorporato per stampare i fogli di lavoro come mostrato anteprima di stampa di Microsoft Excel.</p>|No|Sì|
|Calcolare/Ricalcolare dinamicamente le formule|No|Sì|
|Piattaforme supportate|Windows, .NET|Windows, Linux, Java, .NET, Mono|

È possibile confrontare OpenXML con Aspose.Cells Per farlo, suggeriamo di familiarizzare con il progetto Aspose.Cells for OpenXML, che mostra come eseguire diverse attività utilizzando l'API Aspose.Cells for .NET rispetto a OpenXML. Il progetto copre anche le funzionalità per lavorare con documenti di testo che sono disponibili solo in Aspose.Cells, ma non in OpenXML.

Questo progetto è anche utile per gli sviluppatori che desiderano migrare da OpenXML a Aspose.Cells.

{{% alert color="primary" %}}

Esplora [il plugin con esempi di codice sorgente delle funzionalità Aspose.Cells for .NET a confronto con OpenXML](https://github.com/asposemarketplace/Aspose_for_OpenXML).

Questo plugin utilizza la versione di valutazione di Aspose.Cells. Quando sei soddisfatto della tua valutazione, puoi acquistare una licenza dal [sito Web di Aspose](https://purchase.aspose.com/buy). Per rimuovere il messaggio di valutazione e le limitazioni delle funzionalità, è necessario applicare una licenza del prodotto. Dopo l'acquisto del prodotto, riceverai un file di licenza. Segui le istruzioni nell'articolo ["Licensing and Subscription"](/cells/it/net/licensing/) per farlo.

{{% /alert %}}

**Conclusione**: Open XML SDK e Aspose.Cells non competono direttamente perché affrontano esigenze e pubblici abbastanza diversi.

## **Perché Non Aprire XML SDK**
Open XML SDK è una libreria di classi per fornire un modo strong-typed per lavorare con documenti OOXML. Aspose.Cells è una libreria di elaborazione dei fogli di calcolo molto utile che fornisce un grande supporto per tutti i formati di file di Microsoft Excel e altri.

Se tutto ciò di cui hai bisogno è una operazione di programmazione abbastanza basilare su un documento XLSX, allora Open XML SDK potrebbe essere una scelta adatta. Con Open XML SDK, ti sentirai abbastanza a tuo agio nel svolgere compiti semplici come generare un semplice documento XLSX o rimuovere commenti, intestazioni/piedi di pagina, estrarre immagini o altri. 
Alcuni compiti possono essere realizzati con Open XML SDK, ma non possono essere realizzati con Aspose.Cells. Ad esempio, se hai bisogno di accedere direttamente agli elementi XML e attributi di un documento OOXML, allora dovresti utilizzare Open XML SDK.

Tuttavia, se hai bisogno di eseguire operazioni complesse sui documenti, come alcuni dei seguenti compiti, allora utilizzare Aspose.Cells è la tua migliore opzione:

- Supporta altri formati di file in aggiunta a XLSX.
- Copia frammenti e fogli di lavoro tra i workbook o unisce i workbook in modo che combini oggetti, stili e altre formattazioni in modo appropriato.
- Sostituisci testo formattato o non formattato.
- Funzioni di alto livello, come importare dati da diverse fonti di dati, inclusi Array, ArrayList, DataTable / ResultSet.
- Genera un documento commerciale, come un ordine con dettagli dell'ordine da una fonte di dati.
- Converti un documento in PDF o XPS in modo che appaia esattamente come Microsoft Excel l'avrebbe convertito.
- Sviluppa un'applicazione .NET o Java.

