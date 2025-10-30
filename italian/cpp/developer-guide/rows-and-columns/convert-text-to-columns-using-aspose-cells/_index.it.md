---
title: Convertire il testo in colonne usando Aspose.Cells con C++
linktitle: Converti Testo in Colonne
type: docs
weight: 30
url: /it/cpp/convert-text-to-columns-using-aspose-cells/
description: Impara come convertire il testo in colonne nei file Excel utilizzando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Puoi convertire il tuo testo in colonne utilizzando Microsoft Excel. Questa funzione è disponibile da *Strumenti dati* nella scheda *Dati*. Per dividere i contenuti di una colonna in più colonne, i dati devono contenere un delimitatore specifico come una virgola (o qualsiasi altro carattere) in base al quale Microsoft Excel dividerà i contenuti di una cella in più celle. Anche Aspose.Cells fornisce questa funzione tramite il metodo [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/)

## **Converti testo in colonne utilizzando Aspose.Cells**

Il seguente esempio di codice spiega l'uso del metodo [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/). Il codice prima aggiunge alcuni nomi di persone nella colonna A del primo foglio di lavoro. Il nome e il cognome sono separati da uno spazio. Poi applica il metodo [**Worksheet.Cells.TextToColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/texttocolumns/) sulla colonna A e lo salva come file Excel di output. Se apri il [file Excel di output](25395213.xlsx), vedrai che i nomi sono in colonna A mentre i cognomi in colonna B come mostrato in questo screenshot.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)

## **Codice di Esempio**

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

    // Create a workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Add people name in column A. Fast name and Last name are separated by space.
    ws.GetCells().Get(u"A1").PutValue(u"John Teal");
    ws.GetCells().Get(u"A2").PutValue(u"Peter Graham");
    ws.GetCells().Get(u"A3").PutValue(u"Brady Cortez");
    ws.GetCells().Get(u"A4").PutValue(u"Mack Nick");
    ws.GetCells().Get(u"A5").PutValue(u"Hsu Lee");

    // Create text load options with space as separator
    TxtLoadOptions opts;
    opts.SetSeparator(u' ');

    // Split the column A into two columns using TextToColumns() method
    // Now column A will have first name and column B will have second name
    ws.GetCells().TextToColumns(0, 0, 5, opts);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"outputTextToColumns.xlsx");

    std::cout << "Text to columns conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
