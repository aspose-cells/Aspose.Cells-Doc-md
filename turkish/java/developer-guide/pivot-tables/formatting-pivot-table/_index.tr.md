---
title: Pivot Tabloyu Biçimlendirme
type: docs
weight: 60
url: /tr/java/formatting-pivot-table/
---
## **Pivot Tablo Görünümü**

[Pivot Tablo Nasıl Oluşturulur](/cells/tr/java/create-pivot-table/) basit bir pivot tablonun nasıl oluşturulacağını gösterdi. Bu makale daha da ileri gidiyor ve özellikleri ayarlayarak bir pivot tablonun görünümünün nasıl özelleştirileceğini tartışıyor.

### **Pivot Tablo Format Seçeneklerini Ayarlama**

 bu[**Pivot tablo**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) class, bir pivot tablo için çeşitli biçimlendirme seçeneklerini ayarlamanıza olanak tanır.

#### **AutoFormat ve PivotTableStyle Türlerini Ayarlama**

 Aşağıdaki kod örneği, otomatik biçim türünün ve pivot tablo stili türünün nasıl ayarlanacağını gösterir.[**Otomatik BiçimTürü**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#AutoFormatType) ve[**PivotTableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#PivotTableStyleType) özellikleri.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetAutoFormatandPivotTableStyleTypes-SetAutoFormatandPivotTableStyleTypes.java" >}}

#### **Biçim Seçeneklerini Ayarlama**

Aşağıdaki kod örneği, satırlar ve sütunlar için genel toplamların eklenmesi de dahil olmak üzere bir pivot tablo raporu için bir dizi biçimlendirme seçeneğinin nasıl ayarlanacağını gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingFormatOptions-SettingFormatOptions.java" >}}

### **PivotFields Format Seçeneklerini Ayarlama**

Aspose.Cells for Java Aspose.Cells for Java, genel pivot tablonun biçimlendirmesini kontrol etmenin yanı sıra satır alanları, sütun alanları ve sayfa alanları için biçimlendirmenin ince ayarlı kontrolünü sağlar.

#### **Satır, Sütun ve Sayfa Alanları Biçimini Ayarlama**

Aşağıdaki kod örneği, satır alanlarına nasıl erişileceğini, belirli bir satıra nasıl erişileceğini, ara toplamların nasıl ayarlanacağını, otomatik sıralamanın nasıl uygulanacağını ve autoShow seçeneğinin nasıl kullanılacağını gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetRowColumnPageFieldsFormat-SetRowColumnPageFieldsFormat.java" >}}

### **Veri Alanları Biçimini Ayarlama**

Aşağıdaki kod satırları, veri alanlarının nasıl biçimlendirileceğini göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingDataFieldFormat-SettingDataFieldFormat.java" >}}

### **Pivot Tablonun Hızlı Stilini Değiştirme**

Aşağıdaki kod örnekleri, bir pivot tabloya uygulanan hızlı stilin nasıl değiştirileceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ModifyPivotTableQuickStyle-ModifyPivotTableQuickStyle.java" >}}

### **Pivot Alanlarını Temizleme**

[**Özet Alan Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) adlı bir yöntemi var[**açık()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfieldcollection#clear()pivot alanlarını temizler. Sayfa, sütun, satır veya veri gibi tüm alanlardaki pivot alanları temizlemek için kullanın.
Aşağıdaki kod örneği, veri alanındaki tüm pivot alanlarının nasıl temizleneceğini gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ClearPivotFields-ClearPivotFields.java" >}}

## **Konsolidasyon Fonksiyonu**

### **Pivot Tablonun Veri Alanlarına ConsolidationFunction Uygulama**

 Aspose.Cells, pivot tablonun veri alanlarına (veya değer alanlarına) ConsolidationFunction uygulamak için kullanılabilir. Microsoft Excel'de, değer alanına sağ tıklayıp ardından**Değer Alanı Ayarları...** seçeneği ve ardından sekmeyi seçin**Değerleri Şuna Göre Özetle**. Oradan, Toplam, Sayı, Ortalama, Maks, Min, Ürün, Ayrı Sayım vb. gibi istediğiniz herhangi bir BirleştirmeFonksiyonunu seçebilirsiniz.

 Aspose.Cells sağlar[**KonsolidasyonFonksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) aşağıdaki konsolidasyon işlevlerini desteklemek için numaralandırma.

- [**KonsolidasyonFonksiyonu.ORTALAMA**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#AVERAGE)
- [**Konsolidasyonİşlevi.COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT)
- [**Birleştirme İşlevi.COUNT_NUMS**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT_NUMS)
- [**Konsolidasyonİşlevi.DISTINCT_COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#DISTINCT_COUNT)
- [**KonsolidasyonFonksiyonu.MAX**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MAX)
- [**KonsolidasyonFonksiyonu.MIN**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MIN)
- [**KonsolidasyonFonksiyonu.ÜRÜN**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#PRODUCT)
- [**Konsolidasyon İşlevi.STD_DEV**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEV)
- [**KonsolidasyonFonksiyonu.STD_DEVP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD_DEVP)
- [**KonsolidasyonFonksiyonu.SUM**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#SUM)
- [**KonsolidasyonFonksiyonu.VAR**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VAR)
- [**KonsolidasyonFonksiyonu.VARP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VARP)

 Aşağıdaki kod geçerlidir**Ortalama** ilk veri alanına (veya değer alanına) konsolidasyon işlevi ve**Farklı Sayı** ikinci veri alanına (veya değer alanına) konsolidasyon işlevi.

{{% alert color="primary" %}}

DistinctCount konsolidasyon işlevi yalnızca Microsoft Excel 2013 tarafından desteklenir.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ConsolidationFunctions-ConsolidationFunctions.java" >}}
