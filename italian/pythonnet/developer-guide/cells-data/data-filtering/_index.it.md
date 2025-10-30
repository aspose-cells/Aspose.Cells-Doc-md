---
title: Filtraggio dei dati
type: docs
weight: 85
url: /it/python-net/data-filtering/
description: Scopri come aggiungere un filtro dati utilizzando l API Aspose.Cells per Python via .NET.
keywords: Libreria Excel di Python, Aggiungi filtro per colore, Aggiungi filtri data, Aggiungi filtri numerici, Aggiungi filtro dinamico, Aggiungi filtri testuali, Aggiungi filtro personalizzato con Contiene, Aggiungi filtro personalizzato con NonContiene, Aggiungi filtro personalizzato con IniziaCon, Aggiungi filtro personalizzato con TerminaCon
---

{{% alert color="primary" %}}

Microsoft Excel fornisce alcune buone funzionalità per filtrare i dati dei fogli di lavoro. Aspose.Cells per Python via .NET supporta completamente le funzionalità di autofiltro di Microsoft Excel. Questo articolo spiega come utilizzare le funzionalità in Microsoft Excel e come codificarle utilizzando Aspose.Cells per Python via .NET.

{{% /alert %}}

## **Dati Autofiltra**

L'auto-filtraggio è il modo più rapido per selezionare solo gli elementi del foglio di lavoro che si desidera visualizzare in un elenco. La funzione di autofiltro consente agli utenti di filtrare gli elementi in un elenco in base a determinati criteri. Filtra in base a testo, numeri o date.

### **Autofiltro in Microsoft Excel**

Per attivare la funzione di autofiltro in Microsoft Excel:

1. Fare clic sulla riga dell'intestazione su un foglio di lavoro.
1. Dal menu **Dati**, selezionare **Filtro** e poi **Autofiltro**.

Quando si applica un autofiltro a un foglio di lavoro, compaiono degli interruttori di filtro (frecce nere) alla destra degli intestazioni delle colonne.

1. Fare clic su una freccia del filtro per visualizzare un elenco di opzioni di filtro.

Alcune delle opzioni di autofiltro sono:

|**Opzioni**|**Descrizione**|
| :- | :- |
|All|Mostra tutti gli elementi nell'elenco una volta.|
|Custom|Personalizza i criteri di filtro come contiene/non contiene|
|Filter by Color|Filtra in base al colore riempito|
|Date Filters|Filtra le righe in base a diversi criteri di data|
|Number Filters|Diversi tipi di filtro sui numeri come confronto, medie e i primi 10 ecc.|
|Text Filters|Diversi filtri come inizia con, termina con, contiene ecc.,|
|Blanks/Non Blanks|Questi filtri possono essere implementati tramite Filtro Testo Vuoto|

Gli utenti filtrano manualmente i dati del foglio di lavoro in Microsoft Excel utilizzando queste opzioni.

### **Autofiltro con Aspose.Cells per la libreria Python di Excel**

Aspose.Cells per Python via .NET fornisce una classe, Workbook, che rappresenta un file Excel. La classe Workbook contiene una collezione di fogli di lavoro che consente di accedere ad ogni foglio di lavoro nel file Excel.

Un foglio di lavoro è rappresentato dalla classe Worksheet. La classe Worksheet fornisce una vasta gamma di proprietà e metodi per gestire i fogli di lavoro. Per creare un filtro automatico, utilizzare la proprietà AutoFilter della classe Worksheet. La proprietà AutoFilter è un oggetto della classe AutoFilter, che fornisce la proprietà Range per specificare il range di celle che costituiscono una riga di intestazione. Un filtro automatico viene applicato al range di celle che è la riga di intestazione.

In ogni foglio di lavoro, è possibile specificare solo un intervallo di filtro. Questo è limitato da Microsoft Excel. Per il filtraggio personalizzato dei dati, utilizzare il metodo AutoFilter.Custom.

Nell'esempio riportato di seguito, abbiamo creato lo stesso filtro automatico utilizzando Aspose.Cells for Python via .NET come abbiamo creato utilizzando Microsoft Excel nella sezione precedente.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterData-1.py" >}}

#### **Diversi tipi di filtro**

Aspose.Cells for Python via .NET offre diverse opzioni per applicare diversi tipi di filtri come filtro per colore, filtro per data, filtro per numero, filtro per testo, filtri vuoti e non vuoti.

##### **Colore di riempimento**

Aspose.Cells for Python via .NET fornisce una funzione AddFillColorFilter per filtrare i dati in base alla proprietà del colore di riempimento delle celle. Nell'esempio riportato di seguito, viene utilizzato un file di modello con diversi colori di riempimento nella prima colonna del foglio per testare la funzione di filtraggio del colore. I file di esempio possono essere scaricati dai seguenti link.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterColor-1.py" >}}

##### **Data**

Diversi tipi di filtri per data possono essere implementati, come filtrare tutte le righe con date in gennaio 2018. Il seguente codice di esempio mostra questo filtro utilizzando la funzione AddDateFilter. I file di esempio sono dati di seguito.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterDate-1.py" >}}

##### **Data Dinamica**

A volte sono necessari filtri dinamici basati sulla data come tutte le celle con date a gennaio indipendentemente dall'anno. In questo caso, viene utilizzata la funzione DynamicFilter come indicato nel codice di esempio seguente. I file di esempio sono dati di seguito.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterDynamicFilter-1.py" >}}

##### **Numero**

I filtri personalizzati possono essere applicati utilizzando Aspose.Cells for Python via .NET come la selezione di celle con numeri compresi in un determinato intervallo. L'esempio seguente dimostra l'uso della funzione Custom() per filtrare i numeri. I file di esempio sono dati di seguito.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterNumber-1.py" >}}

##### **Testo**

Se una colonna contiene del testo e si vogliono selezionare celle contenenti un testo particolare, può essere utilizzata la funzione Filter(). Nell'esempio seguente, il file di modello contiene un elenco di paesi e viene selezionata la riga contenente il nome del paese desiderato. Il seguente codice dimostra il filtraggio del testo. I file di esempio sono dati di seguito.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterText-1.py" >}}

##### **Vuoti**

Se una colonna contiene del testo in modo che alcune celle siano vuote e è necessario selezionare solo le righe in cui sono presenti celle vuote, è possibile utilizzare la funzione MatchBlanks() come dimostrato di seguito. I file di esempio sono dati di seguito.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterBlank-1.py" >}}

##### **Non vuoti**

Quando le celle contenenti del testo devono essere filtrate, utilizzare la funzione di filtro MatchNonBlanks come dimostrato di seguito. I file di esempio sono dati di seguito.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterNonBlank-1.py" >}}

##### **Filtro personalizzato con Contiene**

Excel fornisce filtri personalizzati come filtra le righe che contengono una stringa specifica. Questa funzione è disponibile in Aspose.Cells for Python via .NET e viene dimostrata di seguito filtrando i nomi nel file di esempio. I file di esempio sono dati di seguito.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterCustom-Contains-1.py" >}}

##### **Filtro personalizzato con NonContiene**

Excel fornisce filtri personalizzati come filtra le righe che non contengono una stringa specifica. Questa funzione è disponibile in Aspose.Cells for Python via .NET e viene dimostrata di seguito filtrando i nomi nel file di esempio sottostante.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterCustom-NotContains-1.py" >}}

##### **Filtro personalizzato con IniziaCon**

Excel fornisce filtri personalizzati come filtra le righe che iniziano con una stringa specifica. Questa funzione è disponibile in Aspose.Cells for Python via .NET e viene dimostrata di seguito filtrando i nomi nel file di esempio sottostante.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterBeginsWith-1.py" >}}

##### **Filtro personalizzato con TerminaCon**

Excel fornisce filtri personalizzati come filtra le righe che termina con una stringa specifica. Questa funzionalità è disponibile in Aspose.Cells per Python via .NET e dimostrata di seguito filtrando i nomi nel file di esempio fornito di seguito.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterEndsWith-1.py" >}}

## **Argomenti avanzati**
- [Applicare il filtro avanzato di Microsoft Excel per visualizzare i record che soddisfano criteri complessi](/cells/it/python-net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Ottenere tutti gli indici delle righe nascoste dopo l'aggiornamento dell'autofiltro](/cells/it/python-net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
{{< app/cells/assistant language="python-net" >}}
