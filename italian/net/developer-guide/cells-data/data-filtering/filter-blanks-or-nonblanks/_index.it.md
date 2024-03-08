---
title: Come filtrare spazi vuoti o non vuoti
type: docs
weight: 85
url: /it/net/how-to-filter-blanks-and-non-blanks/
description: Scopri come filtrare gli spazi vuoti e quelli non vuoti utilizzando Aspose.Cells for .NET API.
keywords: Filter Blanks, Filter Non-Blanks, Filter Blanks in worksheet, Filter Non-Blanks in worksheet, Filter Blanks in excel, Filter Non-Blanks in excel, Filter Blanks and Non-Blanks in excel
---
##  **Possibili scenari di utilizzo**
Il filtraggio dei dati in Excel è uno strumento prezioso che migliora l'analisi, l'esplorazione e la presentazione dei dati consentendo agli utenti di concentrarsi su sottoinsiemi specifici di dati in base ai propri criteri, rendendo il processo complessivo di manipolazione e interpretazione dei dati più efficiente ed efficace.

##  **Come filtrare spazi vuoti o non vuoti in Excel**
In Excel, puoi facilmente filtrare gli spazi vuoti o non vuoti utilizzando le opzioni di filtro. Ecco come puoi farlo:

###  **Come filtrare gli spazi vuoti in Excel**
1. Seleziona l'intervallo: fai clic sulla lettera dell'intestazione della colonna per selezionare l'intera colonna o seleziona l'intervallo in cui desideri filtrare gli spazi vuoti.
1. Apri il menu Filtro: vai alla scheda "Dati" nella barra multifunzione.
<br>
<image src="1.png" width="70%" />
1. Opzioni filtro: fare clic sul pulsante "Filtro". Ciò aggiungerà le frecce del filtro all'intervallo selezionato.
1. Filtra spazi vuoti: fare clic sulla freccia del filtro nella colonna in cui si desidera filtrare gli spazi vuoti. Deseleziona tutte le opzioni tranne "Vuoti" e fai clic su OK. Verranno visualizzate solo le celle vuote in quella colonna.
<br>
<image src="2.png" width="70%" />
1. Il risultato come segue:
<br>
<image src="3.png" width="70%" />

###  **Come filtrare i non vuoti in Excel**
1. Seleziona l'intervallo: fai clic sulla lettera dell'intestazione della colonna per selezionare l'intera colonna o seleziona l'intervallo in cui desideri filtrare gli elementi non vuoti.
1. Apri il menu Filtro: vai alla scheda "Dati" nella barra multifunzione.
<br>
<image src="1.png" width="70%" />
1. Opzioni filtro: fare clic sul pulsante "Filtro". Ciò aggiungerà le frecce del filtro all'intervallo selezionato.
1. Filtra non vuoti: fai clic sulla freccia del filtro nella colonna in cui desideri filtrare i non vuoti. Deseleziona tutte le opzioni tranne "Non vuoti" o "Personalizzato" e imposta le condizioni di conseguenza. Fare clic su OK. Verranno visualizzate solo le celle che non sono vuote in quella colonna.
<br>
<image src="4.png" width="70%" />
1. Il risultato come segue:
<br>
<image src="5.png" width="70%" />

##  **Come filtrare gli spazi vuoti utilizzando Aspose.Cells**
 Se una colonna contiene testo tale che poche celle sono vuote ed è necessario un filtro per selezionare quelle righe solo dove sono presenti celle vuote,[AutoFilter.MatchBlanks(int fieldIndex)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchblanks/) E[AutoFilter.AddFilter(int fieldIndex, criteri stringa)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/addfilter/) le funzioni possono essere utilizzate come illustrato di seguito.

 Consulta il seguente codice di esempio che carica il file[file Excel di esempio](sample.xlsx) che contiene alcuni dati fittizi. Il codice di esempio utilizza tre metodi per filtrare gli spazi vuoti. Quindi salva la cartella di lavoro come[file Excel di output](FilteredBlanks.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-blanks.cs" >}}

##  **Come filtrare gli spazi non vuoti utilizzando Aspose.Cells**

 Consulta il seguente codice di esempio che carica il file[file Excel di esempio](sample.xlsx) che contiene alcuni dati fittizi. Dopo aver caricato il file, chiama il file[AutoFilter.MatchNonBlanks(int fieldIndex)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchnonblanks/) funzione per filtrare i dati non vuoti e infine salvare la cartella di lavoro come[file Excel di output](FilteredNonBlanks.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-non-blanks.cs" >}}

