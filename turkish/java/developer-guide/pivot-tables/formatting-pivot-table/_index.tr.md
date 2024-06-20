---
title: Pivot Tablosunu Biçimlendirme
type: docs
weight: 60
url: /tr/java/formatting-pivot-table/
---

## **Döndürme Tablosu Görünümü**

[Pivot Tablosu Nasıl Oluşturulur](/cells/tr/java/create-pivot-table/) basit bir döndürme tablosu nasıl oluşturulur konusunu ele almaktadır. Bu makale daha ileri giderek, bir döndürme tablosunun görünümünü nasıl özelleştireceğinizi ve özelliklerini nasıl ayarlayacağınızı tartışmaktadır.

### **Döndürme Tablosu Biçim Seçeneklerini Ayarlama**

[**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) sınıfı size döndürme tablosu için çeşitli biçimlendirme seçenekleri belirlemenize olanak tanır.

#### **Otomatik Biçim ve Döndürme Tablosu Stili Türlerinin Ayarlanması**

Aşağıdaki kod örneği, otomatik biçim türünü ve döndürme tablosu stili türünü [**AutoFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#AutoFormatType) ve [**PivotTableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#PivotTableStyleType) özelliklerini kullanarak nasıl ayarlayacağınızı göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetAutoFormatandPivotTableStyleTypes-SetAutoFormatandPivotTableStyleTypes.java" >}}

#### **Biçim Seçeneklerini Ayarlama**

Aşağıdaki kod örneği, satır ve sütunlar için toplamlar eklemek ve diğer birçok biçimlendirme seçeneğini döndürme tablosu raporu için nasıl ayarlayacağınızı göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingFormatOptions-SettingFormatOptions.java" >}}

### **PivotFields Biçim Seçeneklerini Ayarlama**

Genel döndürme tablosunun biçimlendirilmesini kontrol etmenin yanı sıra, Aspose.Cells for Java, sütun alanları, satır alanları ve sayfa alanlarının biçimlendirmesini ince ayarlı bir şekilde kontrol etmeyi sağlar.

#### **Satır, Sütun ve Sayfa Alanları Biçimini Ayarlama**

Aşağıdaki kod örneği, satır alanlarına erişimi, belirli bir satıra erişimi, ara toplamları ayarlama, otomatik sıralama uygulama ve otomatik gösterim seçeneğini kullanma şeklinizi göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetRowColumnPageFieldsFormat-SetRowColumnPageFieldsFormat.java" >}}

### **Veri Alanları Biçimini Ayarlama**

Aşağıdaki kod satırları, veri alanlarını nasıl biçimlendireceğinizi göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingDataFieldFormat-SettingDataFieldFormat.java" >}}

### **Bir Pivot Tablosunun Hızlı Stilini Değiştirme**

Aşağıdaki kod örnekleri, bir döndürme tablosuna uygulanan hızlı stili nasıl değiştireceğinizi göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ModifyPivotTableQuickStyle-ModifyPivotTableQuickStyle.java" >}}

### **Pivot Alanlarını Temizleme**

[**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection)'nin, sayfa, sütun, satır veya veri alanı örneklerinde döndürme alanlarını temizleyen [**clear()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfieldcollection#clear--) adında bir yöntemi bulunmaktadır. Tüm döndürme alanlarını temizlemek için bunu kullanın.
Aşağıdaki kod örneği, veri alanındaki tüm döndürme alanlarını nasıl temizleyeceğinizi göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ClearPivotFields-ClearPivotFields.java" >}}

## **Konsolidasyon İşlevi**

### **Döndürme Tablosunun Veri Alanlarına Konsolidasyon İşlevi Uygulama**

Aspose.Cells, döndürme tablosunun veri alanlarına (veya değer alanlarına) konsolidasyon işlevi uygulamak için kullanılabilir. Microsoft Excel'de, değer alanına sağ tıklayabilir ve ardından **Değer Alanı Ayarları...** seçeneğini seçebilir ve ardından **Değerleri Özetleme Yolu** sekmesini seçebilirsiniz. Oradan, Toplam, Sayı, Ortalama, Maksimum, Minimum, Çarpım, Farklı Sayınız gibi istediğiniz herhangi bir Konsolidasyon İşlevini seçebilirsiniz.

Aspose.Cells, aşağıdaki konsolidasyon işlevlerini desteklemek için [**ConsolidationFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) numaralı sıralamayı sağlamaktadır.

- [**ConsolidationFunction.AVERAGE**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#AVERAGE)
- [**ConsolidationFunction.COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT)
- [**ConsolidationFunction.COUNT_NUMS**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT_NUMS)
- [**ConsolidationFunction.DISTINCT_COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#DISTINCT_COUNT)
- [**ConsolidationFunction.MAX**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MAX)
- [**ConsolidationFunction.MIN**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MIN)
- [**ConsolidationFunction.PRODUCT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#PRODUCT)
- [**ConsolidationFunction.STD_DEV**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEV)
- [**ConsolidationFunction.STD_DEVP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEVP)
- [**ConsolidationFunction.SUM**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#SUM)
- [**ConsolidationFunction.VAR**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VAR)
- [**ConsolidationFunction.VARP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VARP)

Aşağıdaki kod, birinci veri alanına (veya değer alanına) **Ortalama** konsolidasyon işlevini ve ikinci veri alanına (veya değer alanına) **Farklı Sayı Sayımı** konsolidasyon işlevini uygulamaktadır.

{{% alert color="primary" %}}

Farklı Sayı Sayımı konsolidasyon işlevi sadece Microsoft Excel 2013 tarafından desteklenmektedir.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ConsolidationFunctions-ConsolidationFunctions.java" >}}
