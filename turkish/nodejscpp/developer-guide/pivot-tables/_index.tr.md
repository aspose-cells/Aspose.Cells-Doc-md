---
title: Özet Tablosu Ekle
linktitle: Özet Tablosu Ekle
description: C++ aracılığıyla Aspose.Cells for Node.js kullanarak özet tabloları oluşturun ve biçimlendirin.
keywords: Özet Tablosu Oluşturma, Özet Tablosu Ekleme, Özet Tablosu Biçimlendirme.
type: docs
weight: 160
url: /tr/nodejs-cpp/create-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Özet Tablosu Nedir?**
Özet tablosu, etkileşimli bir özet raporudur: Ham, satır satır düzenlenmiş verilerden oluşan büyük bir veri bloğunu tek bir formül kullanmadan kompakt bir matrise dönüştürür. Hangi sütunların satır etiketlerine, hangilerinin sütun etiketlerine dönüşeceğine ve hangilerinin değerler olarak toplanacağına siz karar verirsiniz; gruplama ve hesaplamayı özet tablosu yapar:
- **Özetleme** — uzun formül zincirleri yerine ürün, bölge veya çeyrek bazında toplam satışları özetleme.
- **Karşılaştırma** — satırlarda kategorilerin, sütunlarda dönemlerin bulunduğu düz bir liste, eğilimlerin bir bakışta görülebileceği çapraz rapora dönüşür.
- **Ayrıntıya inme** — herhangi bir özet değere çift tıklayarak arkasındaki kaynak satırları inceleyin.
- **Yenileme** — kaynak veri değiştiğinde tek bir yenileme tüm raporu yeniden hesaplar.
Yaygın kullanım senaryoları, satış panoları, gider dağılımları ve stok analizileri gibi "bu sayılar kategori ve zamana göre nasıl dağılıyor?" biçimindeki soruları ele alır. C++ aracılığıyla Aspose.Cells for Node.js aynı özet tabloları programatik olarak oluşturur; böylece uygulamanızın oluşturduğu çalışma kitapları yalnızca ham veri yerine hazır raporlar içerebilir.

### **Özet Tablosu Nesne Modeli**
Aspose.Cells for Node.js (C++ aracılığıyla), özet tabloları oluşturmak ve yönetmek için kullanılan özel bir sınıf kümesi sağlar. Bu sınıflar, bir özet tablonun yapı taşları olan [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) nesnelerini oluşturmak ve ayarlamak için kullanılır. Nesneler şunlardır:
- [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield), bir [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) içindeki bir alanı temsil eder.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection), bir [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) içindeki tüm [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) nesnelerinden oluşan koleksiyonu temsil eder.
- [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable), bir çalışma sayfası üzerindeki PivotTable nesnesini temsil eder.
- [**PivotTableCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection), bir çalışma sayfası üzerindeki tüm [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) nesnelerinden oluşan koleksiyonu temsil eder.

### **Aspose.Cells Kullanarak Basit Bir Özet Tablosu Oluşturma**
Bir özet tablo oluşturmak üç aşamalı bir yöntemdir: kaynak veriyi çalışma sayfası hücrelerine yazın, özet tabloyu hedef konuma ekleyin ve özet tablo alanlarını satır, sütun ve veri alanlarına yerleştirin.
1. Bir çalışma sayfasına veri eklemek için [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) nesnesinin [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) yöntemini kullanın. Bu veri, özet tablonun veri kaynağı olarak kullanılacaktır.
2. Çalışma sayfasına bir özet tablo eklemek için [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) koleksiyonunun [**add**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#add-string-string-string-) yöntemini çağırın: `add(sourceData, row, column)`. `sourceData` kaynak aralıktır (örneğin, "A1:C8"); `row` ve `column`, özet tablonun sol üst köşesindeki hedef hücrenin 0 tabanlı koordinatlarıdır (E3 hücresi satır 2, sütun 4 anlamına gelir). Yöntem, yeni [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) nesnesini doğrudan döndürür.
3. Özet tablo alanlarını [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) nesnesinin `addFieldToArea` yöntemiyle yerleştirin: bir alan adı satır alanına (`PivotFieldType.Row`), sütun alanına (`PivotFieldType.Column`) veya veri alanına (`PivotFieldType.Data`) gider.
4. Çalışma kitabını kaydedin — özet tablo kaydedilen dosyaya yazılır.
Örnek kodu çalıştırdıktan sonra çalışma sayfasına bir özet tablo eklenir.

```javascript
const AsposeCells = require("aspose.cells.node");

// Yeni bir çalışma kitabı oluşturun ve ilk çalışma sayfasını alın
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Kaynak verileri yazın: spor ve çeyrek bazında satışlar
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

// E3 hedef hücresine A1:C8 kaynaklı bir pivot tablo ekleyin
let pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// Pivot alanlarını atayın: Satır öğesine Sport, Sütun öğesine Quarter, Veri öğesine Sales
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Quarter");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");

// Çalışma kitabını kaydedin
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
Hücre aralığını veri kaynağı olarak atadığınızda aralık sol üstten sağ alta olmalıdır. Örneğin, "A1:C3" geçerlidir ancak "C3:A1" geçerli değildir.
{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}