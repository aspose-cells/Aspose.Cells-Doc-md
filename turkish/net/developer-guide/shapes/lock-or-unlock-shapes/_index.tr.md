---
title: Şekilleri kilitle veya kilidi aç
linktitle: Şekilleri kilitle veya kilidi aç
type: docs
weight: 200
url: /tr/net/lock-or-unlock-shapes/
description: Bu makale, Aspose.Cells kütüphanesini kullanarak şekilleri korumak için kilitleme veya kilidini açma kodunu açıklayan bir kod sunar.
keywords: C# Kilit Şekillerini Korumak, C# da Şekilleri Kilitlemek veya kilidini açmak, C# da şekilleri korumak için Kilitlemek veya kilidini açmak.
---

## **Olası Kullanım Senaryoları**

Bazı durumlarda, istenmeyen durumlar tarafından yok edilmekten korumak için belirli çalışma sayfalarındaki tüm şekilleri korumanız gerekebilir. Bu durumda, belirtilen çalışma sayfasındaki tüm şekilleri kilitlemeniz gerekir. 

Bir elektronik tablo veya belgedeki şekillerin kilidini açmak birkaç nedenle faydalı olabilir:
1. Kazara Değişiklikleri Önleme: Şekillerin kilidini açmak, kullanıcıların onları kazara hareket ettirmelerini, yeniden boyutlandırmalarını veya silmelerini önler. Bu, şekillerin özellikle açıklamalar, illüstrasyonlar veya belgenin tasarımının bir parçası olarak kullanıldığı karmaşık belgelerde önemlidir.
1. Şablonu ve Tasarımı Koruma: Şekiller belgenin düzeni ve görsel tasarımında genellikle kritik bir role sahiptir. Onları kilitlemek, belgenin planlanan görünümünü korur, belgenin profesyonel ve görsel olarak çekici kalmasını sağlar.
1. Veri Bütünlüğü: Tablolarda, şekiller önemli veri noktalarını vurgulamak, yorum eklemek veya görsel açıklamalar sağlamak için kullanılabilir. Bu şekillerin kilidini açmak, sağladıkları bağlamsal bilgilerin doğru ve sağlam kalmasını sağlar.
1. Paylaşılan Belgelerde Tutarlılık: Belgeler üzerinde işbirliği yaparken, farklı kullanıcılar farklı seviyelerde uzmanlığa sahip olabilir. Şekillerin kilidini açarak belgenin farklı bölgelerinin yanlışlıkla değiştirilmesini önleyerek, belgedeki tutarlılığı korumaya yardımcı olur.
1. Güvenlik: Hassas belgelerde şekillerin kilidini açmak, bilgiyi korumak için daha geniş bir stratejinin bir parçası olabilir. Örneğin, finansal raporlar veya yasal belgelerde, kilitli şekiller özel açıklamaları veya kritik bağlamı sağlayan vurguları korumak için kullanılabilir.

Bazı durumlarda, belirli korunan çalışma kitaplarındaki belirli şekilleri değiştirebilmek isteyebilirsiniz, bu durumda, bu şekillerin kilidini açmanız gerekir. Bu makale, belirli şekilleri nasıl kilitleyip kilidini açacağınızı detaylı olarak tanıtacaktır.

## **Excel'de şekilleri korumak için nasıl kilitlenir**

Microsoft Excel'de hücreleri kitlemenin yolları şunlardır:

1. Excel Dosyanızı Açın: Kilidini açmak istediğiniz şekilleri içeren Excel dosyasını açın.

1. Şekli Seçin: Kilidini açmak istediğiniz şekle tıklayın. Her bir şekle Ctrl tuşuna basılı tutarak ve her bir şekle tıklayarak birden fazla şekli seçebilirsiniz.

1. Format Şekli Bölmesini Açın: Seçili şekillerin üzerine sağ tıklayın ve "Boyut ve Özellikler" seçeneğini seçin. Alternatif olarak, Şerit'te "Biçim" sekmesine gidin ve "Boyut" grubunda, "Biçim Şekli" bölmesini açmak için bir diyalog açıcı (küçük ok) tıklayın.
1. Şekli Kilitleyin: "Biçim Şekli" bölmesinde, "Boyut ve Özellikler" sekmesine gidin (simge oklarla donatılmış bir kareye benzer). "Özellikler" bölümünde, "Kilitli" için kutuyu işaretleyin.
<br>
<img src="1.png" width=60% />
1. Sayfayı Koruyun: Menü Şeridindeki "İnceleme" sekmesine gidin. "Sayfayı Koru" seçeneğine tıklayın. Bir şifre belirleyin (isteğe bağlı) ve izin vermek istediğiniz izinleri seçin (örneğin, kilitli hücreleri seçme, hücreleri biçimlendirme vb.). "Tamam" a tıklayın.
<br>
<img src="2.png" width=60% />

## **Belirli bir çalışma sayfasındaki tüm şekilleri nasıl kilitleyebilirsiniz**

Belirli bir çalışma sayfasındaki tüm şekilleri korumak için [Worksheet.Protect( ProtectionType.Objects)](https://reference.aspose.com/cells/net/aspose.cells/worksheet/protect/#protect) yöntemini kullanın, aşağıdaki örnek kodda gösterildiği gibi.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-1.cs" >}}

## **Korumalı bir çalışma sayfasında belirli şekillerin nasıl kilidini açacağınızı**

Korunan bir çalışma sayfasındaki belirli bir şeklin kilidini açmak için [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/) özelliğini kullanın, aşağıdaki örnek kodda gösterildiği gibi.

Not: [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/) özelliği, çalışma sayfası korunduğunda anlamlıdır.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-2.cs" >}}

