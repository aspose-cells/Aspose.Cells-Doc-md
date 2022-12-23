---
title: Aspose.Cells for .NET 7.1.1 Note di rilascio
type: docs
weight: 100
url: /it/net/aspose-cells-for-net-7-1-1-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 7.1.1](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-7.1.1/)

{{% /alert %}} 

 Siamo lieti di annunciareAspose.Cells for .NET v7.1.1!

\1) Aspose.Cells 

 Nuove caratteristiche

- Rintracciare precedenti e dipendenti

 Miglioramenti

- Il salvataggio della cartella di lavoro in XLSX genera un errore
- Opzioni AutoFitColumn
- Esiste il metodo GetDependents() nella versione .NET

 -Supporta gli elementi TH nella tabella HTML

- Da Excel a PDF (arabo) - Formattazione parola/data errata durante la conversione
- Il software antivirus rimuove i file Excel dalle e-mail

 Eccezioni

- Errore durante l'apertura di un file che ha un foglio di lavoro con nome contenente: "!" carattere
- Eccezioni al caricamento di file Excel validi - ogni volta
- L'intervallo del filtro automatico non è valido
- Eccezione dopo l'utilizzo dei metodi Combine() e Save() per le cartelle di lavoro con riferimenti esterni

 Insetti

- Problema di formattazione condizionale a partire dalla versione v4.8.1

 -Proprietà del pulsante

- Cells con piedi e pollici non sono corretti se convertiti in PDF
- Problema durante il rendering dei trattini em nell'output PDF
- Layout di pagina modificato nella cartella di lavoro unita
- Salva come XLSX a volte produce un file non valido

 -XLS il file si apre in modalità protetta dopo aver utilizzato Aspose.Cells

- Cell.GetDependents() non funziona con NamedRange
- Problema con AutoFitRow e IndentLevel
- Problema con l'intervallo denominato durante l'utilizzo dell'operazione Combina
- Le TickLabel non sono visibili quando il n. del conteggio di Ticklabels è maggiore
- Problemi con la traduzione di grafici MS Excel in PDF, asse Y assente
- Problemi con la larghezza della linea nella grafica e nelle aree di testo vuote
- Problema con le funzioni ADDRESS, COUNTBLANK e IF
- FUNZIONI CERCA.VERT E OFFSET Problemi
- Nessuna convalida della formula MS Excel
- Problemi con la funzione NETWORKDAYS nell'output XLS
- HTML Problemi di conversione da Excel a Excel

 ` `- HTML'srowspan e problemi relativi agli attributi di classe

-Cells supporta datauri

- Bordi formattati personalizzati persi durante la conversione in PDF
- Griglia nell'esportazione PDF

 -Excel ha trovato un errore di contenuto illeggibile

- Estrai lo stile pivot personalizzato dal file modello
- Problema riscontrato in MS Excel: "Excel trovato contenuto illeggibile..."
- Allineamento delle colonne nell'immagine quando si utilizza SheetRender API
- Problema di rendering di Excel

\2)
 Aspose.Cells.GridWeb

 Insetti

- Problema di a capo automatico per GridWeb

 GridWeb.SaveToExcelFile esclusi i dati appena inseriti

- L'impostazione dell'allineamento verticale del testo non funziona

\3)
 Aspose.Cells. GrigliaDesktop

 Insetti

- La stringa non è stata riconosciuta come booleano valido
