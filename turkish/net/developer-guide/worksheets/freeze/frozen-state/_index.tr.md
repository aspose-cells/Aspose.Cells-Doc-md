---
title: Frozen State'i Excel olmadan nasıl kontrol edebilirim?
linktitle: Dondurulmuş Durum
type: docs
weight: 190
url: /tr/net/how-to-check-frozen-state-of-excel-worksheet
description: Bu makalede, .NET API ile C# Kütüphanesini kullanarak excel çalışma sayfasının dondurulmuş durumunu programlı olarak nasıl kontrol edeceğinizi öğreneceksiniz.
---
{{% alert color="primary" %}}

Bu yazıda excel çalışma sayfasının dondurulmuş durumunu programlı olarak nasıl kontrol edeceğinizi öğreneceğiz.
MS Excel'de çalışma sayfasının dondurulmuş mu yoksa bölünmüş mü olduğunu kolayca bulabiliriz. Ancak CSharp ile dondurulmuş mu yoksa bölünmüş mü olduğunu bulmanın bir yolu var mı?
Bunu .Net için Aspose.Cells ile kolayca yapabiliriz.
{{% /alert %}}

##  **Pencere Bölmeleri Donmuş mu?**
.Net için Aspose.Cells ile pencerenin donup donmadığını, kaç satır ve sütunun kilitli olduğunu kontrol edebiliriz.

 Lütfen şunu kullanın:[**Çalışma Sayfası.PaneState**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/PaneState/) pencere bölmelerinin durumunu kontrol etme özelliği
 ve kilitli satır ve sütunları alır[**Çalışma Sayfası.GetFreezedPanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFreezedPanes/)yöntem.
1. Dosyayı açmak için Çalışma Kitabı oluşturun.
2. Çalışma sayfasının donmuş olup olmadığını kontrol edin.
3. Kilitli satır ve sütunları alır

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Is-Worksheet-Frozen.cs" >}}