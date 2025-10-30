---
title: Çalışma Sayfasını Resim veya Yazdırma Seçenekleriyle Dönüştürme  C++ kullanımı
linktitle: Çalışma Sayfasını Görüntüye Dönüştürme
type: docs
weight: 90
url: /tr/cpp/converting-worksheet-to-image-using-imageorprint-options/
description: Bir çalışma sayfasını görüntü dosyasına dönüştürmek ve farklı görüntü ve yazdırma seçenekleri uygulamak için Aspose.Cells ve C++ kullanarak öğrenin.
---

{{% alert color="primary" %}}

Bu belge, bir çalışma sayfasını görüntü dosyasına dönüştürme ve görüntü için farklı görüntü ve yazdırma seçenekleri uygulama konusunda detaylı bilgi sağlar.

{{% /alert %}}

## **Çalışma Sayfalarını Resim Olarak Kaydetme - Farklı Yaklaşımlar**

Bazen, çalışma sayfalarınızı görsel temsili olarak sunmanız gerekebilir. Çalışma sayfası görüntülerini uygulamalarınızda veya web sayfalarınızda göstermeniz, Word belgesine, PDF dosyasına, PowerPoint sunumuna eklemeniz veya başka bir senaryoda kullanmanız gerekebilir. Basitçe söylemek gerekirse, çalışma sayfasının başka bir yerde kullanabilmeniz için bir görsel olarak render edilmesini istiyorsunuz. Aspose.Cells, Excel dosyalarındaki çalışma sayfalarını görüntüye dönüştürmeyi destekler. Ayrıca, Aspose.Cells farklı seçenekler belirlemenize olanak sağlar, örneğin, görsel formatı, çözünürlük (dikey ve yatay), görsel kalitesi ve diğer baskı ve görsel seçenekleri.

Office Otomasyonu'nu düşünebilirsiniz, ancak kendi dezavantajları vardır. Güvenlik, stabilite, ölçeklenebilirlik, hız, fiyat ve özellikler gibi birçok sebep ve sorun vardır. Kısacası, birçok neden vardır ve bunların en önemlisi Microsoft'un kendisinin yazılım çözümlerinden Office otomasyonuna kesinlikle karşı olduğunu önermesidir.

Bu makale, Aspose.Cells API kullanarak çok az ve en basit satır kodla çeşitli görsel ve baskı seçenekleriyle bir çalışma sayfasını görsele dönüştürmek için Visual Studio'da bir konsol uygulaması oluşturmayı gösterir.

Programınıza/Projenize [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) isim alanını dahil etmelisiniz. Bu alan birkaç değerli sınıf içerir, örneğin, [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/) ve diğerleri.

[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) sınıfı, çalışma sayfasını görsellerde gösterilecek çalışma sayfasını temsil eder. Yüklenmiş [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/) metodu, doğrudan bir çalışma sayfasını istediğiniz özellikler veya seçeneklerle belirtilmiş görüntü dosyasına dönüştürebilir. Bu bir bitmap nesnesi dönebilir ve bir görüntü dosyasını disk/akışa kaydedebilirsiniz. BMP, PNG, GIF, JPEG, TIFF, EMF gibi çeşitli görüntü formatları desteklenmektedir.

## **Aspose.Cells kullanarak GörüntüSeçenekleri ile Çalışma Sayfasını Görüntüye Dönüştürme**

### **Microsoft Excel'de Şablon Çalışma Kitabı Oluşturma**

MS Excel'de yeni bir çalışma kitabı oluşturdum ve ilk çalışma sayfasına bazı veriler ekledim. Şimdi, şablon dosyasının “Sheet1” çalışma sayfasını “SheetImage.tiff” görüntü dosyasına dönüştüreceğim ve yatay-y-ütopsuz çözünürlükler, TiffSıkıştırması gibi farklı görüntü seçenekleri uygulayacağım.

### **Aspose.Cells'i İndirin ve Yükleyin**

İlk olarak, [indir](https://downloads.aspose.com/cells/cpp) Aspose.Cells for C++. geliştirme bilgisayarınıza kurmalısınız. Tüm [Aspose](http://www.aspose.com/) bileşenleri, kurulduğunda değerlendirme modunda çalışır. Değerlendirme modu zaman sınırlaması olmadan çalışır ve üretilen belgelere yalnızca su damgaları ekler.

### **Bir Proje Oluşturun**

Visual Studio'yu başlatın ve yeni bir konsol uygulaması oluşturun. Bu örnek, bir C++ konsol uygulamasını gösterecektir.

### **Referanslar Ekle**

Bu proje Aspose.Cells kullanacaktır. Bu yüzden, projenize Aspose.Cells bileşenine bir referans eklemelisiniz. Örneğin, `...\Program Files\Aspose\Aspose.Cells for C++\Bin\Aspose.Cells.lib` referansı ekleyebilirsiniz.

### **Çalışma Sayfasını Görüntü Dosyasına Dönüştür**

```c++
#include <iostream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleWorksheetToAnImage.xlsx");

    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(300);
    options.SetVerticalResolution(300);
    options.SetTiffCompression(TiffCompression::CompressionLZW);
    options.SetImageType(ImageType::Tiff);
    options.SetPrintingPage(PrintingPageType::Default);

    SheetRender sr(sheet, options);

    int pageIndex = 3;
    int pageNumber = pageIndex + 1;
    std::wstring pageStr = std::to_wstring(pageNumber);
    U16String pageNumberStr(reinterpret_cast<const char16_t*>(pageStr.c_str()));
    U16String outputPath = outDir + U16String(u"outputWorksheetToAnImage_") + pageNumberStr + U16String(u".tiff");
    sr.ToImage(pageIndex, outputPath);

    std::cout << "Worksheet converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Dönüşüm Seçenekleri**

Belirli sayfaları görüntüye kaydetmek mümkündür. Aşağıdaki kod, bir çalışma kitabındaki ilk ve ikinci çalışma sayfalarını JPG görüntülerine dönüştürür.

```c++
#include <iostream>
#include <fstream>
#include <sstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputPath = srcDir + u"sampleSpecificPagesToImages.xlsx";
    Workbook workbook(inputPath);

    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(Aspose::Cells::Drawing::ImageType::Jpeg);

    SheetRender sr(worksheet, imgOptions);

    int32_t pageIndex = 3;

    Vector<uint8_t> imageData = sr.ToImage(pageIndex);

    std::wstringstream ws;
    ws << (pageIndex + 1);
    U16String pageNumStr(reinterpret_cast<const char16_t*>(ws.str().c_str()));

    U16String outputPath = outDir + u"outputSpecificPagesToImage_" + pageNumStr + u".jpg";
    std::ofstream outputFile(outputPath.ToUtf8(), std::ios::binary);
    outputFile.write(reinterpret_cast<const char*>(imageData.GetData()), imageData.GetLength());
    outputFile.close();

    std::cout << "Page rendered successfully to: " << outputPath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **WorkbookRender kullanarak Görüntü Dönüştürme**

Bir TIFF görüntüsü birden fazla çerçeve içerebilir. Tüm çalışma kitabını tek bir TIFF görüntüsüne çoklu çerçeve veya sayfa olarak kaydedebilirsiniz:

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

    // Load the workbook
    Workbook wb(srcDir + u"sampleUseWorkbookRenderForImageConversion.xlsx");

    // Set image options
    ImageOrPrintOptions opts;
    opts.SetImageType(ImageType::Tiff);

    // Render workbook to image
    WorkbookRender wr(wb, opts);
    wr.ToImage(outDir + u"outputUseWorkbookRenderForImageConversion.tiff");

    std::cout << "Workbook rendered to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
