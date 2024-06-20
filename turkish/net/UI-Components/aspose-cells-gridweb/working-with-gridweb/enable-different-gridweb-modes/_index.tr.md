---
title: Farklı GridWeb Modlarını Etkinleştir
type: docs
weight: 60
url: /tr/net/aspose-cells-gridweb/enable-different-gridweb-modes/
keywords: GridWeb,EditMode,SessionMode
description: Bu makale, GridWeb de EditMode ve SessionMode ile nasıl çalışılacağını tanıtır.
---

{{% alert color="primary" %}} 

Bu makale, Aspose.Cells.GridWeb'in farklı modlarını açıklar. Bu modlar, farklı özelliklere ve davranışlara sahip oldukları için mantıksal olarak ayrılır. Birden fazla mod türü tespit ettik:

- Edit Modu
- Görünüm Modu
- Oturum Modu
- Oturumsuz Modu

Bu modların hepsinin kendi özellikleri vardır. Geliştiriciler, gereksinimlerine göre Aspose.Cells.GridWeb'i herhangi bir modda kullanabilir. Aşağıda her bir moda bakacağız.

{{% /alert %}} 
## **Edit Modu**
Varsayılan olarak, Aspose.Cells.GridWeb kontrolü Edit modundadır. Edit modunda, Aspose.Cells.GridWeb kontrolünün sunduğu tüm özellikleri kullanarak ızgara içeriğini tamamen düzenleyebilir veya değiştirebilirsiniz. Bu özellikler şunları içerir:

- İçeriğin Microsoft Excel dosyalarına kaydedilmesi.
- Verileri sunucuya gönderme.
- Formüllerin hesaplanması.
- Önceki işlemlerin geri alınması veya atılması.
- Satır ve sütunları yönetme.
- Veri kesme, kopyalama veya yapıştırma.
- Hücreleri biçimlendirme vb.

**GridWeb denetimi Düzenleme Modunda** 

![todo:image_alt_text](enable-different-gridweb-modes_1.png)

Geliştiriciler GridWeb denetiminin EditMode özelliğini true olarak ayarlayarak programlı olarak Düzenleme moduna da geçebilirler.

Aşağıdaki örnek programlı olarak düzenleme modunu etkinleştirme şeklini göstermektedir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyEditMode.cs" >}}

{{% alert color="primary" %}} 

Kullanıcı **Geri Al** düğmesine her tıkladığında, GridWeb'i önceki durumuna geri getirir (sunucuya son gönderim öncesindeki durum). Önceki işlemleri tek tek iptal etmez.

{{% /alert %}} 
## **Görünüm Modu**
GridWeb denetimi Görünüm modundayken, kullanıcılar ızgara içeriğini düzenleyemez veya değiştiremez, bu da kullanıcıların yalnızca ızgara içeriğini görebileceği anlamına gelir. Bu mod, Görünüm modu olarak adlandırılır. Görünüm modunda birkaç düğme (**Gönder**, **Kaydet** ve **Geri Al**) gizlidir ve sağ tıkladığınızda çıkan menü yalnızca **Kopyala** seçeneğini içerir.

**GridWeb denetimi Görünüm Modunda** 

![todo:image_alt_text](enable-different-gridweb-modes_1.png)

Geliştiriciler, kullanıcılarının yalnızca veri görmesini istiyorlarsa, GridWeb denetiminin EditMode özelliğini false olarak ayarlayarak programlı olarak Görünüm moduna geçebilirler.

Aşağıdaki örnek programlı olarak görünüm modunu etkinleştirme şeklini göstermektedir



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyViewMode.cs" >}}

{{% alert color="primary" %}} 

Görünüm modunda bile, kullanıcılar satır ve sütunların yüksekliğini ve genişliğini değiştirebilirler.

{{% /alert %}} 
## **Oturum Modu**
Aspose.Cells.GridWeb denetimi, web sunucusunun Kullanıcı Oturumu arasında her istekte sayfa verilerini saklar. Bu, GridWeb denetiminin varsayılan olarak her zaman Oturum modunda çalıştığı anlamına gelir. Ancak, Oturum modunda çalışmıyorsanız, GridWeb denetiminin SessionMode özelliğini SessionMode.Session olarak ayarlayarak etkinleştirebilirsiniz.

Aşağıdaki örnek programlı olarak oturum modunu etkinleştirme şeklini göstermektedir



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionMode.cs" >}}
## **Oturumsuz Mod**
Oturum modu yaklaşımının, kullanıcı oturumunu yükleme ve sayfa verilerini saklama yoluyla en iyi performansı sağladığını daha önce tartıştık. Ancak, sunucu belleğini tüketir. Bu nedenle, büyük sayıda eşzamanlı kullanıcı varsa bellek sorunları ortaya çıkabilir. Sunucu belleğini kaydetmek ve büyük sayıda eşzamanlı kullanıcıyı desteklemek için Oturumsuz modu düşünün.

Oturumsuz mod, GridWeb denetiminin SessionMode özelliğini SessionMode.ViewState olarak ayarlayarak etkinleştirilebilir.

Aşağıdaki örnek programlı olarak oturumsuz modu etkinleştirme şeklini göstermektedir



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionlessMode.cs" >}}

{{% alert color="primary" %}} 

ÖNEMLİ: GridWeb'in SessionMode özelliği SessionMode.ViewState olarak ayarlandığında, ızgara verileri sayfanın ViewState'ine saklanır. Bu, oluşturulan sayfanın daha büyük ve daha fazla ağ trafiği tüketmesi anlamına gelir.

{{% /alert %}} {{% alert color="primary" %}} 

Eğer SQL Server veya StateServer kullanarak oturumları tutmak istiyorsanız, Oturum modunu kullanın. GridWeb denetimi, verilerini SQL Server veya StateServer'a serileştirmeyi destekler.

Daha fazla yardım için lütfen aşağıdaki makaleyi kontrol edin.

- [ASP.NET Oturum durumu modu SQL Server olan GridWeb'in çalışması](/cells/tr/net/aspose-cells-gridweb/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/)

{{% /alert %}}
