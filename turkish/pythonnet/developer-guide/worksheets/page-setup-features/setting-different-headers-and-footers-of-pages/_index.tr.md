---
title: Farklı Sayfalar için Farklı Üstbilgi ve Altbilgileri Ayarlama
type: docs
weight: 35
url: /tr/python-net/setting-different-headers-and-footers-for-pages-to-Excel/
description: Bu makale, Aspose.Cells for Python API sını kullanarak Excel çalışma sayfası Sayfa Ayarı ayarlarına programlı olarak çeşitli üstbilgi ve altbilgi ayarlarını nasıl yapacağınızı gösteren örnek bir kod sunar. Üstbilgi ve altbilgileri ilk sayfa, tek sayfalar ve çift sayfalar için ayarlayabilirsiniz.
keywords: Python Excel Kütüphanesi, Python ile excel başlık altbilgi ilk sayfa, Python ile excel başlık altbilgi tek sayfalar, Python ile excel başlık altbilgi çift sayfaları ayarlama.
---

{{% alert color="primary" %}}

MS Excel, Excel 2007'den beri ilk sayfa, tek sayfalar ve çift sayfalar için farklı üstbilgi ve altbilgi ayarlama desteği sunmaktadır.
Aspose.Cells için Python via .NET aynı özelliği destekler.

{{% /alert %}}

## **MS Excel'de Farklı Başlık ve Alt Bilgi Nasıl Ayarlanır**

**![Farklı Üstbilgi ve Altbilgiler Ayarlama](difpage.png)**

1. **Sayfa Düzeni > Başlık ve Alt Bilgi > Üstbilgi/Altbilgi**'ye tıklayın.
1. **Farklı Tek ve Çift Sayfalar** veya **Farklı ilk sayfa**'yı işaretleyin.
1. Farklı başlık ve altbilgileri girin.

## **Aspose.Cells Python Excel Kütüphanesi ile Farklı Başlıkları ve Altlıkları Nasıl Ayarlanır**

Aspose.Cells için Python via .NET Excel ile aynı davranışı sergiler.
1. [PageSetup.is_hf_diff_odd_even](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_odd_even/) ve [PageSetup.is_hf_diff_first](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_first/) bayraklarını ayarlar. 
1. Farklı başlık ve altbilgileri girin.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-DiffHeaderFooter.py" >}}
