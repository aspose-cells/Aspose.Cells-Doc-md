---
title: Sayfa ile Çalışma Sayfasını Görüntüye Dönüştürme ve Sayfaya Göre Çalışma Sayfasını Görüntüye Dönüştürme  C++
linktitle: Çalışma Sayfasını Görüntüye Dönüştürme ve Sayfa Başına Çalışma Sayfasını Görüntüye Dönüştürme
type: docs
weight: 80
url: /tr/cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/
description: Bir çalışma sayfasını görüntü dosyasına ve çok sayfalı çalışma sayfasını sayfa başına görüntü dosyasına nasıl dönüştüreceğinizi Aspose.Cells ve C++ kullanarak öğrenin.
---

{{% alert color="primary" %}}

Bu belge, bir çalışma sayfasını görüntü dosyasına dönüştürme ve çok sayfalı çalışma sayfasını sayfa başına görüntü dosyasına dönüştürme konusunda detaylı bilgi sağlar.

Bazı durumlarda, çalışma sayfalarını örneğin uygulamalarda veya web sayfalarında kullanmak için resim olarak sunmanız gerekebilir. Resimleri bir Word belgesine, bir PDF dosyasına, bir PowerPoint sunumuna eklemek veya başka bir senaryoda kullanmak gerekebilir. Temel olarak, çalışma sayfasını bir resim olarak oluşturmak istersiniz. Aspose.Cells, Microsoft Excel dosyalarındaki çalışma sayfalarını resimlere dönüştürmeyi destekler. Ayrıca, Aspose.Cells, bir çalışma kitabını birden fazla resim dosyasına, sayfa başına bir tane olmak üzere dönüştürmeyi destekler.

Bunu başarmak için Office Otomasyon kullanabilirsiniz, ancak Office otomasyonun kendi dezavantajları da vardır. Güvenlik, kararlılık, ölçeklenebilirlik/hız, fiyat ve özellikler gibi birçok neden ve sorun söz konusudur. Kısaca, birçok sebep olsa da en önemli neden, Microsoft'un kendisinin Office otomasyonu kullanmamız konusunda kesinlikle şiddetle tavsiye etmemesidir.

{{% /alert %}}

## **Aspose.Cells Kullanarak Çalışma Sayfasını Resim Dosyasına Dönüştürme**

Bu makalede, Visual Studio'da bir konsol uygulaması oluşturmayı, bir çalışma sayfasını bir resme dönüştürmeyi ve Aspose.Cells API'sını kullanarak birkaç basit satır kodla her çalışma sayfasını bir resim olarak dönüştürmeyi gösteriyor.

Programınıza [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) isim alanını dahil etmelisiniz. Bu alan, [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/) gibi değerler içeren birkaç değerli sınıf içerir. [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) sınıfı, çalışma sayfasını görüntülemek için kullanılan bir sınıftır ve doğrudan herhangi bir özellik veya seçenek ayarlarıyla çalışma sayfasını görüntü dosyasına dönüştürme yeteneğine sahip aşırı yüklenmiş [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/) metodunu içerir. Bu metod, `System.Drawing.Bitmap` nesnesi döndürebilir ve görüntü dosyasını diske veya akışa kaydedebilirsiniz. BMP, PNG, GIF, JPG, JPEG, TIFF, EMF ve diğerleri gibi birçok görüntü formatını destekler.

Bu makalede şunları açıklar:

- Bir çalışma sayfasını bir resme dönüştürme
- Bir çalışma sayfasındaki her sayfayı bir resme dönüştürme

Bu görev, Aspose.Cells'ı kullanarak bir şablon çalışma kitabındaki bir çalışma sayfasını bir resim dosyasına dönüştürmenin nasıl yapıldığını gösterir.

### **Proje Kurulumu**

1. İlk olarak, [Aspose.Cells for C++ indir](https://downloads.aspose.com/cells/cpp).
1. Geliştirme bilgisayarınıza kurun. Tüm [Aspose](http://www.aspose.com/) bileşenleri, kurulduğunda değerlendirme modunda çalışır. Değerlendirme modu zaman sınırı olmadan çalışır ve yalnızca üretilen belgelere filigran ekler. Şimdi Visual Studio'yu başlatın ve yeni bir konsol uygulaması oluşturun. Bu örnek, bir C++ konsol uygulaması kullanır. Oluşturulan projeye Aspose.Cells referansı ekleyin.

### **Çalışma Sayfasını Resim Dosyasına Dönüştürme**

Microsoft Excel'de yeni bir çalışma kitabı oluşturdum ve ilk çalışma sayfasına bazı veriler ekledim: **Testbook.xlsx** (1 çalışma sayfası). Daha sonra, şablon dosyasının Sheet1 çalışma sayfasını SheetImage.jpg adında bir resim dosyasına dönüştürdüm.

Bileşen tarafından görevi tamamlamak için kullanılan kod aşağıda verilmiştir. Bu kod, **Testbook.xlsx**'teki Sheet1'i, bu dönüşümün ne kadar kolay olduğunu açıklamak için bir resim dosyasına dönüştürür.

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

std::string convert_u16_to_string(const U16String& u16str);

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheettoImageFile.xlsx");
    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions imgOptions;
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetImageType(ImageType::Jpeg);

    SheetRender sr(sheet, imgOptions);
    sr.ToImage(0, outDir + u"outputConvertWorksheettoImageFile.jpg");

    std::cout << "Worksheet converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Aspose.Cells Kullanarak Sayfa Sayfa Çalışma Sayfasını Resim Dosyasına Dönüştürme**

Bu örnek, birkaç sayfası olan bir şablon çalışma kitabından bir çalışma sayfasını bir resim dosyasına dönüştürmek için Aspose.Cells'ı kullanmanın nasıl yapıldığını göstermektedir.

### **Sayfa bazında Çalışma Sayfasını Görüntüye Dönüştürme**

Microsoft Excel'de yeni bir çalışma kitabı oluşturdum ve ilk çalışma sayfasına bazı veriler ekledim: **Testbook2.xlsx** (1 çalışma sayfası).

Şimdi, şablon dosyasının Sheet1 çalışma sayfasını resim dosyalarına dönüştür (sayfa başına bir dosya). Zaten kopyalama görevini gerçekleştirmek için konsol uygulaması oluşturmuştum, bu nedenle konsol uygulaması oluşturma adımlarını atlayacak ve doğrudan çalışma sayfası dönüşüm adımlarına geçeceğim.

Bunu gerçekleştirmek için kullanılan kod aşağıdadır. Sheet1 in Testbook2.xlsx dosyasını sayfa başına görüntü dosyalarına dönüştürür.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

std::u16string intToU16String(int value) {
    std::u16string result;
    if (value == 0) {
        result.push_back(u'0');
        return result;
    }
    while (value > 0) {
        result.insert(result.begin(), static_cast<char16_t>(u'0' + (value % 10)));
        value /= 10;
    }
    return result;
}

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheetToImageByPage.xlsx");

    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);
    options.SetImageType(ImageType::Tiff);

    SheetRender sr(sheet, options);
    for (int j = 0; j < sr.GetPageCount(); j++)
    {
        std::u16string pageNum = intToU16String(j + 1);
        U16String fileName = outDir + U16String(u"outputConvertWorksheetToImageByPage_") + U16String(pageNum.c_str()) + U16String(u".tif");
        sr.ToImage(j, fileName);
    }

    std::cout << "Worksheet converted to images by page successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
