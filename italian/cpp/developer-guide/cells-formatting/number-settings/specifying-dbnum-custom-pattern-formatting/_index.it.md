---
title: Specificare la formattazione di pattern personalizzati DBNum con C++
linktitle: Specificare la formattazione del modello personalizzato DBNum
description: Aspose.Cells è una libreria C++ per lavorare con file di fogli di calcolo che supporta la formattazione di date e numeri usando pattern di formattazione personalizzati. Questo articolo mostrerà come usare la libreria Aspose.Cells per specificare il pattern di formattazione personalizzato dbnum per offrire agli utenti maggiore controllo su come vengono visualizzati i numeri.
keywords: Aspose.Cells, libreria C++, foglio di calcolo elettronico, pattern di formattazione personalizzato, formattazione, dbnum , controllo visualizzazione
type: docs
weight: 110
url: /it/cpp/specifying-dbnum-custom-pattern-formatting/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells supporta la formattazione di pattern personalizzati *DBNum*. Per esempio, se il valore della tua cella è 123 e tu specifichi la sua formattazione personalizzata come [DBNum2][$-804]General, verrà visualizzato come 壹佰贰拾叁. Puoi specificare la tua formattazione personalizzata della cella usando il metodo [**Cell.GetStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) e la proprietà [**Style.Custom**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/).

## **Codice di Esempio**

Il codice esempio seguente illustra come specificare il formato di pattern personalizzato *DBNum*. Si prega di controllare il [output PDF](43352081.pdf) per ulteriori aiuti.

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

    // Access cell A1 and put value 123
    Cell cell = ws.GetCells().Get(u"A1");
    cell.PutValue(123);

    // Access cell style
    Style st = cell.GetStyle();

    // Specifying DBNum custom pattern formatting
    st.SetCustom(u"[DBNum2][$-804]General", true);

    // Set the cell style
    cell.SetStyle(st);

    // Set the first column width
    ws.GetCells().SetColumnWidth(0, 30);

    // Save the workbook in output pdf format
    wb.Save(outDir + u"outputDBNumCustomFormatting.pdf", SaveFormat::Pdf);

    std::cout << "DBNum custom formatting applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
