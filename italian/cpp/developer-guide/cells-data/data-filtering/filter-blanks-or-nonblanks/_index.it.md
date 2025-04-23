---
title: Come filtrare valori vuoti o non vuoti con C++
linktitle: Come Filtrare Spazi Vuoti o Non Spazi Vuoti
type: docs
weight: 85
url: /it/cpp/how-to-filter-blanks-and-non-blanks/
description: Impara come filtrare valori vuoti e non vuoti usando l API Aspose.Cells for C++.
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
Se una colonna contiene testo in modo tale che alcune celle sono vuote e è necessario filtrare per selezionare solo quelle righe in cui ci sono celle vuote, le funzioni [AutoFilter.MatchBlanks(int fieldIndex)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/matchblanks/) e [AutoFilter.AddFilter(int fieldIndex, string criteria)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/addfilter/) possono essere usate come mostrato di seguito. 

Si prega di vedere il seguente codice di esempio che carica il [file Excel di esempio](sample.xlsx) che contiene alcuni dati finti. Il codice di esempio utilizza tre metodi per filtrare le celle vuote. Poi salva il workbook come [file Excel di output](FilteredBlanks.xlsx). 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Open the Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Method 1: Call MatchBlanks function to apply the filter
    // worksheet.GetAutoFilter().MatchBlanks(1);

    // Method 2: Call AddFilter function and set criteria to ""
    // worksheet.GetAutoFilter().AddFilter(1, u"");

    // Method 3: Call AddFilter function and set criteria to nullptr
    worksheet.GetAutoFilter().AddFilter(1, nullptr);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Saving the modified Excel file
    workbook.Save(u"FilteredBlanks.xlsx");

    std::cout << "Excel file modified and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Come filtrare le celle non vuote utilizzando Aspose.Cells**

Si prega di vedere il seguente esempio di codice che carica il [file Excel di esempio](sample.xlsx) che contiene alcuni dati di prova. Dopo aver caricato il file, chiamare la funzione [AutoFilter.MatchNonBlanks(int fieldIndex)](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/matchnonblanks/) per filtrare i dati non vuoti, e infine salvare il foglio di lavoro come [file Excel di output](FilteredNonBlanks.xlsx). 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook by opening an existing Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet in the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Call MatchNonBlanks function to apply the filter on the second column (index 1)
    worksheet.GetAutoFilter().MatchNonBlanks(1);

    // Call refresh function to update the worksheet
    worksheet.GetAutoFilter().Refresh();

    // Save the modified Excel file
    workbook.Save(u"FilteredNonBlanks.xlsx");

    std::cout << "Filtered non-blanks saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```


