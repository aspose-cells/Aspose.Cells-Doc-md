---
title: Pivot Tablosunu Biçimlendirme
type: docs
weight: 10
url: /tr/nodejs-cpp/formatting-pivot-table/
description: Aspose.Cells for Node.js via C++ ile pivot tabloyu biçimlendirme nasıl yapılır.
keywords: Pivot Tablo Biçimlendirme.
---

## **Döndürme Tablosu Görünümü**

Bir Pivot Tablosu Nasıl Oluşturulur, basit bir pivot tablosu nasıl oluşturulurun açıklanmasının yanı sıra bu makale, çeşitli özellikleri ayarlayarak bir pivot tablosunun görünümünü özelleştirmeyi açıklar:

- Pivot tablo format seçenekleri
- Pivot alanları format seçenekleri
- Veri alanı format seçenekleri

### **Pivot Tablo Format Seçeneklerini Ayarlama**

Toplam Otomatik Biçim Türünü Ayarlama

#### **Otomatik Biçim Türünün Ayarlanması**

Microsoft Excel çeşitli önceden ayarlanmış rapor formatları sunar. Aspose.Cells for Node.js via C++ bu biçimlendirme seçeneklerini de destekler. Bu seçeneklere erişmek için:

1. [**PivotTable.setIsAutoFormat(value)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsAutoFormat-boolean-) değerini **true** olarak ayarlayın.
1. [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/nodejs-cpp/pivottableautoformattype/) numaralandırmasından bir biçimlendirme seçeneği atayın.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingAutoFormat-1.js" >}}

#### **Biçim Seçeneklerini Ayarlama**

Biçim Seçeneklerini Ayarlama

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingFormatOptions-1.js" >}}

#### **Aşağıdaki kod örneği, pivot tablosunu satır ve sütunlar için toplamları göstermek üzere biçimlendirme ve raporun alan sırasını ayarlamayı gösterir. Ayrıca, null değerler için özel bir dize ayarlamak da gösterilir.**

Önceden belirlenmiş rapor biçimleri yerine, pivot tablo raporunun nasıl görüneceğini manuel olarak düzenlemek için [**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#formatAll-style-) ve [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#format-number-number-style-) yöntemlerini kullanın. İstenen biçimlendirme için bir stil nesnesi oluşturun.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-FormattingLook-1.js" >}}

### **Pivot Alanı Biçim Seçeneklerini Ayarlama**

Pivot Alanı Biçim Seçeneklerini Ayarlama

- Satır alanlarına erişim.
- Alt toplamları ayarlama.
- Otomatik sıralamayı ayarlama.
- Otomatik gösterimi ayarlama.

#### **Satır/Sütun/Sayfa Alan Biçimini Nasıl Ayarlanır**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingPageFieldFormat-1.js" >}}

### **Veri alanı biçimini nasıl ayarlanır**

Aşağıdaki kod örneği, veri alanları için görüntü biçimlerini ve sayı biçimini ayarlamayı göstermektedir.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SettingDataFieldFormat-1.js" >}}

### **Pivot Alanlarını Temizleme Yöntemi**

[**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection/), örneğin sayfa, sütun, satır veya veri gibi tüm pivot alanlarını temizlemenize izin veren [**clear()**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection/#clear--) adında bir yönteme sahiptir. Örneğin, tüm veri alanlarını temizlemek istediğinizde, bunu kullanın.
Aşağıdaki kod örneği, bir veri alanındaki tüm pivot alanlarını temizlemeyi göstermektedir.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-ClearPivotFields-1.js" >}}
