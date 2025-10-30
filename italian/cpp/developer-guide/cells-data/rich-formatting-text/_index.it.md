---
title: Accedi e aggiorna le porzioni di testo ricco della cella con C++
linktitle: Formattazione del testo arricchito
type: docs
weight: 40
url: /it/cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Impara come accedere e aggiornare le porzioni di testo ricco della cella tramite l API Aspose.Cells for C++.
keywords: Accedere e aggiornare il testo formattato ricco della cella, ottenere il testo formattato ricco della cella, modificare il testo formattato ricco della cella, accedere al testo formattato ricco della cella, aggiornare il testo formattato ricco della cella, modificare il testo formattato ricco della cella
---

{{% alert color="primary" %}}

Aspose.Cells ti consente di accedere e aggiornare le porzioni di testo formattato della cella. A questo scopo, puoi utilizzare i metodi [**Cell->GetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcharacters/) e [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/). Questi metodi restituiranno e accetteranno l'array di [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/) oggetti che potrai utilizzare per accedere e aggiornare varie proprietà del font come nome del font, colore del font, grassetto, ecc.

{{% /alert %}}

## **Accedere e aggiornare le porzioni di testo arricchito della cella**

Il seguente codice dimostra l'uso dei metodi [**Cell->GetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcharacters/) e [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/) usando il [file excel di origine](5112369.xlsx). Il file excel di origine contiene un testo ricco nella cella A1 con 3 porzioni, ognuna con un font diverso. Il codice accede a queste porzioni e aggiorna il font della prima porzione a **"Arial"**. Il libro modificato viene salvato come [file excel di output](5112366.xlsx).

### Codice C++ per accedere e aggiornare le porzioni di testo ricco

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputPath = srcDir + u"Sample.xlsx";
    U16String outputPath = outDir + u"Output.out.xlsx";

    Workbook workbook(inputPath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Cell cell = worksheet.GetCells().Get(U16String(u"A1"));

    std::cout << "Before updating the font settings...." << std::endl;

    Vector<FontSetting> fnts = cell.GetCharacters();

    for (int i = 0; i < fnts.GetLength(); ++i)
    {
        FontSetting& fs = fnts[i];
        std::cout << fs.GetFont().GetName().ToUtf8() << std::endl;
    }

    if (fnts.GetLength() > 0)
    {
        FontSetting& fs = fnts[0];
        fs.GetFont().SetName(u"Arial");
        cell.SetCharacters(fnts);
    }

    std::cout << std::endl << "After updating the font settings...." << std::endl;

    fnts = cell.GetCharacters();

    for (int i = 0; i < fnts.GetLength(); ++i)
    {
        FontSetting& fs = fnts[i];
        std::cout << fs.GetFont().GetName().ToUtf8() << std::endl;
    }

    workbook.Save(outputPath);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### Uscita della console generata dal codice di esempio

Ecco l'output della console quando si utilizza il [file excel di origine](5112369.xlsx):

{{< highlight java >}}

Before updating the font settings....
Century
Courier New
Verdana

After updating the font settings....
Arial
Courier New
Verdana

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
