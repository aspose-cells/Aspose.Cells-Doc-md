---
title: Aspose.Cells for Java 8.3.2 Note di rilascio
type: docs
weight: 90
url: /it/java/aspose-cells-for-java-8-3-2-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 8.3.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.3.2/)

{{% /alert %}} 

\1) Aspose.Cells 


Caratteristiche principali

Modifiche all'archivio rilasciate per JDK supportato

D'ora in poi forniamo solo un singolo file Jar per 1.6 e versioni successive nell'archivio.

Altri miglioramenti e modifiche

Nuove caratteristiche

(CELLSJAVA-41144) - Possibilità di eliminare lo stile da StyleCollection durante il salvataggio dell'HTML
(CELLSJAVA-41127) - Specifica i separatori personalizzati per la cartella di lavoro completa
(CELLSJAVA-41143) - Specificare il nome del lavoro/documento durante la stampa con Aspose.Cells

Miglioramenti

(CELLSJAVA-41145) - Generazione intelligente di CSS durante l'esportazione di fogli di calcolo in HTML
(CELLSJAVA-41177) - Cell.setHtmlString non funziona quando si utilizza "<s><span style="color:#ff00ff;">S2</span></s>"
(CELLSJAVA-41162) - Aggiunte directory di font predefinite per Mac e Linux nell'elenco di ricerca dei font

Prestazione

(CELLSJAVA-41119) - Chart.toImage si blocca per un tempo indefinito

Insetti

(CELLSJAVA-41165) - Il grafico pivot non si aggiorna dopo l'aggiornamento dei dati di origine e il rendering del foglio di calcolo in PDF
(CELLSJAVA-41156) - Chart.refreshPivotData fa sì che le date nell'asse del grafico vengano convertite in numeri durante la conversione del foglio di calcolo in PDF
(CELLSJAVA-41154) - Nell'output HTML viene visualizzata una riga aggiuntiva mentre si incolla l'intervallo con PasteType.ALL
(CELLSJAVA-41151) - Strano comportamento relativo alla formattazione nel rapporto di tabella pivot di output quando si utilizza e non si utilizza la riga di codice che corrisponde al recupero dell'intervallo di righe
(CELLSJAVA-41150) - FormatCondition non supportato per quanto riguarda il formato Numbers durante il rendering in formato file HTML
(CELLSJAVA-41146) - Rendering errato del bordo durante la conversione del foglio di calcolo in HTML
(CELLSJAVA-41134) - XLSB2007TestNewS.xlsb non si carica e continua ad aumentare il consumo di memoria
(CELLSJAVA-41129) - Vengono visualizzate righe aggiuntive quando l'HTML di output viene visualizzato in Chrome
(CELLSJAVA-41122) - Apertura e risparmio finanziario_Dichiarazione_Ingresso_Rapporto_Withdata.xlsb lo rende corrotto
(CELLSJAVA-41098) - Aggiorna tabella pivot rimuove la formattazione della tabella pivot durante la conversione in PDF
(CELLSJAVA-41157) - MemorySetting.MEMORY_PREFERENCE provoca il danneggiamento di XLS
(CELLSJAVA-41149) - Visualizzazione errata dell'ora quando il foglio di calcolo viene convertito in PDF
(CELLSJAVA-41148) - Excel ha trovato contenuto illeggibile... errore durante l'apertura e il salvataggio della cartella di lavoro
(CELLSJAVA-41141) - Cell non viene impostato con il metodo ListObject.putCellValue()
(CELLSJAVA-41140) - La tabella estesa non copia la formula in nuove righe
(CELLSJAVA-41166) - XPS Viewer non può aprire Aspose.Cells XPS generato
(CELLSJAVA-41163) - L'esportazione SVG crea un file non valido
(CELLSJAVA-41153) - Shape.toImage memorizza l'immagine in formato BMP anziché SVG per forme diverse da Chart
(CELLSJAVA-41137) - Problema con l'impostazione dei valori dell'intervallo di celle delle etichette dati
(CELLSJAVA-41128) - I grafici non vengono riprodotti correttamente quando si salva nuovamente il file XLSX
(CELLSJAVA-41125) - L'immagine del grafico presenta un disturbo quando viene convertita con una risoluzione inferiore
(CELLSJAVA-40928) - Il testo cinese nei titoli delle categorie di grafici non viene visualizzato correttamente
(CELLSJAVA-41158) - Problema con la formattazione dei dati nel rapporto di tabella pivot
(CELLSJAVA-41159) - Problema con il calcolo dei dati della tabella pivot
(CELLSJAVA-41175) - Le serie Trendline non sono mostrate nella legenda

Eccezioni

(CELLSJAVA-41164) - java.lang.NullPointerException a Cells.find
(CELLSJAVA-41131) - Il salvataggio in PDF si blocca e si verifica un problema di memoria con il file XLSB di origine

Pubblico API e modifiche incompatibili con le versioni precedenti

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

 Aggiunge le proprietà WorkbookSettings.NumberDecimalSeparator, NumberGroupSeparator
 Ottiene/imposta i separatori utilizzati per la formattazione/l'analisi dei valori numerici.

 Aggiunge il metodo WorkbookSettings.CheckWriteProtectedPassword()
 Controlla se la password è corretta password protetta da scrittura.

 Aggiunge la proprietà Picture.SignatureLine e la classe SignatureLine.
 Utilizzato per creare e leggere l'impostazione della riga della firma.

 Aggiunge la proprietà PivotItem.Position.
 Specifica l'indice di posizione in tutti i PivotItems, non i PivotItems sotto lo stesso nodo padre.

 Aggiunge la proprietà PivotItem.PositionInSameParentNode.
 Specifica l'indice di posizione nei PivotItems sotto lo stesso nodo padre.

 Aggiunge il metodo PivotItem.Move(int count, bool isSameParent).
Sposta l'elemento in alto o in basso.

 Aggiunge il metodo Worksheet.RefreshPivotTables().
Aggiorna tutte le tabelle pivot in questo foglio di lavoro.

 Aggiunge il metodo Workbook.GetNamedStyle(string name).
Ottiene lo stile denominato nel pool di stili della cartella di lavoro in base al nome.

 Aggiunge Cells.ImportTwoDimensionArray(object,, object,, int, int, TxtLoadOptions)
Importa una matrice di dati a due dimensioni in un foglio di lavoro con opzioni più flessibili definite in TxtLoadOptions.

 Aggiunge la proprietà PageSetup.IsAutomaticPaperSize.
 Indica se il formato carta è automatico.

 Aggiunge le proprietà XpsSaveOptions.OnePagePerSheet
Se OnePagePerSheet è true , tutto il contenuto di un foglio verrà restituito a una sola pagina nel risultato.

 Aggiunge le proprietà XpsSaveOptions.PageIndex
Ottiene o imposta l'indice in base 0 della prima pagina da salvare.

 Aggiunge le proprietà XpsSaveOptions.PageCount
Ottiene o imposta il numero di pagine da salvare.

 Aggiunge il metodo SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)
Rende il foglio di lavoro alla stampante.

Aggiunge il metodo WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)
Rende la cartella di lavoro alla stampante.

 Aggiunge le proprietà PdfSaveOptions.IsFontSubstitutionCharGranularity
Indica se sostituire solo il carattere del carattere quando il carattere della cella non è compatibile con esso.

 Aggiunge la proprietà GridWeb.AutoRefreshChart
Indica se l'immagine del grafico viene aggiornata durante l'aggiornamento del valore della cella. L'impostazione predefinita è true.

 Aggiunge il metodo GridWeb.RefreshChartShape()
Aggiorna tutta l'immagine del grafico per il foglio di lavoro attivo.

 Proprietà Workbook.SaveOptions obsoleta
Gli utenti dovrebbero creare SaveOptions appropriati e quindi utilizzare Workbook.Save() con esso.

 Classe StyleCollection e proprietà Workbook.Styles obsolete
Gli utenti devono utilizzare Workbook.CreateStyle() per creare e manipolare lo stile per la cartella di lavoro anziché StyleCollection.Add() e utilizzare Workbook.GetNamedStyle(string) per ottenere lo stile denominato anziché StyleCollectionstring.

 Metodo PivotItem.Move(int count) obsoleto.
Usando invece il metodo PivotItem.Move(int count, bool isSameParent).

Elimina tutti i metodi Open() e Save() obsoleti di Workbook.

 Elimina il metodo Workbook.SetOleSize() obsoleto.

 Elimina le proprietà IsProtected, Language e Region obsolete della cartella di lavoro.

 Elimina i metodi Workbook.LoadData() obsoleti.

 Elimina i metodi Open() e Save() obsoleti di WorkbookDesigner.

 Elimina le proprietà ReCalcOnOpen, Language, Encoding e ConvertNumericData obsolete di WorkbookSettings.

 Elimina le proprietà HidePivotFieldList,EnableHTTPCompression,IsMinimized,IsHidden,SheetTabBarWidth obsolete di WorksheetCollection.

 Elimina le proprietà obsolete WindowLeft,WindowLeftInch,WindowLeftCM,WindowTop,WindowTopInch,WindowTopCM,WindowWidth,WindowWidthInch,WindowWidthCM,WindowHeight,WindowHeightInch,WindowHeightCM di WorksheetCollection.

 Elimina il metodo obsoleto DeleteName() di WorksheetCollection.

 Elimina HPageBreaks e VPageBreaks obsoleti del foglio di lavoro.

Elimina DisplayHTMLCrossString ed ExportChartImageFormat obsoleti di HtmlSaveOptions.

 Elimina la proprietà ExpCellNameToXLSX obsoleta di SaveOptions.

 Elimina le proprietà obsolete DefaultFont, Compliance, PdfBookmark e PdfImageCompression di SaveOptions.

 Elimina la proprietà TxtSaveOptions.AlwaysQuoted obsoleta.


Nota
Poiché la base di codice di Aspose.Cells for Java corrisponde al codice della versione .NET pertinente, la maggior parte delle modifiche, miglioramenti e correzioni inclusi in Aspose.Cells for .NET v8.3.2 sono inclusi anche in questo Aspose.Cells for Java v8.3.2.
