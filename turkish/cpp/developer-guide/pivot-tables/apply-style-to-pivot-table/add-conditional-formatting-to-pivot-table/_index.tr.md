---
title: Pivot Tablosuna Koşullu Biçimlendirme Ekle
linktitle: Pivot Tablosuna Koşullu Biçimlendirme Ekle
description: Aspose.Cells for C++'da bir pivot tablosuna koşullu biçimlendirme ekleyin - ApplyTo ve PivotConditionFormatScopeType kapsamıyla bir kuralı veri bölgesine bağlayın, ya da hedefi AddCellArea ve PivotAreas ile tanımlayın, ardından FormatConditions.AddCondition aracılığıyla kuralları ve stilleri ekleyin.
keywords: Aspose.Cells for C++, Pivot Tablosu, koşullu biçimlendirme, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Veri, Alan, Seçim, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C++
type: docs
weight: 30
url: /tr/cpp/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Üst sayfada ve kardeş sayfada açıklanan stiller statiktir - bir `PivotArea` ya da `CellArea` bölgesi bir kez boyanır ve değerler ne olursa olsun stilini korur. Koşullu biçimlendirme ise kural tabanlı bir eşdeğerdir - 200'ün üzerindeki her tutarı vurgular, orta yüzde elliyi gölgelendirir veya en düşük sıralı öğeleri işaretler - ve vurgulama, pivot tablosu yeniden hesaplandığında veya yenilendiğinde değerleri izler.
Aspose.Cells'ta, pivot tablosu koşullu biçimlendirme `pivotTable.GetConditionalFormats()` koleksiyonunda bulunur. Her giriş, iki soruyu bağımsız olarak yanıtlayan bir `PivotConditionalFormat` nesnesidir:
- **Kural nerede uygulanır?** Hedef bölge, Excel kullanıcı arayüzündeki kapsam seçimcisine benzer şekilde `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)` aracılığıyla ya da `AddCellArea(CellArea)` ve `GetPivotAreas()` koleksiyonu ile açıkça bölgeyi adlandırarak tanımlanır.
- **Kural neyi test eder?** Bir veya daha fazla koşul, `GetFormatConditions()` üzerinden `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` kullanılarak eklenir ve her koşul kendi `Style`'ını taşır.

{{% alert color="primary" %}}
Bir pivot koşullu formatının `GetFormatConditions()` nesnesinde `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` veya `FormatConditionCollection.AddArea(CellArea)` metodunu çağırmayın. Bu iki aşırı yükleme, normal çalışma sayfası koşullu biçimlendirme API'sinden miras alınmıştır ve pivot tablolar için çalışmaz - hücre bölgesi hiçbir zaman pivot bölgesine dönüştürülmez, bu yüzden istek sessizce yok sayılır. Bölgeyi her zaman `PivotConditionalFormat` nesnesi üzerinde (`ApplyTo`, `AddCellArea` veya `GetPivotAreas()`) tanımlayın ve kuralları `AddCondition` aşırı yüklemelerinden biriyle ekleyin.
{{% /alert %}}

## **Kapsamla Bir Kural Uygulama (Excel UI Yöntemi)**
İlk yöntem, kuralı Excel kullanıcı arayüzünün yaptığı gibi konumlandırır. Pivot tablosunun bir hücresi, sıfır tabanlı çalışma sayfası koordinatlarıyla adlandırılır ve bir `PivotConditionFormatScopeType` kapsamı, Aspose.Cells'e bu hücreden kuralın ne kadar uzağa yayılması gerektiğini bildirir:
- `PivotConditionFormatScopeType::Data` - pivot tablosunun ürettiği tüm değer hücreleri, genel toplamlar dahil.
- `PivotConditionFormatScopeType::Field` - hücrenin belirttiği alana ait değer hücreleri, genel toplamlar hariç. Hücre bir satır‑alan etiketi gibi bir alan hücresi olmalıdır; bir değer hücresi geçirilirse istisna fırlatılır.
- `PivotConditionFormatScopeType::Selection` - hücrenin seçtiği kesişimdeki sadece değer hücreleri, genellikle tek bir değer hücresi.
Aşağıdaki örnek, sol üst köşesi E3'te bulunan bir meyve-satışı pivot tablosu oluşturur, `Data` kapsamı ile hücre F4'te (satır 3, sütun 5) bir koşullu biçimlendirme sabitleyerek 200'ün üzerindeki her tutarı kırmızıda beyaz kalın olarak vurgular. Değerler Apple 220, Banana 330, Cherry 200 ve genel toplam 750 olduğunda, kural F4, F5 ve F7'yı boyar - çözülmüş bölge tüm veri sütunu F4:F7'dir ve yalnızca kuralı geçen hücreler aydınlatılır.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    const char16_t* fruits[] = {u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry"};
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    int index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    format.ApplyTo(3, 5, PivotConditionFormatScopeType::Data);
    int conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue, OperatorType::GreaterThan, u"200", nullptr);
    Style style = workbook.CreateStyle();
    Font font = style.GetFont();
    font.SetIsBold(true);
    font.SetColor(Color::White());
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatData.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

Aynı kuralı `Field` kapsamı ile satır‑alan etiketi E4'te (satır 3, sütun 4) sabitlemek, F4:F6'ya çözülür - aynı veri sütunu ancak genel toplam satırı olmadan - çünkü kapsam artık tüm değer alanı yerine `Fruit` alanını tanımlar. `Selection` kapsamı F4'te sabitlendiğinde sadece F4'e çözülür.

## **Bölgeyi Manuel Olarak Tanımlama**
İkinci yöntem, kapsam seçiciyi atlayarak bölgeyi `PivotConditionalFormat` üzerinde açıkça adlandırır.

### **AddCellArea ile bir çalışma sayfası dikdörtgeni**
`AddCellArea(CellArea)`, verilen dikdörtgeni kuralın hedefi olarak kaydeder. Koordinatlar sıfır tabanlı çalışma sayfası koordinatlarıdır ve bölge tam olarak sağlanan dikdörtgendir - veri sütununa genişleme yok ve genel toplam mantığı yoktur. İlgili hücreler mevcut pivot düzeninin bilinen sabit bir dikdörtgeni olduğunda kullanın.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    U16String fruits[] = {
        U16String(u"Apple"),
        U16String(u"Banana"),
        U16String(u"Apple"),
        U16String(u"Banana"),
        U16String(u"Cherry"),
        U16String(u"Cherry")
    };
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"Amount"));
    pivotTable.CalculateData();
    int32_t index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    CellArea area;
    area.StartRow = 3;
    area.EndRow = 5;
    area.StartColumn = 5;
    area.EndColumn = 5;
    format.AddCellArea(area);
    int32_t conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue,
        OperatorType::Between,
        u"150",
        u"300");
    Style style = workbook.CreateStyle();
    style.GetFont().SetIsItalic(true);
    style.SetForegroundColor(Color::LightYellow());
    style.SetPattern(BackgroundType::Solid);
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatCellArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### **PivotAreas ile anlamsal bir pivot bölgesi**
`GetPivotAreas()`, kardeş sayfanın statik stiller için kullandığı aynı anlamsal-bölge modelini sağlar. Bir `PivotArea` oluşturun, `Select` veya `SelectField` ile bir alan ya da bölge seçin ve `GetPivotAreas().AddPivotArea(PivotArea)` ile ekleyin. Anlamsal bir bölge alanına bağlı kalır, bu yüzden pivot tablo yenilendiğinde ve düzen değiştiğinde koşullu biçimlendirme alanı takip eder. `GetPivotAreas().Add(PivotArea)` aşırı yüklemesi hâlâ derlenir ancak artık eski olarak işaretlenmiştir - `AddPivotArea` tercih edin.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    const char16_t* fruits[] = {u"Apple", u"Banana", u"Apple", u"Banana", u"Cherry", u"Cherry"};
    int years[] = {2024, 2024, 2025, 2025, 2024, 2025};
    int amounts[] = {100, 150, 120, 180, 90, 110};
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    for (int i = 0; i < 6; ++i) {
        cells.Get(i + 1, 0).PutValue(fruits[i]);
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=A1:C7", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.CalculateData();
    int index = pivotTable.GetConditionalFormats().Add();
    PivotConditionalFormat format = pivotTable.GetConditionalFormats().Get(index);
    PivotArea area(pivotTable);
    area.SelectField(PivotFieldType::Data, u"Amount");
    format.GetPivotAreas().AddPivotArea(area);
    int conditionIndex = format.GetFormatConditions().AddCondition(
        FormatConditionType::CellValue, OperatorType::LessThan, u"150", nullptr);
    Style style = workbook.CreateStyle();
    style.GetFont().SetColor(Color::Gray());
    format.GetFormatConditions().Get(conditionIndex).SetStyle(style);
    workbook.Save(u"PivotConditionalFormatPivotArea.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Kuralların Nerede Saklandığı ve Yeniden Yüklemede Nasıl Korunduğu**
Her `pivotTable.GetConditionalFormats().Add()` çağrısı, pivot tabloya bir `PivotConditionalFormat` ekler. Koşullar, formülleri ve stilleri çalışma kitabıyla birlikte kaydedilir - aşağıdaki örnekte dosya yeniden açıldığında aynı kural türü, operatörü ve formülüyle birlikte korunmuş olarak gösterilir ve `GetCellAreas()` aynı bölgeleri rapor eder. Hiç koşul almayan girdiler, çalışma kitabı kaydedildiğinde silinir; bu, Excel'in kuralı olmayan bir koşullu biçimlendirmeyi atmasıyla aynı şekildedir.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
static const char* ToString(FormatConditionType type)
{
    switch (type)
    {
    case FormatConditionType::CellValue:
        return "CellValue";
    default:
        return "Unknown";
    }
}
static const char* ToString(OperatorType op)
{
    switch (op)
    {
    case OperatorType::GreaterThan:
        return "GreaterThan";
    default:
        return "Unknown";
    }
}
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook(u"PivotConditionalFormatData.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(0).GetPivotTables().Get(0);
    auto conditionalFormats = pivotTable.GetConditionalFormats();
    int formatCount = conditionalFormats.GetCount();
    std::cout << "Conditional formats: " << formatCount << std::endl;
    for (int i = 0; i < formatCount; ++i)
    {
        PivotConditionalFormat format = conditionalFormats.Get(i);
        auto formatConditions = format.GetFormatConditions();
        int conditionCount = formatConditions.GetCount();
        for (int j = 0; j < conditionCount; ++j)
        {
            FormatCondition condition = formatConditions.Get(j);
            std::cout << "Format " << i << ": "
                      << ToString(condition.GetType()) << " "
                      << ToString(condition.GetOperator())
                      << " formula1=" << condition.GetFormula1().ToUtf8()
                      << std::endl;
        }
        Vector<CellArea> areas = format.GetCellAreas();
        for (int k = 0; k < areas.GetLength(); ++k)
        {
            CellArea area = areas[k];
            std::cout << "    rows " << area.StartRow + 1 << "-" << area.EndRow + 1
                      << ", columns " << area.StartColumn + 1 << "-" << area.EndColumn + 1
                      << std::endl;
        }
    }
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Related Articles**
- [Pivot Tablosuna Stil Uygulama](/cells/tr/cpp/apply-style-to-pivot-table/)
- [Pivot Tablosunun Bir Bölümünü Biçimlendirme](/cells/tr/cpp/format-part-of-pivot-table/)
- [Pivot Tablosunda En İyi 10 Göster veya Filtrele](/cells/tr/cpp/top-10-show-or-filter-in-pivot-table/)
- [Pivot Tablolarını Etiket veya Değerle Filtreleme](/cells/tr/cpp/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="cpp" >}}