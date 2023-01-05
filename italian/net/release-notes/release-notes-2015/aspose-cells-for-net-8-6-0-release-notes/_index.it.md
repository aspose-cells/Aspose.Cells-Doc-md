---
title: Aspose.Cells for .NET 8.6.0 Note di rilascio
type: docs
weight: 40
url: /it/net/aspose-cells-for-net-8-6-0-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 8.6.0](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.6.0/)

{{% /alert %}} 

 Di seguito è riportato un elenco di miglioramenti e modifiche in questa versione di Aspose.Cells



\1) Aspose.Cells 


## **Altri miglioramenti e modifiche**

## **Nuove caratteristiche**


 (CELLSNET-43880) - Assegna macro ai controlli del modulo


## **Miglioramenti**


 (CELLSNET-43832) - Worksheet.Shapes.UpdateSelectedValue genera CellsException a volte

 (CELLSNET-43823) - L'inclusione di una directory dei caratteri con CellsHelper non sembra funzionare

 (CELLSNET-43900) - Hyperlink.TextToDisplay non viene aggiornato

 (CELLSNET-43892) - XLSX la dimensione del documento aumenta a ogni salvataggio

 (CELLSNET-43869) - Aspose.Cells non è in grado di funzionare nel Medium Trust


## **Insetti**


(CELLSNET-43884) - I simboli Wingdings non vengono visualizzati correttamente durante la conversione di alcuni fogli di calcolo in HTML

 (CELLSNET-43877) - Excel ripara sempre il foglio di calcolo risultante dopo l'aggiunta della tabella pivot

 (CELLSNET-43831) - HTML in Excel - Stile CSS ignorato

 (CELLSNET-43750) - Modifiche al grafico nel foglio di calcolo risultante dopo l'aggiornamento del grafico

 (CELLSNET-43843) - Workbook.CalculateFormula non viene mai restituito

 (CELLSNET-43842) - Aspose.Cells Errore di inserimento riga

 (CELLSNET-43879) - caratteri sovrapposti e convertiti in ######## in Excel per il rendering PDF

 (CELLSNET-43854) - L'apice e il pedice sono stati spostati troppo durante la generazione dell'immagine

 (CELLSNET-42762) - Le etichette degli assi del grafico vengono visualizzate con testo frastagliato

 (CELLSNET-42384) - Le caselle WordArt vengono disattivate quando XLSX viene convertito in PDF

 (CELLSNET-42380) - Le scatole SmartArt stanno diventando nere.

(CELLSNET-42377) - L'intestazione del layout SmartArt si sovrappone alla sottolineatura sotto l'intestazione Immagine.

 (CELLSNET-41493) - Il testo viene troncato/inserito nel codice PDF generato

 (CELLSNET-41398) - Il documento foglio di calcolo produce più documenti quando viene convertito

 (CELLSNET-43894) - Impossibile aggiornare ObjectSourceFullName del collegamento OLE

 (CELLSNET-43882) - PageSetup.Zoom è stato modificato dopo l'apertura e il salvataggio della cartella di lavoro

 (CELLSNET-43881) - Alcune formule di cella vengono perse quando la riga viene copiata

 (CELLSNET-43876) - Doppia lettura dei feed di riga di ritorno a capo

 (CELLSNET-43864) - La combinazione di due cartelle di lavoro XLSM produce una cartella di lavoro danneggiata

 (CELLSNET-43839) - Le immagini nel foglio di calcolo non vengono visualizzate durante la conversione in PDF

 (CELLSNET-43837) - L'immagine collegata non è all'interno del grafico dopo aver istanziato l'oggetto cartella di lavoro e averlo salvato

 (CELLSNET-43836) - Range.CopyData funziona ma Range.Copy non funziona

(CELLSNET-43830) - L'aggiunta di più di 2084 caratteri nel collegamento ipertestuale danneggia il file xlsx di output

 (CELLSNET-43829) - La funzione Excel esegue il rendering con #NOME? errore sul Foglio 1


## **Eccezioni**


 (CELLSNET-43866) - CellsException durante il rendering di un foglio di calcolo su PDF

 (CELLSNET-43847) - Si verifica un'eccezione quando si tenta di richiamare RefreshPivotTables

 (CELLSNET-43852) - CellsException in Workbook.CalculateFormula

 (CELLSNET-43893) - CellsException durante il rendering di un foglio di calcolo nel formato PDF

 (CELLSNET-42108) - CellsException: parametro non valido: durante la conversione da XLS a PDF

 (CELLSNET-43835) - System.OutOfMemoryException durante la conversione di un file XLS nel formato file PDF

 (CELLSNET-43865) - ArgumentException durante il rendering del foglio di calcolo su PDF e HTML

 (CELLSNET-43862) - NullReferenceException in Workbook.Save



 \2) Aspose.Cells Griglia Suite


## **Altri miglioramenti e modifiche**

## **Insetti**


 (CELLSNET-43875) - Gridweb Print su Chrome non funziona correttamente


## **Pubblico API e modifiche incompatibili con le versioni precedenti**


 Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.



 Aggiunge lo spazio dei nomi e le classi di WorkbookMetadata.

È utilizzato per leggere e salvare i metadati del file.



 Aggiunge HtmlSaveOptions. Proprietà ExportFrameScriptsAndProperties

 Indica se esportare gli script dei frame e le proprietà del documento. Il valore predefinito è vero.



 Aggiunge la proprietà Shape.MarcoName

 Viene utilizzato per ottenere e impostare il nome della macro.



 Aggiunge la proprietà OoxmlSaveOptions.UpdateZoom

 Viene utilizzato per aggiornare PageSetup.Zoom se le proprietà PageSetup.FitToPagesWide e PageSetup.FitToPagesTall controllano la modalità di ridimensionamento del foglio di lavoro.


