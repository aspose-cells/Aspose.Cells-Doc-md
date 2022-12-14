---
title: Aspose.Cells for .NET 22.2 Note di rilascio
type: docs
weight: 11
url: /it/net/aspose-cells-for-net-22-2-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 22.2](https://www.nuget.org/packages/Aspose.Cells/22.2.0).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-50332| Estrai tutte le NameCollections di un particolare foglio di lavoro|
|CELLSNET-50353|Aggiungere la proprietà StandardHeightInch nella classe Cells|
|CELLSNET-50152| Vari problemi di formattazione e di rendering di altre forme in PDF e HTML di file Excel|
|CELLSNET-50300|Alcune forme non vengono visualizzate correttamente nella conversione da Excel a PDF|
|CELLSNET-50301|Valore non valido per riferimento esterno nel campo DataSource della tabella pivot|
|CELLSNET-50241|Regressione: la conversione da CSV a PDF non funziona|
|CELLSNET-50268|Array CellsArea vuoto restituito per i file CSV/TSV|
|CELLSNET-50269|Lingua finlandese: i numeri formattati come percentuale non contengono lo spazio prima del simbolo di percentuale|
|CELLSNET-50333|Aspose.cell non è riuscito a raccogliere i registri di revisione della cartella di lavoro|
|CELLSNET-50239|Pagina mancante dopo la conversione di un file Excel in PDF|
|CELLSNET-50255|Il tipo Cell è errato dopo l'esportazione in html e il ricaricamento dell'html esportato|
|CELLSNET-50266|Chart.ToImage() Problema di sicurezza del thread|
|CELLSNET-50302|Regressione: la conversione in numeri HTML non è stata resa correttamente|
|CELLSNET-50328|Cell lo sfondo diventa nero dopo la conversione in pdf|
|CELLSNET-50225|La legenda del grafico viene ripristinata durante il salvataggio di Excel in PDF|
|CELLSNET-50247|Inserendo righe nel foglio, le serie dei grafici perdono i loro Xvalori|
|CELLSNET-50295|Chart.SetChartDataRange(area, false) non riconosce le celle unite|
|CELLSNET-50308|Intervallo a PNG: output non come previsto|
|CELLSNET-50240| Gli oggetti OLE non protetti su un foglio protetto diventano protetti dopo il salvataggio|
|CELLSNET-50273|Rileva il formato del file del file html speciale|
|CELLSNET-50294|I pulsanti di controllo ActiveX vengono convertiti in forme e il file viene danneggiato per XLS in XLSM e quindi di nuovo in XLS|
|CELLSNET-50340|Righe di colonna della tabella mancanti durante la conversione di file specifici in HTML|
|CELLSNET-50286|Cells.RemoveDuplicates genera "System.IndexOutOfRangeException: l'indice era al di fuori dei limiti dell'array"|
|CELLSNET-50270|La stringa di input non era in un formato corretto. eccezione quando si apre il file XLS|
|CELLSNET-50271|Il formato di questo file non è supportato o non hai specificato un formato corretto. eccezione quando si apre il file XLS|
|CELLSNET-50293|ExportXml con XML Map genera "NullReferenceException" per un altro file complesso|
|CELLSNET-50352|NullReferenceException durante la conversione del file XLSM in XLS|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Metodo Cells.AddAddInFunction() obsoleto.**

Utilizzare invece i metodi WorksheetCollection.RegisterAddInFunction().

### **Aggiunge il metodo NameCollection.Filter() e l'enumerazione NameScopeType.**

Ottiene i nomi definiti in base all'ambito.

### **Aggiunge l'enumerazione MsoDrawingType.Timeline.**

Rappresenta il tipo di oggetti di disegno della linea temporale.
