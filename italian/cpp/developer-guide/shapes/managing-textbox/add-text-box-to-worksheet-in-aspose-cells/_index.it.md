---
title: Come aggiungere/inserire TextBox nel Foglio di Lavoro con C++
linktitle: Aggiungi una casella di testo al foglio di lavoro
type: docs
weight: 10
url: /it/cpp/add-text-box-to-worksheet-in-aspose-cells/
description: Come aggiungere/inserire TextBox nel Foglio di Lavoro in Aspose.Cells con C++.
keywords: aggiungere/inserire casella di testo al foglio di lavoro Excel Aspose
---

## Aggiungere casella di testo al foglio di lavoro in Excel

Nel programma Excel (versione 07 e successive), ci sono due punti in cui puoi inserire caselle di testo. Uno in "inserisci-shapes", l'altro sulla destra del menu superiore dell'opzione "Inserisci".

### Metodo Uno:

![1](1.png)

### Metodo Due:

![2](2.png)

## Come Creare

Puoi creare caselle di testo con testo orizzontale o verticale.

- Seleziona l'opzione corrispondente (orizzontale o verticale)
- Fai clic sinistro sulla pagina
- Tieni premuto il pulsante sinistro e trascina una distanza sulla pagina
- Rilascia il pulsante sinistro

Ora hai una casella di testo.

## Aggiungi casella di testo al foglio di lavoro in Aspose.Cells

Quando è necessario inserire automaticamente molte caselle di testo nel foglio di lavoro, il metodo di inserimento manuale è chiaramente un disastro. Se questo ti disturba, penso che questo documento ti sarà di aiuto. [Aspose.Cells](https://products.aspose.com/cells/) ti fornisce un'API per effettuare facilmente inserimenti di massa nel tuo codice.

Il seguente codice di esempio crea una casella di testo.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create an object of the Workbook class
    Workbook workbook;

    // Access first worksheet from the collection
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add the TextBox to the worksheet
    sheet.GetTextBoxes().Add(6, 10, 100, 200);

    // Save the workbook with the text box
    workbook.Save(outDir + u"result.xlsx", SaveFormat::Xlsx);

    std::cout << "Text box added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Otterrai un file simile a [file risultato](result.xlsx). Nel file, vedrai quanto segue:

![](52449.png)
{{< app/cells/assistant language="cpp" >}}
