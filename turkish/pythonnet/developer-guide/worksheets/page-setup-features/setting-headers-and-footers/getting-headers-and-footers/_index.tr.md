---
title: Başlık veya Altlık Alınması
type: docs
weight: 30
url: /tr/python-net/get-headers-or-footers/
description: Bu makale, Aspose.Cells for Python via .NET API sini kullanarak Excel veya OpenOffice dosyalarından başlık ve ayaklıkları programatik olarak nasıl alacağınızı açıklar.
keywords: Python Excel Kütüphanesi, Python başlıkları ve ayaklıkları alma, Başlıkları ve Ayaklıkları Python kullanarak Komut Listesine Ayrıştırmak.
---

{{% alert color="primary" %}}

Başlıklar ve altlıklar yalnızca Sayfa Düzeni görünümünde, Baskı Önizleme'de ve yazdırılan sayfalarda gösterilir. 

Ayrıca, birden fazla çalışma sayfasında başlıkları veya altlıkları görüntülemek istiyorsanız, Sayfa Düzeni iletişim kutusunu da kullanabilirsiniz. 

Grafik sayfaları veya grafikler gibi diğer sayfa türleri için, başlık ve altyazıları yalnızca Sayfa Düzeni iletişim kutusunu kullanarak ekleyebilirsiniz.

{{% /alert %}}

## **MS Excel'de Başlıkları ve Ayaklıkları Nasıl Alınır**
1. Başlık veya altyazıları görüntülemek veya değiştirmek istediğiniz çalışma sayfasına tıklayın.
2. Grup içinde Vie sekmesinde, Sayfa Düzeni'ne tıklayın.
  Excel, çalışma sayfasını Sayfa Düzeni görünümünde gösterir.
3. Bir başlık veya altlık görüntülemek veya düzenlemek için, çalışma sayfasının üstünde veya altında (Üstbilgi altında) sol, orta veya sağ başlık veya altlık metin kutusuna tıklayın.


## **Aspose.Cells for Python Excel Kütüphanesi kullanarak Başlıkları ve Ayaklıkları Nasıl Alınır**
[**Worksheet.page_setup.get_header**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/get_header/#int) ve [**Worksheet.page_setup.get_footer**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/get_footer/#int) yöntemleri ile, .Net geliştiricileri dosyalardan başlık veya altlık alabilir.

1. Dosyayı açmak için Workbook'u oluşturun.
2. Başlık veya altlık almak istediğiniz çalışma sayfasını alır.
3. Belirli bir bölüm kimliği ile başlık veya altlık alır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Gets-Header-Footer.py" >}}

## **Başlıkları ve Ayaklıkları Komut Listesine Ayrıştırma Nasıl Yapılır**
Başlık veya altlık metni özel komutları içerebilir, örneğin sayfa numarası, geçerli tarih veya metin biçimlendirme öznitelikleri için bir yer tutucu.

Özel komutlar başında bir tek harf ve başında bir et ile temsil edilir ("&").

Başlık ve altlık dizeleri ABNF gramerini kullanarak oluşturulur. Görüntüleyici olmadan anlamak kolay değildir.

Aspose.Cells for Python via .NET, başlıkları ve ayaklıkları komut listesine ayrıştırmak için [**Worksheet.page_setup.get_commands**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/get_commands/#str) yöntemi sağlar.

Aşağıdaki kodlar başlık veya altlığı komut listesi olarak ayrıştırmayı ve komutları işlemeyi açıklar:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Parses-Header-Footer.py" >}}
