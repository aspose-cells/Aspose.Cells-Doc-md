---
title: Özet Tablolar
linktitle: Özet Tablolar
description: Aspose.Cells for Python via Java ile özet tabloları oluşturun ve biçimlendirin.
keywords: Özet Tablosu Oluştur, Özet Tablosu Ekle, Özet Tablosu Biçimlendir.
type: docs
weight: 160
url: /tr/python-java/create-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Özet Tablo Nedir?**
Özet tablo, etkileşimli bir özet raporudur: Ham satır satır verilerden oluşan büyük bir bloğu, tek bir formül kullanmadan kompakt bir matrise yoğunlaştırır. Hangi sütunların satır etiketi, hangilerinin sütun etiketi olacağına ve hangilerinin değer olarak özetleneceğine siz karar verirsiniz; gruplama ve hesaplamayı özet tablo yapar:
- **Özetleme** — uzun formül zincirleri yerine ürün, bölge veya çeyrek bazında toplam satışları gösterir.
- **Karşılaştırma** — satırlarda kategorilerin ve sütunlarda dönemlerin yer alması, düz bir listeyi eğilimlerin bir bakışta görülebildiği çapraz bir rapora dönüştürür.
- **Detaylandırma** — herhangi bir özet değere çift tıklayarak değerin arkasındaki kaynak satırları inceleyin.
- **Yenileme** — kaynak veriler değiştiğinde tek bir yenileme işlemi raporun tamamını yeniden hesaplar.
Tipik kullanım senaryoları; satış panoları, gider dağılımları ve stok analizidir. "Bu sayılar kategoriye ve zamana göre nasıl dağılıyor?" biçimindeki tüm sorular da bu kapsama girer. Aspose.Cells for Python via Java aynı özet tablolarını programatik olarak oluşturur; böylece uygulamanızın oluşturduğu çalışma kitapları yalnızca ham veri taşımak yerine hazır raporlar da içerebilir.

### **Özet Tablo Nesne Modeli**
Aspose.Cells, özet tabloları oluşturmak ve yönetmek için bir sınıf kümesi sunar. Temel yapı taşları şunlardır:
- `PivotField`, bir `PivotTable` içindeki alanı temsil eder.
- `PivotFieldCollection`, `PivotTable` içindeki tüm `PivotField` nesnelerinin koleksiyonunu temsil eder.
- `PivotTable`, bir çalışma sayfası üzerindeki özet tabloyu temsil eder.
- `PivotTableCollection`, bir çalışma sayfası üzerindeki tüm `PivotTable` nesnelerinin koleksiyonunu temsil eder.

### **Aspose.Cells Kullanarak Basit Bir Özet Tablo Oluşturma**
Bir özet tablo oluşturmak üç adımlık bir işlemdir: kaynak verileri çalışma sayfası hücrelerine yazın, özet tabloyu hedef konuma ekleyin ve özet alanlarını satır, sütun ve veri alanlarına yerleştirin.
1. Hücrenin `putValue` yöntemini kullanarak çalışma sayfasına veri ekleyin. Bu veriler, özet tablonun veri kaynağı olarak kullanılacaktır.
2. `PivotTables` koleksiyonunun `add` yöntemini çağırarak çalışma sayfasına bir özet tablo ekleyin: `add(sourceData, row, column)`. `sourceData`, kaynak aralıktır (örneğin "A1:C8"); `row` ve `column`, özet tablonun sol üst köşesine yerleştirilecek hedef hücrenin 0 tabanlı koordinatlarıdır (E3 hücresi 2. satır ve 4. sütun anlamına gelir). Yöntem, yeni `PivotTable` nesnesini doğrudan döndürür.
3. Özet alanlarını `PivotTable` nesnesinin `addFieldToArea` yöntemiyle yerleştirin: alan adını satır alanına (`PivotFieldType.ROW`), sütun alanına (`PivotFieldType.COLUMN`) veya veri alanına (`PivotFieldType.DATA`) ekleyin.
4. Çalışma kitabını kaydedin — özet tablo kaydedilen dosyaya yazılır.
Örnek kodu çalıştırdıktan sonra çalışma sayfasına bir özet tablo eklenir.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType

# Yeni bir çalışma kitabı oluştur ve ilk çalışma sayfasını al
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Kaynak verileri yaz: spor ve çeyrek bazında satışlar
cells.get("A1").putValue("Sport")
cells.get("B1").putValue("Quarter")
cells.get("C1").putValue("Sales")
cells.get("A2").putValue("Golf")
cells.get("B2").putValue("Qtr3")
cells.get("C2").putValue(1500)
cells.get("A3").putValue("Golf")
cells.get("B3").putValue("Qtr4")
cells.get("C3").putValue(2000)
cells.get("A4").putValue("Tennis")
cells.get("B4").putValue("Qtr3")
cells.get("C4").putValue(600)
cells.get("A5").putValue("Tennis")
cells.get("B5").putValue("Qtr4")
cells.get("C5").putValue(1500)
cells.get("A6").putValue("Tennis")
cells.get("B6").putValue("Qtr3")
cells.get("C6").putValue(4070)
cells.get("A7").putValue("Tennis")
cells.get("B7").putValue("Qtr4")
cells.get("C7").putValue(5000)
cells.get("A8").putValue("Golf")
cells.get("B8").putValue("Qtr3")
cells.get("C8").putValue(6430)

# A1:C8 kaynak aralığından E3 hücresine bir pivot tablo ekle
pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4)

# Pivot alanlarını ata: Sport satırlara, Quarter sütunlara, Sales veri alanına
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Quarter")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales")

# Çalışma kitabını kaydet
workbook.save("pivotTable_test_out.xlsx")
```

{{% alert color="primary" %}}
Hücre aralığını veri kaynağı olarak atadığınızda, aralık sol üstten sağ alta doğru ilerlemelidir. Örneğin, "A1:C3" geçerlidir ancak "C3:A1" geçerli değildir.
{{% /alert %}}

## İlgili Makaleler
- [Aspose.Cells for Python via Java ile bir özet tablosuna filtre alanları ekleme](/cells/tr/python-java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Python via Java ile özet tablolarına stil uygulama](/cells/tr/python-java/apply-style-to-pivot-table/)
- [Özet tabloda sayfa alanı düzenini değiştirme](/cells/tr/python-java/change-page-field-layout/)
- [Etikete veya değere göre özet tabloları filtreleme](/cells/tr/python-java/filter-by-label-or-value-of-pivot-table/)
- [Aspose.Cells for Python via Java ile özet tablosu değer alanlarını yönetme](/cells/tr/python-java/manage-value-fields/)

{{< app/cells/assistant language="python" >}}