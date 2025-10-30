---
title: Golang ile C++ aracılığıyla Pivot Tablo Şeritlerini devre dışı bırakma
linktitle: Pivot Tablo Şeritlerini Devre Dışı Bırak
type: docs
weight: 90
url: /tr/go-cpp/disable-pivot-table-ribbons/
description: Aspose.Cells for C++ kullanarak Excel dosyalarında pivot tablo şeritlerini nasıl devre dışı bırakacağınızı öğrenin.
---

{{% alert color="primary" %}}

Pivot tablo tabanlı raporlar kullanışlıdır ancak hedef kullanıcılar bu raporları yapılandırmak için Excel hakkında detaylı bilgiye sahip olmadığında hata yapmaya yatkındır. Bu durumda, kuruluşlar kullanıcıların pivot tablo tabanlı raporları değiştirmesini engellemek isteyebilir. Ek filtreler, dilimler, alanlar eklemek veya rapordaki bazı sıralamaları değiştirmek gibi yaygın özellikler genellikle tüm kullanıcılar için önerilmez. Öte yandan, bu kullanıcılar da raporu yenileme ve mevcut filtreleri veya dilimleri kullanma yetisine sahip olmalıdır. Aspose.Cells, bu raporları değiştirmenin engellenmesi için geliştiricilere bu yeteneği sağlar. Bu amaçla, Excel pivot tablo şeridini devre dışı bırakma özelliği sunar ve bu özellik Aspose.Cells tarafından da sağlanmıştır. Geliştiriciler, bu raporları değiştirme kontrollerini içeren şeridi devre dışı bırakabilir.

{{% /alert %}}

## **PivotTable.EnableWizard Kullanarak Pivot Tablo Şeridini Devre Dışı Bırakma**

Aşağıdaki kod, bir sayfadan pivot tabloya erişerek [**GetEnableWizard()**](https://reference.aspose.com/cells/go-cpp/pivottable/getenablewizard/) değerini **false** yapar. Bir örnek pivot tablo dosyasını buradan indirebilirsiniz: [bağlantı](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisablePivotTableRibbons.go" >}}
