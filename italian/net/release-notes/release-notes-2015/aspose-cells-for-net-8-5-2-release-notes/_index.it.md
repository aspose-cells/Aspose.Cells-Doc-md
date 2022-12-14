---
title: Aspose.Cells for .NET 8.5.2 Note di rilascio
type: docs
weight: 50
url: /it/net/aspose-cells-for-net-8-5-2-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 8.5.2](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.5.2/)

{{% /alert %}} 

 Di seguito è riportato un elenco di miglioramenti e modifiche in questa versione di Aspose.Cells



\1) Aspose.Cells 


## **Altri miglioramenti e modifiche**

## **Nuove caratteristiche**


 (CELLSNET-43758) - Rendering nel contesto grafico


## **Insetti**


 (CELLSNET-43786) - Il file è danneggiato dopo l'aggiornamento della tabella pivot nel file modello

 (CELLSNET-43594) - PivotField.IsRepeatItemLabels non funzionante nella tabella pivot

 (CELLSNET-43367) - Problema con PivotTable.Format() per formattare l'intestazione PivotField

 (CELLSNET-41618) - Mancata visualizzazione di alcune immagini e forme dopo la conversione di Xls in Html

(CELLSNET-43817) - CalculateFormula() non termina mai per alcune formule di Excel SOMMA.SE

 (CELLSNET-43675) - Problema nel calcolo della funzione DISTRIB.NORM.S.N

 (CELLSNET-43741) - Il numero non aumenta quando Workbook.Settings.CreateCalcChain è impostato su true

 (CELLSNET-43818) - Aspose.Cells genera 2 pagine mentre l'anteprima di stampa di Excel mostra 1 pagina

 (CELLSNET-43780) - Formato carta esecutivo errato durante la conversione in PDF

 (CELLSNET-43776) - L'immagine viene convertita in nero durante la conversione del foglio di calcolo in PdfA1b

 (CELLSNET-43769) - Cell i contenuti sono leggermente ritagliati in alto nell'immagine di output

 (CELLSNET-43806) - La trama/curva non è la stessa per i grafici a dispersione XY.

 (CELLSNET-43805) - Conversione da foglio di calcolo a PDF: lo stile audace è perduto

 (CELLSNET-43804) - Conversione da foglio di calcolo a PDF: il contenuto nella casella di testo viene visualizzato con rientro

 (CELLSNET-43779) - Incoerenza tra grafico e immagine per il formato di file EMF

(CELLSNET-43772) - Il testo nella forma del disegno non viene racchiuso correttamente

 (CELLSNET-43771) - L'immagine è stata spostata dopo il rendering del foglio di calcolo in PDF

 (CELLSNET-43748) - Il testo della casella di testo viene sovrapposto nel rendering da Excel a PDF

 (CELLSNET-43820) - Il foglio di calcolo contenente i filtri dei dati diventa danneggiato dopo il nuovo salvataggio

 (CELLSNET-43812) - Il grafico diventa vuoto nel file excel di output e non viene visualizzato in Excel 2013

 (CELLSNET-43810) - Errore durante l'apertura del file XLSX salvato tramite le API Aspose.Cells

 (CELLSNET-43807) - Il foglio di calcolo contenente la tabella pivot è danneggiato dopo averlo salvato nuovamente

 (CELLSNET-43802) - Il file Excel si corrompe all'apertura e al nuovo salvataggio e non si apre in Excel 2013

 (CELLSNET-43799) - Il nuovo salvataggio del foglio di calcolo danneggia i risultati e i filtri dei dati vengono rimossi

 (CELLSNET-43792) - La connessione dati della cartella di lavoro viene rimossa dopo aver salvato nuovamente il foglio di calcolo


## **Eccezioni**


 (CELLSNET-43629) - PivotTable.RefreshData() - Impossibile eseguire il cast dell'oggetto di tipo

(CELLSNET-43778) - System.FormatException in Chart.ToImage quando la locale del sistema è Russia

 (CELLSNET-43822) - La cartella di lavoro contenente il grafico non può essere salvata e genera un'eccezione

 (CELLSNET-43814) - Il caricamento di Excel in formato xlsm genera un errore di riferimento nullo

 (CELLSNET-43793) - Aspose.Cells.CellsException: ignora l'errore dell'elemento durante il caricamento di un file XLSX

 (CELLSNET-43784) - System.ArgumentException in Workbook.Combine

 (CELLSNET-43783) - Eccezione durante il rendering di un foglio di calcolo nel formato di file delimitato da tabulazioni

 (CELLSNET-43828) - System.InvalidCastException durante il nuovo salvataggio di un file XLSX modello



\2) Aspose.Cells Griglia Suite


## **Nuove caratteristiche**


 (CELLSNET-43809) - Aggiunge l'evento di callback asincrono per griddesktop

 (CELLSNET-42316) - La scorciatoia da tastiera Ctrl + Maiusc + Freccia non funziona.

 (CELLSNET-42174) - Control + tasti freccia non passano alla cella con i dati


## **Altri miglioramenti e modifiche**

## **Insetti**


 (CELLSNET-43782) - La proprietà GridCell.Protected è stata rimossa

 (CELLSNET-43688) - L'altezza della riga per alcune celle unite non è corretta.


## **Pubblico API e modifiche incompatibili con le versioni precedenti**


 Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.



 Aggiunge la proprietà SaveOptions.MergeAreas.

 Viene utilizzato per unire singole CellArea della formattazione e della convalida condizionale.



 Aggiunge il metodo PivotTable.GetCellByDisplayName(string displayName).

 Ottiene l'oggetto Cell in base al DisplayName di PivotField.



Aggiunge il metodo SheetRender.ToImage(int pageIndex, Graphics g, float x, float y).

 Renderizza determinate pagine di SheetRender in una grafica.



 Aggiunge il metodo SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height).

 Renderizza determinate pagine di SheetRender in una grafica.



 Aggiunge la proprietà Shape.Geometry.ShapeAdjustValues.

 Ottiene una raccolta di valori di regolazione della forma.



Aggiunge gli eventi GridDesktop.BeforeLoadFile/FinishLoadFile/BeforeCalculate/FinishCalculate.

 Si verifica nel diverso stato di caricamento del file della cartella di lavoro in GridDesktop.


