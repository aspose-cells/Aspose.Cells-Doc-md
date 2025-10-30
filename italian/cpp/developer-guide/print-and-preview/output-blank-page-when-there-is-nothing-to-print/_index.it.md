---  
title: Output pagina vuota quando non c’è nulla da stampare con C++  
linktitle: Genera una pagina vuota quando non c è nulla da stampare  
type: docs  
weight: 90  
url: /it/cpp/output-blank-page-when-there-is-nothing-to-print/  
description: Gestisci fogli di lavoro vuoti e stampa pagine bianche con Aspose.Cells usando C++.  
---  

## **Possibili Scenari di Utilizzo**  

Se il foglio è vuoto, Aspose.Cells non stamperà nulla quando esporti il foglio di lavoro in immagine. È possibile modificare questo comportamento usando la proprietà [**ImageOrPrintOptions.GetOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getoutputblankpagewhennothingtoprint/). Quando la imposti su **true**, stamperà la pagina bianca.  

## **Output Pagina Bianca quando non c'è Nulla da Stampare**  

Il seguente esempio di codice crea la cartella di lavoro vuota che ha un foglio di lavoro vuoto e visualizza il foglio di lavoro vuoto come immagine dopo aver impostato la proprietà [**ImageOrPrintOptions.GetOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getoutputblankpagewhennothingtoprint/) su **true**. Di conseguenza, genera la pagina bianca in quanto non c'è nulla da stampare che puoi vedere nell'immagine sottostante.  

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)  

## **Codice di Esempio**  

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Output directory
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook wb;

    // Access first worksheet - it is an empty sheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Specify image or print options
    // Since the sheet is blank, we will set OutputBlankPageWhenNothingToPrint to true
    // So that an empty page gets printed
    ImageOrPrintOptions opts;
    opts.SetImageType(Drawing::ImageType::Png);
    opts.SetOutputBlankPageWhenNothingToPrint(true);

    // Render empty sheet to png image
    SheetRender sr(ws, opts);
    sr.ToImage(0, outputDir + u"OutputBlankPageWhenNothingToPrint.png");

    std::cout << "Blank page rendered to PNG successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```  
{{< app/cells/assistant language="cpp" >}}
