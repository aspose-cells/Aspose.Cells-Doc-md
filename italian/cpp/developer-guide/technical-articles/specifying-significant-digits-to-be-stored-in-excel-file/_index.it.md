---
title: Specificare le cifre significative da memorizzare in un file Excel con C++
linktitle: Specificare le cifre significative
type: docs
weight: 30
url: /it/cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: Scopri come specificare le cifre significative da memorizzare nei file Excel usando Aspose.Cells con C++.
---

## **Possibili Scenari di Utilizzo**

Di default, Aspose.Cells memorizza 17 cifre significative di valori double all’interno del file Excel, a differenza di MS-Excel che ne memorizza solo 15. Puoi modificare il comportamento predefinito di Aspose.Cells da 17 a 15 cifre significative usando la proprietà [**GetSignificantDigits()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/getsignificantdigits/).

## **Specifica delle cifre significative da memorizzare nel file Excel**

Il seguente esempio di codice impone ad Aspose.Cells di usare 15 cifre significative durante la memorizzazione di valori double nel file Excel. Controlla il file Excel di output [22774105.xlsx](https://example.com). Cambia l’estensione in .zip, estrailo, e vedrai che sono memorizzate solo 15 cifre significative. Lo screenshot seguente spiega l’effetto della proprietà [**GetSignificantDigits()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/getsignificantdigits/) sul file Excel di output.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

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

    // By default, Aspose.Cells stores 17 significant digits unlike
    // MS-Excel which stores only 15 significant digits
    CellsHelper::SetSignificantDigits(15);

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell c = worksheet.GetCells().Get(u"A1");

    // Put double value, only 15 significant digits as specified by
    // CellsHelper.SignificantDigits above will be stored in excel file just like MS-Excel does
    c.PutValue(1234567890.123451711);

    // Save the workbook
    workbook.Save(outDir + u"out_SignificantDigits.xlsx");

    std::cout << "Workbook saved successfully with significant digits set to 15!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
