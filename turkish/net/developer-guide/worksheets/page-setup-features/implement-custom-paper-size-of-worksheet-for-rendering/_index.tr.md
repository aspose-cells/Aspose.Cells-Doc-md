---
title: İşleme için Çalışma Sayfasının Özel Kağıt Boyutunu Uygulayın
type: docs
weight: 70
url: /tr/net/implement-custom-paper-size-of-worksheet-for-rendering/
description: Bu makalede, Excel dosyasını programlı olarak PDF dosya biçimine dönüştürürken istediğiniz çalışma sayfalarının özel kağıt boyutunu ayarlamak için C# API veya .NET Kitaplık örnek kodunun nasıl kullanılacağı açıklanmaktadır.
keywords: set custom paper size while rendering excel to pdf c#
---
##  **Olası Kullanım Senaryoları**

MS Excel'de özel kağıt boyutları oluşturmak için doğrudan bir seçenek yoktur, ancak Excel dosyasını PDF dosya biçiminde işlerken istediğiniz çalışma sayfalarının özel kağıt boyutunu ayarlayabilirsiniz. Bu belge, Aspose.Cells API'leri kullanılarak bir çalışma sayfasının özel kağıt boyutunun nasıl ayarlanacağını açıklar.

##  **İşleme için Çalışma Sayfasının Özel Kağıt Boyutunu Uygulayın**

 Aspose.Cells, çalışma sayfasının istediğiniz kağıt boyutunu uygulamanıza olanak tanır. kullanabilirsiniz[**Özel KağıtBoyutu**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/custompapersize) yöntemi[**Sayfa ayarı**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) özel bir sayfa boyutu belirtmek için sınıf. Aşağıdaki örnek kod, çalışma kitabındaki ilk çalışma sayfası için özel bir kağıt boyutunun nasıl belirleneceğini gösterir. Lütfen şuna da bakın:[çıkış PDF](45056028.pdf)bir referans için aşağıdaki kod ile oluşturulmuştur.

##  **Ekran görüntüsü**

![yapılacaklar:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

##  **Basit kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.cs" >}}
