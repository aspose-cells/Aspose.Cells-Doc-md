---
title: Pivot Tablo Şeritlerini Devre Dışı Bırak
type: docs
weight: 90
url: /tr/net/disable-pivot-table-ribbons/
---

{{% alert color="primary" %}}

Pivot tablo tabanlı raporlar faydalıdır ancak hedef kullanıcıların bu raporları yapılandırmak için Excel hakkında detaylı bilgiye sahip olmamaları durumunda hata yapmaya müsaittir. Bu durumlarda, organizasyonlar kullanıcıların bu raporları değiştirmesini sınırlamak isteyeceklerdir. Ek filtreler, dilimleyiciler, alanlar eklemenin yanı sıra raporda belirli şeylerin sırasını değiştirmek gibi yaygın pivot tablo özelliklerinin çoğu her kullanıcı için önerilmez. Diğer taraftan, bu kullanıcılar raporu tazeleyebilmeli ve var olan filtreleri veya dilimleyicileri kullanabilmelidir. Aspose.Cells, bu raporları oluştururken kullanıcıların bu raporları değiştirmesini sınırlama yeteneği sağlamıştır. Bu amaçla, Excel, pivot tablo şeridini devre dışı bırakma özelliği sağlar ve aynısı Aspose.Cells tarafından sağlanır, yani geliştirici, bu raporları değiştirmek için kullanılan şeridi devre dışı bırakabilir.

{{% /alert %}}

## **PivotTable.EnableWizard Kullanarak Pivot Tablo Şeridini Devre Dışı Bırakma**

Aşağıdaki kod, bir sayfadan pivot tablosuna erişerek [**EnableWizard**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/properties/enablewizard) değeri **false** olarak ayarlar ve bu özelliği gösterir. Örnek pivot tablo dosyasını bu [bağlantıdan](pivot_table_test.xlsx) indirebilirsiniz.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-DisablePivotTableRibbon.cs" >}}
{{< app/cells/assistant language="csharp" >}}
