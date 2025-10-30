---
title: C++ kullanarak Çalışma Sayfalarından Görüntüleri Çıkarma ve ImageOrPrintOptions kullanma
linktitle: Çalışma Sayfalarından Görüntüleri Çıkar
type: docs
weight: 140
url: /tr/cpp/extract-images-from-worksheets-using-imageorprintoptions/
description: Excel çalışma sayfalarından görselleri nasıl çıkaracağınızı ve onları yerel sürücüye nasıl kaydedeceğinizi öğrenin, Aspose.Cells for C++ kullanılarak.
---

{{% alert color="primary" %}} 

Microsoft Excel kullanıcıları resimleri çalışma sayfalarına ekleyebilirler. Aspose.Cells ile Microsoft Excel dosyalarından resimleri okuyup bunları yerel bir sürücüye kaydetmek mümkündür. Bu makalede bunun nasıl yapılacağı gösterilmektedir.

{{% /alert %}} 

Aşağıdaki örnek kod, Excel dosyasından resimleri çıkarmayı ve kaydetmeyi gösterir.

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

    // Open a template Excel file
    Workbook workbook(srcDir + u"sampleExtractImagesFromWorksheets.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first Picture in the first worksheet
    Picture pic = worksheet.GetPictures().Get(0);

    // Define ImageOrPrintOptions
    ImageOrPrintOptions printoption;

    // Specify the image format
    printoption.SetImageType(ImageType::Jpeg);

    // Save the image
    pic.ToImage(outDir + u"outputExtractImagesFromWorksheets.jpg", printoption);

    std::cout << "Image extracted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
