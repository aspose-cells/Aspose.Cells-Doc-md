---
title: Estrazione di dati tema da file Excel con C++
linktitle: Estrai dati del tema dai file Excel
description: Aspose.Cells è una libreria C++ per lavorare con file di fogli di calcolo. Supporta l estrazione di dati tema dai file Excel, consentendo agli utenti di ottenere informazioni sullo stile e la formattazione dei documenti. Questo articolo introdurrà come estrarre dati tema dai file Excel usando la libreria Aspose.Cells.
keywords: Aspose.Cells, File Excel, Dati del Tema, Stile, Formato
type: docs
weight: 120
url: /it/cpp/extract-theme-data-from-excel-file/
---

{{% alert color="primary" %}}

Aspose.Cells permette agli utenti di estrarre dati relativi al tema da un file Excel. Ad esempio, puoi estrarre il nome del tema applicato al workbook e il colore del tema applicato a una cella o ai bordi della cella, ecc.

Puoi applicare un tema al tuo workbook usando Microsoft Excel tramite il comando Layout di pagina > Temi.

{{% /alert %}}

## Codice C++ per estrarre dati tema dal file Excel

Il seguente esempio di codice estrae il nome del tema applicato al workbook di origine e poi estrae il colore del tema applicato alla cella A1 e il colore del tema applicato al bordo inferiore della cella.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object
    Workbook workbook(srcDir + u"source.xlsx");

    // Extract theme name applied to this workbook
    std::cout << "Theme: " << workbook.GetTheme().ToUtf8() << std::endl;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Get the style object
    Style style = cell.GetStyle();

    // Check if theme has foreground color defined
    if (style.GetForegroundThemeColor().IsNull())
    {
        std::cout << "Theme has not foreground color defined." << std::endl;
    }
    else
    {
        // Extract theme color applied to this cell
        std::cout << "Foreground Theme Color Type: " << static_cast<int>(style.GetForegroundThemeColor().GetColorType()) << std::endl;
    }

    // Extract theme color applied to the bottom border of the cell
    Border bot = style.GetBorders().Get(BorderType::BottomBorder);
    if (bot.GetThemeColor().IsNull())
    {
        std::cout << "Theme has not Border color defined." << std::endl;
    }
    else
    {
        std::cout << "Border Theme Color Type: " << static_cast<int>(bot.GetThemeColor().GetColorType()) << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
