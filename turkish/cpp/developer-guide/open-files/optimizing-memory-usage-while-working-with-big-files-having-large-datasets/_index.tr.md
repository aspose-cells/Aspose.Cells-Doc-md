---
title: Büyük Dosyalar ve Büyük Veri Setleriyle Çalışırken Bellek Kullanımını Optimize Etmek (C++)
linktitle: Bellek Kullanımını Optimize Etmek
type: docs
weight: 180
url: /tr/cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
description: Aspose.Cells kullanarak büyük Excel dosyalarıyla çalışırken bellek kullanımını nasıl optimize edeceğinizi öğrenin.
---

{{% alert color="primary" %}}

Büyük veri setleri ile elektronik tablo oluştururken veya büyük bir Microsoft Excel dosyasını okurken, işlemin alacağı toplam RAM miktarı her zaman bir endişe kaynağıdır. Bu zorlukla başa çıkmak için adapte edilebilecek önlemler bulunmaktadır. Aspose.Cells, bellek kullanımını düşürmek, azaltmak ve optimize etmek için ilgili seçenekler ve API çağrıları sağlar. Ayrıca, işlemi daha verimli hale getirerek daha hızlı çalışmasına yardımcı olabilir.

Hücre verisi için bellek kullanımını optimize etmek ve genel bellek maliyetini azaltmak için [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) seçeneğini kullanın. Büyük veri setleri için hücreler oluştururken, varsayılan ayar ([**MemorySetting.Normal**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/)) kullanmaktan belirli bir miktarda bellek tasarrufu sağlayabilir.

{{% /alert %}}

## **Bellek Kullanımını Optimize Etme**

### **Büyük Excel Dosyaları Okuma**

Aşağıdaki örnek, optimize edilmiş modda büyük bir Microsoft Excel dosyasını nasıl okuyacağınızı göstermektedir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Specify the LoadOptions
    LoadOptions opt;

    // Set the memory preferences
    opt.SetMemorySetting(MemorySetting::MemoryPreference);

    // Instantiate the Workbook
    // Load the Big Excel file having large Data set in it
    Workbook wb(srcDir + u"Book1.xlsx", opt);

    std::cout << "Workbook loaded successfully with memory preference setting!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Büyük Excel Dosyaları Yazma**

Aşağıdaki örnek, optimize edilmiş bir modda bir çalışma sayfasına büyük bir veri seti yazmanın nasıl yapılacağını gösterir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook wb;

    // Set the memory preferences
    // Note: This setting cannot take effect for the existing worksheets that are created before using the below line of code
    wb.GetSettings().SetMemorySetting(MemorySetting::MemoryPreference);

    // Note: The memory settings also would not work for the default sheet i.e., "Sheet1" etc. automatically created by the Workbook

    // To change the memory setting of existing sheets, please change memory setting for them manually:
    Cells cells = wb.GetWorksheets().Get(0).GetCells();
    cells.SetMemorySetting(MemorySetting::MemoryPreference);

    // Input large dataset into the cells of the worksheet.
    // Your code goes here.
    // .........

    // Get cells of the newly created Worksheet "Sheet2" whose memory setting is same with the one defined in WorkbookSettings:
    cells = wb.GetWorksheets().Add(u"Sheet2").GetCells();

    // Input large dataset into the cells of the worksheet.
    // Your code goes here.
    // .........

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Dikkat**

Varsayılan seçenek, [**MemorySetting.Normal**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) tüm sürümler için uygulanır. Ancak, bazı durumlarda, örneğin bir çalışma kitabı oluştururken hücreler için büyük bir veri kümesi oluşturmaları gereken durumlarda, [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) seçeneği hafıza kullanımını optimize edebilir ve uygulama için hafıza maliyetini azaltabilir. Bununla birlikte, bu seçenek bazı özel durumlarda performansı düşürebilir.

1. **Rastgele ve Tekrarlanan Şekilde Hücrelere Erişme**: Hücre koleksiyonuna erişmek için en verimli sıralama, önce bir satırda hücre hücre, ardından satır satır erişmektir. Özellikle, [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/), [**RowCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/rowcollection/) ve [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/)'den elde edilen Numaralayıcı ile satırlara/hücrelere erişiyorsanız, performans [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) ile maksimize edilecektir.
1. **Hücreleri ve Satırları Ekleme ve Silme**: Hücreler/Satırlar için çok sayıda ekleme/silme işlemi varsa, *MemoryPreference* modu, *Normal* moduna göre performansın gözle görülür derecede düşmesine neden olacaktır.
1. **Farklı Hücre Türlerinde Çalışma**: Eğer hücrelerin çoğu dize değerleri veya formülleri içeriyorsa, hafıza maliyeti *Normal* mod ile aynı olacaktır, ancak boş hücreler veya hücre değerleri sayısal, mantıksal vb. ise, [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/cpp/aspose.cells/memorysetting/) seçeneği daha iyi performans sunacaktır.
{{< app/cells/assistant language="cpp" >}}
