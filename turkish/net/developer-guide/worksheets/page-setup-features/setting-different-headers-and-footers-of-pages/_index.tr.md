---
title: Farklı Sayfalar İçin Farklı Üstbilgiler ve Altbilgiler Ayarlama
type: docs
weight: 35
url: /tr/net/setting-different-headers-and-footers-for-pages-to-Excel/
description: Bu makale, C# Kitaplığı ve .NET API kullanılarak Excel çalışma sayfası Sayfa Yapısı ayarlarının çeşitli üstbilgilerinin ve altbilgilerinin programlı olarak nasıl ayarlanacağını gösteren örnek kod sağlar. Üstbilgileri ve altbilgileri ilk sayfa, tek sayfalar ve çift sayfalar için ayarlayabilirsiniz.
keywords: set excel header footer first page c#, set excel header footer odd pages c#, set excel header footer even pages c#
---
{{% alert color="primary" %}}

MS Excel, Excel 2007'den bu yana ilk sayfa, tek sayfalar ve çift sayfalar için farklı üst bilgiler ve alt bilgiler ayarlamayı destekler.
Aspose.Cells aynı özelliği destekler.

{{% /alert %}}

##  **MS Excel'de Farklı Üstbilgiler ve Altbilgiler Ayarlama**

**![Farklı Üstbilgileri ve Altbilgileri Ayarlama](difpage.png)**

1. *sayfa Düzeni > Başlıkları Yazdır > Üstbilgi/Altbilgi**'ye tıklayın.
1.  Kontrol etmek**Farklı Tek ve Çift Sayfalar** veya *Farklı köknar sayfası**.
1. Farklı üst bilgiler ve alt bilgiler girin.

##  **Aspose.Cells ile Farklı Üstbilgiler ve Altbilgiler Ayarlama**

Aspose.Cells, Excel ile aynı şekilde davranır.
1.  Bayrakları ayarlar[PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/) Ve[PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) 
1. Farklı üst bilgiler ve alt bilgiler girin.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}
