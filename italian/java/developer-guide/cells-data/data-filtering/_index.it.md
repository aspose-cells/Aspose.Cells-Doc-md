---
title: Filtraggio dei dati
type: docs
weight: 60
url: /it/java/data-filtering/
---
{{% alert color="primary" %}}

Microsoft Excel offre alcune buone funzionalità per filtrare automaticamente i dati del foglio di lavoro. Aspose.Cells supporta completamente le funzionalità di filtro automatico di Microsoft Excel. Questo articolo spiega come utilizzare le funzionalità in Microsoft Excel e come codificarle utilizzando Aspose.Cells.

{{% /alert %}}

## **Dati filtro automatico**

Il filtro automatico è il modo più rapido per selezionare dal foglio di lavoro solo gli elementi che si desidera visualizzare in un elenco. La funzione di filtro automatico consente agli utenti di filtrare gli elementi in un elenco in base a criteri impostati. Filtra in base a testo, numeri o date.

### **Filtro automatico in Microsoft Excel**

Per attivare la funzione di filtro automatico in Microsoft Excel:

1. Fare clic sulla riga dell'intestazione in un foglio di lavoro.
1. Dal**Dati**menù, selezionare**Filtro**poi**Filtro automatico**.

Quando applichi un filtro automatico a un foglio di lavoro, i parametri del filtro (frecce nere) vengono visualizzati a destra delle intestazioni di colonna.

1. Fare clic sulla freccia di un filtro per visualizzare un elenco di opzioni di filtro.

Alcune delle opzioni di filtro automatico sono:

|**Opzioni**|**Descrizione**|
|:- |:- |
|Tutto|Mostra tutti gli elementi nell'elenco una volta.|
|Costume|Personalizza i criteri di filtro come contiene/non contiene|
|Filtra per colore|Filtri basati sul colore pieno|
|Filtri data|Filtra le righe in base a diversi criteri in base alla data|
|Filtri numerici|Diversi tipi di filtro su numeri come confronto, medie e Top 10 ecc.|
|Filtri di testo|Diversi filtri come inizia con, finisce con, contiene ecc.|
|Spazi vuoti/Non spazi vuoti|Questi filtri possono essere implementati tramite Text Filter Blank|
Gli utenti filtrano manualmente i dati del foglio di lavoro in Microsoft Excel utilizzando queste opzioni.

### **Filtro automatico con Aspose.Cells**

Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)che rappresenta un file Excel. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)la classe contiene un[**Raccolta di fogli di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)che consente l'accesso a ciascun foglio di lavoro nel file Excel.

Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)classe. Il[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)class fornisce un'ampia gamma di proprietà e metodi per gestire i fogli di lavoro. Per creare un filtro automatico, utilizzare il file[**Filtro automatico**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)proprietà del[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)classe. Il[**Filtro automatico**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)la proprietà è un oggetto di[**Filtro automatico**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)classe, che fornisce il[**Gamma**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#Range)proprietà per specificare l'intervallo di celle che compongono una riga di intestazione. Un filtro automatico viene applicato all'intervallo di celle che è la riga di intestazione.

In ogni foglio di lavoro è possibile specificare un solo intervallo di filtri. Questo è limitato da Microsoft Excel. Per il filtraggio dei dati personalizzati, utilizzare il file[**Filtro automatico.Personalizzato**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)) metodo.

Nell'esempio fornito di seguito, abbiamo creato lo stesso filtro automatico utilizzando Aspose.Cells che abbiamo creato utilizzando Microsoft Excel nella sezione precedente.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterData.java" >}}

#### **Diversi tipi di filtro**

Aspose.Cells offre più opzioni per applicare diversi tipi di filtri come Filtro colore, Filtro data, Filtro numero, Filtro testo, Filtri vuoti e Nessuno Filtri vuoti.

##### **Colore di riempimento**

Aspose.Cells fornisce una funzione[**addFillColorFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addFillColorFilter(int,%20int,%20com.aspose.cells.CellsColor,%20com.aspose.cells.CellsColor)per filtrare i dati in base alla proprietà del colore di riempimento delle celle. Nell'esempio riportato di seguito, un file modello con colori di riempimento diversi nella prima colonna del foglio viene utilizzato per testare la funzione di filtraggio dei colori. I seguenti file possono essere scaricati per verificarne la funzionalità.

1. [CelleColorate.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterColor.java" >}}

##### **Data**

È possibile implementare diversi tipi di filtri di data come filtrare tutte le righe con date nel gennaio 2018. Il seguente codice di esempio mostra questo filtro utilizzando[**addDateFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addDateFilter(int,%20int,%20int,%20int,%20int,%20int,%20int,%20int)) funzione. I seguenti file possono essere utilizzati per testare questa funzionalità.

1. [Data.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDate.java" >}}

##### **Data dinamica**

A volte sono richiesti filtri dinamici basati su una data come tutte le celle che hanno date a gennaio indipendentemente dall'anno. In questo caso,[**Filtro dinamico**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#dynamicFilter(int,%20int)) viene utilizzata come indicato nel codice di esempio seguente. I seguenti file possono essere utilizzati per il test.

1. [Data.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDynamicFilter.java" >}}

##### **Numero**

filtri personalizzati possono essere applicati utilizzando Aspose.Cells come selezionare le celle con un numero compreso tra un determinato intervallo. L'esempio seguente mostra l'utilizzo di[**costume()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)) per filtrare i numeri. I file di esempio possono essere scaricati dai seguenti collegamenti.

1. [Numero.xlsx](72417320.xlsx)
1. [NumeroFiltrato.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNumber.java" >}}

##### **Testo**

Se una colonna contiene testo e devono essere selezionate celle contenenti testo particolare,[**filtro()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#filter(int,%20java.lang.String)) può essere utilizzata. Nell'esempio seguente, il file modello contiene un elenco di paesi e la riga deve essere selezionata contenente un particolare nome di paese. Il codice seguente illustra il filtraggio del testo utilizzando i file di esempio seguenti.

1. [Testo.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterText.java" >}}

##### **Spazi vuoti**

Se una colonna contiene testo tale che poche celle sono vuote ed è necessario filtrare per selezionare quelle righe solo dove sono presenti celle vuote,[**matchBlanks()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchBlanks(int)) può essere utilizzata come illustrato di seguito. I file di esempio possono essere scaricati dai seguenti collegamenti.

1. [Vuoto.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterBlank.java" >}}

##### **Non spazi vuoti**

Quando le celle contenenti testo devono essere filtrate, utilizzare[**MatchNonBlanks**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchNonBlanks(int)) funzione di filtro come illustrato di seguito. I file di esempio possono essere scaricati dai seguenti collegamenti.

1. [Vuoto.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNonBlank.java" >}}

##### **Filtro personalizzato con Contiene**

Excel fornisce filtri personalizzati come righe di filtro che contengono una stringa specifica. Questa funzione è disponibile in Aspose.Cells e illustrata di seguito filtrando i nomi nel file di esempio. I file di esempio possono essere scaricati dai seguenti collegamenti.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-Contains.java" >}}

##### **Filtro personalizzato con NotContains**

Excel fornisce filtri personalizzati come righe di filtro che non contengono una stringa specifica. Questa funzione è disponibile in Aspose.Cells e illustrata di seguito filtrando i nomi nel file di esempio fornito di seguito.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-NotContains.java" >}}

##### **Filtro personalizzato con BeginsWith**

Excel fornisce filtri personalizzati come righe di filtro che iniziano con una stringa specifica. Questa funzione è disponibile in Aspose.Cells e illustrata di seguito filtrando i nomi nel file di esempio fornito di seguito.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-BeginsWith.java" >}}

##### **Filtro personalizzato con EndsWith**

Excel fornisce filtri personalizzati come righe di filtro che terminano con una stringa specifica. Questa funzione è disponibile in Aspose.Cells e illustrata di seguito filtrando i nomi nel file di esempio fornito di seguito.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-EndsWith.java" >}}

## **Argomenti avanzati**
- [Applica il filtro avanzato di Microsoft Excel per visualizzare i record che soddisfano criteri complessi](/cells/it/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Ottieni tutti gli indici delle righe nascoste dopo l'aggiornamento del filtro automatico](/cells/it/java/get-all-hidden-rows-indices-after-refreshing-autofilter/)

