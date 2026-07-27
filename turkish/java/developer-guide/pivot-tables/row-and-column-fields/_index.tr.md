---
title: Aspose.Cells for .NET'te PivotTable'a satır ve sütun alanları ekleme
linktitle: Satır ve Sütun Alanları
description: Aspose.Cells for Java'da PivotField.setSubtotals kullanarak bir pivot tablosunun satır ve sütun bölgelerine temel alanlar eklemeyi ve pivot alanı alt toplamlarını kontrol etmeyi öğrenin.
keywords: Aspose.Cells, Java, pivot tablosu, satır alanı, sütun alanı, PivotField, setSubtotals, PivotFieldSubtotalType, alt toplamlar
type: docs
weight: 220
url: /tr/java/pivot-table-add-row-column-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Satır veya Sütun Bölgesine Alan Ekleme**

`PivotTable.addFieldToArea(int fieldType, String fieldName)` yöntemi, kaynak verilerden bir temel alanı dört pivot bölgesinden birine taşır. `fieldType` argümanı aşağıdaki `PivotFieldType` değerlerinden birini kabul eder.

- `ROW` — sol tarafa dikey olarak yerleştirilen alanlar
- `COLUMN` — üst kısma yatay olarak yerleştirilen alanlar
- `DATA` — değerleri toplanan alanlar
- `PAGE` — rapor filtreleri olarak kullanılan alanlar

Alanlar eklendikten sonra, bunlara `PivotTable.getRowFields()` ve `PivotTable.getColumnFields()` özellikleri aracılığıyla erişebilirsiniz. Her özellik bir `PivotFieldCollection` döndürür. `RowFields` koleksiyonunun 0 indeksindeki alan en dıştaki satır alanıdır ve sonraki dizinler onun içine yuvalanmış alanları temsil eder. Aynı indeksleme kuralı `ColumnFields` için de geçerlidir.

Alanların yuvalanma sırası önemlidir. Önce satır bölgesine `Category` ve ardından `Item` eklemek, dış gruplandırması `Category` ve iç gruplandırması `Item` olan bir pivot üretir. Sıranın tersine çevrilmesi hiyerarşiyi de tersine çevirir.

## **Pivot Alanı Alt Toplamları**

`PivotField.setSubtotals(int subtotalType, boolean shown)` yöntemi, bir pivot alanı için hangi alt toplam satırlarının görüneceğini kontrol eder. Her çağrı, tek bir alt toplam türünü bağımsız olarak değiştirir. `shown = true` geçmek alt toplamı görüntülerken, `shown = false` geçmek onu gizler. Her çağrı yalnızca bir türü etkilediğinden, farklı `subtotalType` değerleriyle yöntemi birden çok kez çağırmak özel bir alt toplam alt kümesi oluşturur.

`PivotFieldSubtotalType` enum'u mevcut alt toplam türlerini tanımlar.

- `AUTOMATIC` — Aspose.Cells varsayılan seçimi seçer (genellikle sayısal alanlar için `SUM`)
- `NONE` — her alt toplam satırını bastır
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
Alt toplamlar yalnızca satır bölgesinde (veya sütun bölgesinde) iki veya daha fazla pivot alanı olduğunda görüntülenir. Tek bir alanın aralarında alt toplam yapılacak anlamlı bir şey yoktur, bu nedenle `setSubtotals` çağrılarının bu durumda görünür bir etkisi olmaz. Bu nedenle bu makale, her bir `Category` grubu arasındaki alt toplam sınırının görünür olması için her örnekte iki satır alanı (`Category` dış, `Item` iç) yerleştirir.
{{% /alert %}}

## **Senaryo 1 — Otomatik (Varsayılan) Alt Toplamlar**

`setSubtotals` yöntemini hiç çağırmadığınızda, Aspose.Cells sayısal alanlar için `AUTOMATIC` seçimini uygular. Aşağıdaki örnek, dış `Category` satır alanı üzerinde `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` çağırarak bu davranışı açıkça doğrular.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);

worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);

worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);

worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);

worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);

worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);

worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);

worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);

int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

PivotField categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true);

pivotTable.calculateData();

workbook.save("output_automatic.xlsx");
```

## **Senaryo 2 — Tüm Alt Toplamların Bastırılması (Yok)**

`setSubtotals(PivotFieldSubtotalType.NONE, true)` çağırmak, pivot'tan her alt toplam satırını kaldırarak yalnızca alan satırlarını ve en altta genel toplamı bırakır. Bu, herhangi bir özet satırı olmadan ham gruplandırılmış verileri istediğinizde faydalıdır.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

String[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.length; j++)
{
    worksheet.getCells().get(0, j).putValue(headers[j]);
}

Object[][] data = {
    { "Fruit",     "Apple",  2020, 100 },
    { "Fruit",     "Apple",  2021, 150 },
    { "Fruit",     "Banana", 2020, 80  },
    { "Fruit",     "Banana", 2021, 90  },
    { "Vegetable", "Carrot", 2020, 50  },
    { "Vegetable", "Carrot", 2021, 60  },
    { "Vegetable", "Daikon", 2020, 40  },
    { "Vegetable", "Daikon", 2021, 45  }
};

for (int i = 0; i < data.length; i++)
{
    for (int j = 0; j < data[i].length; j++)
    {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

PivotField categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(PivotFieldSubtotalType.NONE, true);
pivotTable.calculateData();

workbook.save("output_none.xlsx");
```

## **Senaryo 3 — Özel Alt Toplam Alt Kümesi (Toplam + Ortalama)**

Tek bir alt toplam türüyle sınırlı değilsiniz. Her `setSubtotals` çağrısı bir tür üzerinde bağımsız olarak çalışır; bu nedenle yöntemi bir kez `SUM` ve bir kez de `AVERAGE` ile çağırmak, her `Category` grubu için iki alt toplam satırından oluşan özel bir alt küme üretir.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get("A1").putValue("Category");
worksheet.getCells().get("B1").putValue("Item");
worksheet.getCells().get("C1").putValue("Year");
worksheet.getCells().get("D1").putValue("Amount");

worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);

worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);

worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);

worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);

worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);

worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);

worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);

worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);

PivotTableCollection pivotTables = worksheet.getPivotTables();
int pivotIndex = pivotTables.add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = pivotTables.get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

PivotField categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(PivotFieldSubtotalType.SUM, true);
categoryField.setSubtotals(PivotFieldSubtotalType.AVERAGE, true);

pivotTable.calculateData();

workbook.save("output_custom.xlsx");
```

## **Özet**

Yukarıdaki üç senaryo aynı veri kümesini ve pivot tablo yapısını paylaşır. Aralarındaki tek fark, dış `Category` satır alanına uygulanan `setSubtotals` çağrısıdır. İki alan kuralını unutmayın: bir bölgedeki tek alanın aralarında alt toplam yapılacak bir şey yoktur; bu nedenle `setSubtotals`'ın görünür bir etkiye sahip olmasını istediğinizde, satır veya sütun bölgesine her zaman en az iki alan yerleştirin.

## **İlgili Makaleler**

- [Pivot Tablolardaki Sayfa Alanları](/cells/tr/java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Java'da Pivot Tabloları Yenileme](/cells/tr/java/refresh-pivot-table/)
- [Pivot Tablolara Stil Uygulama](/cells/tr/java/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
