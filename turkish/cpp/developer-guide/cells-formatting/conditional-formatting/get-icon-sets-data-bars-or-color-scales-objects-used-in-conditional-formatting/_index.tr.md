---
title: Koşullu Biçimlendirmede Kullanılan Simge Setleri, Veri Çubukları veya Renk Ölçekleri Nesneleri Alın C++ ile
linktitle: İkon Setleri, Veri Çubukları veya Renk Ölçekleri Nesnesi Alır
description: Aspose.Cells for C++, elektronik tablo dosyalarıyla çalışmak için kullanılan bir kütüphanedir. Koşullu biçimlendirmede ikon setleri, veri çubukları ve renk ölçekleri nesnelerinin kullanılmasını destekler ve elektronik tablolardan veri görüntülemeye olanak sağlar. Bu makale, Aspose.Cells kütüphanesini kullanarak bu nesneler için veri nasıl alınır anlatmaktadır.
keywords: Aspose.Cells, Koşullu Biçimlendirme, Simge Seti, Veri Çubuğu, Renk Ölçeği, Elektronik Tablo
type: docs
weight: 10
url: /tr/cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/
---

{{% alert color="primary" %}} 

Bazen, bir hücre veya hücre aralığının koşullu biçimlendirmesinde kullanılan ikon setlerini almanız gerekebilir ve bunun üzerine bir resim dosyası oluşturmak isteyebilirsiniz. Koşullu biçimlendirmede kullanılan veri çubuklarını veya renk ölçeklerini okumanız gerekebilir. Aspose.Cells for C++ bu özelliği destekler.

{{% /alert %}} 

Aşağıdaki kod örneği, koşullu biçimlendirmelerde kullanılan ikon setlerini nasıl okuyacağınızı gösterir. Aspose.Cells’in basit API’siyle, ikon setinin görüntü verileri bir resim olarak kaydedilir.

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the A1 cell
    Cell cell = sheet.GetCells().Get(u"A1");

    // Get the conditional formatting result object
    ConditionalFormattingResult cfr = cell.GetConditionalFormattingResult();

    // Get the icon set
    ConditionalFormattingIcon icon = cfr.GetConditionalFormattingIcon();

    // Get the image data from the icon
    Vector<uint8_t> imageData = icon.GetImageData();

    // Create the image file based on the icon's image data
    ofstream outputFile((outDir + u"imgIcon.out.jpg").ToUtf8(), ios::binary);
    outputFile.write(reinterpret_cast<const char*>(imageData.GetData()), imageData.GetLength());
    outputFile.close();

    std::cout << "Icon image saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
