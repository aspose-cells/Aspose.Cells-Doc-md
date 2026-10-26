---
title: Özet Tablo Oluştur
linktitle: Özet Tablo Oluştur
description: Aspose.Cells for Java ile özet tabloları oluşturun ve biçimlendirin.
keywords: Özet Tablo Oluştur, Özet Tablo Ekle, Özet Tablo Biçimlendir.
type: docs
weight: 160
url: /tr/java/create-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Özet Tablo Nedir?**
Özet tablo, etkileşimli bir özet raporudur: Ham ve satır satır düzenlenmiş verilerden oluşan geniş bir bloğu, tek bir formül kullanmadan kompakt bir matrise yoğunlaştırır. Hangi sütunların satır etiketi, hangilerinin sütun etiketi olacağına ve hangilerinin değer olarak toplanacağına siz karar verirsiniz; gruplama ve hesaplamayı özet tablo yapar:
- **Özetle** — uzun formül zincirleri yerine ürün, bölge veya çeyrek bazında toplam satışları özetleyin.
- **Karşılaştır** — kategorileri satırlara ve dönemleri sütunlara yerleştirerek düz bir listeyi, eğilimlerin bir bakışta görülebildiği çapraz rapora dönüştürün.
- **Ayrıntıya in** — arkasındaki kaynak satırları incelemek için özetlenmiş bir değere çift tıklayın.
- **Yenile** — kaynak veri değiştiğinde tek bir yenileme tüm raporu yeniden hesaplar.
Tipik senaryolar arasında satış panoları, gider dökümleri ve stok analizi bulunur; "bu sayılar kategori ve zamana göre nasıl dağılıyor?" biçimindeki sorular da bu kapsamdadır. Aspose.Cells for Java aynı özet tabloları programatik olarak oluşturur; böylece uygulamanızın oluşturduğu çalışma kitapları, yalnızca ham veri yerine hazır raporlar içerebilir.

### **Aspose.Cells Kullanarak Özet Tablo Oluşturma**

{{% alert color="primary" %}}
Aspose.Cells ile elektronik tablolara özet tablolar eklenebilir. Aspose.Cells, özet tabloları oluşturmak ve yönetmek için özel olarak tasarlanmış çeşitli sınıflar içerir. Bu sınıflar, özet tabloların yapı taşı olan bir [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) nesnesini oluşturmak ve özelliklerini ayarlamak için kullanılır.
Özet tablo nesneleri şunlardır:
- [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField): Özet tablodaki bir alanı temsil eder.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection): Özet tablodaki tüm [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField) nesnelerinin koleksiyonunu temsil eder.
- [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): Bir özet tabloyu temsil eder.
- [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): Çalışma sayfasındaki tüm özet tablo nesnelerinin koleksiyonunu temsil eder.
{{% /alert %}}

### **Basit Bir Özet Tablo Oluşturma**
Özet tablo oluşturmak için kaynak veriyi çalışma sayfası hücrelerine yazın, özet tabloyu hedef konuma ekleyin, özet alanlarını satır, sütun ve veri alanlarına yerleştirin ve çalışma kitabını kaydedin.
1. Çalışma sayfası hücrelerine veri eklemek için [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) nesnesinin [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setValue-java.lang.Object-) yöntemini kullanın (çoğu örnekte `putValue` kullanılır). Bu veri, özet tablonun veri kaynağı olarak kullanılacaktır.
2. Özet tabloyu çalışma sayfasına eklemek için [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) sınıfının [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add-com.aspose.cells.PivotTable-int-int-) yöntemini çağırın: `add(sourceData, row, column)`. `sourceData` kaynak aralığıdır (örneğin, "A1:C8"); `row` ve `column`, özet tablonun sol üst köşesindeki hedef hücrenin 0 tabanlı koordinatlarıdır (E3 hücresi satır 2, sütun 4 anlamına gelir). Yöntem, yeni [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) nesnesini doğrudan döndürür.
3. Özet alanlarını [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) nesnesinin `addFieldToArea` yöntemiyle yerleştirin: alan adını satır alanına (`PivotFieldType.ROW`), sütun alanına (`PivotFieldType.COLUMN`) veya veri alanına (`PivotFieldType.DATA`) ekleyin.
4. Çalışma kitabını kaydedin — özet tablo kaydedilen dosyaya yazılır.
Aşağıdaki kod örneği, bu adımları izleyerek basit bir özet tablo oluşturur. Çalıştırıldığında kaynak verisine dayalı bir özet tablo çalışma sayfasına eklenir:
![todo:görsel_alt_metni](create-pivot-table_1.png)

```java
import com.aspose.cells.*;

// Yeni bir çalışma kitabı oluşturun ve ilk çalışma sayfasını alın
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();

// Kaynak verileri yazın: spor ve çeyrek bazında satışlar
cells.get("A1").putValue("Sport");
cells.get("B1").putValue("Quarter");
cells.get("C1").putValue("Sales");
cells.get("A2").putValue("Golf");
cells.get("B2").putValue("Qtr3");
cells.get("C2").putValue(1500);
cells.get("A3").putValue("Golf");
cells.get("B3").putValue("Qtr4");
cells.get("C3").putValue(2000);
cells.get("A4").putValue("Tennis");
cells.get("B4").putValue("Qtr3");
cells.get("C4").putValue(600);
cells.get("A5").putValue("Tennis");
cells.get("B5").putValue("Qtr4");
cells.get("C5").putValue(1500);
cells.get("A6").putValue("Tennis");
cells.get("B6").putValue("Qtr3");
cells.get("C6").putValue(4070);
cells.get("A7").putValue("Tennis");
cells.get("B7").putValue("Qtr4");
cells.get("C7").putValue(5000);
cells.get("A8").putValue("Golf");
cells.get("B8").putValue("Qtr3");
cells.get("C8").putValue(6430);

// E3 hücresine A1:C8 kaynaklı bir pivot tablo ekleyin
PivotTable pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// Pivot alanlarını atayın: Satırlar için Sport, Sütunlar için Quarter, Veriler için Sales
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Quarter");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");

// Çalışma kitabını kaydedin
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
Bir hücre aralığı veri kaynağı olarak atanırken aralık sol üstten sağ alta doğru tanımlanmalıdır. Örneğin, "A1:C3" geçerlidir; "C3:A1" geçersizdir.
{{% /alert %}}

{{< app/cells/assistant language="java" >}}