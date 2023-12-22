---
title: Başlıklar ve Gövde Teması Yazı Tipi
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmaya yönelik bir .NET kitaplığıdır. Excel belgelerinde başlık ve gövde teması yazı tiplerini ayarlamayı destekleyerek kullanıcıların belgenin görünümünü ve stilini özelleştirmesine olanak tanır. Bu makalede, Excel belgelerindeki başlık ve gövde teması yazı tipleriyle çalışmak için Aspose.Cells kitaplığının nasıl kullanılacağı tanıtılacaktır.
keywords: Aspose.Cells, Excel Document, Heading, Body, Theme Font, Appearance, Style
type: docs
weight: 120
url: /tr/net/headings-and-body-theme-font/
---
{{% alert color="primary" %}}

 Yeniden başlama ayarı değiştirildiğinde varsayılan yazı tipi otomatik olarak değişecektir.

Varsayılan yazı tipi değiştirilirse satır yüksekliği ve sütun genişliği de değişir ve bu durum sayfa düzenini bile bozabilir.

Varsayılan yazı tipinin değişmesine ne sebep oldu?

Excel tema yazı tipi ayarlanırsa Excel, geçerli dil ortamına bağlı olarak farklı yazı tipleri arasında otomatik olarak geçiş yapar.


{{% /alert %}}

##  **Excel'de Başlıklar ve Gövde Teması Yazı Tipi**

Excel'de Ana Sayfa sekmesini seçin, yazı tipi açılır kutusuna tıklayın, iki tema yazı tipine sahip "Tema Yazı Tipleri" göreceksiniz: Calibri Light (Başlıklar) ve Calibri (Gövde), İngilizce bölge ayarıyla üstte.

**![Tema Yazı Tipleri](Tema-Fonts.png)**

Tema Yazı Tipi seçilirse yazı tipi adı farklı bölgelerde farklı görünecektir.
Yazı tipinin farklı bölgelerde otomatik olarak değiştirilmesini istemiyorsanız iki Tema Yazı Tipini seçmeyin.


##  **Başlıkları ve Gövde Yazı Tipini Programlı Olarak Değiştirme**
 .Net için Aspose.Cells ile varsayılan yazı tipinin tema yazı tipi olup olmadığını kontrol edebilir veya tema yazı tipini ayarlayabiliriz.[**Font.SchemeType**](https://reference.aspose.com/cells/net/aspose.cells/font/schemetype/) mülk.

Aşağıdaki örnek kod, tema yazı tipinin nasıl değiştirileceğini gösterir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Headings-and-body-font.cs" >}}


##  **Programsal Olarak Yerel Tema Yazı Tipini Dinamik Olarak Alır**
Bazen sunucularımız ve kullanıcılarımızın makineleri aynı bölgede olmayabilir. Kullanıcıların dosya işleme için istediği yazı tipinin aynısını nasıl elde edebiliriz?

 Dosyayı yüklemeden önce sistemin bölgesel ayarlarını yapmalıyız.[**LoadOptions.Region**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/region/) mülk

Aşağıdaki örnek kod, yerel tema yazı tipinin nasıl alınacağını gösterir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Local-Theme-Font.cs" >}}