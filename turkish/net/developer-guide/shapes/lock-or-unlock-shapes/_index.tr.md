---
title: Şekilleri kilitle veya kilidi aç
linktitle: Şekilleri kilitle veya kilidi aç
type: docs
weight: 200
url: /tr/net/lock-or-unlock-shapes/
description: Bu makale, Aspose.Cells kütüphanesi kullanılarak şekilleri kilitleme veya kilidini açma konusunda kodlar içermektedir.
keywords: C# ile şekilleri kilitleyerek koruma, C# kullanarak şekilleri nasıl kilitleyeceğinizi veya açacağınızı anlatıyor, şekilleri kilitleme veya açma yöntemleri.
---

## **Olası Kullanım Senaryoları**

Bazı durumlarda, istenmeyen durumlar tarafından yok edilmekten korumak için belirli çalışma sayfalarındaki tüm şekilleri korumanız gerekebilir. Bu durumda, belirtilen çalışma sayfasındaki tüm şekilleri kilitlemeniz gerekir. 

Bir elektronik tabloda veya dokümanda şekillerin kilitlenmesi çeşitli nedenlerle faydalı olabilir:
1. Kazara Değişiklikleri Önleme: Şekilleri kilitlemek, kullanıcıların bunları kazara taşımalarını, yeniden boyutlandırmalarını veya silmelerini engeller. Bu, şekillerin açıklama, çizim veya dokümanın tasarımının bir parçası olarak kullanıldığı karmaşık belgelerde özellikle önemlidir.
1. Düzeni ve Tasarımı Koru: Şekiller genellikle bir belgenin düzeninde ve görsel tasarımında önemli rol oynar. Bunları kilitlemek, istenen görünümü koruyarak, belgenin profesyonel ve görsel olarak çekici kalmasını sağlar.
1. Veri Bütünlüğü: Elektronik tablolarda, şekiller önemli veri noktalarını vurgulamak, yorum eklemek veya görsel açıklamalar yapmak için kullanılabilir. Bu şekillerin kilitlenmesi, sağladıkları bağlamsal bilginin doğru ve bütün kalmasını sağlar.
1. Paylaşılan Belgelerde Tutarlılık: Birlikte çalışırken, farklı kullanıcıların uzmanlık seviyeleri farklı olabilir. Şekillerin kilitlenmesi, beklenmedik değişiklikleri engelleyerek belgenin tutarlılığını korumaya yardımcı olur.
1. Güvenlik: Hassas belgelerde şekillerin kilitlenmesi, bilgileri korumak için daha geniş bir stratejinin parçası olabilir. Örneğin, finansal raporlarda veya yasal belgelerde, kilitli şekiller, kritik bağlam sağlayan açıklamaları veya vurguları korumak için kullanılabilir.

Bazen, korunmuş çalışma sayfalarında belirli şekilleri değiştirebilmeniz gerekebilir, bu durumda bu şekilleri kilidini açmanız gerekir. Bu makale, belirli şekilleri nasıl kilitleyeceğiniz ve kilidini açacağınız konusunda detaylı bilgi verecektir.

## **Excel'de Şekilleri Nasıl Kilitlersiniz ve Korursunuz**

İşte Microsoft Excel'de hücreleri kilitlemenin yolu:

1. Excel Dosyanızı Açın: Kilitlemek istediğiniz şekillerin bulunduğu Excel dosyasını açın.

1. Şekli Seçin: Kilitlemek istediğiniz şekle tıklayın. Ayrıca, Ctrl tuşunu basılı tutarak birden çok şekli de seçebilirsiniz.

1. Şekil Biçimlendirme Panelini Açın: Seçilen şekle sağ tıklayın ve "Boyut ve Özellikler"i seçin. Alternatif olarak, Şerit üzerindeki "Biçim" sekmesine gidip "Boyut" grubundan, küçük ok işaretine tıklayarak "Şekil Biçimi" panelini açabilirsiniz.
1. Şekli Kilitleyin: "Şekil Biçimi" panelinde, "Boyut ve Özellikler" sekmesine (kare ve ok işareti gibi görünen ikon) gidin. "Özellikler" bölümünde, "Kilitle" kutusunu işaretleyin.
<br>
<img src="1.png" width=60% />
1. Sayfayı Koruyun: Şerit üzerindeki "Gözden Geçir" sekmesine gidin. "Sayfayı Koru" seçeneğine tıklayın. Bir şifre belirleyin (isteğe bağlı) ve izin vermek istediğiniz işlemleri seçin (ör. kilitli hücreleri seçme, hücreleri biçimlendirme vb.). "Tamam" düğmesine tıklayın.
<br>
<img src="2.png" width=60% />

## **Belirli bir çalışma sayfasındaki tüm şekilleri nasıl kilitlersiniz**

Belirli bir çalışma sayfasındaki tüm şekilleri korumak için [Worksheet.Protect( ProtectionType.Objects)](https://reference.aspose.com/cells/net/aspose.cells/worksheet/protect/#protect) yöntemini kullanın, aşağıdaki örnek kodda gösterildiği gibi.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-1.cs" >}}

## **Korunan bir çalışma sayfasında belirli şekillerin kilidini nasıl açarsınız**

Korunan bir çalışma sayfasındaki belirli bir şeklin kilidini açmak için [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/) özelliğini kullanın, aşağıdaki örnek kodda gösterildiği gibi.

Not: [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/) özelliği, çalışma sayfası korunduğunda anlamlıdır.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-2.cs" >}}

{{< app/cells/assistant language="csharp" >}}
