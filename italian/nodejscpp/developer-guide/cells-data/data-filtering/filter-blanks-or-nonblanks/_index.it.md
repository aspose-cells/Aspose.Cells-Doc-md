---
title: Come Filtrare Spazi Vuoti o Non Spazi Vuoti
type: docs
weight: 85
url: /it/nodejs-cpp/how-to-filter-blanks-and-non-blanks/
description: Scopri come filtrare i vuoti e i non vuoti utilizzando l API Aspose.Cells for Node.js via C++.
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

## **Come filtrare i vuoti usando Aspose.Cells for Node.js via C++**
Se una colonna contiene testo tale che alcune celle sono vuote, e si desidera filtrare per selezionare solo le righe con celle vuote, le funzioni [**AutoFilter.matchBlanks(number)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#matchBlanks-number-) e [**AutoFilter.addFilter(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#addFilter-number-string-) possono essere usate come mostrato di seguito. 

Si prega di vedere il seguente codice di esempio che carica il [file Excel di esempio](sample.xlsx) che contiene alcuni dati finti. Il codice di esempio utilizza tre metodi per filtrare le celle vuote. Poi salva il workbook come [file Excel di output](FilteredBlanks.xlsx). 

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-FilterBlanks.js" >}}


## **Come filtrare i non-vuoti usando Aspose.Cells for Node.js via C++**

Si prega di vedere il seguente esempio di codice che carica il [file Excel di esempio](sample.xlsx) contenente alcuni dati fittizi. Dopo aver caricato il file, chiama la funzione [AutoFilter.matchNonBlanks(number)](https://reference.aspose.com/cells/nodejs-cpp/autofilter/#matchNonBlanks-number-) per filtrare i dati non vuoti, e infine salva il foglio di lavoro come [file Excel di output](FilteredNonBlanks.xlsx). 

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-FilterNonBlanks.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
