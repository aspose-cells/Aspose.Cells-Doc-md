---
title: Come Filtrare Spazi Vuoti o Non Spazi Vuoti
type: docs
weight: 85
url: /it/net/how-to-filter-blanks-and-non-blanks/
description: Scopri come filtrare le celle vuote e non vuote utilizzando l API Aspose.Cells for .NET.
keywords: Filtra Celle Vuote, Filtra Celle Non Vuote, Filtra Celle Vuote nel foglio di lavoro, Filtra Celle Non Vuote nel foglio di lavoro, Filtra Celle Vuote in excel, Filtra Celle Non Vuote in excel, Filtra Celle Vuote e Non Vuote in excel
---

## **Possibili Scenari di Utilizzo**
Filtrare i dati in Excel è uno strumento prezioso che migliora l'analisi, l'esplorazione e la presentazione dei dati consentendo agli utenti di concentrarsi su sottoinsiemi specifici di dati in base ai loro criteri, rendendo il processo generale di manipolazione e interpretazione dei dati più efficiente ed efficace.

## **Come Filtrare Spazi Vuoti o Non Spazi Vuoti in Excel**
In Excel, è possibile filtrare facilmente gli spazi vuoti o non spazi vuoti utilizzando le opzioni di filtraggio. Ecco come puoi farlo:

### **Come Filtrare Spazi Vuoti in Excel**
1. Seleziona l'Intervallo: Fai clic sulla lettera dell'intestazione della colonna per selezionare l'intera colonna o seleziona l'intervallo in cui desideri filtrare gli spazi vuoti.
1. Apri il Menu Filtro: Vai alla scheda "Dati" nella barra multifunzione.
<br>
<image src="1.png" width="70%" />
1. Opzioni di Filtro: Fai clic sul pulsante "Filtro". Questo aggiungerà delle freccette di filtro all'intervallo selezionato.
1. Filtra Spazi Vuoti: Fai clic sulla freccia di filtro nella colonna in cui desideri filtrare gli spazi vuoti. Deseleziona tutte le opzioni tranne "Spazi vuoti" e fai clic su OK. Questo mostrerà solo le celle vuote in quella colonna.
<br>
<image src="2.png" width="70%" />
1. Il risultato è il seguente:
<br>
<image src="3.png" width="70%" />

### **Come Filtrare Non Spazi Vuoti in Excel**
1. Seleziona l'Intervallo: Fai clic sulla lettera dell'intestazione della colonna per selezionare l'intera colonna o seleziona l'intervallo in cui desideri filtrare non spazi vuoti.
1. Apri il Menu Filtro: Vai alla scheda "Dati" nella barra multifunzione.
<br>
<image src="1.png" width="70%" />
1. Opzioni di Filtro: Fai clic sul pulsante "Filtro". Questo aggiungerà delle freccette di filtro all'intervallo selezionato.
1. Filtra Non Spazi Vuoti: Fai clic sulla freccia di filtro nella colonna in cui desideri filtrare non spazi vuoti. Deseleziona tutte le opzioni tranne "Non spazi vuoti" o "Personalizzato" e imposta le condizioni di conseguenza. Fai clic su OK. Questo mostrerà solo le celle che non sono vuote in quella colonna.
<br>
<image src="4.png" width="70%" />
1. Il risultato è il seguente:
<br>
<image src="5.png" width="70%" />

## **Come filtrare le celle vuote utilizzando Aspose.Cells**
Se una colonna contiene testo in modo che alcune celle siano vuote e è necessario selezionare solo le righe in cui sono presenti celle vuote, possono essere utilizzate le funzioni [AutoFilter.MatchBlanks(int fieldIndex)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchblanks/) e [AutoFilter.AddFilter(int fieldIndex, string criteria)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/addfilter/) come dimostrato di seguito. 

Si prega di vedere il seguente codice di esempio che carica il [file Excel di esempio](sample.xlsx) che contiene alcuni dati finti. Il codice di esempio utilizza tre metodi per filtrare le celle vuote. Poi salva il workbook come [file Excel di output](FilteredBlanks.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-blanks.cs" >}}

## **Come filtrare le celle non vuote utilizzando Aspose.Cells**

Si prega di vedere il seguente codice di esempio che carica il [file Excel di esempio](sample.xlsx) che contiene alcuni dati finti. Dopo aver caricato il file, chiama la funzione [AutoFilter.MatchNonBlanks(int fieldIndex)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchnonblanks/) per filtrare i dati non vuoti, e infine salva il workbook come [file Excel di output](FilteredNonBlanks.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-non-blanks.cs" >}}

{{< app/cells/assistant language="csharp" >}}
