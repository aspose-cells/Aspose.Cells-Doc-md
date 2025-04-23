---
title: Microsoft Excel de Gelişmiş Filtre kullanarak karmaşık kriterlere uyan kayıtları görüntülemek için C++ ile uygulama
linktitle: Microsoft Excel İleri Filtresini Kullanarak Karmaşık Kriterleri Karşılayan Kayıtları Göstermek
type: docs
weight: 280
url: /tr/cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Gelişmiş filtre uygulama yollarını ve karmaşık kriterlere uyan kayıtları görüntüleme konusunda öğrenin, Aspose.Cells for C++ API kullanarak.
keywords: Gelişmiş Filtre Uygula, Gelişmiş Filtre Ayarla, Gelişmiş Filtre Ekle, Gelişmiş Filtre Oluştur, Bir aralığa Gelişmiş Filtre ekleme hakkında bilgi
---

## **Olası Kullanım Senaryoları**

Microsoft Excel, karmaşık kriterleri karşılayan kayıtları göstermek için çalışma sayfası verilerinde *Gelişmiş Filtre* uygulamanıza olanak tanır. Gelişmiş Filtre'yi *Veri > Gelişmiş* komutu ile uygulayabilirsiniz, ekran görüntüsünde gösterildiği gibi.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells ayrıca [**GetAdvancedFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getadvancedfilter/) yöntemi kullanılarak Gelişmiş Filtre'yi uygular. Tıpkı Microsoft Excel gibi, aşağıdaki parametreleri kabul eder.

**isFilter**

Listeyi yerinde filtrelemenin belirtilip belirtilmediğini gösterir.

**listRange**

Liste aralığı.

**criteriaRange**

Kriter aralığı.

**copyTo**

Verilerin kopyalanacağı aralık.

**uniqueRecordOnly**

Yalnızca benzersiz satırların gösterimi veya kopyalanması.

## **Karmaşık Kriterleri Karşılayan Kayıtları Göstermek İçin Microsoft Excel'in İleri Filtresini Uygulayın**

Aşağıdaki örnek kod, [Örnek Excel Dosyası](48496692.xlsx) üzerinde gelişmiş filtreyi uygular ve [Çıktı Excel Dosyası](48496691.xlsx) oluşturur. Ekran görüntüsü her iki dosyayı karşılaştırmak için gösterir. Ekran görüntüsü içindekileri incelediğinizde, verilerin karmaşık kriterlere göre çıktı Excel dosyası içinde filtrelendiğini görebilirsiniz.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Load your source workbook
    Workbook workbook(sourceDir + u"sampleAdvancedFilter.xlsx");

    // Access first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Apply advanced filter on range A5:D19 and criteria range is A1:D2
    // Besides, we want to filter in place
    // And, we want all filtered records not just unique records
    ws.Advanced_Filter(true, u"A5:D19", u"A1:D2", u"", false);

    // Save the workbook in xlsx format
    workbook.Save(outputDir + u"outputAdvancedFilter.xlsx", SaveFormat::Xlsx);

    std::cout << "Advanced filter applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
