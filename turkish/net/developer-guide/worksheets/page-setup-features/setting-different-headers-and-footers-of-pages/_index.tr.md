---
title: Farklı Sayfalar İçin Farklı Üstbilgiler ve Altbilgiler Ayarlama
type: docs
weight: 35
url: /tr/net/setting-different-headers-and-footers-for-pages-to-Excel/
---
{{% alert color="primary" %}}

MS Excel, Excel 2007'den bu yana ilk sayfa, tek sayfalar ve çift sayfalar için farklı üst bilgiler ve alt bilgiler ayarlamayı destekler.
Aspose.Cells aynı özelliği destekler.

{{% /alert %}}

## **MS Excel'de Farklı Üstbilgiler ve Altbilgiler Ayarlama**

**![Farklı Üstbilgileri ve Altbilgileri Ayarlama](difpage.png)**

1.  Tıklamak**sayfa Düzeni > Başlıkları Yazdır > Üst Bilgi/Alt Bilgi**.
1.  Kontrol**Farklı Tek ve Çift Sayfalar** veya**Farklı köknar sayfası**.
1. Farklı üst bilgiler ve alt bilgiler girin.

## **Aspose.Cells ile Farklı Üstbilgiler ve Altbilgiler Ayarlama**

Aspose.Cells, Excel ile aynı şekilde davranır.
1.  Bayrakları ayarlar[PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/) ve[PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) 
1. Farklı üst bilgiler ve alt bilgiler girin.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}
