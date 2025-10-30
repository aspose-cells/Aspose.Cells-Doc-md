---
title: Lettura e scrittura della tabella di query del foglio di lavoro con C++
linktitle: Lettura e Scrittura Tabelle Query del Foglio di lavoro di Aspose.Cells
type: docs
weight: 40
url: /it/cpp/reading-and-writing-query-table-of-worksheet/
description: Impara come leggere e scrivere tabelle di query nei fogli di lavoro Excel usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Aspose.Cells fornisce la collezione `Worksheet.QueryTables`, che restituisce un oggetto di tipo `QueryTable` per indice. Ha le seguenti due proprietà:

- `QueryTable.AdjustColumnWidth`
- `QueryTable.PreserveFormatting`

Entrambi sono valori booleani. Puoi visualizzarli in Microsoft Excel tramite **Dati > Connessioni > Proprietà**.

{{% /alert %}}

## Lettura e Scrittura della Tabella di Query del Foglio di Lavoro

Il codice di esempio seguente legge il primo `QueryTable` del primo foglio di lavoro e poi stampa entrambe le proprietà di `QueryTable`. Quindi imposta `QueryTable.PreserveFormatting` su `true`.

È possibile scaricare il file Excel di origine utilizzato in questo codice e il file Excel di output generato dal codice dai seguenti link.

- [File Excel di Origine](5115533.xlsx)
- [File Excel di Output](5115537.xlsx)

```c++
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

    // Create workbook from source excel file
    Workbook workbook(srcDir + u"Sample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first Query Table
    QueryTable qt = worksheet.GetQueryTables().Get(0);

    // Print Query Table Data
    std::cout << "Adjust Column Width: " << qt.GetAdjustColumnWidth() << std::endl;
    std::cout << "Preserve Formatting: " << qt.GetPreserveFormatting() << std::endl;

    // Now set Preserve Formatting to true
    qt.SetPreserveFormatting(true);

    // Save the workbook
    workbook.Save(outDir + u"Output_out.xlsx");

    std::cout << "Query Table properties updated and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### Output della console

Ecco la visualizzazione sulla console del codice di esempio sopra descritto:

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Recuperare l'intervallo di risultato della tabella di query

Aspose.Cells offre un'opzione per leggere l'indirizzo (cioè l'intervallo di celle risultato) di una tabella di query. Il codice seguente dimostra questa funzionalità leggendo l'indirizzo dell'intervallo di risultato di una tabella di query. Il file di esempio può essere scaricato [qui](72417290.xlsx).

```cpp
#include <iostream>
#include <locale>
#include <codecvt>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

std::string convert_u16_to_string(const char16_t* data) {
    std::wstring_convert<std::codecvt_utf8_utf16<char16_t>, char16_t> converter;
    return converter.to_bytes(data);
}

int main()
{
    Aspose::Cells::Startup();

    Workbook wb(u"Query TXT.xlsx");
    std::cout << convert_u16_to_string(wb.GetWorksheets().Get(0).GetQueryTables().Get(0).GetResultRange().GetAddress().GetData()) << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
