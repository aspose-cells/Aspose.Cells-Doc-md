---
title: C++ ile Elektronik Tablo Çizimleri için Yazı Tiplerini Yapılandırma
linktitle: Yayınlanan İşlenmiş Elektronik Tablolar için Yazı Tiplerini Yapılandırma
type: docs
weight: 10
url: /tr/cpp/configuring-fonts-for-rendering-spreadsheets/
description: Aspose.Cells for C++ kullanarak elektronik tabloların resim, PDF ve XPS formatlarına dönüştürülmesi ve bunların görüntüleme ayarlarının yapılandırılması hakkında bilgi edinin.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells API'leri, elektronik tabloların resim formatlarında render edilmesi ve PDF veya XPS formatlarına dönüştürülmesi için imkan sağlar. Dönüşüm doğruluğunu maksimize etmek için, kullanılan yazı tiplerinin işletim sisteminin varsayılan yazı tipi dizininde bulunması gerekir. Gerekli yazı tipleri mevcut değilse, Aspose.Cells API'leri gereken yazı tiplerini mevcut olanlarla değiştirmeye çalışacaktır.

## **Yazı Tiplerinin Seçimi**

Aşağıda, Aspose.Cells API'lerinin gizli süreçleri bulunmaktadır:

1. API, elektronik tabloda kullanılan tam olarak eşleşen yazı tipini dosya sistemi üzerinde bulmaya çalışır.
1. API, tam olarak aynı adı taşıyan yazı tiplerini bulamazsa, çalışma kitabının [**DefaultStyle.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) özelliği altında belirtilen varsayılan yazı tipini kullanmaya çalışır.
1. API, çalışma kitabının [**DefaultStyle.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) özelliği altında belirtilen yazı tipini bulamazsa, [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) veya [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) özelliği altında belirtilen yazı tipini kullanmaya çalışır.
1. API, [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) veya [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) özelliği altında belirtilen yazı tipini bulamazsa, [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getdefaultfontname/) özelliği altında belirtilen yazı tipini kullanmaya çalışır.
1. API, [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getdefaultfontname/) özelliği altında belirtilen yazı tipini bulamazsa, kullanılabilir tüm yazı tiplerinden en uygun olanları seçmeye çalışır.
1. Son olarak, API, dosya sistemi üzerinde herhangi bir yazı tipi bulamazsa, elektronik tabloyu Arial kullanarak render eder.

## **Özel Yazı Tipi Klasörlerini Ayarlayın**

Aspose.Cells API'leri, gerekli yazı tiplerini işletim sisteminin varsayılan yazı tipi dizininde arar. Gerekli yazı tipleri sistem dizininde yoksa, API'ler özel (kullanıcı tanımlı) dizinlerde arama yapar. [**FontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/) sınıfı, özel yazı tipi dizinleri ayarlamak için birkaç yol sağlar; detaylar aşağıda belirtilmiştir:

1. [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolder/): Bu yöntem, sadece bir klasör ayarlanacaksa kullanışlıdır.
1. [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolders/): Bu yöntem, yazı tipleri birden fazla klasörde bulunuyorsa ve kullanıcı tüm klasörleri ayrı ayrı ayarlamak istiyorsa kullanışlıdır.
1. [**FontConfigs.SetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontsources/): Bu mekanizma, kullanıcı birden çok klasörden font yüklemek, tek bir font dosyası veya bayt dizisinden font verisi yüklemek istediğinde kullanışlıdır.

{{% alert color="primary" %}}

Hem [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolder/) hem de [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolders/) yöntemleri Boolean türünde ikinci parametre kabul eder. İkinci parametre olarak **true** geçirilirse, Aspose.Cells API'leri alt klasörlerde font dosyalarını aramaya yönlendirilir.

{{% /alert %}}

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

Vector<uint8_t> GetDataFromFile(const U16String& file)
{
    std::string f = file.ToUtf8();
    // open a file 
    std::ifstream fileStream(f, std::ios::binary);

    if (!fileStream.is_open()) {
        std::cerr << "Failed to open the file." << std::endl;
        return 1;
    }

    // Get file size
    fileStream.seekg(0, std::ios::end);
    std::streampos fileSize = fileStream.tellg();
    fileStream.seekg(0, std::ios::beg);

    // Read file contents into uint8_t array
    uint8_t* buffer = new uint8_t[fileSize];
    fileStream.read(reinterpret_cast<char*>(buffer), fileSize);
    fileStream.close();

    Vector<uint8_t>data(buffer, fileSize);
    delete[] buffer;

    return data;
}

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String fontFolder1 = srcDir + u"Arial";
    U16String fontFolder2 = srcDir + u"Calibri";
    U16String fontFile = srcDir + u"arial.ttf";

    FontConfigs::SetFontFolder(fontFolder1, true);

    Vector<U16String> fontFolders{ fontFolder1 , fontFolder2 };

    FontConfigs::SetFontFolders(fontFolders, false);

    FolderFontSource sourceFolder(fontFolder1, false);
    FileFontSource sourceFile(fontFile);
    Vector<uint8_t> fontData = GetDataFromFile(fontFile);
    MemoryFontSource sourceMemory(fontData);

    Vector<FontSourceBase> fontSources{ sourceFolder ,sourceFile ,sourceMemory };

    FontConfigs::SetFontSources(fontSources);

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Lütfen yukarıda belirtilen yöntemlerden herhangi birini, Aspose.Cells API'lerinin diğer nesnelerini çağırmadan, uygulamanın başlangıcında kullanın.

{{% /alert %}}

{{% alert color="primary" %}}

Yukarıda bahsedilen tüm yöntemler, yazı tiplerini ayarlamak için kullanıldığında, sadece son ayarlamalar etkili olacaktır.

{{% /alert %}}

## **Yazı Tipi Yedekleme Mekanizması**

Aspose.Cells API'leri ayrıca render amaçlarıyla yedek fontların belirlenmesi imkanı sağlar. Bu mekanizma, dönüşümün yapılacağı makinede gerekli fontun bulunmadığı durumlarda faydalıdır. Kullanıcılar, gereken orijinal fontun yerine alternatif olarak font isimleri listesi sağlayabilir. Bunu başarmak için, Aspose.Cells API'leri [**FontConfigs.SetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontsubstitutes/) metodunu expose etmiştir; bu metod iki parametre alır. Birinci parametre, değiştirilmesi gereken fontun adı olan **string** tipindedir. İkinci parametre ise **string** tipinde bir dizidir. Kullanıcılar, orijinal font isminin yerine kullanılacak font isimleri listesini sağlayabilirler (birinci parametre ile belirtilmiş).

İşte basit bir kullanım senaryosu:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Substituting the Arial font with Times New Roman & Calibri
    Vector<U16String> substituteFonts{ u"Times New Roman", u"Calibri" };
    FontConfigs::SetFontSubstitutes(u"Arial", substituteFonts);

    Aspose::Cells::Cleanup();
}
```

## **Bilgi Toplama**

Yukarıda bahsedilen yöntemlere ek olarak, Aspose.Cells API'leri, hangi kaynakların ve yedeklerin ayarlandığına dair bilgi toplamaya imkan sağlar:

1. [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsources/) metodu, belirtilen font kaynaklarının listesini içeren [**FontSourceBase**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsourcebase/) türünde bir dizi döndürür. Eğer hiç kaynak ayarlanmadıysa, [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsources/) metodu boş bir dizi döner.
1. [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsubstitutes/) metodu, ayarlanan yedekleme için font adını belirlemek üzere **string** türü bir parametre kabul eder. Belirtilen font adına yedekleme ayarlanmadıysa, [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsubstitutes/) metodu null döner.

## **Gelişmiş Konular**
- [Yaygın Olarak Kullanılan Yazı tipini Resimlere Dönüştürürken Belirleme](/cells/tr/cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [PdfSaveOptions ve ImageOrPrintOptions'ın DefaultFont özelliğini öncelikli şekilde ayarlayın](/cells/tr/cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Desteklenen Yazı Tipi Biçimleri](/cells/tr/cpp/supported-font-formats/)
{{< app/cells/assistant language="cpp" >}}
