---
title: Perché non usare Open XML SDK
type: docs
weight: 20
url: /it/java/why-not-open-xml-sdk/
---

{{% alert color="primary" %}} 

A volte ci capita di sentire questa domanda:

**Perché dovremmo usare i prodotti Aspose anziché il gratuito Open XML SDK?**

Questa domanda è facile da rispondere: **funzionalità e capacità**.

{{% /alert %}} 
## **Cos'è Open XML SDK?**
Secondo la libreria MSDN, l'Open XML SDK è definito come: L'Open XML SDK 2.0 semplifica il compito di manipolare i pacchetti Open XML e gli elementi dello schema Open XML sottostanti all'interno di un pacchetto. L'Open XML SDK 2.0 incapsula molte attività comuni che gli sviluppatori eseguono sui pacchetti Open XML, in modo che tu possa eseguire operazioni complesse con poche righe di codice.I documenti OOXML sono essenzialmente file XML zippati e l'Open XML SDK è una raccolta di classi che ti consente di lavorare con il contenuto dei documenti OOXML in modo fortemente tipizzato. In pratica, anziché estrarre un file, caricare XML in un albero DOM e lavorare direttamente con elementi e attributi XML, l'Open XML SDK fornisce classi per fare ciò.
## **Cos'è Aspose.Cells?**
Aspose.Cells è una libreria di classi che consente all'applicazione di svolgere le seguenti attività di elaborazione dei fogli di calcolo: conversioni di alta qualità tra tutti i formati Excel più diffusi, inclusa la conversione in PDF, HTML, TIFF e la stampa; programmazione con un modello di oggetti di foglio di lavoro; possibilità di creare documenti da frammenti, da uno o più documenti, mentre si uniscono automaticamente i dati mediante formattazione stilistica, grafici e grafica; funzioni di alto livello, quali importazione dati da diverse origini dati, compreso Array, ArrayList, DataTable / ResultSet; motore di calcolo delle formule robusto che supporta quasi tutte le funzioni standard e avanzate di Microsoft Excel.


## **Confronta Open XML SDK e Aspose.Cells**
Il seguente elenco confronta le funzionalità di Open XML SDK e Aspose.Cells. 

|**Funzionalità o Categoria di funzionalità**|**Open XML SDK**|**Aspose.Cells**|
| :- | :- | :- |
|Formati Excel o altri supportati|XLSX|XLS, CSV, SpreadsheetML 2003, XLSX, HTML, Tabella delimitata, ODS, Testo semplice (TXT), PDF, XPS|
|Convertire tra formati Excel|No|Sì|
|<p>Programmazione di alto livello con un modello di oggetto di cartelle di lavoro:</p><p>- Trova e sostituisci.</p><p>- Assembla fogli di calcolo.</p><p>- Copia frammenti e fogli di lavoro tra cartelle di lavoro.</p>|No|Sì|
|Programmazione dettagliata con un modello di oggetto documento, accesso agli elementi individuali e alle proprietà di formattazione di tutti gli elementi del foglio di calcolo.|Sì|Sì|
|Accesso diretto e completo a basso livello agli elementi XML sottostanti e ai relativi attributi come identificatori di relazione, identificatori di elenchi di un documento OOXML.|Sì|No|
|<p>Genera report, popola documenti con dati:</p><p>- Importa/Esporta dati in/from un *DataTable/* ResultSet.</p><p>- Funzione Smart Markers.</p><p>- Inserisci/elimina righe/colonne/intervallo.</p><p>- Origini dati personalizzate.</p>|No|Sì|
|<p>Rendering e stampa:* Rappresenta pagine di fogli di lavoro in immagini raster (TIFF, TIFF multipagina, PNG, JPEG, BMP).* Rappresenta pagine di fogli di calcolo in immagini vettoriali (EMF).* Converti grafici in immagini (TIFF, TIFF multipagina, PNG, JPEG, BMP, EMF, ecc.)</p><p>- Specifica risoluzione immagine, qualità, compressione e altre opzioni.</p><p>- Stampa fogli di calcolo utilizzando l'infrastruttura di stampa .NET. Il componente ha un metodo di stampa incorporato per stampare i fogli di lavoro come mostrato in Anteprima di stampa di MS Excel.</p>|No|Sì|
|Calcola/Ricalcola formule dinamicamente|No|Sì|
|Piattaforme supportate|Windows, .NET|Windows, Linux, Java, .NET, Mono|
## **Conclusioni**
  {{% alert color="primary" %}}Open XML SDK and Aspose.Cells do not compete head to head because they address quite different needs and audiences. Open XML SDK is a class library to provide a strong-typed way to work with OOXML documents. Aspose.Cells is a very useful spreadsheet processing library that provides great support for all Microsoft Excel and other file formats. If all you need to do is a fairly basic programming operation on a XLSX document, then Open XML SDK might be a suitable choice. With Open XML SDK you will be fairly comfortable doing simple tasks like generating a simple XLSX document or removing comments, headers/footers, extracting images or others. Some tasks can be achieved with Open XML SDK, but cannot be achieved with Aspose.Cells. For example, if you need to directly access the XML elements and attributes of an OOXML document, then you should use Open XML SDK.However, if you need to perform complex operations on documents, such as some of the following tasks, then using Aspose.Cells is your best option: Support other file formats in addition to XLSX. Copy fragments and worksheets between workbooks or join workbooks in a way that combines objects, styles and other formatting in an appropriate manner. Replace formatted or unformatted text. High-level functions, such as, import data from different data sources including Array, ArrayList, DataTable / ResultSet. Generate a business document, such as an order with order details from a data source. Convert a document to PDF or XPS so it appears exactly like Microsoft Excel would have converted it. Develop a .NET or Java application. {{% /alert %}}
{{< app/cells/assistant language="java" >}}
