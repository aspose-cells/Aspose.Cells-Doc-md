---
title: Importare ed esportare dati
type: docs
weight: 130
url: /it/java/import-and-export-data/
---
{{% alert color="primary" %}}

Questo articolo illustra alcune tecniche di importazione ed esportazione dei dati a cui gli sviluppatori hanno accesso tramite Aspose.Cells.

{{% /alert %}}

## Importa i dati nel foglio di lavoro

I dati rappresentano il mondo così com'è. Per dare un senso ai dati, li analizziamo e acquisiamo una comprensione del mondo. I dati si trasformano in informazioni.

Esistono molti modi per eseguire l'analisi: inserire i dati in fogli di calcolo e manipolarli in modi diversi è un metodo comune. Con Aspose.Cells, è facile creare fogli di calcolo che prendono i dati da una serie di fonti esterne e li preparano per l'analisi.

Questo articolo discute alcune tecniche di importazione dei dati a cui gli sviluppatori hanno accesso tramite Aspose.Cells.

### Importazione dei dati utilizzando Aspose.Cells

Quando apri un file Excel con Aspose.Cells, tutti i dati nel file vengono importati automaticamente. Aspose.Cells può anche importare dati da altre fonti di dati:

- [Vettore](/cells/it/java/import-and-export-data/).
- [Lista di array](/cells/it/java/import-and-export-data/).
- [Insieme di risultati](/cells/it/java/import-and-export-data/).
- [JSON](/cells/it/java/import-and-export-data/)

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , che rappresenta un file Excel Microsoft. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class contiene la raccolta[**Raccolta di fogli di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) collezione.[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)collection fornisce metodi molto utili per importare dati da altre fonti di dati. Questo articolo spiega come utilizzare questi metodi.

#### Importazione dall'array

 Per importare dati in un foglio di calcolo da un array, chiama il metodo importArray di[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)collezione. Esistono molte versioni di overload del metodo importArray, ma un tipico overload accetta i seguenti parametri:

- **Vettore**, l'oggetto array da cui stai importando il contenuto.
- **Numero di riga**il numero di riga della prima cella in cui verranno importati i dati.
- **Numero di colonna**, il numero di colonna della prima cella in cui verranno importati i dati.
- **È verticale**, un valore booleano che specifica se importare i dati verticalmente o orizzontalmente.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArray-ImportingFromArray.java" >}}

#### Importazione da array multidimensionali

 Per importare dati in un foglio di calcolo da matrici multidimensionali, chiama l'overload importArray pertinente del metodo[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)collezione:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromMultiDimensionalArray-ImportingFromMultiDimensionalArray.java" >}}

#### Importazione da un ArrayList

 Per importare i dati da un file*Lista di array* ai fogli di lavoro, chiamare il[**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean) ) metodo del[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) collezione. Il[**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean)) accetta i seguenti parametri:

- **Lista di array** , il*Lista di array*oggetto il cui contenuto verrà importato.
- **Numero riga**, il numero di riga della prima cella dell'intervallo di celle da cui verranno importati i contenuti.
- **Numero di colonna**, il numero di colonna della prima cella da cui verranno importati i dati.
- **è verticale**è un valore booleano che specifica se importare i dati verticalmente o orizzontalmente.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### Importazione da oggetti personalizzati nell'area unita

Per importare dati da una raccolta di oggetti in un foglio di lavoro contenente celle unite, utilizzare[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)proprietà. Se il modello di Excel ha celle unite, impostare il valore di[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)proprietà su true. Passa il[**ImportTableOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImportTableOptions)oggetto insieme all'elenco di colonne/proprietà al metodo per visualizzare l'elenco di oggetti desiderato. L'esempio di codice seguente illustra l'utilizzo di[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)proprietà per importare i dati dagli oggetti personalizzati alle celle unite. Per favore vedere l'allegato[fonte Excel](90112035.xlsx)file e il[uscita Excel](90112036.xlsx)file per riferimento.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### Importazione dati da JSON

 Aspose.Cells fornisce a[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) classe per l'elaborazione JSON.[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) la classe ha un[**Importa dati**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions) ) metodo per l'importazione dei dati JSON. Aspose.Cells fornisce anche a[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)classe che rappresenta le opzioni del layout JSON. Il[**Importa dati**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions) ) metodo accetta[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) come parametro. Il[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) class fornisce le seguenti proprietà.

- [**ArrayComeTabella**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable): indica che l'array deve essere elaborato come tabella o meno.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ConvertNumericOrDate): Ottiene o imposta un valore che indica se la stringa in JSON deve essere convertita in numerico o data.
- [**Formato data**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#DateFormat): Ottiene e imposta il formato del valore della data.
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle): Indica se ignorare il titolo se la proprietà dell'oggetto è un array
- [**IgnoraNull**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreNull): Indica se il valore null deve essere ignorato o meno.
- [**IgnoraTitoloOggetto**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreObjectTitle): Indica se ignorare il titolo se la proprietà dell'oggetto è un oggetto.
- [**NumeroFormato**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#NumberFormat): Ottiene e imposta il formato del valore numerico.
- [**TitleStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#TitleStyle): Ottiene e imposta lo stile del titolo.

 Il codice di esempio fornito di seguito illustra l'uso di[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) e[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) classi per importare i dati JSON.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportingFromJson-1.java" >}}

## Esporta dati dal foglio di lavoro

Aspose.Cells non solo consente ai suoi utenti di importare dati in fogli di lavoro da fonti di dati esterne, ma consente anche loro di esportare i dati del foglio di lavoro in un array.

### Esportazione dei dati tramite Aspose.Cells - Esportazione dei dati nell'array

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , che rappresenta un file Excel Microsoft. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la classe contiene un[**Raccolta di fogli di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) che consente l'accesso a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la classe fornisce a[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) collezione.

 I dati possono essere facilmente esportati in un oggetto Array utilizzando il file[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) classe'[**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int)) metodo.

#### Colonne contenenti dati fortemente tipizzati

 I fogli di calcolo memorizzano i dati come una sequenza di righe e colonne. Usa il[**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int) ) per esportare i dati da un foglio di lavoro a un array.[**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int) ) accetta i seguenti parametri per esportare i dati del foglio di lavoro come file*Vettore* oggetto:

- Numero di riga, il numero di riga della prima cella da cui verranno esportati i dati.
- Numero di colonna, il numero di colonna della prima cella da cui verranno esportati i dati
- Numero di righe, il numero di righe da esportare.
- Numero di colonne, il numero di colonne da esportare.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ExportingDataFromWorksheets-1.java" >}}

## **Argomenti avanzati**
- [Importa dati dall'oggetto ResultSet del database di accesso Microsoft al foglio di lavoro](/cells/it/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/)
- [Specificare i campi formula durante l'importazione dei dati nel foglio di lavoro](/cells/it/java/specify-formula-fields-while-importing-data-to-worksheet/)
