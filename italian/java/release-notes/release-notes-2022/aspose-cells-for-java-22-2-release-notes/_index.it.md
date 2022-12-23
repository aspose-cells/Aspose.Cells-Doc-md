---
title: Aspose.Cells for Java 22.2 Note di rilascio
type: docs
weight: 11
url: /it/java/aspose-cells-for-java-22-2-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 22.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-22.2/).

{{% /alert %}}

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-44317|Il testo in questo xlsx è confuso|
|CELLSJAVA-44271|Quando si converte Excel in PDF, la posizione di output si sposta rispetto al caso della conversione manuale|
|CELLSJAVA-44197|Durante la conversione da XLSX a PDF, la forma della sequenza temporale della tabella pivot (finestra) non viene visualizzata|
|CELLSJAVA-44267|La cartella di lavoro contenente una tabella pivot viene danneggiata|
|CELLSJAVA-44114|Da XLSX a PDF: i dati nel formato numero scientifico del file XLSX non corrispondono ai dati nel file di output PDF|
|CELLSJAVA-44293|Il file Excel salvato di nuovo deve essere recuperato quando lo si apre in MS Excel|
|CELLSJAVA-43194|Immagini visualizzate in modo errato|
|CELLSJAVA-44243|Il file di salvataggio della demo primaverile di GridWeb non è riuscito in jdk1.8|
|CELLSJAVA-44276|mancata corrispondenza dell'altezza dell'intestazione di riga con il contenuto della riga dopo la modifica della cella per il file 249.xls|
|CELLSJAVA-44284|sollevare un'eccezione di memoria insufficiente per il file bug.xlsx|
|CELLSJAVA-44229|La formula viene persa quando il contenuto td viene avvolto dal tag div|
|CELLSJAVA-44247|Il testo a riga singola viene avvolto durante la conversione in pdf|
|CELLSJAVA-44175| problema con le etichette del grafico a ciambella sovrapposte|
|CELLSJAVA-44192|Il nome dell'elemento dell'asse delle categorie nel grafico è tagliato in Excel alla conversione PDF|
|CELLSJAVA-44233|Ciclo infinito durante la conversione del file XLSX|
|CELLSJAVA-44263|L'impostazione della direzione del testo dell'etichetta del grafico su verticale non ha effetto|
|CELLSJAVA-44268| Eccezione "java.lang.NullPointerException" sul metodo Chart.toPdf|
|CELLSJAVA-44302|La direzione del testo dell'asse delle coordinate è errata dopo che il file Excel è stato convertito in HTML|
|CELLSJAVA-44314|Etichette dell'asse delle categorie del grafico errate nel rendering dal grafico all'immagine|
|CELLSJAVA-44274|Il formato SVG è supportato per la lettura o il rendering in PDF|
|CELLSJAVA-44311|Eccezione "java.lang.OutOfMemoryError: Java spazio heap" durante il rendering nel formato file HTML|
|CELLSJAVA-44285|Eccezione "java.lang.ClassCastException: impossibile eseguire il cast di com.aspose.cells.n2f su com.aspose.cells.o90" quando si chiama Workbook.calculateFormula()|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Metodo Cells.AddAddInFunction() obsoleto.**

Utilizzare invece i metodi WorksheetCollection.RegisterAddInFunction().

### **Aggiunge il metodo NameCollection.Filter() e l'enumerazione NameScopeType.**

Ottiene i nomi definiti in base all'ambito.

### **Aggiunge l'enumerazione MsoDrawingType.Timeline.**

Rappresenta il tipo di oggetti di disegno della linea temporale.
