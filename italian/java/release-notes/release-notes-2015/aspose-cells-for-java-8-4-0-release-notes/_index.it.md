---
title: Aspose.Cells for Java 8.4.0 Note di rilascio
type: docs
weight: 80
url: /it/java/aspose-cells-for-java-8-4-0-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 8.4.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.4.0/)

{{% /alert %}} 

\1) Aspose.Cells

Altri miglioramenti e modifiche

Nuove caratteristiche

(CELLSJAVA-41198) - Estrai i dati del tema dai file Excel
(CELLSJAVA-41185) - Generazione di immagini della barra dati

Miglioramenti

(CELLSJAVA-41169) - Rimuove gli attributi null fasulli nel file HTML generato
(CELLSJAVA-41179) - Supporto del calendario giapponese

Insetti

(CELLSJAVA-41222) - Il campo di ordinamento della tabella pivot è errato nell'output XLSX
(CELLSJAVA-41173) - HtmlSaveOptions.setExportHiddenWorksheet(true) non funziona correttamente
(CELLSJAVA-41168) - Modifiche nel ritaglio del testo tra celle da 8.3.1 a 8.3.1.5
(CELLSJAVA-41167) - L'aggiornamento delle tabelle pivot genera una cartella di lavoro danneggiata
(CELLSJAVA-41232) - Bug - La formula contiene un nome definito che termina con numero+e
(CELLSJAVA-41215) - I campi elettromagnetici generati con Aspose.Cells vengono visualizzati in modo diverso nei diversi visualizzatori
(CELLSJAVA-41196) - XLSB viene danneggiato dopo aver aggiunto un foglio di lavoro e un valore di cella
(CELLSJAVA-41227) - API non può sostituire il carattere Arial con Liberation Fonts
(CELLSJAVA-41224) - Errore nella conversione dell'immagine durante il rendering di Excel in PDF
(CELLSJAVA-41223) - La firma dei file PDF esportati non riesce
(CELLSJAVA-41208) - Suggerimenti per il rendering (Anti Aliasing) non funziona con SheetRender
(CELLSJAVA-41193) - I simboli Wingdings non vengono visualizzati correttamente quando il foglio di lavoro viene visualizzato nell'immagine
(CELLSJAVA-41184) - Problemi con il rendering dell'immagine di output dal grafico
(CELLSJAVA-41106) - Le etichette dei dati del grafico a torta si sovrappongono nell'immagine del grafico
(CELLSJAVA-40941) - Sovrapposizione di etichette dati del grafico a torta quando il grafico viene visualizzato come immagine
(CELLSJAVA-40813) - L'etichetta dei dati del grafico a torta si sovrappone nell'HTML di cui è stato eseguito il rendering
(CELLSJAVA-41182) - La linea uniforme non è corretta quando il colore del punto è diverso

Eccezioni

(CELLSJAVA-41201) - java.lang.IllegalArgumentException: Area sconosciuta, in PivotTable.refreshData
(CELLSJAVA-41192) - Eccezione: "java.lang.Exception: Fine del flusso raggiunta" all'apertura di un file XLS
(CELLSJAVA-41228) - java.lang.ArrayIndexOutOfBoundsException nella cartella di lavoro ctor durante il caricamento di un XLS
(CELLSJAVA-41211) - Si verifica un'eccezione durante la risoluzione del riferimento alla formula quando il nome del file viene impostato utilizzando Workbook.setFileName()

\2) Aspose.Cells Griglia Suite

Altri miglioramenti e modifiche

(CELLSJAVA-41202) - Visualizza i commenti Cell nel componente GridWeb

Insetti

(CELLSJAVA-41214) - Trascinando l'altezza della riga su 0, GridWeb non visualizza il valore
(CELLSJAVA-41209) - L'elenco di convalida dei dati non viene visualizzato in GridWeb
(CELLSJAVA-41205) - Quando i bordi sono spessi, l'altezza aumenta quando si elimina il valore della cella in GridWeb
(CELLSJAVA-41204) - Quando i bordi sono spessi, le altezze delle intestazioni non corrispondono in GridWeb
(CELLSJAVA-41203) - Le larghezze delle celle e dell'intestazione non corrispondono in GridWeb
(CELLSJAVA-41073) - Le larghezze delle intestazioni per le colonne sono diverse dalle larghezze delle celle in Chrome/Opera

Pubblico API e modifiche incompatibili con le versioni precedenti

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

 Aggiunge l'attributo HtmlSaveOptions.ExportBogusRowData
Indica se esportare i dati della riga inferiore fasulli. il valore predefinito è true.

 Aggiunge l'attributo HtmlSaveOptions.CellCssPrefix
Ottiene e imposta il prefisso del nome css, il valore predefinito è "".

 Aggiunge il metodo PivotTable.ShowInCompactForm()
Dispone la tabella pivot in formato compatto.

 Aggiunge il metodo PivotTable.ShowInOutlineForm()
Dispone la tabella pivot sotto forma di struttura.

Aggiunge il metodo PivotTable.ShowInTabularForm()
Dispone la tabella pivot in formato tabulare.

 Aggiunge il metodo PivotTableCollection.Remove(PivotTable pivotTable).
Elimina la tabella pivot specificata

 Aggiunge il metodo PivotTableCollection.RemoveAt(int index).
Elimina la tabella pivot in corrispondenza dell'indice specificato

 Aggiunge lo spazio dei nomi Aspose.Cells.Vba, le classi VbaPorject, VbaModuleCollection e VbaModule.
Sono utilizzati per leggere e modificare il progetto VBA nel file.

 Aggiunge la proprietà Border.ThemeColor.
Ottiene e imposta il colore del tema del bordo.

 Aggiunge la classe TxtLoadStyleStrategy e la proprietà TxtLoadOptions.LoadStyleStrategy.
Indica la strategia per applicare lo stile ai valori analizzati durante la conversione del valore stringa in numero o data/ora.

 Metodi TxtLoadOptions.KeepExactFormat obsoleti.
Utilizzare invece la proprietà TxtLoadOptions.LoadStyleStrategy.

 Metodi obsoleti Cells.GetCellByIndex() e Row.GetCellByIndex().
Utilizzare invece il metodo GetEnumerator() per iterare tutte le celle.

 Proprietà DrawObject.Image obsoleta
Utilizzare invece la proprietà DrawObject.ImageBytes per ottenere i dati dell'immagine.

 Aggiunge la proprietà DrawObject.ImageBytes
Ottiene i byte dell'immagine convertita da Chart o Shape.


Nota
Poiché la base di codice di Aspose.Cells for Java corrisponde al codice della versione .NET pertinente, la maggior parte delle modifiche, miglioramenti e correzioni inclusi in Aspose.Cells for .NET v8.4.0 sono inclusi anche in questo Aspose.Cells for Java v8.4.0.
