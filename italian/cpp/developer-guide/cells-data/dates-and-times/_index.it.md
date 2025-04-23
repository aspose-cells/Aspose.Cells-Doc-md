---
title: Come gestire date e orari con C++
linktitle: Come gestire le date e gli orari
type: docs
weight: 600
url: /it/cpp/how-to-manage-dates-and-times/
description: Impara come gestire date e orari tramite l API Aspose.Cells for C++.
keywords: Come gestire date e orari, Il sistema di data 1900, Il sistema di data 1904, Imposta date e orari, Ottieni date e orari, Gestisci date e orari, Archivia date e orari in Excel, Visualizza date e orari nelle celle.
---

## **Come archiviare date e orari in Excel**
Le date e gli orari sono memorizzati nelle celle come numeri. Pertanto, i valori delle celle contenenti date e orari sono di tipo numerico. Un numero che specifica una data e un'ora consiste nelle componenti di data (parte intera) e ora (parte frazionale). Il metodo `Cell::GetDoubleValue()` restituisce questo numero.

## **Come visualizzare date e orari in Aspose.Cells**
Per visualizzare un numero come data e ora, applica il formato di data e ora richiesto a una cella tramite il metodo `Style::SetNumber()` o `Style::SetCustom()`. Il metodo `Cell::GetDateTimeValue()` restituisce l'oggetto `DateTime`, che specifica la data e l'ora rappresentate dal numero contenuto in una cella.
<br>
<image src="1.png" width="70%" />

## **Come passare da un sistema di date a un altro in Aspose.Cells**
MS-Excel archivia le date come numeri chiamati valori seriali. Un valore seriale è un intero che rappresenta il numero di giorni trascorsi dal primo giorno nel sistema di date. Excel supporta i seguenti sistemi di data per i valori seriali:

1. Il sistema di data 1900. La prima data è il 1 gennaio 1900 e il suo valore seriale è 1. L'ultima data è il 31 dicembre 9999 e il suo valore seriale è 2.958.465. Questo sistema di data è utilizzato nel foglio di lavoro per impostazione predefinita.
1. Il sistema di data 1904. La prima data è 1 gennaio 1904, e il suo valore seriale è 0. L'ultima data è 31 dicembre 9999, e il suo valore seriale è 2.957.003. Per usare questo sistema di data nel workbook, imposta la proprietà `Workbook::GetSettings()->SetDate1904(true)`.

Questo esempio mostra che i valori seriali archiviati nella stessa data in sistemi di date diversi sono diversi.
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook workbook;
    workbook.GetSettings().SetDate1904(false);

    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    a1.PutValue(45237.0);

    if (a1.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A1 is Numeric Value: " << a1.GetDoubleValue() << std::endl;
    }

    workbook.GetSettings().SetDate1904(true);
    std::cout << "use The 1904 date system====================" << std::endl;

    Cell a2 = cells.Get(u"A2");
    a2.PutValue(43775.0);

    if (a2.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A2 is Numeric Value: " << a2.GetDoubleValue() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
Risultato in output:
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

## **Come impostare il valore di data e ora in Aspose.Cells**
Questo esempio imposta un valore `DateTime` nelle celle A1 e A2, imposta un formato personalizzato per A1 e un formato numerico per A2, e successivamente mostra i tipi di valore.

```c++
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    time_t now = time(nullptr);
    double oaDate1 = static_cast<double>(now) / (60 * 60 * 24) + 25569.0;
    a1.PutValue(oaDate1);

    if (a1.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A1 is Numeric Value: " << a1.IsNumericValue() << std::endl;
    }

    Style a1Style = a1.GetStyle();
    a1Style.SetCustom(u"mm-dd-yy hh:mm:ss", true);
    a1.SetStyle(a1Style);

    if (a1.GetType() == CellValueType::IsDateTime)
    {
        std::cout << "Cell A1 contains a DateTime value." << std::endl;
    }
    else
    {
        std::cout << "Cell A1 does not contain a DateTime value." << std::endl;
    }

    Cell a2 = cells.Get(u"A2");
    now = time(nullptr);
    double oaDate2 = static_cast<double>(now) / (60 * 60 * 24) + 25569.0;
    a2.SetValue(oaDate2);

    if (a2.GetType() == CellValueType::IsNumeric)
    {
        std::cout << "A2 is Numeric Value: " << a2.IsNumericValue() << std::endl;
    }

    Style a2Style = a2.GetStyle();
    a2Style.SetNumber(22);
    a2.SetStyle(a2Style);

    if (a2.GetType() == CellValueType::IsDateTime)
    {
        std::cout << "Cell A2 contains a DateTime value." << std::endl;
    }
    else
    {
        std::cout << "Cell A2 does not contain a DateTime value." << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

Risultato in output:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

## **Come ottenere il valore di data e ora in Aspose.Cells**
Questo esempio imposta un valore `DateTime` nelle celle A1 e A2, imposta un formato personalizzato per A1 e un formato numerico per A2, verifica i tipi di valore di entrambe le celle e visualizza poi il valore `DateTime` e la stringa formattata.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell a1 = cells.Get(u"A1");
    a1.PutValue(Date{2023, 5, 15});

    if (a1.GetType() == CellValueType::IsNumeric) {
        std::cout << "A1 is Numeric Value: " << a1.IsNumericValue() << std::endl;
    }

    Style a1Style = a1.GetStyle();
    a1Style.SetCustom(u"mm-dd-yy hh:mm:ss", true);
    a1.SetStyle(a1Style);

    if (a1.GetType() == CellValueType::IsDateTime) {
        std::cout << "Cell A1 contains a DateTime value." << std::endl;
        Date dateTimeValue = a1.GetDateTimeValue();
        std::cout << "A1 DateTime String Value: " << a1.GetStringValue().ToUtf8() << std::endl;
    }
    else {
        std::cout << "Cell A1 does not contain a DateTime value." << std::endl;
    }

    Cell a2 = cells.Get(u"A2");
    a2.PutValue(Date{2023, 5, 16});

    if (a2.GetType() == CellValueType::IsNumeric) {
        std::cout << "A2 is Numeric Value: " << a2.IsNumericValue() << std::endl;
    }

    Style a2Style = a2.GetStyle();
    a2Style.SetNumber(22);
    a2.SetStyle(a2Style);

    if (a2.GetType() == CellValueType::IsDateTime) {
        std::cout << "Cell A2 contains a DateTime value." << std::endl;
        Date dateTimeValue = a2.GetDateTimeValue();
        std::cout << "A2 DateTime String Value: " << a2.GetStringValue().ToUtf8() << std::endl;
    }
    else {
        std::cout << "Cell A2 does not contain a DateTime value." << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

Risultato in output:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A1 DateTime Value: 11/23/2023 5:59:09 PM
A1 DateTime String Value: 11-23-23 17:59:09
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
A2 DateTime Value: 11/23/2023 5:59:09 PM
A2 DateTime String Value: 11/23/2023 17:59
```
