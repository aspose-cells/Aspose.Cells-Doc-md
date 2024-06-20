---
title: Importa ed esporta dati
type: docs
weight: 130
url: /it/java/import-and-export-data/
---

{{% alert color="primary" %}}

Questo articolo discute alcune tecniche di importazione ed esportazione dati a cui i programmatori hanno accesso tramite Aspose.Cells.

{{% /alert %}}

## Importa Dati nel Foglio di Lavoro

I dati rappresentano il mondo così com'è. Per dare un senso ai dati, li analizziamo e acquisiamo una comprensione del mondo. I dati si trasformano in informazioni.

Ci sono molti modi di effettuare analisi: inserire dati nei fogli di calcolo e manipolarli in modi diversi è un metodo comune. Con Aspose.Cells, è facile creare fogli di calcolo che prelevano dati da una serie di fonti esterne e li preparano per l'analisi.

Questo articolo discute alcune tecniche di importazione dati a cui i programmatori hanno accesso attraverso Aspose.Cells.

### Importare Dati Utilizzando Aspose.Cells

Quando si apre un file Excel con Aspose.Cells, tutti i dati nel file vengono automaticamente importati. Aspose.Cells può anche importare dati da altre fonti di dati:

- [Matrice](/cells/it/java/import-and-export-data/).
- [Elenco di array](/cells/it/java/import-and-export-data/).
- [Set di risultati](/cells/it/java/import-and-export-data/).
- [JSON](/cells/it/java/import-and-export-data/)

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene la raccolta [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fornisce una raccolta [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells). La raccolta [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) fornisce metodi molto utili per l'importazione di dati da altre fonti di dati. Questo articolo spiega come possono essere utilizzati questi metodi.

#### Importazione da Array

Per importare dati in un foglio di calcolo da una matrice, chiamare il metodo importArray della raccolta [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells). Ci sono molte versioni sovraccaricate del metodo importArray ma una sovraccarica tipica richiede i seguenti parametri:

- **Array**, l'oggetto array da cui si sta importando il contenuto.
- **Numero di riga**, il numero di riga della prima cella in cui saranno importati i dati.
- **Numero di colonna**, il numero di colonna della prima cella in cui saranno importati i dati.
- **È verticale**, un valore booleano che specifica se importare i dati verticalmente o orizzontalmente.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArray-ImportingFromArray.java" >}}

#### Importazione da Matrici Multidimensionali

Per importare dati in un foglio di calcolo da matrici multidimensionali, chiamare il sovraccarico di importArray rilevante della raccolta [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells):

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromMultiDimensionalArray-ImportingFromMultiDimensionalArray.java" >}}

#### Importazione da un ArrayList

Per importare dati da un *ArrayList* ai fogli di lavoro, chiamare il metodo [**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean)) della raccolta [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells). Il metodo [**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean)) richiede i seguenti parametri:

- **ArrayList**, l'oggetto *ArrayList* i cui contenuti verranno importati.
- **Numero di riga**, il numero di riga della prima cella del campo da cui verranno importati i contenuti.
- **Numero Colonna**, il numero di colonna della prima cella da cui verranno importati i dati.
- **È Verticale**, è un valore booleano che specifica se importare i dati verticalmente o orizzontalmente.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### Importare da oggetti personalizzati in un'area unita

Per importare dati da una raccolta di oggetti in un foglio contenente celle unite, utilizzare la proprietà [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells). Se il modello Excel ha celle unite, impostare il valore della proprietà [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells) su true. Passare l'oggetto [**ImportTableOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImportTableOptions) insieme alla lista di colonne/proprietà al metodo per visualizzare l'elenco desiderato di oggetti. Il seguente esempio di codice dimostra l'uso della proprietà [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells) per importare dati da oggetti personalizzati in celle unite. Si prega di fare riferimento al file Excel [sorgente](90112035.xlsx) allegato e al file Excel [output](90112036.xlsx) per ulteriori informazioni.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### Importazione di dati da JSON

Aspose.Cells fornisce una classe [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) per l'elaborazione di JSON. La classe [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) ha un metodo [**ImportData**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions)) per l'importazione di dati JSON. Aspose.Cells fornisce anche una classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) che rappresenta le opzioni della struttura JSON. Il metodo [**ImportData**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions)) accetta [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) come parametro. La classe [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) fornisce le seguenti proprietà.

- [**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable): Indica se l'array deve essere elaborato come una tabella o meno.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ConvertNumericOrDate): Ottiene o imposta un valore che indica se la stringa in JSON deve essere convertita in un valore numerico o in una data.
- [**DateFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#DateFormat): Ottiene e imposta il formato del valore della data.
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle): Indica se ignorare o meno il titolo se la proprietà dell'oggetto è un array.
- [**IgnoreNull**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreNull): Indica se il valore nullo deve essere ignorato o meno.
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreObjectTitle): Indica se ignorare o meno il titolo se la proprietà dell'oggetto è un oggetto.
- [**NumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#NumberFormat): Ottiene e imposta il formato del valore numerico.
- [**TitleStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#TitleStyle): Ottiene e imposta lo stile del titolo.

Il codice di esempio riportato di seguito illustra l'uso delle classi [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) e [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) per importare dati JSON.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportingFromJson-1.java" >}}

## Esportare dati dal foglio di lavoro

Aspose.Cells non solo consente ai suoi utenti di importare dati nei fogli di lavoro da origini di dati esterne ma consente anche di esportare i dati del foglio di lavoro in un array.

### Esportazione dei dati utilizzando Aspose.Cells - Esportazione dei dati in un array

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fornisce una raccolta [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells).

I dati possono essere facilmente esportati in un oggetto Array utilizzando il metodo [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int)) della classe [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells).

#### Colonne contenenti dati fortemente tipizzati

I fogli elettronici memorizzano i dati come una sequenza di righe e colonne. Usa il metodo [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int)) per esportare i dati da un foglio di lavoro in un array. [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int)) richiede i seguenti parametri per esportare i dati del foglio di lavoro come oggetto *Array*:

- Numero di riga, il numero di riga della prima cella da cui verranno esportati i dati.
- Numero di colonna, il numero di colonna della prima cella da cui verranno esportati i dati.
- Numero di righe, il numero di righe da esportare.
- Numero di colonne, il numero di colonne da esportare.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ExportingDataFromWorksheets-1.java" >}}

## **Argomenti avanzati**
- [Importazione dati da un oggetto ResultSet del database Microsoft Access nel foglio di lavoro](/cells/it/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/)
- [Specifica i campi di formula durante l'importazione dei dati nel foglio di lavoro.](/cells/it/java/specify-formula-fields-while-importing-data-to-worksheet/)
