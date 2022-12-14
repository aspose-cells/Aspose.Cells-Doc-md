---
title: Pivot Tabloyu Biçimlendirme
type: docs
weight: 10
url: /tr/net/formatting-pivot-table/
---
## **Pivot Tablo Görünümü**

Pivot Tablo Nasıl Oluşturulur, basit bir pivot tablonun nasıl oluşturulacağını açıklar. Bu makalede, çeşitli özellikleri ayarlayarak bir pivot tablonun görünümünün nasıl özelleştirileceği açıklanmaktadır:

- Pivot tablo biçimi seçenekleri
- Pivot alanları biçim seçenekleri
- Veri alanı biçim seçenekleri

### **Pivot Tablo Format Seçeneklerini Ayarlama**

 bu[**Pivot tablo**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)class, genel pivot tabloyu kontrol eder ve çeşitli şekillerde biçimlendirilebilir.

#### **Otomatik Biçim Türünü Ayarlama**

Microsoft Excel, bir dizi farklı önceden ayarlanmış rapor formatı sunar. Aspose.Cells, bu biçimlendirme seçeneklerini de destekler. Onlara erişmek için:

1.  Ayarlamak[**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isautoformat) ile**doğru**.
1.  Bir biçimlendirme seçeneği atayın.[**PivotTableAutoFormatType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottableautoformattype)numaralandırma.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingAutoFormat-1.cs" >}}

#### **Biçim Seçeneklerini Ayarlama**

Aşağıdaki kod örneği, pivot tablonun satırlar ve sütunlar için genel toplamları gösterecek şekilde nasıl biçimlendirileceğini ve raporun alan sırasının nasıl ayarlanacağını gösterir. Ayrıca boş değerler için bir müşteri dizesinin nasıl ayarlanacağını da gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingFormatOptions-1.cs" >}}

#### **Görünümü ve Hissi Manuel Olarak Biçimlendirme**

 Pivot tablo raporunun nasıl görüneceğini manuel olarak biçimlendirmek için önceden ayarlanmış rapor formatlarını kullanmak yerine[**PivotTable.Format()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/format) ve[**PivotTable.FormatAll()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/formatall)yöntemler. İstediğiniz biçimlendirme için bir stil nesnesi oluşturun, örneğin:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-FormattingLook-1.cs" >}}

### **Pivot Alan Formatı Seçeneklerini Ayarlama**

 bu[**PivotAlanı**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield)class, bir pivot tablodaki bir alanı temsil eder ve çeşitli şekillerde biçimlendirilebilir. Aşağıdaki kod örneği, nasıl yapılacağını gösterir:

- Satır alanlarına erişin.
- Ara toplamlar ayarlanıyor.
- Otomatik sıralama ayarlanıyor.
- Otomatik gösterme ayarlanıyor.

#### **Satır/Sütun/Sayfa Alanları Biçimini Ayarlama**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingPageFieldFormat-1.cs" >}}

### **Veri alanları biçimini ayarlama**

Aşağıdaki kod örneği, veri alanları için görüntüleme biçimlerinin ve sayı biçiminin nasıl ayarlanacağını gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingDataFieldFormat-1.cs" >}}

### **Pivot Alanlarını Temizleme**

 bu[**Özet Alan Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) adlı bir yöntemi var[**Temizlemek()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection/methods/clear)bu, pivot alanlarını temizlemenizi sağlar. Sayfa, sütun, satır veya veri gibi alanlardaki tüm pivot alanları temizlemek istediğinizde kullanın.
Aşağıdaki kod örneği, bir veri alanındaki tüm pivot alanlarının nasıl temizleneceğini gösterir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ClearPivotFields-1.cs" >}}
