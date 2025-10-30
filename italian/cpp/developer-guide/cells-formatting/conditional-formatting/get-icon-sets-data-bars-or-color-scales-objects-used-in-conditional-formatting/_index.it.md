---
title: Ottieni Set di Icone, Barre Dati o Oggetti Scala Cromatica usati nella formattazione condizionale con C++
linktitle: Ottieni set di icone, barre dei dati o oggetti scala colore
description: Aspose.Cells for C++ è una libreria per lavorare con file di fogli di calcolo. Supporta l uso di set di icone, barre dei dati e oggetti scala colore nella formattazione condizionale per visualizzare i dati dai fogli di calcolo. Questo articolo descrive come usare la libreria Aspose.Cells per recuperare i dati di questi oggetti.
keywords: Aspose.Cells, Formattazione Condizionale, Serie Icone, Barra Dati, Scala Colore, Foglio di Calcolo
type: docs
weight: 10
url: /it/cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/
---

{{% alert color="primary" %}} 

A volte, è necessario recuperare i set di icone utilizzati nella formattazione condizionale di una cella o di un intervallo di celle e si desidera creare un file immagine basato su di essi. Potresti aver bisogno di leggere le barre dei dati o le scale colore usate nella formattazione condizionale. Aspose.Cells for C++ supporta questa funzione.

{{% /alert %}} 

Il seguente esempio di codice mostra come leggere i set di icone usati per la formattazione condizionale. Con l'API semplice di Aspose.Cells, i dati immagine del set di icone vengono salvati come immagine.

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the A1 cell
    Cell cell = sheet.GetCells().Get(u"A1");

    // Get the conditional formatting result object
    ConditionalFormattingResult cfr = cell.GetConditionalFormattingResult();

    // Get the icon set
    ConditionalFormattingIcon icon = cfr.GetConditionalFormattingIcon();

    // Get the image data from the icon
    Vector<uint8_t> imageData = icon.GetImageData();

    // Create the image file based on the icon's image data
    ofstream outputFile((outDir + u"imgIcon.out.jpg").ToUtf8(), ios::binary);
    outputFile.write(reinterpret_cast<const char*>(imageData.GetData()), imageData.GetLength());
    outputFile.close();

    std::cout << "Icon image saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
