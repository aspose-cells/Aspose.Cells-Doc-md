---
title: Filtra gli oggetti durante il caricamento della cartella di lavoro o del foglio di lavoro
type: docs
weight: 1060
url: /it/java/filter-objects-while-loading-workbook-or-worksheet/
---
## **Possibili scenari di utilizzo**
 Si prega di utilizzare[LoadOptions.LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#LoadFilter) property durante il filtraggio dei dati dalla cartella di lavoro. Ma se vuoi filtrare i dati da singoli fogli di lavoro, dovrai eseguire l'override[LoadFilter.startSheet](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#startSheet\(com.aspose.cells.Worksheet\) ) metodo. Si prega di fornire il valore appropriato da[LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) enumerazione durante la creazione o l'utilizzo[Carica filtro](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter).

 Il[LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions)enumerazione ha i seguenti valori.

- [NESSUNO](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#NONE)
- [TUTTO](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#ALL)
- [CELLA_VUOTO](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BLANK)
- [CELL_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_STRING)
- [CELL_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_NUMERIC)
- [CELL_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_ERROR)
- [CELL_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BOOL)
- [CELL_VALUE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_VALUE)
- [FORMULA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#FORMULA)
- [DATI_CELLA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_DATA)
- [GRAFICO](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CHART)
- [FORMA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE)
- [UNIONE_AREA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#MERGED_AREA)
- [FORMATTAZIONE CONDIZIONALE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CONDITIONAL_FORMATTING)
- [CONVALIDA DEI DATI](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DATA_VALIDATION)
- [TABELLA PIVOT](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#PIVOT_TABLE)
- [TAVOLO](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#TABLE)
- [COLLEGAMENTI IPERTESTUALI](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#HYPERLINKS)
- [IMPOSTAZIONI_FOGLIO](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_SETTINGS)
- [FOGLIO_DATI](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_DATA)
- [IMPOSTAZIONI_LIBRO](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#BOOK_SETTINGS)
- [IMPOSTAZIONI](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SETTINGS)
- [XML_MAP](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#XML_MAP)
- [STRUTTURA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STRUCTURE)
- [PROPRIETÀ_DOCUMENTO](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DOCUMENT_PROPERTIES)
- [DEFINED_NAMES](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)
- [VBA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#VBA)
- [STILE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STYLE)
## **Filtra oggetti durante il caricamento della cartella di lavoro**
 Il codice di esempio seguente illustra come filtrare i grafici dalla cartella di lavoro. Si prega di controllare[file excel di esempio](5472489.xlsx) utilizzato in questo codice e il[uscita PDF](5472488.pdf)generato da esso. Come puoi vedere nell'output PDF, tutti i grafici sono stati filtrati dalla cartella di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilterObjectsLoadingWorkbook-FilterObjectsLoadingWorkbook.java" >}}
## **Filtra oggetti durante il caricamento del foglio di lavoro**
 Il codice di esempio seguente carica il file[file excel di origine](5472492.xlsx) e filtra i seguenti dati dai fogli di lavoro utilizzando un filtro personalizzato.

- Filtra i grafici dal foglio di lavoro denominato NoCharts.
- Filtra le forme dal foglio di lavoro denominato NoShapes.
- Filtra la formattazione condizionale dal foglio di lavoro denominato NoConditionalFormatting.

 Una volta, carica il file[file excel di origine](5472492.xlsx) con un filtro personalizzato, prende le immagini di tutti i fogli di lavoro uno per uno. Ecco le immagini di output per riferimento. Come puoi vedere, la prima immagine non ha grafici, la seconda immagine non ha forme e la terza immagine non ha formattazione condizionale.

- [NoCharts.png](5472493.png)
- [NoShapes.png](5472491.png)
- [NoConditionalFormatting.png](5472490.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterObjectsLoadingWorksheets-1.java" >}}
