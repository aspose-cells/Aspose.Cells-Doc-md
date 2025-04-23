---
title: Başlık ve Metin Tema Yazı Tipi
linktitle: Başlık ve Metin Tema Yazı Tipi
description: Aspose.Cells, Node.js kütüphanesidir. Excel belgelerinde başlık ve gövde tema yazı tiplerini ayarlamayı destekler, böylece kullanıcılar belge görünümünü ve stilini kişiselleştirebilir. Bu makale, Aspose.Cells kütüphanesini kullanarak Excel belgelerinde başlık ve gövde tema yazı tipleri ile çalışma yollarını tanıtacaktır.
keywords: Aspose.Cells, Excel Dosyası, Başlık, Gövde, Tema Yazı Tipi, Görünüm, Stil, Node.js C++ ile
type: docs
weight: 120
url: /tr/nodejs-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

Varsayılan yazı tipi, bölge ayarı değiştirildiğinde otomatik olarak değişecektir.

Varsayılan yazı tipinin değişmesine ne sebep oldu?

Varsayılan yazı tipinin değişmesine ne sebep oldu?

Excel tema yazı tipi ayarlandığında, Excel mevcut dil ortamına göre farklı yazı tipleri arasında otomatik olarak geçiş yapacaktır.

{{% /alert %}}

## **Excel'de, Ana Menü sekmesini seçin, yazı tipi açılır kutusuna tıklayın, İngilizce bölge ayarıyla en üstte iki tema yazı tipi : Üstbilgi (Calibri Light) ve Metin (Calibri) göreceksiniz.**

Excel'de, Ana Sayfa sekmesini seçin, yazı tipi açılır kutusuna tıklayın, "Tema Yazı Tipleri" göreceksiniz; üstte İngiliz bölge ayarına sahip olarak Kalibri Hafif (Başlıklar) ve Kalibri (Gövde) iki tema yazı tipi bulunur.

**![Tema Yazı Tipleri](Theme-Fonts.png)**

Eğer Tema Yazı Tipi seçilirse, font adı farklı bölgelerde farklı görünebilir. Yazı tipinin farklı bölgelerde otomatik değişmesini istemiyorsanız, iki Tema Yazı Tipi seçmeyin.

## **Başlıklar Ve Gövde Yazı Tiplerini Programatik Olarak Değiştirme**
Aspose.Cells for Node.js via C++ ile varsayılan yazı tipinin tema yazısı mı olup olmadığını kontrol edebilir veya [**Font.setSchemeType(FontSchemeType)**](https://reference.aspose.com/cells/nodejs-cpp/font/#setSchemeType-fontschemetype-) metoduyla tema yazı tipi ayarlayabilirsiniz.

Aşağıdaki örnek kod, tema yazı tiplerini nasıl manipüle edeceğinizi gösterir.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-HeadingsAndBodyThemeFont.js" >}}



## **Dinamik olarak, Yerel Tema Yazı Tipini Programatik Olarak Almak**
Bazı durumlarda, sunucularımız ve kullanıcı makineleri aynı bölgede değildir. Kullanıcıların dosya işleme için istediği aynı yazı tipini nasıl elde edebiliriz?

Çalıştırmadan önce, sistem bölge ayarlarını [**LoadOptions.setRegion(CountryCode)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setRegion-countrycode-) metoduyla ayarlamalısınız.

Aşağıdaki örnek kod, yerel tema yazı tipini nasıl alacağımızı göstermektedir.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-GetLocalThemeFont.js" >}}

