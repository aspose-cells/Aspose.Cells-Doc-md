---
title: Filtraggio dei dati
type: docs
weight: 60
url: /it/java/data-filtering/
---

{{% alert color="primary" %}}

Microsoft Excel fornisce alcune buone funzionalità per filtrare automaticamente i dati del foglio di lavoro. Aspose.Cells supporta pienamente le funzionalità di autofiltro di Microsoft Excel. Questo articolo spiega come utilizzare le funzionalità in Microsoft Excel e come codificarle utilizzando Aspose.Cells.

{{% /alert %}}

## **Dati Autofiltra**

L'auto-filtraggio è il modo più rapido per selezionare solo gli elementi del foglio di lavoro che si desidera visualizzare in un elenco. La funzione di autofiltro consente agli utenti di filtrare gli elementi in un elenco in base a determinati criteri. Filtra in base a testo, numeri o date.

### **Autofiltro in Microsoft Excel**

Per attivare la funzione di autofiltro in Microsoft Excel:

1. Fare clic sulla riga dell'intestazione su un foglio di lavoro.
1. Dal menu **Dati**, seleziona **Filtro** e quindi **Filtro automatico**.

Quando si applica un autofiltro a un foglio di lavoro, compaiono degli interruttori di filtro (frecce nere) alla destra degli intestazioni delle colonne.

1. Fare clic su una freccia del filtro per visualizzare un elenco di opzioni di filtro.

Alcune delle opzioni di autofiltro sono:

|**Opzioni**|**Descrizione**|
| :- | :- |
|All|Mostra tutti gli elementi nell'elenco una volta.|
|Custom|Personalizza i criteri di filtro come contiene/non contiene|
|Filter by Color|Filtra in base al colore riempito|
|Date Filters|Filtra le righe in base a diversi criteri di data|
|Number Filters|Diverse tipologie di filtro sui numeri come confronto, medie e Top 10 ecc.|
|Text Filters|Diversi filtri come inizia con, termina con, contiene ecc.,|
|Blanks/Non Blanks|Questi filtri possono essere implementati tramite Filtro Testo Vuoto|
Gli utenti filtrano manualmente i dati del foglio di lavoro in Microsoft Excel utilizzando queste opzioni.

### **Filtro automatico con Aspose.Cells**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) che consente l'accesso a ciascun foglio di lavoro nel file Excel.

Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fornisce una vasta gamma di proprietà e metodi per gestire i fogli di lavoro. Per creare un filtro automatico, utilizzare la proprietà [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter) della classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La proprietà [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter) è un oggetto della classe [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter), che fornisce la proprietà [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#Range) per specificare l'intervallo di celle che costituiscono una riga di intestazione. Un filtro automatico viene applicato all'intervallo di celle che costituisce la riga di intestazione.

In ogni foglio di lavoro, è possibile specificare solo un intervallo di filtro. Questo è limitato da Microsoft Excel. Per il filtraggio dei dati personalizzato, utilizzare il metodo [**AutoFilter.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)).

Nell'esempio qui sotto, abbiamo creato lo stesso autofiltro utilizzando Aspose.Cells come abbiamo creato utilizzando Microsoft Excel nella sezione precedente.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterData.java" >}}

#### **Diversi tipi di filtro**

Aspose.Cells offre molteplici opzioni per applicare diversi tipi di filtri come Filtro colore, Filtro data, Filtro numero, Filtro testo, Filtri vuoti e non vuoti.

##### **Colore di riempimento**

Aspose.Cells fornisce una funzione [**addFillColorFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addFillColorFilter(int,%20int,%20com.aspose.cells.CellsColor,%20com.aspose.cells.CellsColor)) per filtrare i dati in base alla proprietà del colore di riempimento delle celle. Nell'esempio riportato di seguito, viene utilizzato un file modello con diversi colori di riempimento nella prima colonna del foglio per testare la funzione di filtraggio per colore. È possibile scaricare i seguenti file per verificare la funzionalità.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterColor.java" >}}

##### **Data**

Possono essere implementati diversi tipi di filtri data come filtrare tutte le righe con date a gennaio 2018. Il codice di esempio seguente dimostra questo filtro utilizzando la funzione [**addDateFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addDateFilter(int,%20int,%20int,%20int,%20int,%20int,%20int,%20int)). I seguenti file possono essere utilizzati per testare questa funzionalità.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDate.java" >}}

##### **Data Dinamica**

A volte sono necessari filtri dinamici in base a una data come tutte le celle con date a gennaio indipendentemente dall'anno. In questo caso, la funzione [**DynamicFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#dynamicFilter(int,%20int)) viene utilizzata come indicato nel codice di esempio seguente. I seguenti file possono essere utilizzati per i test.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDynamicFilter.java" >}}

##### **Numero**

I filtri personalizzati possono essere applicati utilizzando Aspose.Cells come selezionare celle con numeri compresi in un determinato intervallo. L'esempio seguente dimostra l'uso della funzione [**custom()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)) per filtrare i numeri. I file di esempio possono essere scaricati dai seguenti link.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNumber.java" >}}

##### **Testo**

Se una colonna contiene testo e si devono selezionare celle contenenti un testo particolare, è possibile utilizzare la funzione [**filter()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#filter(int,%20java.lang.String)). Nell'esempio seguente, il file di modello contiene un elenco di paesi e deve essere selezionata la riga contenente un particolare nome di paese. Il codice seguente dimostra il filtraggio del testo utilizzando i seguenti file di esempio.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterText.java" >}}

##### **Vuoti**

Se una colonna contiene testo in modo che alcune celle siano vuote e sia necessario selezionare solo le righe in cui sono presenti celle vuote, è possibile utilizzare la funzione [**matchBlanks()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchBlanks(int)) come illustrato di seguito. I file di esempio possono essere scaricati dai seguenti link.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterBlank.java" >}}

##### **Non vuoti**

Quando si desidera filtrare le celle che contengono un qualsiasi testo, utilizzare la funzione di filtro [**MatchNonBlanks**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchNonBlanks(int)) come illustrato di seguito. I file di esempio possono essere scaricati dai seguenti link.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNonBlank.java" >}}

##### **Filtro personalizzato con Contiene**

Excel fornisce filtri personalizzati come filtrare le righe che contengono una stringa specifica. Questa funzione è disponibile in Aspose.Cells e dimostrata di seguito filtrando i nomi nel file di esempio. I file di esempio possono essere scaricati dai seguenti link.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-Contains.java" >}}

##### **Filtro personalizzato con NonContiene**

Excel fornisce filtri personalizzati come filtrare le righe che non contengono una stringa specifica. Questa funzione è disponibile in Aspose.Cells e dimostrata di seguito filtrando i nomi nel file di esempio fornito di seguito.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-NotContains.java" >}}

##### **Filtro personalizzato con IniziaCon**

Excel fornisce filtri personalizzati come filtrare le righe che iniziano con una stringa specifica. Questa funzione è disponibile in Aspose.Cells e dimostrata di seguito filtrando i nomi nel file di esempio fornito di seguito.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-BeginsWith.java" >}}

##### **Filtro personalizzato con TerminaCon**

Excel fornisce filtri personalizzati come filtrare le righe che terminano con una stringa specifica. Questa funzione è disponibile in Aspose.Cells e dimostrata di seguito filtrando i nomi nel file di esempio fornito di seguito.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-EndsWith.java" >}}

## **Argomenti avanzati**
- [Applicare il filtro avanzato di Microsoft Excel per visualizzare i record che soddisfano criteri complessi](/cells/it/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Ottenere tutti gli indici delle righe nascoste dopo l'aggiornamento dell'autofiltro](/cells/it/java/get-all-hidden-rows-indices-after-refreshing-autofilter/)

