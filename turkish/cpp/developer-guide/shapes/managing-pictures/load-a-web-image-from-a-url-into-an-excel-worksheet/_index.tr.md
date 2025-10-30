---
title: C++ ile Web URL den Excel Çalışma Sayfasına Web Görseli yükleyin
linktitle: Bir URL den Web Resmini Excel Çalışma Sayfasına Yükleme
type: docs
weight: 30
url: /tr/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/
description: C++ ve Aspose.Cells for C++ API kullanarak URL den Excel gömülü resme dönüştürme öğrenin.
keywords: excel url’den resim göster, excel url’den resim, url’den excelde resim göster, excel resim ekle, url’den resim dönüştür, excel’den url resim, excel’de url’den resim yükle, C++, Excel
---

## Bir URL'den Bir Resmi Excel Çalışma Sayfasına Yükleme

Aspose.Cells for C++ API, URL'lerden Excel Çalışma Sayfalarına resim yükleme konusunda basit bir yöntem sağlar. Bu makale, görsel verilerini bellek akışına indirip Aspose.Cells kullanarak çalışma sayfasına eklemeyi açıklar. Resim, Excel dosyasına gömülü hale gelir ve açılırken harici indirmeler gerekmez.

## Örnek Kod

```c++
#include <iostream>
#include <Aspose.Cells.h>
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    try
    {
        // Create a new workbook
        Workbook wb;

        // Get the first worksheet
        WorksheetCollection worksheets = wb.GetWorksheets();
        Worksheet sheet = worksheets.Get(0);

        // Get the pictures collection
        PictureCollection pictures = sheet.GetPictures();

        // Insert the picture from local file to B2 cell (row 1, column 1)
        // Note: Image file should be pre-downloaded to source directory
        U16String imagePath = srcDir + u"aspose-logo.jpg";
        pictures.Add(1, 1, imagePath);

        // Save the Excel file
        wb.Save(outDir + u"webimagebook.out.xlsx");
        std::cout << "Image added successfully." << std::endl;
    }
    catch (const std::exception& ex)
    {
        std::cerr << "Error: " << ex.what() << std::endl;
        return 1;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Her zaman güncellenen URL'den resim gerektiren durumlar için, [Web Adresinden Bağlantılı Resim Ekle](/cells/tr/cpp/insert-a-linked-picture-from-web-address/) metodunu kullanın. Bu yöntem, çalışma sayfası her açıldığında URL'den resmi yükler.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
