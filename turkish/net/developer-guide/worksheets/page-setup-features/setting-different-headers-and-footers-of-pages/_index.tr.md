---
title: Farklı Sayfalar için Farklı Üstbilgi ve Altbilgileri Ayarlama
type: docs
weight: 35
url: /tr/net/setting-different-headers-and-footers-for-pages-to-Excel/
description: Bu makale, Excel çalışma sayfası Sayfa Ayarı ayarlarını programlı olarak çeşitli üstbilgi ve altbilgiler ayarlayan örnek kodları sağlar. İlk sayfa, tek sayfalar ve çift sayfalar için üstbilgi ve altbilgileri ayarlayabilirsiniz.
keywords: c# da excel üstbilgi altbilgi ilk sayfa, c# da excel üstbilgi altbilgi tek sayfalar, c# da excel üstbilgi altbilgi çift sayfalar ayarlama
---

{{% alert color="primary" %}}

MS Excel, Excel 2007'den beri ilk sayfa, tek sayfalar ve çift sayfalar için farklı üstbilgi ve altbilgi ayarlama desteği sunmaktadır.
Aspose.Cells aynı özelliği destekler.

{{% /alert %}}

## **MS Excel'de Farklı Üstbilgi ve Altbilgiler Ayarlama**

**![Farklı Üstbilgi ve Altbilgiler Ayarlama](difpage.png)**

1. **Sayfa Düzeni > Başlık ve Alt Bilgi > Üstbilgi/Altbilgi**'ye tıklayın.
1. **Farklı Tek ve Çift Sayfalar** veya **Farklı ilk sayfa**'yı işaretleyin.
1. Farklı başlık ve altbilgileri girin.

## **Aspose.Cells ile Farklı Üstbilgi ve Altbilgi Ayarlama**

Aspose.Cells, Excel ile aynı davranışı sergiler.
1. [PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/) ve [PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) bayraklarını ayarlar 
1. Farklı başlık ve altbilgileri girin.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}
