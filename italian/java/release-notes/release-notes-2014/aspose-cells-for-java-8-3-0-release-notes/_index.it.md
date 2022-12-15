---
title: Aspose.Cells for Java 8.3.0 Note di rilascio
type: docs
weight: 10
url: /it/java/aspose-cells-for-java-8-3-0-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 8.3.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.3.0/)

{{% /alert %}} 

\1) Aspose.Cells 


Altri miglioramenti e modifiche

Miglioramenti

(CELLSJAVA-41052) - Aumenta le prestazioni memorizzando nella cache l'oggetto MessageFormat preparato
(CELLSJAVA-41050) - Rimuovi o memorizza nella cache MessageFormat/DecimalFormat.format() per migliorare le prestazioni
(CELLSJAVA-41069) - Rimuovi riferimenti XLA

Insetti

(CELLSJAVA-41084) - Le barre del grafico per i valori negativi perdono colore quando il foglio di calcolo viene salvato da Aspose.Cells
(CELLSJAVA-41082) - Errore nel calcolo delle celle - eccezione nel calcolo della formula
(CELLSJAVA-41070) - Problema da HTML a XLS - il numero formattato viene reso vuoto
(CELLSJAVA-41034) - Il testo della casella di testo non è incluso nell'immagine del grafico
(CELLSJAVA-41083) - La funzione Excel NOW() non funziona nell'impostazione russa
(CELLSJAVA-41062) - Color.getBlack().equals(Color.getEmpty()) restituisce true. Dovrebbe restituire false
(CELLSJAVA-41014) - Il valore DateTime non viene letto nel formato corretto
(CELLSJAVA-41076) - Il riferimento XLA non è stato rimosso correttamente da ExternalLink.setDataSource
(CELLSJAVA-41068) - Il file XLSX è danneggiato dopo aver salvato nuovamente il file tramite le API Aspose.Cells
(CELLSJAVA-41066) - I passaggi dell'asse del grafico si interrompevano dopo la copia del foglio di lavoro
(CELLSJAVA-41060) - La modifica della tavolozza dei colori della cartella di lavoro durante il salvataggio di XLSX in XLS fa sì che MS Excel apra il foglio di calcolo risultante in visualizzazione protetta
(CELLSJAVA-41059) - Modifica dell'ordine delle regole di formattazione condizionale durante il salvataggio di XLSX in XLS con cambio pallet
(CELLSJAVA-41057) - Quote in perdita per determinati intervalli denominati
(CELLSJAVA-41056) - Il metodo Cells.copyRows() non copia i grafici sparkline nel formato di file XLSX
(CELLSJAVA-41055) - Problema di formattazione del testo durante la lettura degli stili delle celle
(CELLSJAVA-41049) - Ottenere #VALORE! errore durante l'utilizzo della funzione RATE
(CELLSJAVA-41038) - Le serie nascoste all'interno della legenda riappaiono dopo aver copiato il foglio di lavoro.
(CELLSJAVA-41036) - I passaggi dell'asse del grafico si interrompevano quando la cartella di lavoro veniva nuovamente salvata
(CELLSJAVA-41054) - L'immagine copiata e incollata non viene visualizzata nel PDF
(CELLSJAVA-41044) - Il PDF generato Aspose.Cells non supera il test di conformità PDF/A-1b
(CELLSJAVA-41015) - Aspose.Cells Il documento PD/A-1b generato non supera la convalida preliminare
(CELLSJAVA-40951) - Il documento PDF è danneggiato e non può essere aperto in Acrobat Reader dopo la conversione dal file modello di Excel
(CELLSJAVA-40725) - Le clipart non vengono visualizzate in pdf
(CELLSJAVA-40692) - Conformità PDF/A-1b non riuscita con Adobe Preflight
(CELLSJAVA-41086) - I nomi delle serie di grafici definiti dall'utente sono vuoti
(CELLSJAVA-41065) - I titoli dei grafici sono incasinati
(CELLSJAVA-41047) - Il separatore dati dell'istogramma in pila ha uno spessore diverso durante il rendering del foglio di calcolo in formato PDF
(CELLSJAVA-41045) - Le colonne del grafico si sovrappongono all'asse inferiore durante il rendering del foglio di calcolo in formato PDF
(CELLSJAVA-40989) - Il grafico a barre ha linee verticali extra sulla destra delle barre quando viene visualizzato come PDF
(CELLSJAVA-40988) - L'etichetta dati del grafico è tagliata nel PDF renderizzato
(CELLSJAVA-40987) - Le etichette e la legenda degli assi del grafico si sovrappongono nel PDF renderizzato
(CELLSJAVA-40945) - Le caselle di testo vengono perse dal grafico

Eccezioni

(CELLSJAVA-41067) - Random CellsException: formato immagine sconosciuto, in Cartella di lavoro ctor

\2) Aspose.Cells Griglia Suite

Altri miglioramenti e modifiche

Nuove caratteristiche

(CELLSJAVA-41074) - Esporta dati da GridWeb a file Excel o file XML - GridWeb per JAVA
(CELLSJAVA-41078) - Supporto per l'esportazione di file SpreadsheetML (.xml) - GridWeb (JAVA)

Insetti

(CELLSJAVA-41063) - La messa a fuoco della cella con un solo clic e l'inserimento dei dati non funziona in IE8
(CELLSJAVA-41081) - Il tag della cella visualizza l'errore del valore della cella nella demo GridWeb Logical
(CELLSJAVA-41073) - Le larghezze delle intestazioni per le colonne sono diverse dalle larghezze delle celle in Chrome/Opera (GridWeb per JAVA)
(CELLSJAVA-41077) - L'espressione regolare non è valida nella demo di GridWeb
(CELLSJAVA-41071) - Formato numerico errato in customformat.jsp
(CELLSJAVA-41079) - Le demo DateAndTime e CustomFormat forniscono risultati non formattati quando si specifica una data personalizzata

API pubblica e modifiche non compatibili con le versioni precedenti

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.

 Aggiunge la proprietà TxtLoadOptions.KeepExactFormat
Indica se la formattazione esatta deve essere mantenuta per la cella durante la conversione del valore stringa in numero o data/ora.

Aggiorna l'enumerazione Aspose.Cells.Pivot.PivotItemPosition
Aggiornamenti come: precedente, successivo e personalizzato.

Aggiunge il metodo SetPositionAuto() di PlotArea.
Imposta la posizione dell'area del tracciato come automatica.

Aggiunge la proprietà Shape.Id
Viene utilizzato per ottenere l'id della forma.

Aggiunge la proprietà GridDesktop.SheetTabWidth
Imposta/Ottiene la larghezza della scheda Foglio.


Nota
Poiché la base di codice di Aspose.Cells for Java corrisponde al codice della versione .NET pertinente, la maggior parte delle modifiche, miglioramenti e correzioni inclusi in Aspose.Cells for .NET v8.3.0 sono inclusi anche in questo Aspose.Cells for Java v8.3.0.
