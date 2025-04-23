---
title: Leggi e scrivi tabella con origine dati QueryTable con C++
linktitle: Leggi e Scrivi Tabella con Origine Dati Tabella Query
type: docs
weight: 30
url: /it/cpp/read-and-write-table-with-query-table-data-source/
description: Scopri come leggere e scrivere tabelle con QueryTable come origine dati usando Aspose.Cells for C++.
---

## **Leggere e scrivere una tabella con dati della tabella di query**
Con Aspose.Cells, puoi leggere e scrivere una tabella che ha una QueryTable come origine dati. il supporto per questa funzione esiste anche per i file XLS. Il seguente esempio di codice dimostra come leggere e scrivere una tale tabella, leggendo prima la tabella e poi modificandola per aggiungere la riga dei totali.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load workbook object
    Workbook workbook(srcDir + u"SampleTableWithQueryTable.xls");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first ListObject (Table) in the worksheet
    ListObject table = worksheet.GetListObjects().Get(0);

    // Check the data source type if it is query table
    if (table.GetDataSourceType() == TableDataSourceType::QueryTable)
    {
        table.SetShowTotals(true);
    }

    // Save the file
    workbook.Save(outDir + u"SampleTableWithQueryTable_out.xls");

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

I file Excel di origine e di output sono allegati a scopo di riferimento.

[File di origine](96928091.xls)

[File di output](96928092.xls)
