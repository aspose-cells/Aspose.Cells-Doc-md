---
title: Aspose.Cells for Java 8.5.1 Note di rilascio
type: docs
weight: 40
url: /it/java/aspose-cells-for-java-8-5-1-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 8.5.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.5.1/)

{{% /alert %}} 

 Di seguito è riportato un elenco di miglioramenti e modifiche in questa versione di Aspose.Cells



\1) Aspose.Cells 


## **Altri miglioramenti e modifiche**

## **Insetti**


 (CELLSJAVA-41378) - L'allineamento di determinate celle non viene mantenuto nell'HTML generato

 (CELLSJAVA-41376) - Viene visualizzato un messaggio di errore dopo il salvataggio della cartella di lavoro

 (CELLSJAVA-41412) - ListColumn.getRange restituisce null

 (CELLSJAVA-41407) - Codice VBA in .xlsb perso dopo il salvataggio

(CELLSJAVA-41396) - Il calcolo delle formule non funziona quando abbiamo più di 65536 celle denominate

 (CELLSJAVA-41389) - L'abilitazione di ShowTotal per ListObject inserisce una riga vuota sopra il totale

 (CELLSJAVA-41388) - La funzione TREND di Excel non è in grado di calcolare utilizzando CalculateFormula

 (CELLSJAVA-41379) - Colori delle schede persi dopo aver salvato nuovamente l'XLSB

 (CELLSJAVA-41370) - Quando si crea un'istanza di una cartella di lavoro con un documento Excel danneggiato e LoadOptions, si verifica un blocco

 (CELLSJAVA-41411) - Strana sostituzione dei caratteri durante l'aggiornamento a 8.5.0 da 8.4.x

 (CELLSJAVA-41410) - Problema relativo al colore dell'immagine nella trasformazione da Excel a PDF

 (CELLSJAVA-41406) - La casella di testo sul grafico viene spostata dopo il rendering del foglio di calcolo in PDF

 (CELLSJAVA-41403) - Fonte: la sostanza chimica è sovrascritta dal bordo della carta in PDF

 (CELLSJAVA-41402) - Fonte: la sostanza chimica è sovrascritta dal bordo del grafico in PNG

 (CELLSJAVA-41387) - Le etichette dei dati vengono sovrascritte dalla sezione dell'intestazione

 (CELLSJAVA-41380) - La conversione da grafico a immagine/PDF non esporta la casella di testo contenuta in modalità di licenza

(CELLSJAVA-41244) - Gli indicatori e le frecce non appaiono bene o sono sfigurati

 (CELLSJAVA-40929) - Le parole in una casella di testo non hanno spazi tra loro all'interno del pdf di output


## **Eccezioni**


 (CELLSJAVA-41405) - Eccezione: java.lang.ArrayIndexOutOfBoundsException sul metodo Workbook.save()

 (CELLSJAVA-41399) - CellsException all'apertura del file xlsb di origine

 (CELLSJAVA-41391) - CELLSJAVA-41225 ArrayIndexOutOfBoundsException si verifica nella versione 8.5.0

 (CELLSJAVA-41383) - java.lang.ArrayIndexOutOfBoundsException: 42, in Workbook.save

 (CELLSJAVA-41408) - CellsException: errore da forma a immagine! durante la conversione del foglio di calcolo in PDF


## **Pubblico API e modifiche incompatibili con le versioni precedenti**


 Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.



 Aggiunge enum TableDataSourceType e ListObject.DataSourceType

 Viene utilizzato per ottenere il tipo di origine dati della tabella.



 Aggiunge il metodo Workbook.Dispose().

 Viene utilizzato per rilasciare risorse non gestite.



 Aggiunge il metodo Cell.GetHeightOfValue().

 Viene utilizzato per ottenere l'altezza del valore in unità di pixel.





 Nota

Poiché la base di codice di Aspose.Cells for Java corrisponde al codice della versione .NET pertinente, la maggior parte delle modifiche, miglioramenti e correzioni inclusi in Aspose.Cells for .NET v8.5.1 sono inclusi anche in questo Aspose.Cells for Java v8.5.1.
