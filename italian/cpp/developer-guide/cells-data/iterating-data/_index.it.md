---
title: Come e Dove Usare gli Enumeratori con C++
linktitle: Iterare i dati
type: docs
weight: 55
url: /it/cpp/how-and-where-to-use-enumerators/
description: Impara come Come e Dove Usare gli Enumeratori tramite l API Aspose.Cells for C++.
keywords: Come utilizzare gli enumeratori, enumeratore celle, enumeratore righe, enumeratore colonne
---

{{% alert color="primary" %}}

 Un enumeratore è un oggetto che consente di attraversare un contenitore o una collezione. Gli enumeratori possono essere usati per leggere i dati nella collezione, ma non possono essere usati per modificare la collezione sottostante, mentre IEnumerable è un'interfaccia che definisce un metodo GetEnumerator che restituisce un'interfaccia IEnumerator, che, a sua volta, permette l'accesso in sola lettura a una collezione.

Le API di Aspose.Cells forniscono una serie di enumeratori, tuttavia, questo articolo discute principalmente dei tre tipi come di seguito elencati.

1. Enumeratore celle
1. Enumeratore righe
1. Enumeratore colonne

{{% /alert %}}

## **Come utilizzare gli enumeratori**

### **Enumeratore celle**

Esistono vari modi per accedere all'enumeratore delle celle, e si può utilizzare uno qualsiasi di questi metodi in base ai requisiti dell'applicazione. Ecco i metodi che restituiscono l'enumeratore delle celle.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getenumerator/)
1. [**Row.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getenumerator/)
1. [**Range.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/range/getenumerator/)

Tutti i metodi sopra menzionati restituiscono l'enumeratore che consente di attraversare la raccolta di celle che sono state inizializzate.

{{% alert color="primary" %}}

Durante il passaggio delle celle, la raccolta non dovrebbe essere modificata (operazioni che causeranno l'istantanea di una nuova Cell o la cancellazione di una Cell esistente). In caso contrario, l'enumeratore potrebbe non essere in grado di attraversare correttamente tutte le celle (alcuni elementi potrebbero essere attraversati più volte o saltati).

{{% /alert %}}

Nell'esempio di codice seguente viene dimostrata l'implementazione dell'interfaccia IEnumerator per una raccolta di celle.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load a file in an instance of Workbook
    Workbook book(srcDir + u"sample.xlsx");

    // Get the enumerator from Cells collection
    auto cellEnumerator = book.GetWorksheets().Get(0).GetCells().GetEnumerator();
    // Traverse cells in the collection
    while (cellEnumerator.MoveNext())
    {
        auto cell = cellEnumerator.GetCurrent();
        std::cout << cell.GetName().ToUtf8() << " " << cell.GetValue().ToString().ToUtf8() << std::endl;
    }

    // Get enumerator from an object of Row
    auto rowEnumerator = book.GetWorksheets().Get(0).GetCells().GetRows().Get(0).GetEnumerator();
    // Traverse cells in the given row
    while (rowEnumerator.MoveNext())
    {
        auto cell = rowEnumerator.GetCurrent();
        std::cout << cell.GetName().ToUtf8() << " " << cell.GetValue().ToString().ToUtf8() << std::endl;
    }

    // Get enumerator from an object of Range
    auto rangeEnumerator = book.GetWorksheets().Get(0).GetCells().CreateRange(u"A1:B10").GetEnumerator();
    // Traverse cells in the range
    while (rangeEnumerator.MoveNext())
    {
        auto cell = rangeEnumerator.GetCurrent();
        std::cout << cell.GetName().ToUtf8() << " " << cell.GetValue().ToString().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

### **Enumeratore di righe**

 L'Enumerator delle Righe può essere accesso durante l'utilizzo del metodo [**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/getenumerator/). Il seguente esempio di codice dimostra l'implementazione dell'interfaccia IEnumerator per [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/).

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load a file in an instance of Workbook
    Workbook book(srcDir + u"sample.xlsx");

    // Get the enumerator for RowCollection
    auto rowsEnumerator = book.GetWorksheets().Get(0).GetCells().GetRows().GetEnumerator();

    // Traverse rows in the collection
    while (rowsEnumerator.MoveNext())
    {
        auto row = rowsEnumerator.GetCurrent();
        std::cout << row.GetIndex() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

### ** Ottieni Colonne Get**

 Le Colonne possono essere accesso durante l'utilizzo del metodo [**ColumnCollection.Get**](https://reference.aspose.com/cells/cpp/aspose.cells/columncollection/get/). Il seguente esempio di codice dimostra l'implementazione del metodo Get per [**ColumnCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/columncollection/).

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook book(srcDir + u"sample.xlsx");

    auto cells = book.GetWorksheets().Get(0).GetCells();
    auto columns = cells.GetColumns();

    for (int i = 0; i < columns.GetCount(); ++i)
    {
        auto col = columns.Get(i);
        std::cout << col.GetIndex() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Dove utilizzare gli enumeratori**

Per discutere i vantaggi dell'uso degli enumeratori, prendiamo un esempio in tempo reale.

**Scenario**

 Un requisito dell'applicazione è attraversare tutte le celle di un [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) dato per leggere i loro valori. Potrebbero esserci diversi modi per implementare questo obiettivo. Alcuni sono dimostrati di seguito.

### **Utilizzo della gamma di visualizzazione**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Load a file in an instance of Workbook
    Workbook book(inputFilePath);

    // Get Cells collection of first worksheet
    Cells cells = book.GetWorksheets().Get(0).GetCells();

    // Get the MaxDisplayRange
    Range displayRange = cells.GetMaxDisplayRange();

    // Loop over all cells in the MaxDisplayRange
    for (int row = displayRange.GetFirstRow(); row < displayRange.GetRowCount(); row++)
    {
        for (int col = displayRange.GetFirstColumn(); col < displayRange.GetColumnCount(); col++)
        {
            // Read the Cell value
            std::cout << displayRange.Get(row, col).GetStringValue().ToUtf8() << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
}
```

### **Utilizzo di MaxDataRow e MaxDataColumn**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load a file in an instance of Workbook
    Workbook book(srcDir + u"sample.xlsx");

    // Get Cells collection of first worksheet
    auto cells2 = book.GetWorksheets().Get(0).GetCells();

    // Get maximum data row and column
    int maxDataRow = cells2.GetMaxDataRow();
    int maxDataColumn = cells2.GetMaxDataColumn();

    // Loop over all cells
    for (int row = 0; row <= maxDataRow; row++)
    {
        for (int col = 0; col <= maxDataColumn; col++)
        {
            // Read the Cell value
            auto currentCell = cells2.GetCell(row, col);
            if (!currentCell.IsNull())
            {
                cout << currentCell.GetStringValue().ToUtf8() << endl;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

Come puoi osservare, entrambi gli approcci sopra menzionati utilizzano più o meno una logica simile, cioè; attraversa tutte le celle nella raccolta per leggere i valori delle celle. Questo potrebbe essere problematico per un certo numero di motivi come discusso di seguito.

1. API come [**GetMaxRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxrow/), [**GetMaxDataRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatarow/), [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxcolumn/), [**GetMaxDataColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdatacolumn/) & [**GetMaxDisplayRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) richiedono tempo extra per raccogliere le statistiche corrispondenti. Nel caso in cui la matrice di dati (righe x colonne) sia grande, utilizzare queste API potrebbe influire sulle prestazioni.
1. Nella maggior parte dei casi, non tutte le celle in un dato intervallo sono istanziate. In tali situazioni controllare ogni cella nella matrice non è così efficiente rispetto al controllo solo delle celle inizializzate.
1. Accedere a una cella in un ciclo come celle riga, colonna farà istanziare tutti gli oggetti cella in un intervallo, che potrebbe alla fine causare OutOfMemoryException.

## **Conclusioni**

Sulla base dei fatti sopra menzionati, di seguito sono riportati i possibili scenari in cui dovrebbero essere utilizzati gli enumeratori.

1. È richiesto l'accesso in sola lettura alla collezione di celle, cioè; il requisito è di ispezionare solo le celle.
1. Deve essere attraversato un gran numero di celle.
1. Si devono attraversare solo le celle/righe/colonne inizializzate.
{{< app/cells/assistant language="cpp" >}}
