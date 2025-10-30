---
title: Başlıklar ve Altbilgiler ile C++ kullanımı
linktitle: Başlık ve Altbilgileri Ayarlama
type: docs
weight: 30
url: /tr/cpp/setting-headers-and-footers/
description: Bu makale, C++ API veya Kütüphane kullanılarak başlık ve altbilgiye resim eklemek için betik komutlarıyla programlı olarak nasıl yapıldığını açıklar.
keywords: Excel başlık ve altbilgiye resim ekleme, C++ betik komutlarıyla ayarlama
---

{{% alert color="primary" %}}

Başlık ve altbilgiler, üst kenar boşluğunun altında veya alt kenar boşluğunun üstünde gösterilen metin satırlarıdır. Çalışma sayfalarına da başlık ve altbilgi eklemek mümkündür. Başlıklar ve altbilgiler, sayfa numarası, yazar adı, konu adı veya tarih ve saat gibi yararlı bilgileri göstermek için kullanılabilir. Başlıklar ve altbilgiler, sayfa düzeni ayarları kullanılarak yönetilir.

{{% /alert %}}

## **Başlık ve Altbilgileri Ayarlama**

Aspose.Cells, çalışma sayfalarına çalışma zamanında başlıklar ve altbilgiler eklemenize olanak tanır, ancak yazdırma için önceden tasarlanmış bir dosyada başlık ve altbilgileri manuel olarak ayarlamanızı öneririz. Çaba ve geliştirme zamanı tasarrufu yapmak için Microsoft Excel'i başlık ve altbilgileri ayarlamak için bir GUI aracı olarak kullanabilirsiniz. Aspose.Cells, dosyayı içe aktarabilir ve ayarlamaları kaydedebilir.

Çalışma zamanında başlık ve altbilgiler eklemek için Aspose.Cells, özel API çağrıları ve betik komutları sağlar.

### **Betik Komutları**

Betik komutları, başlık ve altbilgi biçimlendirmesini ayarlamanıza olanak tanıyan özel komutlardır.

|**Betik Komutları**|**Açıklama**|
| :- | :- |
|&P| Geçerli sayfa numarası
|&G| Bir resim
|&N| Toplam sayfa sayısı
|&D| Geçerli tarih
|&T| Geçerli saat
|&A| Çalışma sayfası adı
|&F| Dosya adı ve yolu olmadan
|&&Yazı|&Yazıyı gösterir. Örneğin: &&WO &WO olarak görüntülenir|
|&"\<FontName>"| Yazı tipi adını temsil eder. Örneğin: &"Arial"|
|&"\<FontName>, \<FontStyle>"| Stil ile yazı tipi adını temsil eder. Örneğin: &"Arial,Kalın"|
|&\<FontSize>| Yazı tipi boyutunu temsil eder. Örneğin: “&14abc”. Ancak, bu komuttan sonra başlığa yazdırılacak düz bir sayı izlenecekse, bu, yazı tipi boyutundan bir boşluk karakteri ile ayrılmalıdır. Örneğin: “&14 123”.|

### **Başlık ve Altbilgileri Ayarlama**

 [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) sınıfı, çalışma sayfasına başlık ve altbilgi eklemek için kullanılan [**SetHeader**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setheader/) ve [**SetFooter**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setfooter/) adlı iki yöntem sağlar. Bu yöntemler yalnızca iki parametre alır:

- **Bölüm** – başlığın veya altbilginin yerleştirileceği bölüm. Sırasıyla sol, merkez ve sağ olmak üzere temsil edilen üç bölüm bulunmaktadır.
- **Betik** – başlık veya altbilgi için kullanılacak betik. Bu betik, başlıkları veya altbilgileri biçimlendirmek için betik komutları içerir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook excel;

    // Get the first worksheet's PageSetup
    PageSetup pageSetup = excel.GetWorksheets().Get(0).GetPageSetup();

    // Set worksheet name at the left section of the header
    pageSetup.SetHeader(0, u"&A");

    // Set current date and time at the central section of the header with custom font
    pageSetup.SetHeader(1, u"&\"Times New Roman,Bold\"&D-&T");

    // Set current file name at the right section of the header with custom font
    pageSetup.SetHeader(2, u"&\"Times New Roman,Bold\"&12&F");

    // Set a string at the left section of the footer with custom font for part of the string
    pageSetup.SetFooter(0, u"Hello World! &\"Courier New\"&14 123");

    // Set the current page number at the central section of the footer
    pageSetup.SetFooter(1, u"&P");

    // Set page count at the right section of the footer
    pageSetup.SetFooter(2, u"&N");

    // Save the workbook
    excel.Save(u"SetHeadersAndFooters_out.xls");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Bir Resmi Başlık veya Altbilgiye Ekleyin**

[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) sınıfı, başlığa ve altbilgiye resim eklemek için kullanılan [**SetHeaderPicture**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setheaderpicture/) ve [**SetFooterPicture**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setfooterpicture/) adlı iki ek yönteme sahiptir. Bu yöntemlerle şu parametreler alınır:

- **Bölüm** – resmin yerleştirileceği başlık veya altbilgi bölümü. Sırasıyla sol, merkez ve sağ olmak üzere temsil edilen üç bölüm bulunmaktadır.
- **Bayt dizisi** – görsel veri (ikili veri bir byte dizisinin tamponuna yazılmalıdır).

Aşağıdaki kodu çalıştırdıktan sonra dosyayı açarak, çalışma sayfasının üstbilgisini kontrol edin:

1. **Dosya** menüsünde **Sayfa Düzeni**'ni seçin. Bir iletişim kutusu görüntülenecektir.
1. **Üst Bilgi/Alt Bilgi** sekmesini seçin.

```cpp
#include <iostream>
#include <fstream>
#include <vector>
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

    // Creating a Workbook object
    Workbook workbook;

    // Creating a string variable to store the url of the logo/picture
    U16String logo_url = srcDir + u"aspose-logo.jpg";

    // Declaring a FileStream object
    ifstream inFile;

    // Declaring a byte array
    vector<uint8_t> binaryData;

    // Opening the logo/picture in the stream
    inFile.open(logo_url.ToUtf8(), ios::binary);

    if (inFile.is_open())
    {
        // Get the size of the file
        inFile.seekg(0, ios::end);
        size_t fileSize = inFile.tellg();
        inFile.seekg(0, ios::beg);

        // Resize the byte array to the size of the file
        binaryData.resize(fileSize);

        // Read the file into the byte array
        inFile.read(reinterpret_cast<char*>(binaryData.data()), fileSize);

        // Creating a PageSetup object to get the page settings of the first worksheet of the workbook
        PageSetup pageSetup = workbook.GetWorksheets().Get(0).GetPageSetup();

        // Convert std::vector to Aspose::Cells::Vector
        Aspose::Cells::Vector<uint8_t> asposeBinaryData(binaryData.data(), static_cast<int32_t>(binaryData.size()));

        // Setting the logo/picture in the central section of the page header
        pageSetup.SetHeaderPicture(1, asposeBinaryData);

        // Setting the script for the logo/picture
        pageSetup.SetHeader(1, u"&G");

        // Setting the Sheet's name in the right section of the page header with the script
        pageSetup.SetHeader(2, u"&A");

        // Saving the workbook
        workbook.Save(outDir + u"InsertImageInHeaderFooter_out.xls");

        // Closing the FileStream object
        inFile.close();
    }
    else
    {
        cerr << "Failed to open the image file." << endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
