---
title: Utilizzo di stili incorporati con C++
linktitle: Uso degli Stili Incorporati
type: docs
weight: 80
url: /it/cpp/using-built-in-styles/
description: Codice C++ per usare gli stili incorporati di Excel con API Aspose.Cells for C++
keywords: c++ utilizza stili incorporati di Excel, applica programmativamente gli stili nel workbook, applica programmativamente gli stili nel workbook, c++ application degli stili incorporati in Excel, c++ application degli stili incorporati nel workbook, codice c++ applica gli stili incorporati nel workbook, codice c++ applica gli stili incorporati nel foglio di lavoro Excel
---

{{% alert color="primary" %}}

Aspose.Cells fornisce una vasta raccolta di stili riutilizzabili per formattare una cella in un documento di foglio di calcolo. Possiamo utilizzare stili predefiniti nel nostro foglio di lavoro e creare anche stili personalizzati.

{{% /alert %}}

## **Come utilizzare gli stili incorporati**

Il metodo [**Workbook.CreateBuiltinStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/createbuiltinstyle/) e l'enumerazione [**BuiltinStyleType**](https://reference.aspose.com/cells/cpp/aspose.cells/builtinstyletype/) rendono comodo l'uso degli stili incorporati. Ecco un elenco di tutti gli stili incorporati possibili:

- TWENTY_PERCENT_ACCENT_1
- TWENTY_PERCENT_ACCENT_2
- TWENTY_PERCENT_ACCENT_3
- TWENTY_PERCENT_ACCENT_4
- TWENTY_PERCENT_ACCENT_5
- VENTI_PERC_ACCENTO_6
- QUARANTA_PERC_ACCENTO_1
- QUARANTA_PERC_ACCENTO_2
- QUARANTA_PERC_ACCENTO_3
- QUARANTA_PERC_ACCENTO_4
- QUARANTA_PERC_ACCENTO_5
- QUARANTA_PERC_ACCENTO_6
- SESSANTA_PERC_ACCENTO_1
- SESSANTA_PERC_ACCENTO_2
- SESSANTA_PERC_ACCENTO_3
- SESSANTA_PERC_ACCENTO_4
- SESSANTA_PERC_ACCENTO_5
- SESSANTA_PERC_ACCENTO_6
- ACCENTO_1
- ACCENTO_2
- ACCENTO_3
- ACCENTO_4
- ACCENTO_5
- ACCENTO_6
- CATTIVO
- CALCOLO
- CONTROLLA_CELLA
- VIRGOLA
- VIRGOLA_1
- VALUTA
- VALUTA_1
- TESTO_ESPLICATIVO
- BUONO
- INTESTAZIONE_1
- INTESTAZIONE_2
- INTESTAZIONE_3
- INTESTAZIONE_4
- HYPERLINK
- COLLEGAMENTO_IPERTESTO_SEGUITO
- INPUT
- CELLA_COLLEGATA
- NEUTRO
- NORMALE
- NOTA
- OUTPUT
- PERCENTUALE
- TITOLO
- TOTALE
- TESTO_AVVISO
- LIVELLO_RIGA
- LIVELLO_COLONNA

## Codice C++ per usare gli stili incorporati

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output file paths
    U16String output1Path = srcDir + u"Output.xlsx";
    U16String output2Path = srcDir + u"Output.out.ods";

    // Create a new workbook
    Workbook workbook;

    // Create a built-in style of type Title
    Style style = workbook.CreateBuiltinStyle(BuiltinStyleType::Title);

    // Get the first worksheet and its cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Access cell A1 and set its value and style
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Aspose");
    cell.SetStyle(style);

    // Auto-fit the first column and row
    worksheet.AutoFitColumn(0);
    worksheet.AutoFitRow(0);

    // Save the workbook to the first output path
    workbook.Save(output1Path);
    std::cout << "File saved " << output1Path.ToUtf8() << std::endl;

    // Save the workbook to the second output path
    workbook.Save(output2Path);
    std::cout << "File saved " << output2Path.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
