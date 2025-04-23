---
title: Aggiungi filigrana WordArt al foglio di lavoro con C++
linktitle: Gestire WordArt
type: docs
weight: 180
url: /it/cpp/add-wordart-watermark-to-worksheet/
description: Impara come aggiungere filigrane WordArt ai fogli di lavoro di Excel usando Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Usa WordArt per aggiungere effetti speciali al testo nei fogli di calcolo. Ad esempio, distendi un titolo sulla parte superiore del file, decora il testo e fai adattare il testo a una forma preimpostata, o applica il testo a un foglio di Excel come un watermark di sfondo. Il WordArt diventa un oggetto che puoi spostare o posizionare nei fogli di calcolo per aggiungere decorazioni.

{{% /alert %}} 

L'esempio seguente mostra come aggiungere una forma WordArt per impostare un watermark di sfondo per un foglio di lavoro.

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

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first default sheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add Watermark
    Shape wordart = sheet.GetShapes().AddTextEffect(MsoPresetTextEffect::TextEffect1,
        u"CONFIDENTIAL", u"Arial Black", 50, false, true,
        18, 8, 1, 1, 130, 800);

    // Get the fill format of the word art
    FillFormat wordArtFormat = wordart.GetFill();

    // Set the transparency
    wordArtFormat.SetTransparency(0.9);

    // Make the line invisible
    LineFormat lineFormat = wordart.GetLine();

    // Save the file
    U16String outputPath = outDir + u"Watermark_Test.out.xls";
    workbook.Save(outputPath);

    std::cout << "Watermark added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Argomenti avanzati**
- [Aggiungi testo Word Art con stili incorporati](/cells/it/cpp/add-word-art-text-with-built-in-styles/)
- [Bloccare WordArt Come Filigrana](/cells/it/cpp/locking-wordart-watermark/)
- [Imposta lo stile predefinito di WordArt al testo della forma](/cells/it/cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
