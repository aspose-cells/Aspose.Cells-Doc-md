---
title: Özet Tablo Ekle
linktitle: Özet Tablo Ekle
description: Aspose.Cells for Python via .NET ile özet tablolar oluşturun ve biçimlendirin.
keywords: Özet Tablo Oluştur, Özet Tablo Ekle, Özet Tablo Biçimlendir.
type: docs
weight: 160
url: /tr/python-net/create-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Özet Tablo Nedir?**
Bir özet tablo, etkileşimli bir özet raporudur: ham ve satır bazlı büyük bir veri bloğunu, tek bir formül kullanmadan kompakt bir matrise yoğunlaştırır. Hangi sütunların satır etiketlerine, hangilerinin sütun etiketlerine dönüşeceğini ve hangilerinin değer olarak toplanacağını siz belirlersiniz; gruplama ve hesaplamayı özet tablo yapar:
- **Özetle** — ürün, bölge veya çeyrek bazında toplam satışları, uzun formül zincirleri yerine gösterir.
- **Karşılaştır** — satırlarda kategoriler ve sütunlarda dönemler, düz bir listeyi eğilimlerin tek bakışta görülebileceği bir çapraz rapora dönüştürür.
- **Detaylandır** — özetlenen bir değere çift tıklayarak arkasındaki kaynak satırları inceleyin.
- **Yenile** — kaynak veri değiştiğinde tek bir yenileme tüm raporu yeniden hesaplar.
Tipik kullanım senaryoları satış panoları, gider dökümleri ve envanter analizidir — “bu sayılar kategori ve zamana göre nasıl dağılıyor?” biçimindeki soruları ele alır. Aspose.Cells for Python via .NET aynı türde özet tabloları programatik olarak oluşturur; böylece uygulamanızın ürettiği çalışma kitapları yalnızca ham veri yerine hazır raporlar içerebilir.

### **Özet Tablosu Nesne Modeli**
Aspose.Cells for Python via .NET, özet tabloları oluşturmak ve denetlemek için kullanılan özel bir sınıf kümesini [**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/) namespace'inde sunar. Bu sınıflar, bir özet tablosunun yapı taşları olan [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/) nesnelerini oluşturmak ve ayarlamak için kullanılır. Nesneler şunlardır:
- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/), bir [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/) içindeki bir alanı temsil eder.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection), bir [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) içindeki tüm [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) nesnelerinin koleksiyonunu temsil eder.
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable), bir çalışma sayfasındaki özet tabloyu temsil eder.
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection), bir çalışma sayfasındaki tüm [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) nesnelerinin koleksiyonunu temsil eder.

### **Aspose.Cells ile Basit Bir Özet Tablo Oluşturma**
Bir özet tablosu oluşturmak için şu adımları izleyin: kaynak veriyi çalışma sayfası hücrelerine yazın, özet tablosunu hedef konuma ekleyin ve özet tablosu alanlarını satır, sütun ve veri alanlarına yerleştirin.
1. Bir çalışma sayfasına veri eklemek için [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) nesnesinin [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) yöntemini kullanın. Bu veri, özet tablosunun veri kaynağı olarak kullanılacaktır.
2. [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) koleksiyonunun [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str) yöntemini çağırarak çalışma sayfasına bir özet tablosu ekleyin: `add(source_data, row, column)`. `source_data` kaynak aralıktır (örneğin, "A1:C8"); `row` ve `column`, özet tablosunun sol üst köşesindeki hedef hücrenin sıfır tabanlı satır ve sütun koordinatlarıdır (E3 hücresi satır 2, sütun 4 anlamına gelir). Yöntem, yeni [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) nesnesini doğrudan döndürür.
3. Özet tablosu alanlarını yerleştirmek için [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) nesnesinin `add_field_to_area` yöntemini kullanın: alan adını satır alanına (`PivotFieldType.ROW`), sütun alanına (`PivotFieldType.COLUMN`) veya veri alanına (`PivotFieldType.DATA`) yerleştirin.
4. Çalışma kitabını kaydedin — özet tablo kaydedilen dosyaya yazılır.
Örnek kodu çalıştırdıktan sonra çalışma sayfasına bir özet tablo eklenir.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType

# Yeni bir çalışma kitabı oluştur ve ilk çalışma sayfasını al
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# Kaynak veriyi yaz: spor ve çeyrek başına satışlar
sheet.cells.get("A1").put_value("Sport")
sheet.cells.get("B1").put_value("Quarter")
sheet.cells.get("C1").put_value("Sales")
sheet.cells.get("A2").put_value("Golf")
sheet.cells.get("B2").put_value("Qtr3")
sheet.cells.get("C2").put_value(1500)
sheet.cells.get("A3").put_value("Golf")
sheet.cells.get("B3").put_value("Qtr4")
sheet.cells.get("C3").put_value(2000)
sheet.cells.get("A4").put_value("Tennis")
sheet.cells.get("B4").put_value("Qtr3")
sheet.cells.get("C4").put_value(600)
sheet.cells.get("A5").put_value("Tennis")
sheet.cells.get("B5").put_value("Qtr4")
sheet.cells.get("C5").put_value(1500)
sheet.cells.get("A6").put_value("Tennis")
sheet.cells.get("B6").put_value("Qtr3")
sheet.cells.get("C6").put_value(4070)
sheet.cells.get("A7").put_value("Tennis")
sheet.cells.get("B7").put_value("Qtr4")
sheet.cells.get("C7").put_value(5000)
sheet.cells.get("A8").put_value("Golf")
sheet.cells.get("B8").put_value("Qtr3")
sheet.cells.get("C8").put_value(6430)

# E3 hedef hücresine A1:C8 kaynaklı bir pivot tablo ekle
pivot_table = sheet.pivot_tables.add("A1:C8", 2, 4)

# Pivot alanlarını ata: Sport satırlara, Quarter sütunlara, Sales veri alanına
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Quarter")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")

# Çalışma kitabını kaydet
workbook.save("pivotTable_test_out.xlsx")
```

{{% alert color="primary" %}}
Bir hücre aralığını veri kaynağı olarak atarken aralığın sol üstten sağ alta doğru ilerlemesi gerekir. Örneğin, "A1:C3" geçerlidir ancak "C3:A1" geçerli değildir.
{{% /alert %}}

## İlgili Makaleler
- [Aspose.Cells for Python via .NET ile Özet Tablosuna Filtre Alanları Ekle](/cells/tr/python-net/add-page-field-in-pivot-table/)
- [Aspose.Cells for Python via .NET ile Özet Tablolarına Stiller Uygula](/cells/tr/python-net/apply-style-to-pivot-table/)
- [Özet Tablosunda Sayfa Alanı Düzenini Değiştir](/cells/tr/python-net/change-page-field-layout/)
- [Özet Tablolarını Etikete veya Değere Göre Filtrele](/cells/tr/python-net/filter-by-label-or-value-of-pivot-table/)
- [Aspose.Cells for Python via .NET ile Özet Tablosu Değer Alanlarını Yönet](/cells/tr/python-net/manage-value-fields/)

{{< app/cells/assistant language="python-net" >}}