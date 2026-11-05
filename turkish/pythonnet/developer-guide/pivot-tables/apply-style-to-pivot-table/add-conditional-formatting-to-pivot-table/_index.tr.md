---
title: Pivot Tablosuna Koşullu Biçimlendirme Ekle
linktitle: Pivot Tablosuna Koşullu Biçimlendirme Ekle
description: Aspose.Cells for Python via .NET içinde bir özet tabloya koşullu biçimlendirme ekleyin - bir kuralı apply_to ve PivotConditionFormatScopeType kapsamı ile veri bölgesine bağlayın, ya da hedefi add_cell_area ve pivot_areas ile tanımlayın, ardından format_conditions.add_condition aracılığıyla kuralları ve stilleri ekleyin.
keywords: Aspose.Cells, Aspose.Cells for Python via .NET, özet tablo, koşullu biçimlendirme, PivotConditionalFormat, conditional_formats, apply_to, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, add_cell_area, pivot_areas, add_pivot_area, format_conditions, add_condition, FormatConditionType, Python
type: docs
weight: 30
url: /tr/python-net/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Üst sayfada ve kardeş sayfada açıklanan stiller statiktir - bir `PivotArea` veya `CellArea` bölgesi bir kez boyanır ve değerler ne olursa olsun stilini korur. Koşullu biçimlendirme ise kural‑tabanlı bir karşılıktır - 200'ün üzerindeki her tutarı vurgular, orta yüzde elliyi gölgelendirir veya en düşük sıralı öğeleri işaretler - ve vurgulama, özet tablo yeniden hesaplandığında veya yenilendiğinde değerleri takip eder.
Aspose.Cells'te, özet tablo koşullu biçimlendirmesi `pivot_table.conditional_formats` koleksiyonunda bulunur. Her giriş, iki soruya bağımsız olarak yanıt veren bir `PivotConditionalFormat` nesnesidir:
- **Kural nerede uygulanır?** Hedef bölge ya `apply_to(row: int, column: int, scope: PivotConditionFormatScopeType)` yöntemiyle tanımlanır; bu yöntem Excel kullanıcı arayüzünün kapsam seçicisini yansıtır, ya da `add_cell_area(cell_area: CellArea)` ve `pivot_areas` koleksiyonu aracılığıyla tanımlanır ve bölgeyi açıkça adlandırır.
- **Kural neyi test eder?** Bir veya daha fazla koşul, `format_conditions.add_condition(type: FormatConditionType, operator_type: OperatorType, formula1: str, formula2: str)` yöntemiyle `format_conditions` koleksiyonuna eklenir ve her koşul kendi `style`'ını taşır.

{{% alert color="primary" %}}
Bir pivot koşullu biçimlendirme nesnesinin `format_conditions` nesnesinde `format_conditions.add(cell_area: CellArea, type: FormatConditionType, operator_type: OperatorType, formula1: str, formula2: str)` veya `format_conditions.add_area(cell_area: CellArea)` metodlarını çağırmayın. Bu iki aşırı yükleme, normal çalışma sayfası koşullu biçimlendirme API'sinden devralınmıştır ve özet tablolar için çalışmaz – hücre bölgesi pivot bölgesine hiç dönüştürülmez, bu yüzden istek sessizce yok sayılır. Bölgeyi her zaman `pivot_conditional_format` nesnesi üzerinde (`apply_to`, `add_cell_area` veya `pivot_areas`) tanımlayın ve kuralı `add_condition` aşırı yüklemelerinden biriyle ekleyin.
{{% /alert %}}

## **Kapsam ile Kural Uygulama (Excel UI Yöntemi)**
İlk yöntem, kuralı Excel kullanıcı arayüzünün yaptığı gibi konumlandırır. Özet tablonun bir hücresi, sıfır‑tabanlı çalışma sayfası koordinatlarıyla adlandırılır ve `PivotConditionFormatScopeType` kapsamı, Aspose.Cells'e kuralın o hücreden ne kadar uzanması gerektiğini bildirir:
- `PivotConditionFormatScopeType.DATA` - özet tablonun ürettiği tüm değer hücreleri, toplam satırları dahil.
- `PivotConditionFormatScopeType.FIELD` - hücrenin belirttiği alana ait değer hücreleri, toplam satırları hariç. Hücre, bir satır‑alan etiketi gibi bir alan hücresi olmalıdır; bir değer hücresi geçirilirse istisna fırlatılır.
- `PivotConditionFormatScopeType.SELECTION` - hücrenin seçtiği kesişimdeki yalnızca değer hücreleri, tipik olarak tek bir değer hücresi.
Aşağıdaki örnek, sol‑üst köşesi E3'te olan bir meyve‑satışları özet tablosu oluşturur, `PivotConditionFormatScopeType.DATA` kapsamı ile hücre F4'te (satır 3, sütun 5) bir koşullu biçimlendirme bağlar ve 200'ün üzerindeki her tutarı kırmızı zemin üzerinde kalın beyaz ile vurgular. Apple 220, Banana 330, Cherry 200 ve toplam 750 değerleriyle, kural F4, F5 ve F7 hücrelerini boyar – çözülmüş bölge bütün veri sütunu F4:F7'dir ve yalnızca kuralı geçen hücreler aydınlanır.

```python
from aspose.cells.pivot import PivotFieldType, PivotConditionFormatScopeType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
# E3 konumunda sol üst köşesi bulunan pivot tablo
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Koşullu biçimi F4'te (satır 3, sütun 5) Veri kapsamı ile sabitle
index = pivot_table.conditional_formats.add()
format = pivot_table.conditional_formats[index]
format.apply_to(3, 5, PivotConditionFormatScopeType.DATA)
# Kural - 200'den büyük tutarları vurgula
condition_index = format.format_conditions.add_condition(
    ac.FormatConditionType.CELL_VALUE,
    ac.OperatorType.GREATER_THAN,
    "200",
    None
)
style = workbook.create_style()
style.font.is_bold = True
style.font.color = Color.white
style.foreground_color = Color.red
style.pattern = ac.BackgroundType.SOLID
format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatData.xlsx")
```

`PivotConditionFormatScopeType.FIELD` kapsamı ile aynı kuralı satır‑alan etiketi E4'te (satır 3, sütun 4) bağlamak, bölgeyi F4:F6 olarak çözer – toplam satırları içermeyen aynı veri sütunu – çünkü kapsam artık tüm değer alanı yerine `Fruit` alanını tanımlamaktadır. `PivotConditionFormatScopeType.SELECTION` kapsamı F4'te bağlandığında sadece F4'ü çözer.

## **Bölgeyi Manuel Olarak Tanımlama**
İkinci yöntem, kapsam seçiciyi atlar ve bölgeyi `PivotConditionalFormat` üzerinde açıkça adlandırır.

### **add_cell_area ile bir çalışma sayfası dikdörtgeni**
`add_cell_area(cell_area: CellArea)` verilen dikdörtgeni kuralın hedefi olarak kaydeder. Koordinatlar sıfır‑tabanlı çalışma sayfası koordinatlarıdır ve bölge tam olarak sağlanan dikdörtgendir – veri sütununa genişleme olmaz ve toplam satırları mantığı yoktur. Mevcut pivot düzeninde ilgi çekici hücreler bilinen sabit bir dikdörtgen olduğunda bunu kullanın.

```python
from aspose.cells import BackgroundType, FormatConditionType, OperatorType
from aspose.cells.pivot import PivotFieldType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# F4:F6 dikdörtgenini hedefleyin (toplam satırı içermeyen değer hücreleri)
index = pivot_table.conditional_formats.add()
conditional_format = pivot_table.conditional_formats[index]
area = ac.CellArea()
area.start_row = 3
area.start_column = 5
area.end_row = 5
area.end_column = 5
conditional_format.add_cell_area(area)
# Kural - 150 ile 300 arasındaki tutarlar için açık sarı renkte italik
condition_index = conditional_format.format_conditions.add_condition(
    FormatConditionType.CELL_VALUE, OperatorType.BETWEEN, "150", "300"
)
style = workbook.create_style()
style.font.is_italic = True
style.foreground_color = Color.light_yellow
style.pattern = BackgroundType.SOLID
conditional_format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatCellArea.xlsx")
```

### **pivot_areas ile anlamsal bir pivot bölgesi**
`pivot_areas`, kardeş sayfanın statik stiller için kullandığı aynı anlamsal‑bölge modelidir. Bir `PivotArea` oluşturun, bir alanı veya bölgeyi `select` veya `select_field` ile seçin ve `pivot_areas.add_pivot_area(pivot_area)` ile ekleyin. Anlamsal bir bölge alanına bağlı kalır, bu yüzden koşullu biçimlendirme, özet tablo yenilendiğinde ve düzen değiştiğinde alanı takip eder. `pivot_areas.add(pivot_area)` aşırı yüklemesi hâlâ derlenebilir ancak kullanımdan kaldırılmıştır – `add_pivot_area` tercih edin.

```python
from aspose.cells.pivot import PivotFieldType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Amount veri alanına anlamsal bir bölge olarak kuralı ekle
index = pivot_table.conditional_formats.add()
format = pivot_table.conditional_formats[index]
area = ac.PivotArea(pivot_table)
area.select_field(PivotFieldType.DATA, "Amount")
format.pivot_areas.add_pivot_area(area)
# Kural - 150'nin altındaki miktarlar için gri metin
condition_index = format.format_conditions.add_condition(
    ac.FormatConditionType.CELL_VALUE,
    ac.OperatorType.LESS_THAN,
    "150",
    None
)
style = workbook.create_style()
style.font.color = Color.gray
format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatPivotArea.xlsx")
```

## **Kuralların Nerede Saklandığı ve Yeniden Yüklemede Nasıl Korunduğu**
Her `pivot_table.conditional_formats.add()` çağrısı özet tabloya bir `PivotConditionalFormat` ekler. Koşullar, formülleri ve stilleri çalışma kitabıyla kaydedilir – aşağıdaki örnekte dosya yeniden açıldığında aynı kural türü, operatörü ve formülüyle birlikte mevcut olur ve `get_cell_areas()` aynı bölgeleri raporlar. Hiçbir koşul almamış girişler, çalışma kitabı kaydedildiğinde silinir; bu, Excel'in kuralı olmayan bir koşullu biçimlendirmeyi atmasıyla aynı şekilde gerçekleşir.

```python
import aspose.cells as ac
workbook = ac.Workbook("PivotConditionalFormatData.xlsx")
pivot_table = workbook.worksheets[0].pivot_tables[0]
print("Conditional formats: " + str(pivot_table.conditional_formats.count))
for i in range(pivot_table.conditional_formats.count):
    format = pivot_table.conditional_formats[i]
    for j in range(format.format_conditions.count):
        condition = format.format_conditions[j]
        print(f"Format {i}: {condition.type} {condition.operator} formula1={condition.formula1}")
    for area in format.get_cell_areas():
        print(
            f"    rows {area.start_row + 1}-{area.end_row + 1}, "
            f"columns {area.start_column + 1}-{area.end_column + 1}"
        )
# Bu çıktıyı verir:
# Koşullu biçimler: 1
# Biçim 0: CellValue GreaterThan formula1==200
#     satırlar 4-7, sütunlar 6-6        (F4:F7, çözülen veri bölgesi)
```

## **İlgili Makaleler**
- [Pivot Tablosuna Stil Uygulama](/cells/tr/python-net/apply-style-to-pivot-table/)
- [Pivot Tablosunun Bir Bölümünü Biçimlendirme](/cells/tr/python-net/format-part-of-pivot-table/)
- [Pivot Tablosunda İlk 10 Gösterme veya Filtreleme](/cells/tr/python-net/top-10-show-or-filter-in-pivot-table/)
- [Pivot Tablolarını Etiket veya Değere Göre Filtreleme](/cells/tr/python-net/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="python-net" >}}