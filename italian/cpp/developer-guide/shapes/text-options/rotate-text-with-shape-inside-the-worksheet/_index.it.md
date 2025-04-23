---
title: Ruota il testo con forma all’interno del foglio di lavoro con C++
linktitle: Ruota il testo con la forma
type: docs
weight: 1300
url: /it/cpp/rotate-text-with-shape-inside-the-worksheet/
description: Impara come controllare la rotazione del testo con le forme nei fogli di lavoro di Excel usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Puoi aggiungere testo all’interno di qualsiasi forma usando Microsoft Excel. Se aggiungi una forma usando la vecchia versione di Microsoft Excel 2003, il testo non ruoterà con la forma. Tuttavia, se usi versioni più recenti come 2007, 2010, 2013 o 2016, il testo ruoterà con la forma. Puoi controllare se il testo dovrebbe ruotare con la forma o meno usando la proprietà [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrotatetextwithshape/). Il valore predefinito di questa proprietà è **true**, il che significa che il testo ruoterà con la forma. Se lo imposti su **false**, il testo non ruoterà con la forma.

## **Ruota il testo con la forma all'interno del foglio di lavoro**

Il seguente esempio di codice carica il [file Excel di esempio](64716896.xlsx) che contiene una forma triangolare, e il suo testo ruota con la forma. Se apri il file in Microsoft Excel e ruoti la forma triangolare, il testo ruoterà anche con essa. Il codice quindi imposta la proprietà [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrotatetextwithshape/) su **false** e lo salva come [file Excel di output](64716897.xlsx). Se ora apri il file di output in Microsoft Excel e ruoti la forma triangolare, il testo non ruoterà più con essa. Vedi lo screenshot seguente che mostra l’effetto del codice sul file Excel di esempio per riferimento.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Codice di Esempio**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Drawing::Texts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load sample Excel file
    Workbook wb(srcDir + u"sampleRotateTextWithShapeInsideWorksheet.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B4 and add message inside it
    Cell b4 = ws.GetCells().Get(u"B4");
    b4.PutValue(u"Text is not rotating with shape because RotateTextWithShape is false.");

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Access shape text alignment
    ShapeTextAlignment shapeTextAlignment = sh.GetTextBody().GetTextAlignment();

    // Do not rotate text with shape by setting RotateTextWithShape as false
    shapeTextAlignment.SetRotateTextWithShape(false);

    // Save the output Excel file
    wb.Save(outDir + u"outputRotateTextWithShapeInsideWorksheet.xlsx");

    Aspose::Cells::Cleanup();
}
```
