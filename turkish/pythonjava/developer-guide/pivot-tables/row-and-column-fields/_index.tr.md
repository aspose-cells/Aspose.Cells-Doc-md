---
title: Aspose.Cells for Python via Java'te PivotTable'a satır ve sütun alanları ekleme
description: Aspose.Cells for Python via Java kullanarak bir pivot tablosunun satır ve sütun bölgelerine temel alanların nasıl ekleneceğini ve PivotField.setSubtotals kullanılarak pivot alanı ara toplamlarının nasıl kontrol edileceğini öğrenin.
linktitle: Satır ve Sütun Alanları
keywords: Aspose.Cells, Python via Java, pivot tablo, satır alanı, sütun alanı, PivotField, setSubtotals, PivotFieldSubtotalType, ara toplamlar
type: docs
weight: 220
url: /tr/python-java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Satır veya Sütun Bölgesine Alan Ekleme**
`PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` yöntemi, kaynak verilerden bir temel alanı dört pivot bölgesinden birine taşır. `fieldType` argümanı aşağıdaki `PivotFieldType` değerlerinden birini kabul eder.
- `ROW` — solda dikey olarak yerleştirilen alanlar
- `COLUMN` — üstte yatay olarak yerleştirilen alanlar
- `DATA` — değerleri toplanan alanlar
- `PAGE` — rapor filtreleri olarak kullanılan alanlar
Alanlar eklendikten sonra, `PivotTable.getRowFields()` ve `PivotTable.getColumnFields()` yöntemleri aracılığıyla bunlara erişebilirsiniz. Her yöntem bir `PivotFieldCollection` döndürür. `RowFields`'in 0 dizinindeki alan en dıştaki satır alanıdır ve sonraki dizinler onun içine yerleştirilmiş alanları temsil eder. Aynı dizin oluşturma kuralı `ColumnFields` için de geçerlidir.
Alan iç içe yerleştirme sırası önemlidir. Önce `Category` alanını satır bölgesine, ardından `Item` alanını eklemek, dış gruplandırması `Category` ve iç gruplandırması `Item` olan bir pivot üretir. Sırayı tersine çevirmek hiyerarşiyi de tersine çevirir.

## **Pivot Alanı Ara Toplamları**
`PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` yöntemi, bir pivot alanı için hangi ara toplam satırlarının görüneceğini kontrol eder. Her çağrı, tek bir ara toplam türünü bağımsız olarak değiştirir. `shown = true` geçmek ara toplamı görüntülerken, `shown = false` onu gizler. Her çağrı yalnızca bir türü etkilediğinden, yöntemi farklı `subtotalType` değerleriyle birden çok kez çağırmak özel bir ara toplam alt kümesi oluşturur.
`PivotFieldSubtotalType` numaralandırması, kullanılabilir ara toplam türlerini tanımlar.
- `AUTOMATIC` — Aspose.Cells varsayılan seçimi seçer (genellikle sayısal alanlar için `SUM`)
- `NONE` — tüm ara toplam satırlarını gizler
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STD_DEV`
- `STD_DEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
Ara toplamlar yalnızca satır bölgesinde (veya sütun bölgesinde) iki veya daha fazla pivot alanı olduğunda görüntülenir. Tek bir alanın ara toplam yapacak anlamlı bir şeyi yoktur, dolayısıyla `setSubtotals` çağrıları bu durumda görünür bir etki yaratmaz. Bu nedenle bu makale, her `Category` grubu arasındaki ara toplam sınırının görünür olması için her örnekte satır bölgesine iki satır alanı (dış `Category`, iç `Item`) yerleştirir.
{{% /alert %}}

## **Senaryo 1 — Otomatik (Varsayılan) Ara Toplamlar**
`setSubtotals` çağrısını hiç yapmadığınızda, Aspose.Cells sayısal alanlar için `AUTOMATIC` seçimini uygular. Aşağıdaki örnek, dış `Category` satır alanı üzerinde `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` çağırarak bu davranışı açıkça doğrular.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, PivotTable, PivotField, PivotFieldType, PivotFieldSubtotalType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
worksheet.getCells().get(0, 0).putValue("Category")
worksheet.getCells().get(0, 1).putValue("Item")
worksheet.getCells().get(0, 2).putValue("Year")
worksheet.getCells().get(0, 3).putValue("Amount")
worksheet.getCells().get(1, 0).putValue("Fruit")
worksheet.getCells().get(1, 1).putValue("Apple")
worksheet.getCells().get(1, 2).putValue(2020)
worksheet.getCells().get(1, 3).putValue(100)
worksheet.getCells().get(2, 0).putValue("Fruit")
worksheet.getCells().get(2, 1).putValue("Apple")
worksheet.getCells().get(2, 2).putValue(2021)
worksheet.getCells().get(2, 3).putValue(150)
worksheet.getCells().get(3, 0).putValue("Fruit")
worksheet.getCells().get(3, 1).putValue("Banana")
worksheet.getCells().get(3, 2).putValue(2020)
worksheet.getCells().get(3, 3).putValue(80)
worksheet.getCells().get(4, 0).putValue("Fruit")
worksheet.getCells().get(4, 1).putValue("Banana")
worksheet.getCells().get(4, 2).putValue(2021)
worksheet.getCells().get(4, 3).putValue(90)
worksheet.getCells().get(5, 0).putValue("Vegetable")
worksheet.getCells().get(5, 1).putValue("Carrot")
worksheet.getCells().get(5, 2).putValue(2020)
worksheet.getCells().get(5, 3).putValue(50)
worksheet.getCells().get(6, 0).putValue("Vegetable")
worksheet.getCells().get(6, 1).putValue("Carrot")
worksheet.getCells().get(6, 2).putValue(2021)
worksheet.getCells().get(6, 3).putValue(60)
worksheet.getCells().get(7, 0).putValue("Vegetable")
worksheet.getCells().get(7, 1).putValue("Daikon")
worksheet.getCells().get(7, 2).putValue(2020)
worksheet.getCells().get(7, 3).putValue(40)
worksheet.getCells().get(8, 0).putValue("Vegetable")
worksheet.getCells().get(8, 1).putValue("Daikon")
worksheet.getCells().get(8, 2).putValue(2021)
worksheet.getCells().get(8, 3).putValue(45)
pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.AUTOMATIC, True)
pivotTable.calculateData()
workbook.save("output_automatic.xlsx")
jpype.shutdownJVM()
```

## **Senaryo 2 — Tüm Ara Toplamların Gizlenmesi (None)**
`setSubtotals(PivotFieldSubtotalType.NONE, true)` çağrısı, pivot'tan tüm ara toplam satırlarını kaldırarak yalnızca alan satırlarını ve alttaki genel toplamı bırakır. Bu, ham gruplandırılmış verileri herhangi bir özet satırı olmadan istediğinizde kullanışlıdır.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PivotFieldSubtotalType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.getCells().get(0, j).putValue(headers[j])
data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020, 80 ],
    ["Fruit",     "Banana", 2021, 90 ],
    ["Vegetable", "Carrot", 2020, 50 ],
    ["Vegetable", "Carrot", 2021, 60 ],
    ["Vegetable", "Daikon", 2020, 40 ],
    ["Vegetable", "Daikon", 2021, 45 ]
]
for i in range(len(data)):
    for j in range(len(data[0])):
        worksheet.getCells().get(i + 1, j).putValue(data[i][j])
pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.NONE, True)
pivotTable.calculateData()
workbook.save("output_none.xlsx")
jpype.shutdownJVM()
```

## **Senaryo 3 — Özel Ara Toplam Alt Kümesi (Sum + Average)**
Tek bir ara toplam türüyle sınırlı değilsiniz. Her `setSubtotals` çağrısı bir tür üzerinde bağımsız olarak çalışır, dolayısıyla yöntemi iki kez çağırmak — bir kez `SUM` ve bir kez `AVERAGE` ile — her `Category` grubu için iki ara toplam satırından oluşan özel bir alt küme üretir.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTableCollection, PivotTable, PivotFieldType, PivotField, PivotFieldSubtotalType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
worksheet.getCells().get("A1").putValue("Category")
worksheet.getCells().get("B1").putValue("Item")
worksheet.getCells().get("C1").putValue("Year")
worksheet.getCells().get("D1").putValue("Amount")
worksheet.getCells().get(1, 0).putValue("Fruit")
worksheet.getCells().get(1, 1).putValue("Apple")
worksheet.getCells().get(1, 2).putValue(2020)
worksheet.getCells().get(1, 3).putValue(100)
worksheet.getCells().get(2, 0).putValue("Fruit")
worksheet.getCells().get(2, 1).putValue("Apple")
worksheet.getCells().get(2, 2).putValue(2021)
worksheet.getCells().get(2, 3).putValue(150)
worksheet.getCells().get(3, 0).putValue("Fruit")
worksheet.getCells().get(3, 1).putValue("Banana")
worksheet.getCells().get(3, 2).putValue(2020)
worksheet.getCells().get(3, 3).putValue(80)
worksheet.getCells().get(4, 0).putValue("Fruit")
worksheet.getCells().get(4, 1).putValue("Banana")
worksheet.getCells().get(4, 2).putValue(2021)
worksheet.getCells().get(4, 3).putValue(90)
worksheet.getCells().get(5, 0).putValue("Vegetable")
worksheet.getCells().get(5, 1).putValue("Carrot")
worksheet.getCells().get(5, 2).putValue(2020)
worksheet.getCells().get(5, 3).putValue(50)
worksheet.getCells().get(6, 0).putValue("Vegetable")
worksheet.getCells().get(6, 1).putValue("Carrot")
worksheet.getCells().get(6, 2).putValue(2021)
worksheet.getCells().get(6, 3).putValue(60)
worksheet.getCells().get(7, 0).putValue("Vegetable")
worksheet.getCells().get(7, 1).putValue("Daikon")
worksheet.getCells().get(7, 2).putValue(2020)
worksheet.getCells().get(7, 3).putValue(40)
worksheet.getCells().get(8, 0).putValue("Vegetable")
worksheet.getCells().get(8, 1).putValue("Daikon")
worksheet.getCells().get(8, 2).putValue(2021)
worksheet.getCells().get(8, 3).putValue(45)
pivotTables = worksheet.getPivotTables()
pivotTable = pivotTables.add("A1:D9", 2, 5)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category")
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
categoryField = pivotTable.getRowFields().get(0)
categoryField.setSubtotals(PivotFieldSubtotalType.SUM, True)
categoryField.setSubtotals(PivotFieldSubtotalType.AVERAGE, True)
pivotTable.calculateData()
workbook.save("output_custom.xlsx")
jpype.shutdownJVM()
```

## **Özet**
Bu üç senaryo yalnızca `setSubtotals` çağrıları açısından farklılık gösterir. Geri kalan her şey — veri kümesi, alanlar ve bu alanların atandığı bölgeler — aynıdır, bu durum düzenlerin doğrudan karşılaştırılabilir olmasının nedenidir.
- **Alanların yerleştirilmesi.** `PivotTable.addFieldToArea(PivotFieldType.ROW, fieldName)` çağrısı, bir kaynak sütunu bir bölgeye yerleştirir. Bir bölge içinde, çağrıların sırası gösterim sırasını belirler; bu nedenle ilk çağrı en dıştaki grubu oluşturur. Alt toplamlar, aynı bölgede iki veya daha fazla alana ihtiyaç duyar: tek bir alanla gruplar arasında alt toplam yapılacak hiçbir şey bulunmaz.
- **Senaryo 1 — otomatik alt toplamlar.** `setSubtotals` çağrısının yapılmaması, seçimi Excel’e bırakır ve Excel, sayısal alanlara kendi varsayılan alt toplamını uygular. `PivotFieldSubtotalType.AUTOMATIC` ile `setSubtotals` çağrısı, bu seçimi açıkça kaydeder ve dolaylı bırakmaz.
- **Senaryo 2 — alt toplam yok.** `PivotFieldSubtotalType.NONE` ile `setSubtotals` çağrısı, varsayılan alt toplamı kapatır; bu durumda pivot tablo, alanı satır olarak ve genel toplamı tutar ancak Excel’in aksi takdirde araya ekleyeceği alt toplam satırlarını kaldırır.
- **Senaryo 3 — seçilmiş bir alt küme.** Her çağrı tam olarak bir alt toplam türünü açar veya kapatır ve çağrılar birbirlerini sıfırlamak yerine birikir. Bu nedenle, bir kez `PivotFieldSubtotalType.SUM` ve bir kez `PivotFieldSubtotalType.AVERAGE` ile çağırılması, her ikisini de etkinleştirir ve pivot tablo bir Toplam alt toplamı, bir Ortalama alt toplamı ve bir genel toplamı görüntüler.

{{% alert color="primary" %}}
Alt toplamlarla ilgili hiçbir şey, satır bölgesine özeldir. `PivotTable.ColumnFields`’tan alınan bir alana yapılan aynı `setSubtotals` çağrıları, sütun ekseninde aynı üç düzeni oluşturur, çünkü ayar, eksende bulunduğu alana değil, kendi pivot alanına aittir.
{{% /alert %}}

## **İlgili Makaleler**
- [Pivot Tablolarda Sayfa Alanları](/cells/tr/python-java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Python via Java ile Pivot Tabloları Yenileme](/cells/tr/python-java/refresh-pivot-table/)
- [Pivot Tablolara Stil Uygulama](/cells/tr/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}