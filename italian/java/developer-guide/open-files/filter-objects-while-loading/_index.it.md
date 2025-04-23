---
title: Filtra gli Oggetti durante il caricamento del Workbook o del Foglio di Lavoro
type: docs
weight: 1060
url: /it/java/filter-objects-while-loading-workbook-or-worksheet/
---

## **Possibili Scenari di Utilizzo**
Si prega di usare la proprietà [LoadOptions.LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#LoadFilter) durante il filtraggio dei dati dal workbook. Ma se si desidera filtrare i dati da fogli di lavoro singoli, allora sarà necessario sovrascrivere il metodo [LoadFilter.startSheet](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#startSheet-com.aspose.cells.Worksheet-). Fornisci il valore appropriato dall'enumerazione [LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) mentre crei o lavori con [LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter).

L'enumerazione [LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) ha i seguenti valori.

- [NESSUNO](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#NONE)
- [TUTTI](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#ALL)
- [CELLA_VUOTA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL-BLANK)
- [CELLA_STRINGA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL-STRING)
- [CELLA_NUMERICA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL-NUMERIC)
- [CELLA_ERRORE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL-ERROR)
- [CELLA_BOOLEANA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL-BOOL)
- [VALORE_CELLA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL-VALUE)
- [FORMULA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#FORMULA)
- [DATI_CELLA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL-DATA)
- [GRAFICO](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CHART)
- [FORMA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE)
- [AREA_UNITA_FUSIONATA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#MERGED-AREA)
- [FORMATTAZIONE_CONDIZIONALE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CONDITIONAL-FORMATTING)
- [VALIDAZIONE_DATI](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DATA-VALIDATION)
- [TAB_PIVOT](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#PIVOT-TABLE)
- [TAB_LAVORO](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#TABLE)
- [COLLEGAMENTI_IPERTESTUALI](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#HYPERLINKS)
- [IMPOSTAZIONI_SHEET](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET-SETTINGS)
- [DATI_SHEET](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET-DATA)
- [IMPOSTAZIONI_BOOK](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#BOOK-SETTINGS)
- [IMPOSTAZIONI](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SETTINGS)
- [XML_MAP](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#XML-MAP)
- [STRUTTURA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STRUCTURE)
- [PROPRIETA_DOCUMENTO](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DOCUMENT-PROPERTIES)
- [NOMI_DEFINITI](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED-NAMES)
- [VBA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#VBA)
- [STILE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STYLE)
## **Filtra oggetti durante il caricamento del workbook**
Il seguente codice di esempio illustra come filtrare i grafici dal workbook. Si prega di controllare il [file excel di esempio](5472489.xlsx) utilizzato in questo codice e il [PDF di output](5472488.pdf) generato da esso. Come si può vedere nel PDF di output, tutti i grafici sono stati filtrati dal workbook.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilterObjectsLoadingWorkbook-FilterObjectsLoadingWorkbook.java" >}}
## **Filtra oggetti durante il caricamento del foglio di lavoro**
Il seguente codice di esempio carica il [file excel di origine](5472492.xlsx) e filtra i seguenti dati dai suoi fogli di lavoro utilizzando un filtro personalizzato.

- Filtra i Grafici dalla cartella di lavoro denominata NoCharts.
- Filtra le Forme dalla cartella di lavoro denominata NoShapes.
- Filtra la formattazione condizionale dalla cartella di lavoro denominata NoConditionalFormatting.

Una volta caricato il [file excel di origine](5472492.xlsx) con un filtro personalizzato, vengono prese le immagini di tutte le cartelle di lavoro una per una. Ecco le immagini di output per il tuo riferimento. Come puoi vedere, la prima immagine non contiene grafici, la seconda immagine non contiene forme e la terza immagine non ha la formattazione condizionale.

- [NoCharts.png](5472493.png)
- [NoShapes.png](5472491.png)
- [NoConditionalFormatting.png](5472490.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterObjectsLoadingWorksheets-1.java" >}}
{{< app/cells/assistant language="java" >}}
