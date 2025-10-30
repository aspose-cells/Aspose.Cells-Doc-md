---
title: impostare il carattere predefinito durante la conversione di fogli di calcolo in immagini con C++
linktitle: Imposta carattere predefinito
type: docs
weight: 360
url: /it/cpp/set-default-font-while-rendering-spreadsheet-to-images/
description: Impara come impostare il carattere predefinito durante la conversione di fogli di calcolo in immagini usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Si prega di utilizzare la proprietà [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) per impostare il carattere predefinito durante la rappresentazione dei fogli di calcolo in immagini. Questa proprietà avrà effetto solo quando il carattere predefinito del foglio di lavoro non potrà rappresentare i tuoi caratteri. Il carattere predefinito specificato con la proprietà [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) viene utilizzato per tutte quelle celle che hanno caratteri non validi o inesistenti.

{{% /alert %}}

## Impostare il carattere predefinito durante la rappresentazione del foglio di calcolo in immagini

Il seguente esempio di codice crea un foglio di lavoro, aggiunge del testo nella cella A4 del primo foglio di lavoro e imposta il carattere su un carattere inesistente o non valido. Quindi, si prendono due immagini del foglio di lavoro. La prima immagine è presa impostando la proprietà [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) su *Courier New* e la seconda immagine è presa impostando la proprietà [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) su *Times New Roman*.

Questa è l'immagine di output dopo aver impostato la proprietà [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) su *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Questa è l'immagine di output dopo aver impostato la proprietà [**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) su *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## Codice di esempio

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook wb;

    // Set default font of the workbook to none
    Style s = wb.GetDefaultStyle();
    s.GetFont().SetName(u"");
    wb.SetDefaultStyle(s);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell A4 and add some text inside it
    Cell cell = ws.GetCells().Get(u"A4");
    cell.PutValue(u"This text has some unknown or invalid font which does not exist.");

    // Set the font of cell A4 which is unknown
    Style st = cell.GetStyle();
    st.GetFont().SetName(u"UnknownNotExist");
    st.GetFont().SetSize(20);
    st.SetIsTextWrapped(true);
    cell.SetStyle(st);

    // Set first column width and fourth column height
    ws.GetCells().SetColumnWidth(0, 80);
    ws.GetCells().SetRowHeight(3, 60);

    // Create image or print options
    ImageOrPrintOptions opts;
    opts.SetOnePagePerSheet(true);
    opts.SetImageType(ImageType::Png);

    // Render worksheet image with Courier New as default font
    opts.SetDefaultFont(u"Courier New");
    SheetRender sr(ws, opts);
    sr.ToImage(0, outDir + u"out_courier_new_out.png");

    // Render worksheet image again with Times New Roman as default font
    opts.SetDefaultFont(u"Times New Roman");
    SheetRender sr2(ws, opts);
    sr2.ToImage(0, outDir + u"times_new_roman_out.png");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
