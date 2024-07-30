---
title: Başlık veya Altlık Alınması
type: docs
weight: 30
url: /tr/net/get-headers-or-footers/
description: Bu makale, C# API veya .NET Kitaplığı nı kullanarak Excel veya OpenOffice dosyalarından başlık ve altlıkları nasıl programlı olarak alacağınızı açıklar.
---

{{% alert color="primary" %}}

Başlıklar ve altlıklar yalnızca Sayfa Düzeni görünümünde, Baskı Önizleme'de ve yazdırılan sayfalarda gösterilir. 

Ayrıca, birden fazla çalışma sayfasında başlıkları veya altlıkları görüntülemek istiyorsanız, Sayfa Düzeni iletişim kutusunu da kullanabilirsiniz. 

Grafik sayfaları veya grafikler gibi diğer sayfa türleri için, başlık ve altyazıları yalnızca Sayfa Düzeni iletişim kutusunu kullanarak ekleyebilirsiniz.

{{% /alert %}}

## **MS Excel'de Başlık ve Altlıkların Alınması**
1. Başlık veya altyazıları görüntülemek veya değiştirmek istediğiniz çalışma sayfasına tıklayın.
2. Grup içinde Vie sekmesinde, Sayfa Düzeni'ne tıklayın.
  Excel, çalışma sayfasını Sayfa Düzeni görünümünde gösterir.
3. Bir başlık veya altlık görüntülemek veya düzenlemek için, çalışma sayfasının üstünde veya altında (Üstbilgi altında) sol, orta veya sağ başlık veya altlık metin kutusuna tıklayın.


## **Aspose.Cells for .Net ile Başlık ve Altlıkların Alınması**
[**Worksheet.PageSetup.GetHeader**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/getheader/) ve [**Worksheet.PageSetup.GetFooter**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/getfooter/) yöntemleri ile, .Net geliştiricileri dosyalardan başlık veya altlık alabilir.

1. Dosyayı açmak için Workbook'u oluşturun.
2. Başlık veya altlık almak istediğiniz çalışma sayfasını alır.
3. Belirli bir bölüm kimliği ile başlık veya altlık alır.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Gets-Header-Footer.cs" >}}

## **Başlık ve Altlıkları Komut Listesine Ayrıştır**
Başlık veya altlık metni özel komutları içerebilir, örneğin sayfa numarası, geçerli tarih veya metin biçimlendirme öznitelikleri için bir yer tutucu.

Özel komutlar başında bir tek harf ve başında bir et ile temsil edilir ("&").

Başlık ve altlık dizeleri ABNF gramerini kullanarak oluşturulur. Görüntüleyici olmadan anlamak kolay değildir.

Aspose.Cells for .Net, başlık ve altlıkları komut listesi olarak ayrıştırmak için [**Worksheet.PageSetup.GetCommands**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/getcommands/) metodu sağlar.

Aşağıdaki kodlar başlık veya altlığı komut listesi olarak ayrıştırmayı ve komutları işlemeyi açıklar:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Parses-Header-Footer.cs" >}}
