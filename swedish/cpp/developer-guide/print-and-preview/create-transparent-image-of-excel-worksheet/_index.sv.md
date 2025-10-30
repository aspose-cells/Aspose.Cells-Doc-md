--- 
title: Skapa Transparent Bild av Excel Arbetsblad med C++ 
linktitle: Create Transparent Image of Excel Worksheet 
type: docs 
weight: 170 
url: /sv/cpp/create-transparent-image-of-excel-worksheet/ 
description: Generera transparenta bilder av Excel arbetsblad med Aspose.Cells och C++. 
--- 

{{% alert color="primary" %}} 

Ibland behöver du generera bilden av ditt arbetsblad som en transparent bild. Du vill applicera transparens på alla celler som inte har fyllnadsfärger. Aspose.Cells tillhandahåller egenskapen [**ImageOrPrintOptions.GetTransparent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettransparent/) för att applicera transparens på arbetsbilden. När denna egenskap är **false**, då ritas celler utan fyllnadsfärger med vit färg och när den är **true**, ritas celler utan fyllnadsfärger transparent. 

{{% /alert %}} 

I följande arbetsbladsbild har inte transparens tillämpats. Celler utan fyllfärger är ritade vita.

|**Utdata utan transparens: cellens bakgrund är vit**| 
| :- | 
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)| 

Medan i följande arbetsbladsbild har transparens tillämpats. Cellerna utan fyllfärger är transparenta.

|**Utdata med aktiverad transparens**| 
| :- | 
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)| 

Följande exempelkod genererar en transparent bild från ett Excel-ark.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory path
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Create workbook object from source file
    Workbook workbook(sourceDir + u"sampleCreateTransparentImage.xlsx");

    // Apply different image or print options
    ImageOrPrintOptions imgOption;
    imgOption.SetImageType(static_cast<ImageType>(5)); // Png
    imgOption.SetHorizontalResolution(200);
    imgOption.SetVerticalResolution(200);
    imgOption.SetOnePagePerSheet(true);

    // Apply transparency to the output image
    imgOption.SetTransparent(true);

    // Create image after applying image or print options
    SheetRender sr(workbook.GetWorksheets().Get(0), imgOption);
    sr.ToImage(0, outputDir + u"outputCreateTransparentImage.png");

    std::cout << "Image created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
