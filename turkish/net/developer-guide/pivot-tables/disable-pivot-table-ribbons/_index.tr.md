---
title: Pivot Tablo Şeritlerini Devre Dışı Bırak
type: docs
weight: 90
url: /tr/net/disable-pivot-table-ribbons/
---
{{% alert color="primary" %}}

Pivot tablo tabanlı raporlar kullanışlıdır ancak hedef kullanıcıların bu raporları yapılandırmak için ayrıntılı Excel bilgisine sahip olmaması durumunda hataya açıktır. Bu koşullarda kuruluşlar, kullanıcıların pivot tablo tabanlı bir raporu değiştirebilmelerini kısıtlamak isteyecektir. Ek filtreler, dilimleyiciler, alanlar eklemek veya rapordaki belirli şeylerin sırasını değiştirmek gibi yaygın pivot tablo özellikleri çoğunlukla her kullanıcı için önerilmez. Öte yandan, bu kullanıcılar aynı zamanda raporu yenileyebilecek ve mevcut filtreleri veya dilimleyicileri kullanabilecektir. Aspose.Cells, kullanıcıların bu raporları oluştururken bu raporları değiştirmesini kısıtlamak için geliştiricilere bu yeteneği sağlamıştır. Bu amaçla Excel, pivot tablo şeridini devre dışı bırakmak için bir özellik sağlar ve aynısı Aspose.Cells tarafından sağlanır, yani geliştirici, bu raporları değiştirmek için kontroller içeren şeridi devre dışı bırakabilir.

{{% /alert %}}

## **PivotTable.EnableWizard'ı kullanarak Pivot Tablo Şeridi'ni devre dışı bırakın**

Aşağıdaki kod, bir sayfadan bir pivot tabloya erişerek ve ardından ayarlayarak bu özelliği gösterir.[**Etkinleştirme Sihirbazı**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/enablewizard) ile**yanlış** . Örnek pivot tablo dosyası buradan indirilebilir[bağlantı](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-DisablePivotTableRibbon.cs" >}}
