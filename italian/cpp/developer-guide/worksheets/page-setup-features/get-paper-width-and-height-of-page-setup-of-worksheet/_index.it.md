---
title: Ottenere larghezza e altezza della carta dalla configurazione della pagina del foglio di lavoro con C++
linktitle: Ottenere larghezza e altezza della configurazione della pagina
type: docs
weight: 50
url: /it/cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Impara come ottenere la larghezza e l altezza della carta della configurazione della pagina di un foglio di lavoro Excel usando il codice C++ in modo programmatico con l API Aspose.Cells for C++.
keywords: larghezza carta configurazione pagina Excel C++, altezza carta configurazione pagina Excel C++
---

## **Possibili Scenari di Utilizzo**

 A volte, è necessario conoscere la larghezza e l'altezza della carta come impostato nella configurazione della pagina del foglio di lavoro. Utilizza i metodi [**GetPaperWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperwidth/) e [**GetPaperHeight()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperheight/) a questo scopo.

## **Ottenere larghezza e altezza della pagina di configurazione del foglio di lavoro**

 Il seguente codice di esempio spiega come usare i metodi [**GetPaperWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperwidth/) e [**GetPaperHeight()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperheight/). Innanzitutto cambia la dimensione della carta in *A2* e trova la larghezza e l'altezza della carta, poi la modifica in *A3*, *A4*, *Lettera* e trova rispettivamente larghezza e altezza della carta.

### **Codice di Esempio**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook class
    Workbook book;

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Set paper size to A2 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA2);
    cout << "PaperA2: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to A3 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA3);
    cout << "PaperA3: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to A4 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);
    cout << "PaperA4: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to Letter and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperLetter);
    cout << "PaperLetter: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Output della console**

Ecco l'output della console del codice di esempio sopra.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
