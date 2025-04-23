---
title: Pivot Tablosunu Biçimlendirme
type: docs
weight: 10
url: /tr/net/formatting-pivot-table/
---

## **Döndürme Tablosu Görünümü**

Bir Pivot Tablosu Nasıl Oluşturulur, basit bir pivot tablosu nasıl oluşturulurun açıklanmasının yanı sıra bu makale, çeşitli özellikleri ayarlayarak bir pivot tablosunun görünümünü özelleştirmeyi açıklar:

- Pivot tablo format seçenekleri
- Pivot alanları format seçenekleri
- Veri alanı format seçenekleri

### **Döndürme Tablosu Biçim Seçeneklerini Ayarlama**

Toplam Otomatik Biçim Türünü Ayarlama

#### **Microsoft Excel, birkaç farklı önceden ayarlanmış rapor formatı sunar. Aspose.Cells, bu formatlama seçeneklerini de destekler. Bunlara erişmek için:**

1. {0} değeri **true** olarak ayarlayın.

1. [**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/isautoformat) değerini **true** olarak ayarlayın.
1. [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottableautoformattype) numaralandırmasından bir biçimlendirme seçeneği atayın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingAutoFormat-1.cs" >}}

#### **Biçim Seçeneklerini Ayarlama**

Biçim Seçeneklerini Ayarlama

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingFormatOptions-1.cs" >}}

#### **Aşağıdaki kod örneği, pivot tablosunu satır ve sütunlar için toplamları göstermek üzere biçimlendirme ve raporun alan sırasını ayarlamayı gösterir. Ayrıca, null değerler için özel bir dize ayarlamak da gösterilir.**

Görünümü Manuel Olarak Ayarlama

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-FormattingLook-1.cs" >}}

### **Pivot Tablo Raporunun nasıl göründüğü ile ilgili nasıl biçimlendirileceğiniz, önceden ayarlanmış rapor formatlarını değil, {0} ve {1} yöntemlerini kullanarak el ile ayarlamak için kullanılır. İstenen biçimlendirme için bir stil nesnesi oluşturun, örneğin:**

Pivot Alanı Biçim Seçeneklerini Ayarlama

- Satır alanlarına erişim.
- Alt toplamları ayarlama.
- Otomatik sıralamayı ayarlama.
- Otomatik gösterimi ayarlama.

#### **Satır/Sütun/Sayfa Alanları Biçimi Ayarlama**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingPageFieldFormat-1.cs" >}}

### **Veri alanları biçimini ayarlama**

Aşağıdaki kod örneği, veri alanları için görüntü biçimlerini ve sayı biçimini ayarlamayı göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-SettingDataFieldFormat-1.cs" >}}

### **Pivot Alanlarını Temizleme**

[**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection), örneğin sayfa, sütun, satır veya veri gibi tüm pivot alanlarını temizlemenize izin veren [**Clear()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection/methods/clear) adında bir yönteme sahiptir. Örneğin, tüm veri alanlarını temizlemek istediğinizde, bunu kullanın.
Aşağıdaki kod örneği, bir veri alanındaki tüm pivot alanlarını temizlemeyi göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ClearPivotFields-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
