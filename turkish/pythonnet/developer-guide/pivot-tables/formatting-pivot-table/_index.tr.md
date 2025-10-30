---
title: Pivot Tablosunu Biçimlendirme
type: docs
weight: 10
url: /tr/python-net/formatting-pivot-table/
description: Aspose.Cells for Python via .NET ile pivot tablosu nasıl biçimlendirilir.
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

Microsoft Excel, birkaç farklı önceden belirlenmiş rapor biçimi sunar. Aspose.Cells ile Python için via .NET bu biçimlendirme seçeneklerini destekler. Bunlara erişmek için:

1. [**PivotTable.is_auto_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_auto_format/) değerini **true** olarak ayarlayın.
1. [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottableautoformattype/) numaralandırmasından bir biçimlendirme seçeneği atayın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingAutoFormat-1.py" >}}

#### **Biçim Seçeneklerini Ayarlama**

Biçim Seçeneklerini Ayarlama

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingFormatOptions-1.py" >}}

#### **Aşağıdaki kod örneği, pivot tablosunu satır ve sütunlar için toplamları göstermek üzere biçimlendirme ve raporun alan sırasını ayarlamayı gösterir. Ayrıca, null değerler için özel bir dize ayarlamak da gösterilir.**

Önceden belirlenmiş rapor biçimleri yerine, pivot tablo raporunun nasıl görüneceğini manuel olarak düzenlemek için [**PivotTable.format_all(style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format_all/) ve [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format/) yöntemlerini kullanın. İstenen biçimlendirme için bir stil nesnesi oluşturun.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FormattingLook-1.py" >}}

### **Pivot Alanı Biçim Seçeneklerini Ayarlama**

Pivot Alanı Biçim Seçeneklerini Ayarlama

- Satır alanlarına erişim.
- Alt toplamları ayarlama.
- Otomatik sıralamayı ayarlama.
- Otomatik gösterimi ayarlama.

#### **Satır/Sütun/Sayfa Alan Biçimini Nasıl Ayarlanır**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingPageFieldFormat-1.py" >}}

### **Veri alanı biçimini nasıl ayarlanır**

Aşağıdaki kod örneği, veri alanları için görüntü biçimlerini ve sayı biçimini ayarlamayı göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingDataFieldFormat-1.py" >}}

### **Pivot Alanlarını Temizleme Yöntemi**

[**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/), örneğin sayfa, sütun, satır veya veri gibi tüm pivot alanlarını temizlemenize izin veren [**clear()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/clear/#) adında bir yönteme sahiptir. Örneğin, tüm veri alanlarını temizlemek istediğinizde, bunu kullanın.
Aşağıdaki kod örneği, bir veri alanındaki tüm pivot alanlarını temizlemeyi göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ClearPivotFields-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
