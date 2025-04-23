---
title: Ottimizzazione dell uso della memoria durante il lavoro con grandi file con grandi dataset con C++
linktitle: Ottimizzazione dell uso della memoria
type: docs
weight: 180
url: /it/cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
description: Impara come ottimizzare l uso della memoria durante il lavoro con grandi file Excel usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Quando si costruisce un workbook con grandi set di dati o si legge un grande file Microsoft Excel, la quantità totale di RAM che il processo richiederà è sempre una preoccupazione. Esistono misure che possono essere adottate per far fronte alla sfida. Aspose.Cells fornisce alcune opzioni rilevanti e chiamate API per ridurre e ottimizzare l'uso della memoria. Inoltre, può aiutare il processo a lavorare in modo più efficiente e più veloce.

Usa l'opzione [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) per ottimizzare l'uso della memoria per i dati delle celle e diminuire il costo complessivo della memoria. Quando si costruisce un ampio set di dati per le celle, può risparmiare una certa quantità di memoria rispetto all'utilizzo dell'impostazione predefinita ([**MemorySetting.Normal**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/)).

{{% /alert %}}

## **Ottimizzazione della Memoria**

### **Lettura di File Excel di Grandi Dimensioni**

L'esempio seguente mostra come leggere un grande file Microsoft Excel in modalità ottimizzata.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Specify the LoadOptions
    LoadOptions opt;

    // Set the memory preferences
    opt.SetMemorySetting(MemorySetting::MemoryPreference);

    // Instantiate the Workbook
    // Load the Big Excel file having large Data set in it
    Workbook wb(srcDir + u"Book1.xlsx", opt);

    std::cout << "Workbook loaded successfully with memory preference setting!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Scrittura di file Excel di grandi dimensioni**

L'esempio seguente mostra come scrivere un ampio dataset in un foglio di lavoro in modalità ottimizzata.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook wb;

    // Set the memory preferences
    // Note: This setting cannot take effect for the existing worksheets that are created before using the below line of code
    wb.GetSettings().SetMemorySetting(MemorySetting::MemoryPreference);

    // Note: The memory settings also would not work for the default sheet i.e., "Sheet1" etc. automatically created by the Workbook

    // To change the memory setting of existing sheets, please change memory setting for them manually:
    Cells cells = wb.GetWorksheets().Get(0).GetCells();
    cells.SetMemorySetting(MemorySetting::MemoryPreference);

    // Input large dataset into the cells of the worksheet.
    // Your code goes here.
    // .........

    // Get cells of the newly created Worksheet "Sheet2" whose memory setting is same with the one defined in WorkbookSettings:
    cells = wb.GetWorksheets().Add(u"Sheet2").GetCells();

    // Input large dataset into the cells of the worksheet.
    // Your code goes here.
    // .........

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Attenzione**

L'opzione predefinita, [**MemorySetting.Normal**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) è applicata per tutte le versioni. Per alcune situazioni, come la costruzione di un workbook con un ampio set di dati per le celle, l'opzione [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) può ottimizzare l'uso della memoria e ridurre il costo della memoria dell'applicazione. Tuttavia, questa opzione può degradare le prestazioni in alcuni casi speciali come segue.

1. **Accesso Casuale e Ripetuto alle Celle**: La sequenza più efficiente per accedere alla collezione di celle è cella per cella in una riga e poi riga per riga. In particolare, se si accedono alle righe/celle tramite l'Enumerator acquisito da [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/), [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/) e [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/), le prestazioni sarebbero massimizzate con [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/).
1. **Inserimento ed eliminazione di celle e righe**: Si noti che se ci sono molte operazioni di inserimento/eliminazione per Celle/Righe, la degradazione delle prestazioni sarà notevole per la modalità *MemoryPreference* rispetto alla modalità *Normale*.
1. **Operare su diversi tipi di celle**: Se la maggior parte delle celle contiene valori di stringa o formule, il costo della memoria sarà lo stesso della modalità *Normale*, ma se ci sono molte celle vuote, o i valori delle celle sono numerici, booleani e così via, l'opzione [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) darà migliori prestazioni.
