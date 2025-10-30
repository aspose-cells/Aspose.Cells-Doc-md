---
title: Gestire i dati dei file Excel con C++
linktitle: Dati delle celle
type: docs
weight: 110
url: /it/cpp/view-and-edit-excel-data/
description: Questo articolo descrive come visualizzare e modificare i dati dei file Excel con la libreria Aspose.Cells utilizzando C++.
keywords: Aspose.Cells C++ Gestire i dati del file Excel, aggiungere dati al file Excel, recuperare dati dal file Excel, come migliorare l efficienza dell aggiunta di dati, gestire i dati delle celle, aggiornare i dati delle celle, ottenere i dati delle celle, inserire dati nelle celle
---

{{% alert color="primary" %}}

In [Accesso alle celle di un foglio di lavoro](/cells/it/cpp/accessing-cells-of-a-worksheet/), abbiamo discusso degli approcci di base per accedere alle celle in un foglio di lavoro. Questo articolo utilizza uno di quegli approcci per aggiungere diversi tipi di dati alle celle.

{{% /alert %}}

## **Come aggiungere dati alle celle**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una raccolta [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente di accedere a ciascun foglio di lavoro nel file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce una raccolta [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Ogni elemento della raccolta [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)

Aspose.Cells permette agli sviluppatori di aggiungere dati alle celle nei fogli di lavoro chiamando il metodo [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) della classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). Aspose.Cells fornisce versioni sovraccaricate del metodo [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) che consentono agli sviluppatori di aggiungere diversi tipi di dati alle celle. Utilizzando queste versioni sovraccaricate del metodo [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/), è possibile aggiungere valori booleani, stringhe, doppie, interi o valori data/ora, ecc. alla cella.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;

    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);


    worksheet.GetCells().Get(U16String(u"A1")).PutValue(U16String(u"Hello World"));
    worksheet.GetCells().Get(U16String(u"A2")).PutValue(20.5);
    worksheet.GetCells().Get(U16String(u"A3")).PutValue((int32_t)15);
    worksheet.GetCells().Get(U16String(u"A4")).PutValue(true);

    Cell cellA1 = worksheet.GetCells().Get(U16String(u"A4"));
    Style style = cellA1.GetStyle();
    style.SetNumber(15);
    cellA1.SetStyle(style);

    workbook.Save(outDir + u"output.out.xls");

    std::cout << "Data inserted and workbook saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Come migliorare l'efficienza**

Se si utilizza il metodo [**PutValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/putvalue/) per inserire una grande quantità di dati in un foglio di lavoro, è consigliabile aggiungere valori alle celle, prima per righe e poi per colonne. Questo approccio migliora notevolmente l'efficienza delle applicazioni.

## **Come recuperare i dati dalle celle**

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) che rappresenta un file di Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contiene una collezione [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) che consente di accedere ai fogli di lavoro nel file. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) fornisce una collezione [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Ogni elemento nella collezione [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) rappresenta un oggetto della classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

La classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) fornisce diverse proprietà che consentono agli sviluppatori di recuperare i valori dalle celle in base ai loro tipi di dati. Queste proprietà includono:

- [**StringValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstringvalue/): restituisce il valore di stringa della cella.
- [**DoubleValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/): restituisce il valore decimale della cella.
- [**BoolValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getboolvalue/): restituisce il valore booleano della cella.
- [**DateTimeValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdatetimevalue/): restituisce il valore data/ora della cella.
- [**FloatValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/): restituisce il valore in virgola mobile della cella.
- [**IntValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getintvalue/): restituisce il valore intero della cella.

Quando un campo non è compilato, le celle con [**DoubleValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdoublevalue/) o [**FloatValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getfloatvalue/) generano un'eccezione.

Il tipo di dati contenuti in una cella può anche essere verificato utilizzando la proprietà [**Type**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) della classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/). Infatti, la proprietà [**Type**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gettype/) della classe [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) si basa sull'enumerazione [**CellValueType**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvaluetype/), i cui valori predefiniti sono elencati di seguito:

|**Tipi di Valore della Cella**|**Descrizione**|
| :- | :- |
|IsBool| Specifica che il valore della cella è booleano.
|IsDateTime| Specifica che il valore della cella è data/ora.
|IsNull| Rappresenta una cella vuota.
|IsNumeric| Specifica che il valore della cella è numerico.
|IsString| Specifica che il valore della cella è una stringa.
|IsUnknown| Specifica che il valore della cella è sconosciuto.

È anche possibile utilizzare i tipi di valore di cella predefiniti sopra per confrontare con il tipo di dati presente in ogni cella.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + u"book1.xls";

    Workbook workbook(inputFilePath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    int maxRow = worksheet.GetCells().GetMaxDataRow();
    int maxCol = worksheet.GetCells().GetMaxDataColumn();

    for (int row = 0; row <= maxRow; row++)
    {
        for (int col = 0; col <= maxCol; col++)
        {
            Cell cell = worksheet.GetCells().Get(row, col);

            U16String stringValue;
            double doubleValue = 0.0;
            bool boolValue = false;

            switch (cell.GetType())
            {
                case CellValueType::IsString:
                    stringValue = cell.GetStringValue();
                    std::cout << "String Value: " << stringValue.ToUtf8() << std::endl;
                    break;

                case CellValueType::IsNumeric:
                    doubleValue = cell.GetDoubleValue();
                    std::cout << "Double Value: " << doubleValue << std::endl;
                    break;

                case CellValueType::IsBool:
                    boolValue = cell.GetBoolValue();
                    std::cout << "Bool Value: " << boolValue << std::endl;
                    break;

                case CellValueType::IsDateTime:
                    stringValue = cell.GetStringValue();
                    std::cout << "DateTime Value: " << stringValue.ToUtf8() << std::endl;
                    break;

                case CellValueType::IsUnknown:
                    stringValue = cell.GetStringValue();
                    std::cout << "Unknown Value: " << stringValue.ToUtf8() << std::endl;
                    break;

                case CellValueType::IsNull:
                    break;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Durante il lavoro sui fogli di lavoro, gli utenti possono aggiungere diversi tipi di dati nelle celle. Questi tipi di dati possono includere valori booleani, interi, in virgola mobile, testo o data/ora. Con Aspose.Cells, è possibile ottenere i valori appropriati dalle celle in base ai loro tipi di dati.

{{% /alert %}}

## **Argomenti avanzati**
- [Accesso alle celle di un foglio di lavoro](/cells/it/cpp/accessing-cells-of-a-worksheet/)
- [Converti Dati Numerici Testuali in Numero](/cells/it/cpp/convert-text-numeric-data-to-number/)
- [Creare i Subtotali](/cells/it/cpp/creating-subtotals/)
- [Filtraggio dei dati](/cells/it/cpp/data-filtering/)
- [Ordinamento dati](/cells/it/cpp/sort-data-of-excel/)
- [Convalida Dati](/cells/it/cpp/data-validation/)
- [Trova o cerca dati](/cells/it/cpp/find-or-search-data/)
- [Ottieni il valore stringa della cella con e senza formattazione](/cells/it/cpp/get-cell-string-value-with-and-without-formatting/)
- [Aggiunta di testo ricco in formato HTML all'interno della cella](/cells/it/cpp/adding-html-rich-text-inside-the-cell/)
- [Inserimento di collegamenti ipertestuali in Excel o OpenOffice](/cells/it/cpp/insert-hyperlinks-to-excel/)
- [Come e dove utilizzare gli enumeratori](/cells/it/cpp/how-and-where-to-use-enumerators/)
- [Misurare la larghezza e l'altezza del valore della cella in unità di pixel](/cells/it/cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)
- [Lettura dei valori della cella in più thread contemporaneamente](/cells/it/cpp/reading-cell-values-in-multiple-threads-simultaneously/)
- [Conversione tra nome della cella e indice riga/colonna](/cells/it/cpp/names-and-indices/)
- [Popolare prima i dati per riga e poi per colonna](/cells/it/cpp/populate-data-first-by-row-then-by-column/)
- [Conserva il prefisso apice singolo del valore della cella o dell'intervallo](/cells/it/cpp/preserve-single-quote-prefix-of-cell-value-or-range/)
- [Accedere e aggiornare le porzioni di testo arricchito della cella](/cells/it/cpp/access-and-update-the-portions-of-rich-text-of-cell/)
{{< app/cells/assistant language="cpp" >}}
