---
title: Pivot Tablosuna Koşullu Biçimlendirme Ekle
linktitle: Pivot Tablosuna Koşullu Biçimlendirme Ekle
description: Aspose.Cells for Python via Java'da bir pivot tablosuna koşullu biçimlendirme ekleyin - bir kuralı applyTo ve PivotConditionFormatScopeType kapsamı ile veri bölgesine bağlayın veya hedefi addCellArea ve getPivotAreas ile tanımlayın, ardından kuralları ve stilleri getFormatConditions().addCondition aracılığıyla ekleyin.
keywords: Aspose.Cells for Python via Java, Pivot Tablosu, koşullu biçimlendirme, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Python via Java
type: docs
weight: 30
url: /tr/python-java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Üst sayfada ve yan sayfada açıklanan stiller statiktir - bir `PivotArea` veya `CellArea` bölgesi bir kez boyanır ve değerler ne olursa olsun stilini korur. Koşullu biçimlendirme, kural tabanlı karşılığıdır - 200'ün üzerindeki her tutarı vurgulamak, ortadaki yüzde elliyi gölgelendirmek veya en düşük sıradaki öğeleri işaretlemek - ve vurgulama, pivot tablosu her yeniden hesaplandığında veya yenilendiğinde değerleri takip eder.
Aspose.Cells'ta, pivot‑tablo koşullu biçimlendirmesi `PivotTable.getConditionalFormats()` koleksiyonunda bulunur. Her giriş, iki soruya bağımsız olarak yanıt veren bir `PivotConditionalFormat` içerir:
- **Kural nerede uygulanır?** Hedef bölge, Excel kullanıcı arabiriminin kapsam seçicisini yansıtan `PivotConditionalFormat.applyTo(int row, int column, PivotConditionFormatScopeType scope)` yöntemiyle ya da `PivotConditionalFormat.addCellArea(CellArea)` ve `PivotConditionalFormat.getPivotAreas()` koleksiyonu ile açıkça bölgeyi adlandırarak tanımlanır.
- **Kural neyi test eder?** Bir veya daha fazla koşul, `PivotConditionalFormat.getFormatConditions()` içine `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` yöntemiyle eklenir ve her koşul kendi `Style`'ını taşır.

{{% alert color="primary" %}}
Bir pivot koşullu biçimlendirme için `PivotConditionalFormat.getFormatConditions()` nesnesinde `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` veya `FormatConditionCollection.addArea(CellArea)` çağrısı yapmayın. Bu iki aşırı yükleme, normal çalışma sayfası koşullu biçimlendirme API'sinden devralınmıştır ve pivot tablolar için çalışmaz – hücre alanı hiçbir zaman bir pivot alana dönüştürülmez, bu yüzden istek sessizce yok sayılır. Bölgeyi her zaman `PivotConditionalFormat` üzerindeki (`applyTo`, `addCellArea` veya `getPivotAreas()`) tanımlayın ve kuralı `addCondition` aşırı yüklemelerinden biriyle ekleyin.
{{% /alert %}}

## **Kapsam ile Kural Uygulama (Excel UI Yöntemi)**
İlk yöntem, kuralı Excel kullanıcı arabiriminde olduğu gibi konumlandırır. Pivot tablosundaki bir hücre, sıfır tabanlı çalışma sayfası koordinatlarıyla adlandırılır ve bir `PivotConditionFormatScopeType` kapsamı, Aspose.Cells'e kuralın o hücreden ne kadar uzağa uzanması gerektiğini söyler:
- `PivotConditionFormatScopeType.DATA` - pivot tablosunun ürettiği tüm değer hücreleri, büyük toplamlar dahil.
- `PivotConditionFormatScopeType.FIELD` - hücrenin tanımladığı alana ait değer hücreleri, büyük toplamlar hariç. Hücre, satır‑alan etiketi gibi bir alan hücresi olmalıdır; bir değer hücresi geçirilirse istisna fırlatılır.
- `PivotConditionFormatScopeType.SELECTION` - hücrenin seçtiği kesişimdeki sadece değer hücreleri, genellikle tek bir değer hücresi.
Aşağıdaki örnek, sol üst köşesi E3'te olan bir meyve‑satışı pivot tablosu oluşturur, `DATA` kapsamı ile hücre F4'te (satır 3, sütun 5) bir koşullu biçimlendirme bağlar ve 200'ün üzerindeki her tutarı kırmızı üzerine kalın beyaz olarak vurgular. Apple 220, Banana 330, Cherry 200 ve toplam 750 değerleriyle, kural F4, F5 ve F7'yı boyar – çözülen bölge bütün veri sütunu F4:F7'dir ve sadece kuralı geçen hücreler aydınlanır.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    Color,
    BackgroundType,
    PivotFieldType,
    PivotConditionFormatScopeType,
    FormatConditionType,
    OperatorType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
# Üst sol köşesi E3 olan Pivot tablo
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Koşullu formatı F4'e (satır 3, sütun 5) Veri kapsamı ile bağla
index = pivot_table.getConditionalFormats().add()
format = pivot_table.getConditionalFormats().get(index)
format.applyTo(3, 5, PivotConditionFormatScopeType.DATA)
# Kural - 200'den büyük tutarları vurgula
condition_index = format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.GREATER_THAN,
    "200",
    None,
)
style = workbook.createStyle()
style.getFont().setBold(True)
style.getFont().setColor(Color.getWhite())
style.setForegroundColor(Color.getRed())
style.setPattern(BackgroundType.SOLID)
format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatData.xlsx")
jpype.shutdownJVM()
```

`FIELD` kapsamı ile aynı kuralı satır‑alan etiketi E4'te (satır 3, sütun 4) bağlamak, bölgeyi F4:F6'ya çözer – toplam satırı olmadan aynı veri sütunu – çünkü kapsam artık tüm değer alanı yerine `Fruit` alanını tanımlar. `SELECTION` kapsamı F4'te bağlandığında ise sadece F4 çözümlenir.

## **Bölgeyi Manuel Olarak Tanımlama**
İkinci yöntem, kapsam seçiciyi atlar ve bölgeyi `PivotConditionalFormat` üzerinde açıkça adlandırır.

### **addCellArea() ile bir çalışma sayfası dikdörtgeni**
`addCellArea(CellArea)` verilen dikdörtgeni kuralın hedefi olarak kaydeder. Koordinatlar sıfır tabanlı çalışma sayfası koordinatlarıdır ve bölge tam olarak sağlanan dikdörtgendir – veri sütununa genişleme ya da toplam satırı mantığı yoktur. İlginç hücreler mevcut pivot düzeninin bilinen sabit bir dikdörtgeni olduğunda kullanın.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    CellArea,
    Color,
    BackgroundType,
    PivotFieldType,
    FormatConditionType,
    OperatorType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# F4:F6 dikdörtgenini hedefle (genel toplam olmadan değer hücreleri)
index = pivot_table.getConditionalFormats().add()
conditional_format = pivot_table.getConditionalFormats().get(index)
area = CellArea()
area.StartRow = 3
area.StartColumn = 5
area.EndRow = 5
area.EndColumn = 5
conditional_format.addCellArea(area)
# Kural - 150 ile 300 arasındaki tutarlar için açık sarı renkte italik
condition_index = conditional_format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.BETWEEN,
    "150",
    "300",
)
style = workbook.createStyle()
style.getFont().setItalic(True)
style.setForegroundColor(Color.getLightYellow())
style.setPattern(BackgroundType.SOLID)
conditional_format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatCellArea.xlsx")
jpype.shutdownJVM()
```

### **getPivotAreas() ile anlamsal bir pivot bölgesi**
`getPivotAreas()` koleksiyonu, yan sayfanın statik stiller için kullandığı aynı anlamsal‑bölge modelidir. Bir `PivotArea` oluşturun, `PivotArea.select(...)` veya `PivotArea.selectField(...)` ile bir alan veya bölge seçin ve `getPivotAreas().addPivotArea(PivotArea)` ile ekleyin. Anlamsal bir bölge alanına bağlı kalır, böylece koşullu biçimlendirme pivot tablo yenilendiğinde ve düzen kaydırıldığında alanı takip eder. `getPivotAreas().add(PivotArea)` aşırı yüklemesi hâlâ derlenebilir ancak eski olarak işaretlenmiştir – `addPivotArea` tercih edin.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    Color,
    PivotArea,
    PivotFieldType,
    FormatConditionType,
    OperatorType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Kuralı, Amount veri alanına anlamsal bir bölge olarak ekle
index = pivot_table.getConditionalFormats().add()
conditional_format = pivot_table.getConditionalFormats().get(index)
area = PivotArea(pivot_table)
area.selectField(PivotFieldType.DATA, "Amount")
conditional_format.getPivotAreas().addPivotArea(area)
# Kural - 150'nin altındaki tutarlar için gri metin
condition_index = conditional_format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.LESS_THAN,
    "150",
    None,
)
style = workbook.createStyle()
style.getFont().setColor(Color.getGray())
conditional_format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatPivotArea.xlsx")
jpype.shutdownJVM()
```

## **Kuralların Nerede Saklandığı ve Yeniden Yüklemede Nasıl Yaşadığı**
Her `PivotTable.getConditionalFormats().add()` çağrısı, pivot tabloya bir `PivotConditionalFormat` ekler. Koşullar, formülleri ve stilleri çalışma kitabıyla birlikte kaydedilir – aşağıdaki örnekte dosya yeniden açıldığında aynı kural, tipi, operatörü ve formülü bozulmadan gösterilir ve `PivotConditionalFormat.getCellAreas()` aynı bölgeleri rapor eder. Hiçbir koşul almamış girdiler, çalışma kitabı kaydedildiğinde düşürülür; tıpkı Excel'in kuralı olmayan bir koşullu biçimlendirmeyi atması gibi.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
workbook = Workbook("PivotConditionalFormatData.xlsx")
pivot_table = workbook.getWorksheets().get(0).getPivotTables().get(0)
print("Conditional formats: " + str(pivot_table.getConditionalFormats().getCount()))
for i in range(pivot_table.getConditionalFormats().getCount()):
    pivot_format = pivot_table.getConditionalFormats().get(i)
    format_conditions = pivot_format.getFormatConditions()
    for j in range(format_conditions.getCount()):
        condition = format_conditions.get(j)
        print(
            f"Format {i}: {condition.getType()} "
            f"{condition.getOperator()} formula1={condition.getFormula1()}"
        )
    for area in pivot_format.getCellAreas():
        print(
            f"    rows {area.StartRow + 1}-{area.EndRow + 1}, "
            f"columns {area.StartColumn + 1}-{area.EndColumn + 1}"
        )
# Bu çıktıyı verir:
# Koşullu biçimler: 1
# Biçim 0: CellValue GreaterThan formula1==200
#     satırlar 4-7, sütunlar 6-6        (F4:F7, çözülen veri bölgesi)
jpype.shutdownJVM()
```

## **Related Articles**
- [Pivot Tablosuna Stil Uygulama](/cells/tr/python-java/apply-style-to-pivot-table/)
- [Pivot Tablosunun Bir Bölümünü Biçimlendirme](/cells/tr/python-java/format-part-of-pivot-table/)
- [Pivot Tablosunda İlk 10 Göster veya Filtrele](/cells/tr/python-java/top-10-show-or-filter-in-pivot-table/)
- [Pivot Tablolarını Etiket veya Değer ile Filtreleme](/cells/tr/python-java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="python" >}}