---
title: Başlık ve Metin Tema Yazı Tipi
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için bir .NET kütüphanesidir. Excel belgelerinde başlık ve metin tema yazı tiplerini ayarlama olanağı sağlar ve belgenin görünümünü özelleştirmenize imkan tanır. Bu makale, Aspose.Cells kütüphanesini kullanarak Excel belgelerinde başlık ve metin tema yazı tipleriyle çalışmayı tanıtacaktır.
keywords: Aspose.Cells, Excel Belgesi, Başlık, Metin, Tema Yazı Tipi, Görünüm, Stil
type: docs
weight: 120
url: /tr/net/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

Varsayılan yazı tipi otomatik olarak ayarlandığında, bölge ayarı değiştirildiğinde varsayılan yazı tipi otomatik olarak değişir. 

Varsayılan yazı tipinin değişmesine ne sebep oldu?

Varsayılan yazı tipinin değişmesine ne sebep oldu?

Excel tema yazı tipi ayarlandığında, Excel mevcut dil ortamına göre farklı yazı tipleri arasında otomatik olarak geçiş yapacaktır.


{{% /alert %}}

## **Excel'de, Ana Menü sekmesini seçin, yazı tipi açılır kutusuna tıklayın, İngilizce bölge ayarıyla en üstte iki tema yazı tipi : Üstbilgi (Calibri Light) ve Metin (Calibri) göreceksiniz.**

Excel'de, Ana sekmesini seçin, yazı tipi açılır kutusuna tıklayın, "Tema Yazı Tipleri"ni göreceksiniz ve en üstte iki tema fontu: Calibri Light (Başlıklar) ve Calibri (Gövde) İngilizce bölge ayarında yer almaktadır.

**![Tema Yazı Tipleri](Theme-Fonts.png)**

Tema Yazı Tipi seçilmişse, yazı tipi adı farklı bölgelerde farklı görünecektir.
Eğer yazı tipinin farklı bölgelerde otomatik olarak değişmesini istemiyorsanız, iki Tema Yazı Tipi'ni seçmeyin.


## **Başlıkları ve Metin Yazı Tipini Programlama Yoluyla Değiştirmek**
Aspose.Cells for .Net ile, varsayılan yazı tipinin tema yazı tipi olup olmadığını kontrol edebilir ve [**Font.SchemeType**](https://reference.aspose.com/cells/net/aspose.cells/font/schemetype/) özelliği ile tema yazı tipini ayarlayabiliriz.

Aşağıdaki örnek kod, tema yazı tipini nasıl manipüle edeceğimizi göstermektedir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Headings-and-body-font.cs" >}}


## **Dinamik Olarak Yerel Tema Yazı Tipini Programlama Yoluyla Almak**
Bazı durumlarda, sunucularımız ve kullanıcı makineleri aynı bölgede değildir. Kullanıcıların dosya işleme için istediği aynı yazı tipini nasıl elde edebiliriz?

Dosyayı [**LoadOptions.Region**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/region/) özelliği ile yüklemeden önce sistem bölgesel ayarlarını ayarlamamız gerekiyor.

Aşağıdaki örnek kod, yerel tema yazı tipini nasıl alacağımızı göstermektedir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Local-Theme-Font.cs" >}}
{{< app/cells/assistant language="csharp" >}}
