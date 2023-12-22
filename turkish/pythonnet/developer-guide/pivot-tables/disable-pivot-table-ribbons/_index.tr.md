---
title: Pivot Tablo Şeritlerini Devre Dışı Bırak
type: docs
weight: 90
url: /tr/python-net/disable-pivot-table-ribbons/
description: Aspose.Cells for Python via .NET ile Pivot Tablo Şeritleri nasıl devre dışı bırakılır.
keywords: Disable Pivot Table Ribbons.
---
{{% alert color="primary" %}}

Pivot tablo tabanlı raporlar faydalıdır ancak hedef kullanıcıların bu raporları yapılandırmak için ayrıntılı Excel bilgisine sahip olmaması durumunda hata yapma olasılığı yüksektir. Bu durumlarda kuruluşlar, kullanıcıların pivot tablo tabanlı bir raporu değiştirebilmesini kısıtlamak isteyecektir. Ek filtreler, dilimleyiciler, alanlar eklemek veya rapordaki belirli şeylerin sırasını değiştirmek gibi yaygın pivot tablo özellikleri çoğunlukla her kullanıcı için önerilmez. Öte yandan bu kullanıcılar raporu yenileyebilecek ve mevcut filtreleri veya dilimleyicileri de kullanabilecektir. Aspose.Cells for Python via .NET, kullanıcıların bu raporları oluştururken değiştirmelerini kısıtlamak için geliştiricilere bu yeteneği sağlamıştır. Bu amaçla Excel, pivot tablo şeridini devre dışı bırakma özelliği sağlar ve aynı şey Aspose.Cells for Python via .NET tarafından da sağlanır; yani geliştirici, bu raporları değiştirmek için kontrolleri içeren şeridi devre dışı bırakabilir.

{{% /alert %}}

##  **PivotTable.EnableWizard'ı kullanarak Pivot Table Şeridi'ni devre dışı bırakın**

 Aşağıdaki kod, bir sayfadan bir pivot tabloya erişerek ve ardından ayarları yaparak bu özelliği göstermektedir.[**etkinleştirme_sihirbazı**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/enable_wizard/) *yanlış** olarak. Örnek pivot tablo dosyası buradan indirilebilir[bağlantı](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-DisablePivotTableRibbon.py" >}}
