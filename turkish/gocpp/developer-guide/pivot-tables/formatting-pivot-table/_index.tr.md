---
title: Golang ile C++ aracılığıyla Pivot Tabloyu biçimlendirme
linktitle: Pivot Tablosunu Biçimlendirme
type: docs
weight: 10
url: /tr/go-cpp/formatting-pivot-table/
description: Pivot tablolarının görünümünü nasıl özelleştireceğinizi Aspose.Cells for C++ ile öğrenin.
---

## **Döndürme Tablosu Görünümü**

Bir Pivot Tablosu Nasıl Oluşturulur, basit bir pivot tablosu nasıl oluşturulurun açıklanmasının yanı sıra bu makale, çeşitli özellikleri ayarlayarak bir pivot tablosunun görünümünü özelleştirmeyi açıklar:

- Pivot tablo format seçenekleri
- Pivot alanları format seçenekleri
- Veri alanı format seçenekleri

### **Döndürme Tablosu Biçim Seçeneklerini Ayarlama**

Toplam Otomatik Biçim Türünü Ayarlama

#### **Microsoft Excel, birkaç farklı önceden ayarlanmış rapor formatı sunar. Aspose.Cells, bu formatlama seçeneklerini de destekler. Bunlara erişmek için:**

Microsoft Excel çeşitli ön ayarlı rapor formatları sunar. Aspose.Cells bu biçimlendirme seçeneklerini de destekler. Onlara erişmek için:

1. [**PivotTable.IsAutoFormat**](https://reference.aspose.com/cells/go-cpp/pivottable/isautoformat/) değerini **true** olarak ayarlayın.
1. [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/go-cpp/pivottableautoformattype/) numaralandırmasından bir biçimlendirme seçeneği atayın.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable.go" >}}
#### **Biçim Seçeneklerini Ayarlama**

Aşağıdaki kod örneği, satır ve sütunlar için genel toplamları gösteren ve raporun alan sırasını ayarlayan biçimlendirmeyi gösterir. Ayrıca, boş değerler için özel bir dize ayarlamayı da gösterir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-1.go" >}}
#### **Aşağıdaki kod örneği, pivot tablosunu satır ve sütunlar için toplamları göstermek üzere biçimlendirme ve raporun alan sırasını ayarlamayı gösterir. Ayrıca, null değerler için özel bir dize ayarlamak da gösterilir.**

Pivot tablo raporunun görünümünü manuel olarak biçimlendirmek için, ön ayarlı rapor biçimleri yerine, [**PivotTable.Format()**](https://reference.aspose.com/cells/go-cpp/pivottable/format_pivotarea_style/) ve [**PivotTable.FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) yöntemlerini kullanın. İstediğiniz biçimlendirme için bir stil nesnesi oluşturun, örneğin:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-2.go" >}}
### **Pivot Tablo Raporunun nasıl göründüğü ile ilgili nasıl biçimlendirileceğiniz, önceden ayarlanmış rapor formatlarını değil, {0} ve {1} yöntemlerini kullanarak el ile ayarlamak için kullanılır. İstenen biçimlendirme için bir stil nesnesi oluşturun, örneğin:**

Pivot Alanı Biçim Seçeneklerini Ayarlama

- Satır alanlarına erişim.
- Alt toplamları ayarlama.
- Otomatik sıralamayı ayarlama.
- Otomatik gösterimi ayarlama.

#### **Satır/Sütun/Sayfa Alanları Biçimi Ayarlama**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-3.go" >}}
### **Veri Alanları Biçimini Ayarlama**

Aşağıdaki kod örneği, veri alanları için görüntü biçimlerini ve sayı biçimini ayarlamayı göstermektedir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-4.go" >}}
### **Pivot Alanlarını Temizleme**

[**PivotFieldCollection**](https://reference.aspose.com/cells/go-cpp/pivotfieldcollection/), örneğin sayfa, sütun, satır veya veri gibi tüm pivot alanlarını temizlemenize izin veren [**Clear()**](https://reference.aspose.com/cells/go-cpp/pivotfieldcollection/clear/) adında bir yönteme sahiptir. Örneğin, tüm veri alanlarını temizlemek istediğinizde, bunu kullanın.
Aşağıdaki kod örneği, bir veri alanındaki tüm pivot alanlarını temizlemeyi göstermektedir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormattingPivotTable-5.go" >}}
