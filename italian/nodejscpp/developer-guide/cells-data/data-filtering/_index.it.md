---
title: Filtraggio dei dati
type: docs
weight: 85
url: /it/nodejs-cpp/data-filtering/
description: Impara come aggiungere filtri ai dati usando l API Aspose.Cells for Node.js via C++.
keywords: Aggiungi Filtro per Colore Node.js tramite C++, Aggiungi Filtri Data Node.js tramite C++, Aggiungi Filtri Numero Node.js tramite C++, Aggiungi Filtro Dinamico Node.js tramite C++, Aggiungi Filtri Testo Node.js tramite C++, Aggiungi filtro personalizzato con Contains Node.js tramite C++, Aggiungi filtro personalizzato con NotContains Node.js tramite C++, Aggiungi filtro personalizzato con BeginsWith Node.js tramite C++, Aggiungi filtro personalizzato con EndsWith Node.js tramite C++
---

{{% alert color="primary" %}}
Microsoft Excel offre alcune buone funzionalità per l'autofiltro dei dati del foglio di lavoro. Aspose.Cells supporta pienamente le funzionalità di autofiltro di Microsoft Excel. Questo articolo spiega come utilizzare le funzionalità in Microsoft Excel e come implementarle usando Aspose.Cells for Node.js via C++.
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

### **Autofiltro con Aspose.Cells for Node.js via C++**

Aspose.Cells fornisce una classe, Workbook, che rappresenta un file di Excel. La classe Workbook contiene una collezione di fogli di lavoro che consente di accedere a ciascun foglio di lavoro nel file di Excel.

Un foglio di lavoro è rappresentato dalla classe Worksheet. La classe Worksheet fornisce una vasta gamma di proprietà e metodi per gestire i fogli di lavoro. Per creare un filtro automatico, utilizzare la proprietà AutoFilter della classe Worksheet. La proprietà AutoFilter è un oggetto della classe AutoFilter, che fornisce la proprietà Range per specificare il range di celle che costituiscono una riga di intestazione. Un filtro automatico viene applicato al range di celle che è la riga di intestazione.

In ogni foglio di lavoro, è possibile specificare solo un intervallo di filtro. Questo è limitato da Microsoft Excel. Per il filtraggio personalizzato dei dati, utilizzare il metodo AutoFilter.Custom.

 Nell'esempio sopra, abbiamo creato lo stesso Autofiltro usando Aspose.Cells for Node.js via C++ come fatto con Microsoft Excel nella sezione precedente.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter.js" >}}

#### **Diversi tipi di filtro**

Aspose.Cells offre molteplici opzioni per applicare diversi tipi di filtri come Filtro colore, Filtro data, Filtro numero, Filtro testo, Filtri vuoti e non vuoti.

##### **Colore di riempimento**

Aspose.Cells fornisce una funzione AddFillColorFilter per filtrare i dati in base alla proprietà del colore di riempimento delle celle. Nell'esempio qui sotto, viene utilizzato un file modello con diversi colori di riempimento nella prima colonna del foglio per testare la funzione di filtraggio del colore. I file di esempio possono essere scaricati dai seguenti link.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-FillColor.js" >}}


##### **Data**

 Diversi tipi di filtri data possono essere implementati come filtrare tutte le righe con date a gennaio 2018. Il codice di esempio seguente dimostra questo filtro usando la funzione AddDateFilter. I file di esempio sono forniti di seguito.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Date.js" >}}


##### **Data Dinamica**

A volte sono necessari filtri dinamici basati sulla data come tutte le celle con date a gennaio indipendentemente dall'anno. In questo caso, viene utilizzata la funzione DynamicFilter come indicato nel codice di esempio seguente. I file di esempio sono dati di seguito.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-DynamicFilter.js" >}}


##### **Numero**

I filtri personalizzati possono essere applicati utilizzando Aspose.Cells come la selezione di celle con numeri compresi in un determinato intervallo. L'esempio seguente dimostra l'uso della funzione Custom() per filtrare i numeri. Sono forniti file di esempio di seguito.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Number.js" >}}


##### **Testo**

 Se una colonna contiene testo e si devono selezionare le celle contenenti un testo particolare, può essere utilizzata la funzione Filter(). Nel seguente esempio, il file modello contiene un elenco di paesi e la riga da selezionare contiene un nome di paese particolare. Il codice seguente dimostra il filtraggio di testo. I file di esempio sono forniti di seguito.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Text.js" >}}


##### **Vuoti**

Se una colonna contiene del testo in modo che alcune celle siano vuote e è necessario selezionare solo le righe in cui sono presenti celle vuote, è possibile utilizzare la funzione MatchBlanks() come dimostrato di seguito. I file di esempio sono dati di seguito.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Blanks.js" >}}


##### **Non vuoti**

Quando le celle contenenti del testo devono essere filtrate, utilizzare la funzione di filtro MatchNonBlanks come dimostrato di seguito. I file di esempio sono dati di seguito.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-NonBlanks.js" >}}


##### **Filtro personalizzato con Contiene**

Excel fornisce filtri personalizzati come filtrare le righe che contengono una stringa specifica. Questa funzionalità è disponibile in Aspose.Cells e dimostrata di seguito filtrando i nomi nel file di esempio. Sono forniti file di esempio di seguito.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-Contains.js" >}}


##### **Filtro personalizzato con NonContiene**

Excel fornisce filtri personalizzati come filtra righe che non contengono una stringa specifica. Questa funzione è disponibile in Aspose.Cells e dimostrata di seguito filtrando i nomi nel file di esempio fornito sotto.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-NotContains.js" >}}


##### **Filtro personalizzato con IniziaCon**

Excel fornisce filtri personalizzati come filtra righe che iniziano con una stringa specifica. Questa funzione è disponibile in Aspose.Cells e dimostrata di seguito filtrando i nomi nel file di esempio fornito sotto.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-BeginsWith.js" >}}


##### **Filtro personalizzato con TerminaCon**

Excel fornisce filtri personalizzati come filtrare le righe che terminano con una stringa specifica. Questa funzione è disponibile in Aspose.Cells e dimostrata di seguito filtrando i nomi nel file di esempio fornito di seguito.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-EndsWith.js" >}}


## **Argomenti avanzati**
- [Applicare il filtro avanzato di Microsoft Excel per visualizzare i record che soddisfano criteri complessi](/cells/it/nodejs-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Ottenere tutti gli indici delle righe nascoste dopo l'aggiornamento dell'autofiltro](/cells/it/nodejs-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/)
