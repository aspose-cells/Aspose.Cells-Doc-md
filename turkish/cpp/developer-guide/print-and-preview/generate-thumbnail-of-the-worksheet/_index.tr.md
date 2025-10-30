---
title: Çalışma Sayfasının Küçük Resmini C++ ile Oluşturma
linktitle: Çalışma Sayfasının Küçük Resmi Oluşturma
type: docs
weight: 110
url: /tr/cpp/generate-thumbnail-of-the-worksheet/
description: Aspose.Cells for C++ kullanarak çalışma sayfalarının küçük resimlerini görüntü dosyası olarak üretin.
---

{{% alert color="primary" %}} 

Çalışma sayfalarından küçük resimler oluşturmak faydalı olabilir. Bir küçük resim, çalışma sayfasındaki içeriğin bir ön izlemesini vermek üzere bir Word belgesine veya bir PowerPoint sunumuna yapıştırılabilir. Gerçek belgenin indirme bağlantısına bir bağlantıyla bir web sayfasına eklenebilir ve diğer birçok kullanımı bulunmaktadır.

{{% /alert %}} 

Aspose.Cells for C++, çalışma sayfalarını görüntü dosyalarına dönüştürmenize olanak tanır ve küçük resim üretimini kolaylaştırır. Aşağıdaki örnek kod, çalışma sayfalarını C++ kullanarak görüntü dosyalarına dönüştürmenin nasıl yapılacağını gösterir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load source workbook
    Workbook book(srcDir + u"sampleGenerateThumbnailOfWorksheet.xlsx");

    // Configure image rendering options
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(ImageType::Bmp);
    imgOptions.SetVerticalResolution(200);
    imgOptions.SetHorizontalResolution(200);
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetDesiredSize(600, 600, true); // Set thumbnail dimensions

    // Access first worksheet
    WorksheetCollection worksheets = book.GetWorksheets();
    Worksheet sheet = worksheets.Get(0);

    // Render worksheet to image
    SheetRender sr(sheet, imgOptions);
    sr.ToImage(0, outDir + u"outputGenerateThumbnailOfWorksheet.bmp");

    std::cout << "Worksheet thumbnail generated successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
