---
title: Özet Tablo Ekle
linktitle: Özet Tablo Ekle
description: Excel elektronik tablo dosyalarının özet tablolarını oluşturun ve biçimlendirin.
keywords: Özet Tablo Oluştur, Özet Tablo Ekle, Özet Tabloyu Biçimlendir.
type: docs
weight: 160
url: /tr/net/create-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Özet Tablo Nedir?**
Bir özet tablo, etkileşimli bir özet raporudur: Ham, satır bazlı verilerden oluşan geniş bir bloğu, tek bir formül kullanmadan kompakt bir matrise özetler. Hangi sütunların satır etiketlerine, hangilerinin sütun etiketlerine dönüşeceğini ve hangilerinin değer olarak özetleneceğini siz belirlersiniz — gruplama ve hesaplamayı özet tablo yapar:
- **Özetleme** — ürün, bölge veya çeyrek bazında toplam satışları, uzun formül zincirleri yerine sunar.
- **Karşılaştırma** — satırlarda kategorilerin ve sütunlarda dönemlerin yerleştirilmesi, düz bir listeyi eğilimlerin bir bakışta görülebildiği çapraz bir rapora dönüştürür.
- **Detaylandırma** — herhangi bir özet değerine çift tıklayarak arkasındaki kaynak satırları inceleyin.
- **Yenileme** — kaynak veri değiştiğinde tek bir yenileme tüm raporu yeniden hesaplar.
Tipik senaryolar: satış panoları, gider dökümleri ve stok analizleri — "bu sayılar kategori ve zamana göre nasıl dağılıyor?" biçimindeki tüm sorular. Aspose.Cells for .NET aynı özet tablolarını programatik olarak oluşturur; böylece uygulamanızın oluşturduğu çalışma kitapları, yalnızca ham veri yerine hazır raporlar da içerebilir.

### **Özet Tablosu Nesne Modeli**
Aspose.Cells, özet tabloları oluşturmak ve denetlemek için kullanılan özel bir sınıf grubunu [**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot) namespace içinde sunar. Bu sınıflar, özet tablonun yapı taşları olan [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) nesnelerini oluşturmak ve yapılandırmak için kullanılır. Nesneler şunlardır:
- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield), bir [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) içindeki bir alanı temsil eder.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection), bir [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) içindeki tüm [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) nesnelerinin koleksiyonunu temsil eder.
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable), bir çalışma sayfasındaki özet tablosunu temsil eder.
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection), bir çalışma sayfasındaki tüm [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) nesnelerinin koleksiyonunu temsil eder.

### **Aspose.Cells Kullanarak Basit Bir Özet Tablo Oluşturma**
Bir özet tablo oluşturmak üç adımlık bir süreçtir: kaynak veriyi çalışma sayfası hücrelerine yazın, özet tabloyu hedef konuma ekleyin ve özet tablo alanlarını satır alanına, sütun alanına ve veri alanına yerleştirin.
1. [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) nesnesinin [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) yöntemini kullanarak bir çalışma sayfasına veri ekleyin. Bu veri, özet tablonun veri kaynağı olarak kullanılacaktır.
2. Bir çalışma sayfasına özet tablo eklemek için [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) koleksiyonunun [**Add**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index) yöntemini çağırın: `Add(sourceData, row, column)`. `sourceData` kaynak aralıktır (örneğin, "A1:C8"); `row` ve `column`, özet tablonun sol üst köşesindeki hedef hücrenin 0 tabanlı koordinatlarıdır (E3 hücresi, 2. satır ve 4. sütun anlamına gelir). Yöntem, yeni [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) nesnesini doğrudan döndürür.
3. Özet tablo alanlarını [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) nesnesinin `AddFieldToArea` yöntemiyle yerleştirin. Bir alan adı, satır alanına (`PivotFieldType.Row`), sütun alanına (`PivotFieldType.Column`) veya veri alanına (`PivotFieldType.Data`) olarak eklenir.
4. Çalışma kitabını kaydedin — özet tablo kaydedilen dosyaya yazılır.
Örnek kod çalıştırıldıktan sonra çalışma sayfasına bir özet tablo eklenir.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Yeni bir çalışma kitabı oluştur ve ilk çalışma sayfasını al
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// Kaynak verileri yaz: spor ve çeyrek bazında satışlar
sheet.Cells["A1"].PutValue("Sport");
sheet.Cells["B1"].PutValue("Quarter");
sheet.Cells["C1"].PutValue("Sales");
sheet.Cells["A2"].PutValue("Golf");
sheet.Cells["B2"].PutValue("Qtr3");
sheet.Cells["C2"].PutValue(1500);
sheet.Cells["A3"].PutValue("Golf");
sheet.Cells["B3"].PutValue("Qtr4");
sheet.Cells["C3"].PutValue(2000);
sheet.Cells["A4"].PutValue("Tennis");
sheet.Cells["B4"].PutValue("Qtr3");
sheet.Cells["C4"].PutValue(600);
sheet.Cells["A5"].PutValue("Tennis");
sheet.Cells["B5"].PutValue("Qtr4");
sheet.Cells["C5"].PutValue(1500);
sheet.Cells["A6"].PutValue("Tennis");
sheet.Cells["B6"].PutValue("Qtr3");
sheet.Cells["C6"].PutValue(4070);
sheet.Cells["A7"].PutValue("Tennis");
sheet.Cells["B7"].PutValue("Qtr4");
sheet.Cells["C7"].PutValue(5000);
sheet.Cells["A8"].PutValue("Golf");
sheet.Cells["B8"].PutValue("Qtr3");
sheet.Cells["C8"].PutValue(6430);

// E3 hücresine A1:C8 kaynaklı bir pivot tablo ekle
PivotTable pivotTable = sheet.PivotTables.Add("A1:C8", 2, 4);

// Pivot alanlarını ata: Sport satırlara, Quarter sütunlara, Sales verilere
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Quarter");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");

// Çalışma kitabını kaydet
workbook.Save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
Bir hücre aralığını veri kaynağı olarak atadığınızda, aralığın sol üstten sağ alta doğru ilerlemesi gerekir. Örneğin, "A1:C3" geçerlidir ancak "C3:A1" geçerli değildir.
{{% /alert %}}

## İlgili Makaleler
- [Aspose.Cells for .NET ile Özet Tabloya Filtre Alanları Ekle](/cells/tr/net/add-page-field-in-pivot-table/)
- [Aspose.Cells for .NET ile Özet Tablolarına Biçimler Uygula](/cells/tr/net/apply-style-to-pivot-table/)
- [Özet Tablosunda Sayfa Alanı Düzenini Değiştir](/cells/tr/net/change-page-field-layout/)
- [Özet Tablolarını Etikete veya Değere Göre Filtrele](/cells/tr/net/filter-by-label-or-value-of-pivot-table/)
- [Aspose.Cells for .NET ile Özet Tablosunun Değer Alanlarını Yönet](/cells/tr/net/manage-value-fields/)

{{< app/cells/assistant language="csharp" >}}