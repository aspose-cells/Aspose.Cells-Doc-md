---
title: Özet Tablo Ekle
linktitle: Özet Tablo Ekle
description: Excel elektronik tablo dosyalarında özet tablolar oluşturmak ve biçimlendirmek için Aspose.Cells for Node.js via Java kullanın.
keywords: Özet Tablo Oluştur, Özet Tablo Ekle, Özet Tablosunu Biçimlendir, Aspose.Cells for Node.js via Java.
type: docs
weight: 160
url: /tr/nodejs-java/create-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Özet Tablo Nedir?**
Özet tablo, etkileşimli bir özet raporudur: Ham, satır satır düzenlenmiş büyük bir veri bloğunu tek bir formül kullanmadan kompakt bir matrise dönüştürür. Hangi sütunların satır etiketlerine, hangilerinin sütun etiketlerine dönüşeceğini ve hangilerinin değerler olarak özetleneceğini siz belirlersiniz; gruplama ve hesaplamayı özet tablo yapar:
- **Özetleme** — uzun formül zincirleri yerine ürün, bölge veya çeyrek bazında toplam satışlar.
- **Karşılaştırma** — satırlarda kategoriler ve sütunlarda dönemler, düz bir listeyi eğilimlerin tek bakışta görülebileceği çapraz bir rapora dönüştürür.
- **Ayrıntıya inme** — özetlenmiş bir değere çift tıklayarak arkasındaki kaynak satırları inceleyebilirsiniz.
- **Yenileme** — kaynak veri değiştiğinde tek bir yenileme, raporun tamamını yeniden hesaplar.
Tipik kullanım senaryoları; satış panoları, gider kırılımları ve stok analizidir. Bu alanlar, "bu sayılar kategori ve zamana göre nasıl dağılıyor?" biçimindeki sorulara yanıt verir. Aspose.Cells for Node.js via Java, özet tabloları programatik olarak oluşturmanızı sağlar. Böylece uygulamanızın oluşturduğu çalışma kitapları yalnızca ham veriden oluşmak yerine hazır raporlar da içerebilir.

### **Özet Tablosu Nesne Modeli**
Aspose.Cells, özet tabloları oluşturmak ve denetlemek için kullanılan bir sınıf kümesi sağlar. Temel yapı taşları şunlardır:
- `PivotField`, bir `PivotTable` içindeki bir alanı temsil eder.
- `PivotFieldCollection`, `PivotTable` içindeki tüm `PivotField` nesnelerinin koleksiyonunu temsil eder.
- `PivotTable`, bir çalışma sayfası üzerindeki özet tabloyu temsil eder.
- `PivotTableCollection`, bir çalışma sayfası üzerindeki tüm `PivotTable` nesnelerinin koleksiyonunu temsil eder.

### **Aspose.Cells Kullanarak Basit Bir Özet Tablo Oluşturma**
Bir özet tablo oluşturmak üç adımlı bir işlemdir: kaynak veriyi çalışma sayfası hücrelerine yazın, özet tabloyu hedef konuma ekleyin ve özet alanlarını satır, sütun ve veri alanlarına yerleştirin.
1. Bir çalışma sayfasındaki hücreye `putValue` yöntemini kullanarak veri ekleyin. Bu veri, özet tablonun veri kaynağı olarak kullanılacaktır.
2. `PivotTables` koleksiyonunun `add` yöntemini çağırarak çalışma sayfasına bir özet tablo ekleyin: `add(sourceData, row, column)`. `sourceData` kaynak aralıktır (örneğin, "A1:C8"); `row` ve `column`, özet tablonun sol üst köşesinin yerleştirileceği hedef hücrenin sıfırdan başlayan koordinatlarıdır (E3 hücresi satır 2, sütun 4 anlamına gelir). Yöntem, yeni `PivotTable` nesnesini doğrudan döndürür.
3. `PivotTable` nesnesinin `addFieldToArea` yöntemini kullanarak özet alanlarını yerleştirin. Alan adı, satır alanına (`PivotFieldType.ROW`), sütun alanına (`PivotFieldType.COLUMN`) veya veri alanına (`PivotFieldType.DATA`) eklenir.
4. Çalışma kitabını kaydedin — özet tablo, kaydedilen dosyaya yazılır.
Örnek kodu çalıştırdıktan sonra çalışma sayfasına bir özet tablo eklenir.

```javascript
const AsposeCells = require("aspose.cells");

// Yeni bir çalışma kitabı oluştur ve ilk çalışma sayfasını al
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Kaynak verileri yaz: spor ve çeyrek bazında satışlar
sheet.getCells().get("A1").putValue("Sport");
sheet.getCells().get("B1").putValue("Quarter");
sheet.getCells().get("C1").putValue("Sales");
sheet.getCells().get("A2").putValue("Golf");
sheet.getCells().get("B2").putValue("Qtr3");
sheet.getCells().get("C2").putValue(1500);
sheet.getCells().get("A3").putValue("Golf");
sheet.getCells().get("B3").putValue("Qtr4");
sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Tennis");
sheet.getCells().get("B4").putValue("Qtr3");
sheet.getCells().get("C4").putValue(600);
sheet.getCells().get("A5").putValue("Tennis");
sheet.getCells().get("B5").putValue("Qtr4");
sheet.getCells().get("C5").putValue(1500);
sheet.getCells().get("A6").putValue("Tennis");
sheet.getCells().get("B6").putValue("Qtr3");
sheet.getCells().get("C6").putValue(4070);
sheet.getCells().get("A7").putValue("Tennis");
sheet.getCells().get("B7").putValue("Qtr4");
sheet.getCells().get("C7").putValue(5000);
sheet.getCells().get("A8").putValue("Golf");
sheet.getCells().get("B8").putValue("Qtr3");
sheet.getCells().get("C8").putValue(6430);

// E3 hedef hücresine A1:C8 kaynaklı bir pivot tablo ekle
let pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// Pivot alanlarını ata: Satırlar alanına Sport, Sütunlar alanına Quarter, Veriler alanına Sales
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Quarter");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");

// Çalışma kitabını kaydet
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
Bir hücre aralığını veri kaynağı olarak atarken aralığın sol üstten sağ alta gitmesi gerekir. Örneğin, "A1:C3" geçerlidir ancak "C3:A1" geçerli değildir.
{{% /alert %}}

## İlgili Makaleler
- [Aspose.Cells for Node.js via Java ile Özet Tabloya Filtre Alanları Ekle](/cells/tr/nodejs-java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Node.js via Java ile Özet Tablolara Stiller Uygula](/cells/tr/nodejs-java/apply-style-to-pivot-table/)
- [Özet Tabloda Sayfa Alanı Düzenini Değiştir](/cells/tr/nodejs-java/change-page-field-layout/)
- [Özet Tabloları Etikete veya Değere Göre Filtreleme](/cells/tr/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Aspose.Cells for Node.js via Java ile Özet Tablo Değer Alanlarını Yönetme](/cells/tr/nodejs-java/manage-value-fields/)

{{< app/cells/assistant language="nodejs-java" >}}