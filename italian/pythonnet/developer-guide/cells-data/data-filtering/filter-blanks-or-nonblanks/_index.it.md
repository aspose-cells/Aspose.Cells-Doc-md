---
title: Come Filtrare Spazi Vuoti o Non Spazi Vuoti
type: docs
weight: 85
url: /it/python-net/how-to-filter-blanks-and-non-blanks/
description: Scopri come filtrare Spazi Vuoti e non spazi vuoti utilizzando l API Aspose.Cells per Python via .NET
keywords: Libreria Excel Python, Filtra Spazi Vuoti Python, Filtra Non Spazi Vuoti Python, Filtra Spazi Vuoti nel foglio di lavoro Python, Filtra Non Spazi Vuoti nel foglio di lavoro Python, Filtra spazi vuoti in excel Python, Filtra non spazi vuoti in excel Python, Filtra spazi vuoti e non spazi vuoti in excel Python
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

## **Come filtrare i vuoti utilizzando la libreria Excel Aspose.Cells per Python**
Se una colonna contiene testo in modo che alcune celle siano vuote e è necessario filtrare solo le righe in cui sono presenti celle vuote, è possibile utilizzare le funzioni [AutoFilter.match_blanks(field_index)](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/match_blanks/#int) e [AutoFilter.add_filter(field_index, criteria)](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/add_filter/#int) come dimostrato di seguito. 

Si prega di vedere il seguente codice di esempio che carica il [file Excel di esempio](sample.xlsx) che contiene alcuni dati finti. Il codice di esempio utilizza tre metodi per filtrare le celle vuote. Poi salva il workbook come [file Excel di output](FilteredBlanks.xlsx). 

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filter-blanks.py" >}}

## **Come filtrare i non vuoti utilizzando la libreria Excel Aspose.Cells per Python**

Si prega di vedere il seguente codice di esempio che carica il [file Excel di esempio](sample.xlsx) che contiene alcuni dati fittizi. Dopo aver caricato il file, chiamare la funzione [AutoFilter.match_non_blanks(field_index)](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/match_non_blanks/#int) per filtrare i dati non vuoti e infine salvare il foglio di lavoro come [file Excel di output](FilteredNonBlanks.xlsx). 

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filter-non-blanks.py" >}}

