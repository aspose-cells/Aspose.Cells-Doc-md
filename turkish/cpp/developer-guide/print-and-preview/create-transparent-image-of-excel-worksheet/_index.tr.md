--- 
title: C++ kullanarak Excel Çalışma Sayfasının Şeffaf Görüntüsünü Oluşturma 
linktitle: Create Transparent Image of Excel Worksheet 
type: docs 
weight: 170 
url: /tr/cpp/create-transparent-image-of-excel-worksheet/ 
description: Aspose.Cells kullanarak C++ ile Excel çalışma sayfalarının saydam görüntülerini üretin. 
--- 

{{% alert color="primary" %}} 

Bazen çalışma sayfanızın görüntüsünü şeffaf bir görüntü olarak oluşturmanız gerekebilir. Dolgu renkleri olmayan tüm hücrelere şeffaflık uygulamak istersiniz. Aspose.Cells, çalışma sayfasına şeffaflık uygulamak için [**ImageOrPrintOptions.GetTransparent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettransparent/) özelliğini sağlar. Bu özellik **false** olduğunda, dolgu renkleri olmayan hücreler beyaz renkle çizilir ve **true** olduğunda, dolgu renkleri olmayan hücreler şeffaf şekilde çizilir. 

{{% /alert %}} 

Aşağıdaki çalışma sayfası görüntüsünde şeffaflık uygulanmamıştır. Dolgu rengi olmayan hücreler beyaz olarak çizilmiştir.

|**Şeffaflık olmadan çıktı: hücre arka planı beyazdır**| 
| :- | 
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)| 

Ancak aşağıdaki çalışma sayfası görüntüsünde şeffaflık uygulanmıştır. Dolgu rengi olmayan hücreler şeffaf olarak çizilmiştir.

|**Şeffaflık etkinleştirilmiş çıktı**| 
| :- | 
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)| 

Aşağıdaki örnek kod, bir Excel çalışma sayfasından şeffaf bir görüntü oluşturur.

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
