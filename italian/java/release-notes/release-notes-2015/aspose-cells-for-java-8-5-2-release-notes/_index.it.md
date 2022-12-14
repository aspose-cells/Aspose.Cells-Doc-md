---
title: Aspose.Cells for Java 8.5.2 Note di rilascio
type: docs
weight: 30
url: /it/java/aspose-cells-for-java-8-5-2-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 8.5.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.5.2/)

{{% /alert %}} 

 Di seguito è riportato un elenco di miglioramenti e modifiche in questa versione di Aspose.Cells



\1) Aspose.Cells 


## **Altri miglioramenti e modifiche**

## **Nuove caratteristiche**


 (CELLSJAVA-41374) - Aggiunta della costante "Distinct Count" alla classe ConsolidationFunction nelle tabelle pivot


## **Miglioramenti**


 (CELLSJAVA-41373) - Mancata corrispondenza nelle impostazioni di allineamento dopo il salvataggio del file Excel nel formato file HTML


## **Insetti**


 (CELLSJAVA-41332) - AttachedFilesDirectory e AttachedFilesUrlPrefix non funzionano correttamente

 (CELLSJAVA-41303) - PivotField.IsRepeatItemLabels non funziona nella tabella pivot

 (CELLSJAVA-41430) - L'opzione Unisci e centra è stata selezionata anche se ha una singola cella

 (CELLSJAVA-41429) - Le impostazioni di compatibilità Lotus per l'immissione della formula di transizione vengono modificate dopo aver salvato nuovamente il foglio di calcolo

 (CELLSJAVA-41427) - Troppe convalide Cells danneggia il file XLS

(CELLSJAVA-41424) - L'utilizzo della funzione personalizzata tramite l'interfaccia ICustomFunction non calcola il valore corretto

 (CELLSJAVA-41423) - Layout errato durante il rendering di PDF da un file ODS

 (CELLSJAVA-41422) - Cells.copyRows con formattazione condizionale nelle celle causa un aumento delle dimensioni del file e problemi di prestazioni

 (CELLSJAVA-41419) - OutOfMemoryError, Aspose.Cells trattiene milioni di celle per sempre

 (CELLSJAVA-41395) - Conversione da ODS a HTML - Problemi di stile del testo

 (CELLSJAVA-41426) - Cell grafico con asse x non ridimensionato correttamente durante la conversione in pdf

 (CELLSJAVA-41421) - L'ultima parola nella casella di testo del grafico passa alla riga successiva

 (CELLSJAVA-41416) - Valore del problema di divisione durante il nuovo salvataggio del foglio di calcolo con Aspose.Cells

 (CELLSJAVA-41387) - Le etichette dei dati vengono sovrascritte dalla sezione dell'intestazione


## **Pubblico API e modifiche incompatibili con le versioni precedenti**


 Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.





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





 Nota

 Poiché la base di codice di Aspose.Cells for Java corrisponde al codice della versione .NET pertinente, la maggior parte delle modifiche, miglioramenti e correzioni inclusi in Aspose.Cells for .NET v8.5.2 sono inclusi anche in questo Aspose.Cells for Java v8.5.2.
