---
title: Pivot Tablo Şeritlerini Devre Dışı Bırak
type: docs
weight: 40
url: /tr/java/disable-pivot-table-ribbons/
---
{{% alert color="primary" %}}

Pivot tablo tabanlı raporlar kullanışlıdır ancak hedef kullanıcıların bu raporları yapılandırmak için ayrıntılı Excel bilgisine sahip olmaması durumunda hataya açıktır. Bu koşullarda kuruluşlar, kullanıcıların pivot tablo tabanlı bir raporu değiştirebilmelerini kısıtlamak isteyecektir. Ek filtreler, dilimleyiciler, alanlar eklemek veya rapordaki belirli şeylerin sırasını değiştirmek gibi yaygın pivot tablo özellikleri çoğunlukla her kullanıcı için önerilmez. Öte yandan, bu kullanıcılar aynı zamanda raporu yenileyebilecek ve mevcut filtreleri veya dilimleyicileri kullanabilecektir. Aspose.Cells, kullanıcıların bu raporları oluştururken bu raporları değiştirmesini kısıtlamak için geliştiricilere bu yeteneği sağlamıştır. Bu amaçla Excel, pivot tablo şeridini devre dışı bırakmak için bir özellik sağlar ve aynısı Aspose.Cells tarafından sağlanır, yani geliştirici, bu raporları değiştirmek için kontroller içeren şeridi devre dışı bırakabilir.

{{% /alert %}}

## **PivotTable.setEnableWizard'ı kullanarak Pivot Tablo Şeridi'ni devre dışı bırakın**

Aşağıdaki kod, bir sayfadan bir pivot tabloya erişerek ve ardından[**setEnableWizard**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#EnableWizard) bu bayrağı ayarlamak için**yanlış** . Örnek pivot tablo dosyası buradan indirilebilir[bağlantı](71630876.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-DisablePivotTableRibbon-1.java" >}}
