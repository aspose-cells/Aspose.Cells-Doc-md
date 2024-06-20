---
title: Pivot Tablo Şeritlerini Devre Dışı Bırak
type: docs
weight: 40
url: /tr/java/disable-pivot-table-ribbons/
---

{{% alert color="primary" %}}

Pivot tablo tabanlı raporlar faydalıdır ancak hedef kullanıcıların bu raporları yapılandırmak için Excel hakkında detaylı bilgiye sahip olmamaları durumunda hata yapmaya müsaittir. Bu durumlarda, organizasyonlar kullanıcıların bu raporları değiştirmesini sınırlamak isteyeceklerdir. Ek filtreler, dilimleyiciler, alanlar eklemenin yanı sıra raporda belirli şeylerin sırasını değiştirmek gibi yaygın pivot tablo özelliklerinin çoğu her kullanıcı için önerilmez. Diğer taraftan, bu kullanıcılar raporu tazeleyebilmeli ve var olan filtreleri veya dilimleyicileri kullanabilmelidir. Aspose.Cells, bu raporları oluştururken kullanıcıların bu raporları değiştirmesini sınırlama yeteneği sağlamıştır. Bu amaçla, Excel, pivot tablo şeridini devre dışı bırakma özelliği sağlar ve aynısı Aspose.Cells tarafından sağlanır, yani geliştirici, bu raporları değiştirmek için kullanılan şeridi devre dışı bırakabilir.

{{% /alert %}}

## **PivotTable.setEnableWizard ile Pivot Tablo Şeridini Devre Dışı Bırakma**

Aşağıdaki kod, bir sayfadan pivot tablosuna erişerek ve [**setEnableWizard**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#EnableWizard) çağrarak bu bayrağı **false** olarak ayarlayarak bu özelliği gösterir. Örnek pivot tablo dosyası bu [bağlantıdan](71630876.xlsx) indirilebilir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-DisablePivotTableRibbon-1.java" >}}
