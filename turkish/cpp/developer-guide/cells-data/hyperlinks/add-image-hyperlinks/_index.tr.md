---
title: Görüntü Bağlantılarını C++ ile ekle
linktitle: Resim Bağlantıları Ekle
type: docs
weight: 140
url: /tr/cpp/add-image-hyperlinks/
description: Aspose.Cells for C++ API kullanarak Görüntü Bağlantıları eklemeyi öğrenin.
keywords: Resim Bağlantıları Ekleyin, Resim Bağlantılarını Ekle
---

{{% alert color="primary" %}} 

Bağlantılar diğer çalışma sayfalarındaki veya web sitelerindeki bilgilere erişim için kullanışlıdır. Microsoft Excel kullanıcıların hücrelerdeki metinlere ve resimlere bağlantı eklemesine izin verir. Resim bağlantıları, bir çalışma sayfasında gezinmeyi kolaylaştırabilir, örneğin, önceki ve sonraki düğmeler veya belirli sitelere bağlantı kuran logolar gibi. Bu belge, Aspose.Cells kullanarak bir çalışma sayfasında resim bağlantıları eklemenin nasıl yapılacağını açıklar.

{{% /alert %}} 

Aspose.Cells, çalışma kitaplarında resimlere bağlantı eklemeyi çalışma zamanında sağlar. Bağlantının ekran ipucunu ve adresini belirlemek ve değiştirmek mümkündür. Aşağıdaki örnek kod, bir çalışma sayfasına resim bağlantısı nasıl ekleyeceğinizi gösterir.

```c++
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

    // Instantiate a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a string value to a cell
    worksheet.GetCells().Get(u"C2").PutValue(u"Image Hyperlink");

    // Set the 4th row height
    worksheet.GetCells().SetRowHeight(3, 100);

    // Set the C column width
    worksheet.GetCells().SetColumnWidth(2, 21);

    // Add a picture to the C4 cell
    int index = worksheet.GetPictures().Add(3, 2, 4, 3, srcDir + u"aspose-logo.jpg");

    // Get the picture object
    Picture pic = worksheet.GetPictures().Get(index);

    // Set the placement type
    pic.SetPlacement(PlacementType::FreeFloating);

    // Add an image hyperlink
    Hyperlink hlink = pic.AddHyperlink(u"http://www.aspose.com/");

    // Specify the screen tip
    hlink.SetScreenTip(u"Click to go to Aspose site");

    // Save the Excel file
    workbook.Save(outDir + u"ImageHyperlink_out.xls");

    std::cout << "Image hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
