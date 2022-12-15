---
title: Aspose.Cells for .NET 8.4.2 Note di rilascio
type: docs
weight: 80
url: /it/net/aspose-cells-for-net-8-4-2-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 8.4.2](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.4.2/)

{{% /alert %}} 

 Di seguito è riportato un elenco di miglioramenti e modifiche in questa versione di Aspose.Cells



\1) Aspose.Cells 


## **Altri miglioramenti e modifiche**

## **Nuove caratteristiche**


 (CELLSNET-43596) - Aggiunta di un nuovo modulo al foglio di lavoro VbaProject

(CELLSNET-43569) - Supporto della formula/funzione IFNA


## **Insetti**


 (CELLSNET-43581) - Il testo viene spostato fuori dal banner quando il file Excel viene convertito in PDF

 (CELLSNET-43639) - Le filigrane non vengono visualizzate correttamente

 (CELLSNET-43645) - Impossibile salvare l'oggetto OLE incorporato da XLSX all'HTML

 (CELLSNET-43613) - Il carattere personalizzato non funziona con SheetRender

 (CELLSNET-43573) - Colonne spostate alla pagina successiva durante la conversione in PDF

 (CELLSNET-43571) - Interruzione di pagina errata nel PDF generato tramite Aspose.Cells

 (CELLSNET-43525) - L'immagine generata da SheetRender.ToImage ha il testo che viene tagliato

 (CELLSNET-43591) - Valore etichetta dati del grafico a torta errato

 (CELLSNET-43574) - Il testo delle etichette dati supera l'area del grafico quando viene convertito in PDF

 (CELLSNET-43568) - Conversione del grafico in immagine e inserimento dell'immagine

 (CELLSNET-43502) - Le linee principali della griglia scompaiono e la legenda della serie viene visualizzata al centro

 (CELLSNET-41716) - Le etichette dell'asse X non vengono visualizzate correttamente

(CELLSNET-43641) - Problema con il calcolo delle formule quando si abilita il calcolo iterativo

 (CELLSNET-43637) - Risultati della formula errati per la funzione PERCENT.RANGO

 (CELLSNET-43630) - Problema con il calcolo della formula/funzione REGR.LIN

 (CELLSNET-43628) - Il foglio di calcolo scompare dalla visualizzazione quando si fa clic sul pulsante Ripristina finestra

 (CELLSNET-43612) - System.ArgumentOutOfRangeException durante il caricamento di un file salvato da Aspose.Cells for Java

 (CELLSNET-43604) - ListObjects.DataRange non si aggiorna dopo l'eliminazione di una riga

 (CELLSNET-43603) - Cells.DeleteRows danneggia il foglio di calcolo

 (CELLSNET-43602) - La formula Vlookup non è stata calcolata correttamente

 (CELLSNET-43590) - Il file Xlsx viene danneggiato all'apertura e al salvataggio

 (CELLSNET-43589) - Cell.GetValidationValue non funzionante per l'elenco numerico


## **Eccezioni**


 (CELLSNET-43585) - Aspose.Cells.CellsException durante la conversione del foglio di calcolo in PDF

 (CELLSNET-43609) - Eccezione nel rendering di un file Excel in formato file PDF

(CELLSNET-43583) - Errore GDI nel metodo SheetRender.ToImage

 (CELLSNET-43565) - CellsException al salvataggio di xlsx in pdf

 (CELLSNET-43631) - SheetRender ctor genera un'eccezione NullReferenceException

 (CELLSNET-43646) - IndexOutOfRangeException nella cartella di lavoro.Salva quando il percorso del file non ha un'estensione

 (CELLSNET-43643) - System.NullReferenceException nella cartella di lavoro ctor

 (CELLSNET-43636) - CellsException in Workbook.CalculateFormula

 (CELLSNET-43621) - System.ArgumentException nella cartella di lavoro ctor

 (CELLSNET-43614) - L'aggiunta di un modulo causa un'eccezione di chiavi duplicate durante il salvataggio della cartella di lavoro

 (CELLSNET-43598) - Eccezione durante la conversione di xls in pdf

 (CELLSNET-43572) - System.OverflowException in Workbook.Save

 (CELLSNET-43570) - ListObject.ConvertToRange genera NullReferenceException su una tabella

 (CELLSNET-43564) - NullReferenceException durante il salvataggio di un file XLSB



\2) Aspose.Cells Griglia Suite


## **Altri miglioramenti e modifiche**

## **Insetti**


 (CELLSNET-43610) - L'evento SaveCommand non viene attivato

(CELLSNET-43551) - IE8 non funziona correttamente con il formato personalizzato olandese-belga


## **API pubblica e modifiche non compatibili con le versioni precedenti**


 Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.



 Aggiunge i metodi VbaModuleCollection.Add

 Aggiunge il modulo VBA.



 Aggiunge i metodi override Cells.CopyColumns().

 Copia alcune colonne.



Aggiunge le enumerazioni PasteType.Default e PasteType.DefaultExceptBorders.

 Viene utilizzato per copiare l'intervallo come "Tutto" e "Tutto tranne i bordi" in MS Excel.


