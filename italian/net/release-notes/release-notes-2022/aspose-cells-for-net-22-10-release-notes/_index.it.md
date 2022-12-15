---
title: Aspose.Cells for .NET 22.10 Note di rilascio
type: docs
weight: 3
url: /it/net/aspose-cells-for-net-22-10-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 22.10](https://www.nuget.org/packages/Aspose.Cells/22.10.0).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-42037|Il filtro della sequenza temporale della tabella pivot scompare dopo il caricamento del documento Excel e l'aggiornamento|
|CELLSNET-51963|Supporto per file CRTX|
|CELLSNET-51952|Le formule MAXIFS richiedono molto tempo per essere calcolate|
|CELLSNET-52064|Non è consentito spingere le celle non vuote oltre la fine dell'errore del foglio di lavoro quando si utilizza il metodo Cells.InsertRows|
|CELLSNET-52029|Traduci le etichette delle voci della legenda in base alle impostazioni locali/regionali|
|CELLSNET-51419|Il collegamento esterno della tabella pivot è stato eliminato durante la conversione del file XLS in XLSM|
|CELLSNET-51984|Il file XLSX con il file della tabella pivot è danneggiato dopo il nuovo salvataggio|
|CELLSNET-51987|Problema con alcuni indicatori intelligenti (inseriti) nella tabella pivot e nel grafico pivot|
|CELLSNET-52065|Connessioni dati esterne errate durante la conversione di connessioni esterne|
|CELLSNET-52088| Una riga aggiuntiva viene aggiunta durante la creazione di una tabella pivot classica|
|CELLSNET-52018| GetValidationValue non corretto utilizzando l'operatore NotBetween|
|CELLSNET-52069|I valori decimali nel risultato di Cell.Formula possono essere diversi da quelli mostrati da ms excel|
|CELLSNET-52078|Style.SetPatternColor(BackgroundType,Color,Color) non ha effetto|
|CELLSNET-52105|LightCellsDataHandler.StartSheet(Worksheet) non può saltare il foglio quando restituisce false per il file modello xlsb|
|CELLSNET-46764|Titolo del grafico mancante durante la conversione in pdf|
|CELLSNET-52049|Da XLSX a PDF: testo non formattato correttamente|
|CELLSNET-52073|Problema relativo al carattere Arial Tur nel rendering da Excel a PDF|
|CELLSNET-52083|Alcune celle con il formato Numero contabile vengono visualizzate come #####.|
|CELLSNET-52091|Quando si imposta il contenuto del foglio di lavoro in bianco e nero, viene comunque stampato a colori e i bordi vengono visualizzati inutilmente|
|CELLSNET-51972|Il foglio di lavoro contenente oggetti pulsante non viene riconosciuto correttamente durante la copia del foglio|
|CELLSNET-51973| Tabella HTML in foglio Excel non convertita correttamente|
|CELLSNET-52001|Il nuovo salvataggio di un file XLSX ha generato un file corrotto|
|CELLSNET-52015|Impossibile caricare la formula della query avanzata dal file Excel|
|CELLSNET-52054| Corruzione dello stile dopo il salvataggio e la riapertura di una cartella di lavoro generata da Aspose.Cells|
|CELLSNET-52056| Problema di duplicazione del collegamento ipertestuale|
|CELLSNET-52071| Conversione da Excel a XML: i nomi degli elementi non sono sfuggiti|
|CELLSNET-52074|Da HTML a XLSX: contenuto della cella mancante|
|CELLSNET-52084|La posizione del testo "Northwind Traders" non è corretta (il valore del rientro sinistro non è interpretato correttamente).|
|CELLSNET-52063|PivotTable.CalculateData ha causato NullReferenceException|
|CELLSNET-51986|Il calcolo della cartella di lavoro due volte con la catena di calcolo abilitata ha causato un'eccezione|
|CELLSNET-52081|L'apertura di un file XLSX i cui stili sono stati rimossi genera un'eccezione|
|CELLSNET-52044|Eccezione sollevata durante l'importazione del file del cliente in GridWeb|
|CELLSNET-52002|Viene generata un'eccezione quando si tenta di aprire un documento non protetto con una password|

## **API pubblica e modifiche non compatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.

### **Modificato il limite di spostamento delle celle fuori dal foglio per l'inserimento di righe**

Nelle vecchie versioni, se ci sono celle che hanno impostazioni di formattazione ma non hanno valore e verranno spostate fuori dal foglio, l'operazione di inserimento non è consentita. Dal 22.10, l'operazione di inserimento è consentita per questo tipo di situazione e tale comportamento è lo stesso con ms excel ora.

### **Aggiunge la classe DataModelConnection**

Specifica una connessione al modello di dati.

### **Aggiunge i metodi Chart.ChangeTemplate(byte[]).**

Modifica il tipo di grafico con il file modello preimpostato.

### **Aggiunge il metodo ChartCollection.Add(byte[] data, string dataRange, bool isVertical, int topRow, int leftColumn,int rightRow, int bottomColumn).**

Aggiunge grafico con file modello preimpostato.
