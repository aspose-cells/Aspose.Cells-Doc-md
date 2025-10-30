---
title: C++ ile Gömülü OLE Nesnesinin Sınıf Tanımlayıcısını Al veya Ayarla
linktitle: Gömülü OLE Nesnesinin Sınıf Kimliğini Alın veya Ayarlayın
type: docs
weight: 200
url: /tr/cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: Aspose.Cells kullanarak gömülü OLE nesnelerinin sınıf tanımlayıcısını nasıl alacağınızı veya ayarlayacağınızı öğrenin.
---

## **Olası Kullanım Senaryoları**
Aspose.Cells, gömülü OLE nesnesinin sınıf tanımlayıcısını almak veya ayarlamak için [OleObject.GetClassIdentifier()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getclassidentifier/) özelliğini sağlar. OLE Nesnesi Sınıf Tanımlayıcılar aslında GUID'lerdir, yani Küresel Olarak Benzersiz Tanımlayıcılar. GUID her zaman 16 bayt uzunluğundadır, bu nedenle Sınıf Tanımlayıcılar da 16 bayt uzunluğundadır. Bunlar genellikle Windows Kayıt Defteri içinde bulunur ve ana uygulamaya, içeriğinde çeşitli gömülü kaynaklar bulunan OLE nesnelerini nasıl açacağınız konusunda bilgi sağlar.

## **Gömülü Çalışmayan Elemanın Sınıf Tanımlayıcısını Al veya Ayarla**
Aşağıdaki ekran görüntüsü, gömülü PowerPoint OLE nesnesi içeren [örnek excel dosyasından](5115190.xls) okunmuş olan OLE Nesnesi Sınıf Tanımlayıcısı, yani GUID'yi gösterir.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **Örnek Kod**
Lütfen, [örnek excel dosyasını](5115190.xls) çalıştırılarak ve ekran görüntüsünde gösterilenle birebir aynı olan OLE Nesnesinin Sınıf Tanımlayıcısını, yani GUID'yi yazdıran konsol çıktı ile birlikte örnek kodu inceleyin.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include <guiddef.h>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook wb(srcDir + u"sample.xls");
    Worksheet ws = wb.GetWorksheets().Get(0);
    OleObject oleObj = ws.GetOleObjects().Get(0);

    Vector<uint8_t> classIdentifier = oleObj.GetClassIdentifier();
    GUID guid;
    memcpy(&guid, classIdentifier.GetData(), sizeof(GUID));

    char guidStr[39];
    snprintf(guidStr, sizeof(guidStr), "{%08X-%04X-%04X-%02X%02X-%02X%02X%02X%02X}",
             guid.Data1, guid.Data2, guid.Data3,
             guid.Data4[0], guid.Data4[1], guid.Data4[2], guid.Data4[3],
             guid.Data4[4], guid.Data4[5], guid.Data4[6], guid.Data4[7]);

    std::cout << guidStr << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Konsol Çıktısı**
Yukarıdaki örnek kod çalıştırıldığında [örnek excel dosyası](5115190.xls) ile konsol çıktısıdır.

{{< highlight java >}}
DC020317-E6E2-4A62-B9FA-B3EFE16626F4
{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
