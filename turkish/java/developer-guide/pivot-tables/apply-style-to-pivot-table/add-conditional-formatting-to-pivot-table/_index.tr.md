---
title: Pivot Tablosuna Koşullu Biçimlendirme Ekle
linktitle: Pivot Tablosuna Koşullu Biçimlendirme Ekle
description: Aspose.Cells for Java'da bir Pivot Tablosuna koşullu biçimlendirme ekleyin - bir kuralı applyTo ve PivotConditionFormatScopeType kapsamı ile veri bölgesine bağlayın veya hedefi addCellArea ve getPivotAreas ile tanımlayın, ardından kuralları ve stilleri FormatConditions.addCondition aracılığıyla ekleyin.
keywords: Aspose.Cells for Java, Pivot Tablosu, koşullu biçimlendirme, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Java
type: docs
weight: 30
url: /tr/java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Üst sayfada ve kardeş sayfada açıklanan stiller statiktir – bir `PivotArea` ya da `CellArea` bölgesi bir kez boyanır ve değerler ne olursa olsun stilini korur. Koşullu biçimlendirme ise kural‑tabanlı bir uygulamadır – 200'ün üzerindeki tutarları vurgulayın, orta yüzde ellisini gölgeli yapın veya en alt sıralamadaki öğeleri işaretleyin – ve vurgulama, pivot tablo yeniden hesaplandığında veya yenilendiğinde değerleri izler.
Aspose.Cells içinde, pivot‑tablo koşullu biçimlendirme `PivotTable.getConditionalFormats()` koleksiyonunda bulunur. Her giriş bağımsız olarak iki soruya yanıt veren bir `PivotConditionalFormat` nesnesidir:
- **Kural nerede uygulanır?** Hedef bölge ya `applyTo(int row, int column, PivotConditionFormatScopeType scope)` yöntemiyle (Excel kullanıcı arabiriminin kapsam seçicisini yansıtır) ya da `addCellArea(CellArea)` ve `getPivotAreas()` koleksiyonuyla açıkça adlandırılır.
- **Kural neyi test eder?** Bir veya daha fazla koşul `getFormatConditions()` üzerinden `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` ile eklenir ve her koşul kendi `Style` nesnesine sahiptir.

{{% alert color="primary" %}}
`getFormatConditions()` koleksiyonundaki bir pivot koşullu formatı için `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` veya `FormatConditionCollection.addArea(CellArea)` metodlarını çağırmayın. Bu iki aşırı yükleme, normal çalışma sayfası koşullu biçimlendirme API'sinden miras alınmıştır ve pivot tablolar için çalışmaz – hücre bölgesi pivot bölgesine dönüştürülmez, bu yüzden istek sessizce görmezden gelinir. Bölgeyi her zaman `PivotConditionalFormat` nesnesi üzerinde (`applyTo`, `addCellArea` veya `getPivotAreas()`) tanımlayın ve kuralı `addCondition` aşırı yüklerinden biriyle ekleyin.
{{% /alert %}}

## **Kuralı Bir Kapsamla Uygula (Excel UI Yöntemi)**
İlk yöntem, Excel kullanıcı arabiriminde olduğu gibi kuralı konumlandırır. Pivot tablosundaki bir hücre, sıfır‑tabanlı çalışma sayfası koordinatlarıyla adlandırılır ve bir `PivotConditionFormatScopeType` kapsamı, Aspose.Cells'e kuralın o hücreden ne kadar uzağa yayılacağını söyler:
- `PivotConditionFormatScopeType.DATA` – pivot tablosunun ürettiği tüm değer hücreleri, toplamlar dahil.
- `PivotConditionFormatScopeType.FIELD` – hücrenin tanımladığı alana ait değer hücreleri, toplamlar hariç. Hücre bir alan etiketi (ör. satır‑alan etiketi) olmalıdır; bir değer hücresi geçirilirse istisna fırlatılır.
- `PivotConditionFormatScopeType.SELECTION` – hücrenin seçtiği kesişimdeki değer hücreleri, tipik olarak tek bir değer hücresi.
Aşağıdaki örnek, sol‑üst köşesi E3 olan bir meyve‑satış pivot tablosu oluşturur, `DATA` kapsamıyla F4 (satır 3, sütun 5) hücresine koşullu bir biçimlendirme ekler ve 200'ün üzerindeki tüm tutarları kırmızı zeminde beyaz kalın harflerle vurgular. Değerler Apple 220, Banana 330, Cherry 200 ve toplam 750 olduğunda kural F4, F5 ve F7 hücrelerini boyar – çözülen bölge tüm veri sütunu F4:F7 olur ve sadece koşulu geçen hücreler ışık alır.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
// Pivot tablosu, sol üst köşesi E3'te
PivotTable pivotTable = sheet.getPivotTables().add("A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Koşullu biçimi F4'te (satır 3, sütun 5) Veri kapsamıyla sabitle
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, PivotConditionFormatScopeType.DATA);
// Kural - 200'den büyük tutarları vurgula
int conditionIndex = format.getFormatConditions().addCondition(
        FormatConditionType.CELL_VALUE, OperatorType.GREATER_THAN, "200", null);
Style style = workbook.createStyle();
style.getFont().setBold(true);
style.getFont().setColor(Color.getWhite());
style.setForegroundColor(Color.getRed());
style.setPattern(BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

Aynı kuralı satır‑alan etiketi E4 (satır 3, sütun 4) üzerine `FIELD` kapsamıyla bağladığınızda çözüm F4:F6 olur – aynı veri sütunu ancak toplam satırı hariç – çünkü kapsam artık `Fruit` alanını tanımlar, tüm değer bölgesi değil. `SELECTION` kapsamı F4 üzerine bağlandığında sadece F4 çözülür.

## **Bölgeyi Manuel Olarak Tanımlama**
İkinci yöntem, kapsam seçicisini atlayıp bölgeyi `PivotConditionalFormat` üzerinde doğrudan adlandırır.

### **addCellArea ile bir çalışma sayfası dikdörtgeni**
`addCellArea(CellArea)` verilen dikdörtgeni kuralın hedefi olarak kaydeder. Koordinatlar sıfır‑tabanlı çalışma sayfası koordinatlarıdır ve bölge tam olarak sağlanan dikdörtgendir – veri sütununa genişleme ya da toplam mantığı yoktur. İlginç hücreler mevcut pivot düzeninde önceden bilinen sabit bir dikdörtgen olduğunda bunu kullanın.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Target the rectangle F4:F6 (the value cells without the grand total)
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
CellArea cellArea = new CellArea();
cellArea.StartRow = 3;
cellArea.StartColumn = 5;
cellArea.EndRow = 5;
cellArea.EndColumn = 5;
format.addCellArea(cellArea);
// Rule - italic on light yellow for amounts between 150 and 300
int conditionIndex = format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE, OperatorType.BETWEEN, "150", "300");
Style style = workbook.createStyle();
style.getFont().setItalic(true);
style.setForegroundColor(Color.getLightYellow());
style.setPattern(BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **getPivotAreas ile anlamsal bir pivot bölgesi**
`getPivotAreas()` aynı anlamsal‑bölge modelini döndürür; bu model kardeş sayfada statik stiller için kullanılır. Bir `PivotArea` oluşturun, `select` ya da `selectField` ile bir alan ya da bölge seçin ve `getPivotAreas().addPivotArea(PivotArea)` ile ekleyin. Anlamsal bir bölge, alanına bağlı kalır; böylece koşullu biçimlendirme, pivot tablo yenilendiğinde ve yerleşim değiştiğinde alanı izler. `getPivotAreas().add(PivotArea)` aşırı yüklemesi hâlâ derlenir ancak kullanımdan kaldırılmıştır – `addPivotArea` tercih edilmelidir.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Kuralı, Amount veri alanına anlamsal bir bölge olarak ilişkilendir
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
PivotArea area = new PivotArea(pivotTable);
area.selectField(PivotFieldType.DATA, "Amount");
format.getPivotAreas().addPivotArea(area);
// Kural - 150'nin altındaki miktarlar için gri metin
int conditionIndex = format.getFormatConditions().addCondition(
        FormatConditionType.CELL_VALUE, OperatorType.LESS_THAN, "150", null);
Style style = workbook.createStyle();
style.getFont().setColor(Color.getGray());
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **Kuralların Nerede Saklandığı ve Yeniden Yüklemede Nasıl Korunduğu**
Her `getConditionalFormats().add()` çağrısı, pivot tabloya bir `PivotConditionalFormat` ekler. Koşullar, formülleri ve stilleri çalışma kitabıyla birlikte kaydedilir – aşağıdaki örnekte dosya yeniden açıldığında aynı kural, tipi, operatörü ve formülü bozulmadan görünür ve `getCellAreas()` aynı bölgeleri rapor eder. Koşul almamış girişler, çalışma kitabı kaydedildiğinde atılır; bu, Excel'in kuralı olmayan bir koşullu biçimlendirmeyi silmesiyle aynı şekildedir.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("PivotConditionalFormatData.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
System.out.println("Conditional formats: " + pivotTable.getConditionalFormats().getCount());
for (int i = 0; i < pivotTable.getConditionalFormats().getCount(); i++)
{
    PivotConditionalFormat format = pivotTable.getConditionalFormats().get(i);
    for (int j = 0; j < format.getFormatConditions().getCount(); j++)
    {
        FormatCondition condition = format.getFormatConditions().get(j);
        System.out.println("Format " + i + ": " + condition.getType() + " " + condition.getOperator() + " formula1=" + condition.getFormula1());
    }
    for (CellArea area : format.getCellAreas())
    {
        System.out.println("    rows " + (area.StartRow + 1) + "-" + (area.EndRow + 1)
                + ", columns " + (area.StartColumn + 1) + "-" + (area.EndColumn + 1));
    }
}
// Bu şu çıktıyı verir:
// Koşullu biçimler: 1
// Biçim 0: CellValue GreaterThan formula1==200
//     satırlar 4-7, sütunlar 6-6        (F4:F7, çözülen veri bölgesi)
```

## **İlgili Makaleler**
- [Pivot Tablosuna Stil Uygulama](/cells/tr/java/apply-style-to-pivot-table/)
- [Pivot Tablosunun Bir Bölümünü Biçimlendirme](/cells/tr/java/format-part-of-pivot-table/)
- [Pivot Tablosunda En İyi 10 Gösterme veya Filtreleme](/cells/tr/java/top-10-show-or-filter-in-pivot-table/)
- [Pivot Tablolarını Etiket veya Değer ile Filtreleme](/cells/tr/java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="java" >}}