---
title: Pivot Tabloyu Biçimlendirme
type: docs
weight: 10
url: /tr/net/formatting-pivot-table/
description: Aspose.Cells for Python via .NET ile pivot tablo nasıl formatlanır?
keywords: Format pivot table.
---
##  **Pivot Tablo Görünümü**

Pivot Tablo Nasıl Oluşturulur, basit bir pivot tablonun nasıl oluşturulacağını açıklar. Bu makalede, çeşitli özellikleri ayarlayarak bir pivot tablonun görünümünün nasıl özelleştirileceği açıklanmaktadır:

- Pivot tablo formatı seçenekleri
- Pivot alanları format seçenekleri
- Veri alanı formatı seçenekleri

###  **Pivot Tablo Formatı Seçeneklerini Ayarlama**

[**Pivot tablo**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)class genel pivot tabloyu kontrol eder ve çeşitli şekillerde biçimlendirilebilir.

####  **Otomatik Format Türünü Ayarlama**

Microsoft Excel bir dizi farklı önceden ayarlanmış rapor formatı sunar. Aspose.Cells for Python via .NET de bu biçimlendirme seçeneklerini destekliyor. Onlara erişmek için:

1.  Ayarlamak[**PivotTable.is_auto_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/is_auto_format/)*doğruya**.
1.  Bir biçimlendirme seçeneği atayın[**PivotTableOtomatikFormatTürü**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottableautoformattype/)numaralandırma.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingAutoFormat-1.py" >}}

####  **Format Seçeneklerini Ayarlama**

Aşağıdaki kod örneği, pivot tablonun satırlar ve sütunlar için genel toplamları gösterecek şekilde nasıl biçimlendirileceğini ve raporun alan sırasının nasıl ayarlanacağını gösterir. Ayrıca boş değerler için müşteri dizesinin nasıl ayarlanacağını da gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingFormatOptions-1.py" >}}

####  **Görünüm ve Hissi Manuel Olarak Biçimlendirme**

Pivot tablo raporunun manuel olarak nasıl görüneceğini biçimlendirmek için önceden ayarlanmış rapor formatlarını kullanmak yerine[**PivotTable.format_all(stil)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format_all/) Ve[**PivotTable.format(satır, sütun, stil)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/format/)yöntemler. İstediğiniz biçimlendirme için bir stil nesnesi oluşturun, örneğin:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-FormattingLook-1.py" >}}

###  **Pivot Alanı Formatı Seçeneklerini Ayarlama**

[**Pivot Alanı**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/)sınıf, pivot tablodaki bir alanı temsil eder ve çeşitli şekillerde biçimlendirilebilir. Aşağıdaki kod örneği aşağıdakilerin nasıl yapılacağını gösterir:

- Satır alanlarına erişin.
- Alt toplamları ayarlama.
- Otomatik sıralamayı ayarlama.
- Otomatik gösteriyi ayarlama.

####  **Satır/Sütun/Sayfa Alanları Formatını Ayarlama**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingPageFieldFormat-1.py" >}}

###  **Veri alanları formatını ayarlama**

Aşağıdaki kod örneği, veri alanları için görüntüleme biçimlerinin ve sayı biçiminin nasıl ayarlanacağını gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-SettingDataFieldFormat-1.py" >}}

###  **Pivot Alanlarını Temizleme**

[**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/) adında bir yöntem var[**clear()**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection/clear/#)Bu, pivot alanlarını temizlemenizi sağlar. Sayfa, sütun, satır veya veri gibi alanlardaki tüm pivot alanlarını temizlemek istediğinizde bunu kullanın.
Aşağıdaki kod örneği, bir veri alanındaki tüm pivot alanların nasıl temizleneceğini gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ClearPivotFields-1.py" >}}
