---
title: Bir Çalışma Sayfasındaki Hücrelerin Aralığını Görüntüye Dışa Aktarma (C++)
linktitle: Hücreler aralığını Görüntüye Dışa Aktarma
type: docs
weight: 60
url: /tr/cpp/export-range-of-cells-in-a-worksheet-to-image/
description: Aspose.Cells kullanarak belirli hücre aralığını görüntüye dışa aktarmayı nasıl yapacağınızı C++ ile öğrenin.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells kullanarak bir çalışma sayfasının görüntüsünü alabilirsiniz. Ancak bazen, bir çalışma sayfasındaki yalnızca belirli bir hücre aralığını bir görüntüye aktarmanız gerekebilir. Bu makalede, bu işlemi nasıl gerçekleştireceğiniz açıklanmaktadır.

## **Bir Çalışma Sayfasındaki Hücre Aralığını Görüntüye Aktar**

Bir aralığın görüntüsünü almak için yazdırma alanını istenen aralığa ayarlayın ve tüm kenar boşluklarını sıfıra ayarlayın. Ayrıca [**ImageOrPrintOptions.GetOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getonepagepersheet/) değerini **true** olarak ayarlayın. Aşağıdaki kod, D8:G16 aralığından bir görüntü alır. Koddaki kullanılan örnek Excel dosyasının ekran görüntüsü aşağıdadır. Kodu herhangi bir Excel dosyasıyla deneyebilirsiniz.

## **Örnek Excel Dosyası ve Dışa Aktarılan Görüntü Ekran Görüntüsü**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

Kod çalıştırıldığında yalnızca D8:G16 aralığının bir görüntüsü oluşturulur.

**![todo:image_alt_text](Output-Image.png)**

## **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from source file
    Workbook workbook(srcDir + u"sampleExportRangeOfCellsInWorksheetToImage.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the print area with the desired range
    worksheet.GetPageSetup().SetPrintArea(u"D8:G16");

    // Set all margins to 0
    worksheet.GetPageSetup().SetLeftMargin(0);
    worksheet.GetPageSetup().SetRightMargin(0);
    worksheet.GetPageSetup().SetTopMargin(0);
    worksheet.GetPageSetup().SetBottomMargin(0);

    // Set OnePagePerSheet option as true
    ImageOrPrintOptions options;
    options.SetOnePagePerSheet(true);
    options.SetImageType(Aspose::Cells::Drawing::ImageType::Jpeg);
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);

    // Take the image of the worksheet
    SheetRender sr(worksheet, options);
    sr.ToImage(0, outDir + u"outputExportRangeOfCellsInWorksheetToImage.jpg");

    std::cout << "Worksheet image exported successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
