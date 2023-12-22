---
title: Üstbilgileri veya Altbilgileri Alma
type: docs
weight: 30
url: /tr/net/get-headers-or-footers/
description: Bu makalede, C# API veya .NET Kitaplığı'nı kullanarak Excel veya OpenOffice dosyalarından üstbilgi ve altbilgilerin programlı olarak nasıl alınacağı açıklanmaktadır.
---
{{% alert color="primary" %}}

 Üstbilgiler ve altbilgiler yalnızca Sayfa Düzeni görünümünde, Baskı Önizleme'de ve yazdırılan sayfalarda görüntülenir.

 Aynı anda birden fazla çalışma sayfasının üstbilgilerini veya altbilgilerini görüntülemek istiyorsanız Sayfa Yapısı iletişim kutusunu da kullanabilirsiniz.

Grafik sayfaları veya grafikler gibi diğer sayfa türleri için üstbilgileri ve altbilgileri yalnızca Sayfa Yapısı iletişim kutusunu kullanarak ekleyebilirsiniz.

{{% /alert %}}

##  **MS Excel'de Üstbilgi ve Altbilgi Alma**
1. Üst bilgileri veya alt bilgileri görüntülemek veya değiştirmek istediğiniz çalışma sayfasını tıklayın.
2. Görünüm sekmesinin Çalışma Kitabı Görünümleri grubunda Sayfa Düzeni'ni tıklayın.
Excel, çalışma sayfasını Sayfa Düzeni görünümünde görüntüler.
3. Bir üstbilgiyi veya altbilgiyi görüntülemek veya düzenlemek için, çalışma sayfası sayfasının üst veya alt kısmındaki (Üstbilgi altında veya Altbilginin üstünde) sol, orta veya sağ üstbilgi veya altbilgi metin kutusunu tıklayın.


##  **.Net için Aspose.Cells'i kullanarak Üstbilgileri ve Altbilgileri Alma**
 İle[**Çalışma Sayfası.GetHeader**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetHeader/) Ve[**Worksheet.GetFooter**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetFooter/) yöntemleri kullanarak, .Net geliştiricisi dosyadan üstbilgileri veya altbilgileri kolayca alabilir.

1. Dosyayı açmak için Çalışma Kitabı oluşturun.
2. Çalışma sayfasını üstbilgi veya altbilgiyi almak istediğiniz yere getirir.
3. Belirli bölüm kimliğine sahip üstbilgi veya altbilgiyi alır.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Gets-Header-Footer.cs" >}}

##  **Üstbilgileri ve Altbilgileri Komut Listesine Ayrıştırın**
Üstbilgi veya altbilgi metni, örneğin sayfa numarası, geçerli tarih veya metin biçimlendirme nitelikleri için yer tutucu gibi özel komutlar içerebilir.

Özel komutlar, başında ve işareti ("&") bulunan tek harfle temsil edilir.

Üstbilgi ve altbilgi dizeleri ABNF dilbilgisi kullanılarak oluşturulur. İzleyici olmadan anlaşılması kolay değil.

 .Net için Aspose.Cells şunları sağlar[**Worksheet.GetCommands**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/GetCommands/)Üstbilgileri ve altbilgileri komut listesi olarak ayrıştırma yöntemi.

Aşağıdaki kodlar, üstbilgi veya altbilginin komut listesi ve işlem komutları olarak nasıl ayrıştırılacağını kodlar:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Parses-Header-Footer.cs" >}}
