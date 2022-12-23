---
title: Farklı GridWeb Modlarını Etkinleştirin
type: docs
weight: 60
url: /tr/net/enable-different-gridweb-modes/
---
{{% alert color="primary" %}} 

Bu makale Aspose.Cells.GridWeb'in farklı modlarını açıklamaktadır. Bu modlar, farklı özellikleri ve davranışları nedeniyle mantıksal olarak farklılaşır. Birkaç mod türü belirledik:

- Düzenleme modu
- Görünüm Modu
- Oturum Modu
- Oturumsuz Mod

Bu modların hepsinin kendine has özellikleri vardır. Geliştiriciler Aspose.Cells.GridWeb ile gereksinimlerine göre her modda çalışabilirler. Aşağıda her bir moda bakacağız.

{{% /alert %}} 
## **Düzenleme modu**
Aspose.Cells.GridWeb denetimi varsayılan olarak Düzenleme modundadır. Düzenleme modunda, Aspose.Cells.GridWeb kontrolü tarafından sunulan tüm özellikleri kullanarak ızgara içeriğini tamamen düzenleyebilir veya değiştirebilirsiniz. Bu özellikler şunları içerir:

- Izgara içeriği Microsoft Excel dosyalarına kaydediliyor.
- Verileri bir sunucuya gönderme.
- Hesaplama formülleri.
- Önceki eylemleri geri alma veya silme.
- Satırları ve sütunları yönetme.
- Verileri kesme, kopyalama veya yapıştırma.
- Hücreleri biçimlendirme vb.

**Düzenleme Modunda GridWeb kontrolü** 

![yapılacaklar:resim_alternatif_metin](enable-different-gridweb-modes_1.png)

Geliştiriciler ayrıca GridWeb denetiminin EditMode özelliğini true olarak ayarlayarak program aracılığıyla Düzenleme moduna geçebilirler.

Aşağıdaki örnek, düzenleme modunun programlı olarak nasıl etkinleştirileceğini gösterir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyEditMode.cs" >}}

{{% alert color="primary" %}} 

 Bir kullanıcı her tıkladığında**Geri alma** düğmesi, GridWeb'i önceki durumuna getirir (sunucuya son geri göndermeden önceki durum). Önceki işlemleri tek tek iptal etmez.

{{% /alert %}} 
## **Görünüm Modu**
GridWeb denetimi Görünüm modundayken, kullanıcılar ızgara içeriğini düzenleyemez veya değiştiremez; bu, kullanıcıların yalnızca ızgara içeriğini görüntüleyebileceği anlamına gelir. Bu yüzden bu moda Görünüm modu denir. Görünüm modunda, birkaç düğme (**Göndermek**, **Kayıt etmek** ve**Geri alma** ) gizlenir ve sağ tıklandığında görünen menü yalnızca**kopyala** seçenek.

**Görüntüleme Modunda GridWeb kontrolü** 

![yapılacaklar:resim_alternatif_metin](enable-different-gridweb-modes_1.png)

Geliştiriciler, kullanıcılarının yalnızca verileri görüntülemesini istiyorsa, GridWeb denetiminin EditMode özelliğini false olarak ayarlayarak program aracılığıyla Görünüm moduna geçebilirler.

Aşağıdaki örnek, görüntüleme modunun programlı olarak nasıl etkinleştirileceğini gösterir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyViewMode.cs" >}}

{{% alert color="primary" %}} 

Görünüm modunda bile, kullanıcılar satırların ve sütunların yüksekliğini ve genişliğini değiştirebilir.

{{% /alert %}} 
## **Oturum Modu**
Aspose.Cells.GridWeb denetimi, web sunucusunun Kullanıcı Oturumunda bir web kullanıcısının her isteği arasında sayfa verilerini tutar. Bu, GridWeb kontrolünün varsayılan olarak her zaman Oturum modunda çalıştığı anlamına gelir. Ancak Oturum modunda çalışmıyorsanız, GridWEb control#s SessionMode özelliğini SessionMode.Session olarak ayarlayarak etkinleştirin.

Aşağıdaki örnek, oturum modunun programlı olarak nasıl etkinleştirileceğini gösterir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionMode.cs" >}}
## **Oturumsuz Mod**
Sayfa verilerini yüklemek ve depolamak için bir kullanıcı oturumu kullanarak Oturum modu yaklaşımının en iyi performansı sağladığını zaten tartışmıştık. Ancak, sunucu belleği tüketir. Bu nedenle, çok sayıda eşzamanlı kullanıcı varsa, bellek sorunları ortaya çıkabilir. Sunucu belleğinden tasarruf etmek ve çok sayıda eşzamanlı kullanıcıyı desteklemek için Oturumsuz modu düşünün.

GridWeb denetiminin SessionMode özelliği SessionMode.ViewState olarak ayarlanarak oturumsuz mod açılabilir.

Aşağıdaki örnek, programlı olarak oturumsuz modun nasıl etkinleştirileceğini gösterir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionlessMode.cs" >}}

{{% alert color="primary" %}} 

ÖNEMLİ: GridWeb'in SessionMode özelliği SessionMode.ViewState olarak ayarlandığında, ızgara verileri sayfanın ViewState'inde depolar. Bu, oluşturulan sayfanın daha büyük olduğu ve daha fazla ağ trafiği tükettiği anlamına gelir.

{{% /alert %}} {{% alert color="primary" %}} 

Oturumları tutmak için SQL Server veya StateServer kullanmak istiyorsanız Oturum modunu kullanın. GridWeb denetimi, verilerinin SQL Server veya StateServer'a serileştirilmesini destekler.

Daha fazla yardım için lütfen aşağıdaki makaleye bakın.

- [ASP.NET Oturum durumu modu SQL Server olduğunda GridWeb'in çalışması](/cells/tr/net/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/)

{{% /alert %}}
