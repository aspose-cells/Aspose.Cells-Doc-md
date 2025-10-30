---
title: Aspose.Cells ile OLE Nesnelerini Yönetmek
linktitle: OLE Nesneleri Yönetme
type: docs
weight: 50
url: /tr/cpp/managing-ole-objects/
description: Aspose.Cells kullanarak çalışma sayfalarında OLE nesnelerini eklemeyi, çıkarmayı ve manipüle etmeyi öğrenin.
---

## **Giriş**

OLE (Object Linking and Embedding), Microsoft'un bileşik bir belge teknolojisi için çerçevesidir. Kısaca, bileşik bir belge türü her türlü görsel ve bilgi nesnesini içerebilen bir masaüstü görüntüsü gibidir: metin, takvimler, animasyonlar, ses, hareketli video, 3D, sürekli güncellenen haberler, kontroller vb. Her masaüstü nesnesi, bir kullanıcıyla etkileşime girebilir ve aynı zamanda masaüstünde bulunan diğer nesnelerle iletişim kurabilir.

OLE (Object Linking and Embedding), birçok farklı programa destek sağlar ve bir programda oluşturulan içeriğin başka bir programa kullanılmasını sağlar. Örneğin, bir Microsoft Word belgesini Microsoft Excel'e ekleyebilirsiniz. Ekleyebileceğiniz içerik türlerini görmek için **Ekle** menüsünde **Nesne**'ye tıklayın. Bilgisayara yüklü olan ve OLE nesneleri destekleyen yalnızca programlar **Nesne türü** kutusunda görünür.

### **Çalışsayan Elemanları Çalışsayan Eleman (OLE) Nesnesi Ekleme**

Aspose.Cells, çalışma sayfalarında OLE nesneleri ekleme, çıkarma ve düzenleme desteği sağlar. Bu nedenle, Aspose.Cells, koleksiyon listesine yeni bir OLE Nesnesi ekmek için kullanılan [**OleObjectCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobjectcollection/) sınıfına sahiptir. Diğer bir sınıf olan [**OleObject**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/), bir OLE Nesnesini temsil eder. Bazı önemli üyeleri şunlardır:

- [**ImageData**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getimagedata/) özelliği, bayt dizisi biçiminde olan resim (simge) verisini belirtir. Bu görüntü, çalışma sayfasında OLE Nesnesini göstermek için gösterilecektir.
- [**ObjectData**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/) özelliği, nesne verisini bayt dizisi biçiminde belirtir. Bu veriyi çift tıklayarak ilgili programda gösterilir.

Aşağıdaki örnek, çalışsayan elemanları çalışsayan eleman(lar)ı çalışsayan eleman yapıştırma.

```c++
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

std::vector<uint8_t> ReadFileToVector(const U16String& filePath) {
    std::ifstream file(filePath.ToUtf8(), std::ios::binary | std::ios::ate);
    if (!file) return {};
    std::streamsize size = file.tellg();
    file.seekg(0, std::ios::beg);
    std::vector<uint8_t> buffer(size);
    if (size > 0)
        file.read(reinterpret_cast<char*>(buffer.data()), size);
    return buffer;
}

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    U16String imagePath = srcDir + u"logo.jpg";
    std::vector<uint8_t> imageData = ReadFileToVector(imagePath);

    U16String objectPath = srcDir + u"book1.xls";
    std::vector<uint8_t> objectData = ReadFileToVector(objectPath);
    Vector<uint8_t> data(objectData.data(), static_cast<int32_t>(objectData.size()));
    sheet.GetOleObjects().Add(14, 3, 200, 220, data);
    if (sheet.GetOleObjects().GetCount() > 0) {
        sheet.GetOleObjects().Get(0).SetObjectData(data);
    }

    workbook.Save(outDir + u"output.out.xls");
    std::cout << "OLE object added successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Çalışsayan Elemanlar'ın Çalışsayan Elemanları Çıkarma**

Aşağıdaki örnek, bir çalışma kitabından çalışsayan elemanları çıkarmayı göstermektedir. Örnek, mevcut bir XLS dosyasından farklı çalışsayan elemanlar alır ve farklı dosyalar (DOC, XLS, PPT, PDF vb.) çalışsayan elemanın dosya biçim türüne dayalı olarak kaydeder.

Kodu çalıştırdıktan sonra, ilgili Çalışsayan Elemanın biçim türlerine dayalı olarak farklı dosyaları kaydedebiliriz.

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the template file
    Workbook workbook(srcDir + u"book1.xls");

    // Get the OleObject Collection in the first worksheet
    OleObjectCollection oles = workbook.GetWorksheets().Get(0).GetOleObjects();

    // Loop through all the oleobjects and extract each object
    for (int32_t i = 0; i < oles.GetCount(); i++)
    {
        OleObject ole = oles.Get(i);

        // Specify the output filename
        U16String fileName = srcDir + u"ole_" + U16String(std::to_string(i).c_str()) + u".";

        // Specify each file format based on the oleobject format type
        switch (ole.GetFileFormatType())
        {
        case FileFormatType::Doc:
            fileName += u"doc";
            break;
        case FileFormatType::Xlsx:
            fileName += u"Xlsx";
            break;
        case FileFormatType::Ppt:
            fileName += u"Ppt";
            break;
        case FileFormatType::Pdf:
            fileName += u"Pdf";
            break;
        case FileFormatType::Unknown:
            fileName += u"Jpg";
            break;
        default:
            // Handle other formats if needed
            break;
        }

        // Save the oleobject as a new excel file if the object type is xls
        if (ole.GetFileFormatType() == FileFormatType::Xlsx)
        {
            Vector<uint8_t> objectData = ole.GetObjectData();
            Workbook oleBook(objectData);
            oleBook.GetSettings().SetIsHidden(false);
            oleBook.Save(srcDir + u"Excel_File" + U16String(std::to_string(i).c_str()) + u".out.xlsx");
        }
        else
        {
            // Create the files based on the oleobject format types
            std::ofstream fs(fileName.ToUtf8().c_str(), std::ios::binary);
            Vector<uint8_t> objectData = ole.GetObjectData();
            fs.write(reinterpret_cast<const char*>(objectData.GetData()), objectData.GetLength());
            fs.close();
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Gömülü MOL Dosyasının Çıkarılması**

Aspose.Cells, MOL (Moleküler veriyi içeren atomlar ve bağlar hakkında bilgi içeren dosya) gibi alışılmadık türde nesnelerin çıkarılmasını destekler. Aşağıdaki kod parçacığı, gömülü bir MOL dosyasını çıkarmayı ve bu [örnek excel dosyası](94896196.xlsx) kullanarak diske kaydetmeyi gösterir.

```c++
#include <iostream>
#include <fstream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"EmbeddedMolSample.xlsx");

    int index = 1;

    WorksheetCollection sheets = workbook.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); i++)
    {
        Worksheet sheet = sheets.Get(i);
        OleObjectCollection oles = sheet.GetOleObjects();

        for (int j = 0; j < oles.GetCount(); j++)
        {
            OleObject ole = oles.Get(j);

            std::wstring indexWStr = std::to_wstring(index);
            U16String fileName = outDir + u"OleObject" + U16String(reinterpret_cast<const char16_t*>(indexWStr.c_str())) + u".mol";

            std::ofstream fs(fileName.ToUtf8(), std::ios::binary);
            if (fs.is_open())
            {
                Vector<uint8_t> objectData = ole.GetObjectData();
                fs.write(reinterpret_cast<const char*>(objectData.GetData()), objectData.GetLength());
                fs.close();
                index++;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Gelişmiş Konular**
- [Bağlı Ole Nesnesinin Görüntü Etiketini Erişme ve Değiştirme](/cells/tr/cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Microsoft Excel kullanarak Aspose.Cells ile Çalışmayan Elemanı Otomatik Yenileme](/cells/tr/cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Çalışma Kitabından Çalışmayan Elemanları Çıkarma](/cells/tr/cpp/extract-ole-objects-from-workbook/)
- [Gömülü Çalışmayan Elemanın Sınıf Tanımlayıcısını Al veya Ayarla](/cells/tr/cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Ole Nesnesi Olarak Bir WAV Dosyası Eklemek](/cells/tr/cpp/inserting-a-wav-file-as-an-ole-object/)
{{< app/cells/assistant language="cpp" >}}
