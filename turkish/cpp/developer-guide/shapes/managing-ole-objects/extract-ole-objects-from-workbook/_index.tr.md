---
title: C++ ile Çalışma Kitabından OLE Nesnelerini Çıkar
linktitle: Çalışma Kitabından OLE Nesneleri Çıkarma
type: docs
weight: 110
url: /tr/cpp/extract-ole-objects-from-workbook/
description: Aspose.Cells kullanarak C++ ile çalışma kitabından OLE nesnelerini nasıl çıkaracağınızı öğrenin.
---

{{% alert color="primary" %}}

Bazen, çalışma kitabından OLE nesnelerini çıkarmanız gerekir. Aspose.Cells, bu OLE nesnelerini çıkarma ve kaydetmeyi destekler.

Bu makale, Visual Studio'da bir konsol uygulaması oluşturmayı ve birkaç basit kod satırıyla çalışma kitabından farklı OLE nesnelerini çıkarmayı gösterir.

{{% /alert %}}

## **Bir Çalışma Kitabından OLE Nesneleri Çıkarma**

### **Bir Şablon Çalışma Kitabı Oluşturma**

1. Microsoft Excel'de bir çalışma kitabı oluşturun.
1. İlk çalışma sayfasına bir Microsoft Word belgesi, bir Excel çalışma kitabı ve bir PDF belgesi OLE nesnesi olarak ekleyin.

|**OLE nesneleri bulunan şablon belge (OleFile.xls)**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

Daha sonra, OLE nesnelerini çıkarın ve ilgili dosya türleriyle sabit diske kaydedin.

### **Aspose.Cells'i İndirin ve Yükleyin**

1. [Aspose.Cells for C++'i indirin](https://downloads.aspose.com/cells/cpp).
1. Geliştirme bilgisayarınıza kurun.

Kurulduğunda, tüm Aspose bileşenleri değerlendirme modunda çalışır. Değerlendirme modunun süresiz bir sınırlaması yoktur ve yalnızca üretilen belgelere filigran enjekte eder.

### **Bir Proje Oluşturun**

Başlat **Visual Studio** ve yeni bir konsol uygulaması oluşturun. Bu örnek, bir C++ konsol uygulamasını gösterecek.

1. Referanslar Ekleyin
   1. Projenize Aspose.Cells bileşenine referans ekleyin, örneğin, ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll’ye referans ekleyin.

### **OLE Nesnelerini Çıkarın**

Aşağıdaki kod, OLE nesnelerini bulma ve çıkarma işlemini gerçekleştirir. OLE nesneleri (DOC, XLS ve PDF dosyaları) diske kaydedilir.

```cpp
#include <iostream>
#include <fstream>
#include <memory>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the template file
    Workbook workbook(srcDir + u"oleFile.xlsx");

    // Get the OleObject Collection in the first worksheet
    OleObjectCollection oles = workbook.GetWorksheets().Get(0).GetOleObjects();

    // Loop through all the oleobjects and extract each object in the worksheet
    for (int i = 0; i < oles.GetCount(); i++)
    {
        OleObject ole = oles.Get(i);

        // Specify the output filename
        U16String fileName = srcDir + u"outOle" + U16String(std::to_string(i).c_str()) + u".";

        // Specify each file format based on the oleobject format type
        switch (ole.GetFileFormatType())
        {
            case FileFormatType::Doc:
                fileName += u"doc";
                break;
            case FileFormatType::Excel97To2003:
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
            if (objectData.GetLength() > 0)
            {
                Workbook oleBook(objectData);
                oleBook.GetSettings().SetIsHidden(false);
                oleBook.Save(srcDir + u"outOle" + U16String(std::to_string(i).c_str()) + u".out.xlsx");
            }
        }
        // Create the files based on the oleobject format types
        else
        {
            Vector<uint8_t> objectData = ole.GetObjectData();
            if (objectData.GetLength() > 0)
            {
                std::ofstream fs(fileName.ToUtf8().c_str(), std::ios::binary);
                fs.write(reinterpret_cast<const char*>(objectData.GetData()), objectData.GetLength());
                fs.close();
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
