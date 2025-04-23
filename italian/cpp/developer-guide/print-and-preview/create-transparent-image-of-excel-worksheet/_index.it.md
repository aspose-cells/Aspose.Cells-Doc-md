--- 
title: Creare immagine trasparente di un foglio di lavoro Excel con C++ 
linktitle: Create Transparent Image of Excel Worksheet 
type: docs 
weight: 170 
url: /it/cpp/create-transparent-image-of-excel-worksheet/ 
description: Generare immagini trasparenti di fogli di lavoro Excel usando Aspose.Cells con C++. 
--- 

{{% alert color="primary" %}} 

A volte è necessario generare l'immagine del tuo foglio di lavoro come un'immagine trasparente. Desideri applicare la trasparenza a tutte le celle che non hanno colori di riempimento. Aspose.Cells fornisce la proprietà [**ImageOrPrintOptions.GetTransparent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettransparent/) per applicare la trasparenza all'immagine del foglio di lavoro. Quando questa proprietà è **false**, le celle senza colori di riempimento vengono disegnate con il colore bianco e quando è **true**, le celle senza colori di riempimento vengono disegnate in modo trasparente. 

{{% /alert %}} 

Nell'immagine del foglio di lavoro seguente, la trasparenza non è stata applicata. Le celle senza colori di riempimento vengono disegnate di bianco.

|**Output senza trasparenza: lo sfondo della cella è bianco**| 
| :- | 
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)| 

Mentre, nell'immagine del foglio di lavoro seguente, è stata applicata la trasparenza. Le celle senza colori di riempimento sono trasparenti.

|**Output con trasparenza abilitata**| 
| :- | 
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)| 

Il seguente codice di esempio genera un'immagine trasparente da un foglio di lavoro di Excel.

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
