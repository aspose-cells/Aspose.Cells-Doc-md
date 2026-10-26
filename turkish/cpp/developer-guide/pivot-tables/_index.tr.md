---
title: Özet Tablosu Oluşturma
linktitle: Özet Tablosu Oluşturma
description: Aspose.Cells for C++ ile özet tabloları oluşturun ve biçimlendirin.
keywords: Özet Tablosu Oluşturma, Özet Tablosu Ekleme, Özet Tablosu Biçimlendirme.
type: docs
weight: 160
url: /tr/cpp/create-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Özet Tablo Nedir?**
Özet tablo, etkileşimli bir özet raporudur: büyük bir ham, satır satır veri bloğunu tek bir formül kullanmadan kompakt bir matrise yoğunlaştırır. Hangi sütunların satır etiketlerine, hangilerinin sütun etiketlerine dönüşeceğini ve hangilerinin değer olarak toplanacağını siz belirlersiniz; gruplama ve hesaplamayı özet tablo yapar:
- **Özetleme** — uzun formül zincirleri yerine ürün, bölge veya çeyrek bazında toplam satışları sunar.
- **Karşılaştırma** — satırlara kategoriler, sütunlara dönemler yerleştirildiğinde düz bir liste, eğilimlerin tek bakışta görülebildiği çapraz rapora dönüşür.
- **Detaylandırma** — herhangi bir özet değere çift tıklayarak arkasındaki kaynak satırları inceleyin.
- **Yenileme** — kaynak veriler değiştiğinde tek bir yenileme tüm raporu yeniden hesaplar.
Tipik kullanım senaryoları; satış panoları, gider dökümleri ve stok analizi gibi "bu sayılar kategori ve zamana göre nasıl dağılıyor?" biçimindeki sorulardır. Aspose.Cells for C++ ile bir özet tablo, çalışma sayfasının [PivotTableCollection.Add()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/add/) yöntemiyle oluşturulur. Özet tablo oluşturulduktan sonra [PivotTable](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/) sınıfını kullanarak üzerinde çalışabilirsiniz.

## **Özet Tablosu Oluşturma**
Aşağıdaki örnek kod, bir özet tablosunun nasıl oluşturulacağını ve nasıl kullanılacağını gösterir. Lütfen bu kodla oluşturulan [çıktı Excel dosyasını](23167010.xlsx) ve çıktı Excel dosyasının Microsoft Excel'de görüntülendiği ekran görüntüsünü inceleyin.
![todo:image_alt_text](create-pivot-table_1.png)

## **Örnek Kod**

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Yeni bir çalışma kitabı oluşturun ve ilk çalışma sayfasını alın
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // Kaynak verileri yazın: spor ve çeyrek bazında satışlar
    cells.Get(u"A1").PutValue(u"Sport");
    cells.Get(u"B1").PutValue(u"Quarter");
    cells.Get(u"C1").PutValue(u"Sales");
    cells.Get(u"A2").PutValue(u"Golf");
    cells.Get(u"B2").PutValue(u"Qtr3");
    cells.Get(u"C2").PutValue(1500);
    cells.Get(u"A3").PutValue(u"Golf");
    cells.Get(u"B3").PutValue(u"Qtr4");
    cells.Get(u"C3").PutValue(2000);
    cells.Get(u"A4").PutValue(u"Tennis");
    cells.Get(u"B4").PutValue(u"Qtr3");
    cells.Get(u"C4").PutValue(600);
    cells.Get(u"A5").PutValue(u"Tennis");
    cells.Get(u"B5").PutValue(u"Qtr4");
    cells.Get(u"C5").PutValue(1500);
    cells.Get(u"A6").PutValue(u"Tennis");
    cells.Get(u"B6").PutValue(u"Qtr3");
    cells.Get(u"C6").PutValue(4070);
    cells.Get(u"A7").PutValue(u"Tennis");
    cells.Get(u"B7").PutValue(u"Qtr4");
    cells.Get(u"C7").PutValue(5000);
    cells.Get(u"A8").PutValue(u"Golf");
    cells.Get(u"B8").PutValue(u"Qtr3");
    cells.Get(u"C8").PutValue(6430);

    // E3 hedef hücresine A1:C8 kaynaklı bir pivot tablo ekleyin
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"A1:C8", 2, 4);

    // Pivot alanlarını atayın: Spor satırlara, Çeyrek sütunlara, Satışlar verilere
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Quarter");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");

    // Çalışma kitabını kaydedin
    workbook.Save(u"pivotTable_test_out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{< app/cells/assistant language="cpp" >}}