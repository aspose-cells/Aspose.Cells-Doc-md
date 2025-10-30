---
title: Golang ile C++ kullanarak Başlıklar ve İçerik Tema Yazı Tipi
linktitle: Başlık ve Metin Tema Yazı Tipi
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için kullanılan bir C++ kitaplığıdır. Excel belgelerinde başlık ve gövde tema yazı tiplerini ayarlamayı destekler, bu da kullanıcıların belgenin görünümünü ve stilini kişiselleştirmesine olanak tanır. Bu makale, Aspose.Cells kütüphanesini kullanarak Excel belgelerinde başlık ve gövde tema yazı tipleriyle nasıl çalışılacağını anlatacaktır.
keywords: Aspose.Cells, Excel Belgesi, Başlık, Metin, Tema Yazı Tipi, Görünüm, Stil
type: docs
weight: 120
url: /tr/go-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

Varsayılan yazı tipi, bölge ayarı değiştirildiğinde otomatik olarak değişecektir.

Varsayılan yazı tipinin değişmesine ne sebep oldu?

Varsayılan yazı tipinin değişmesine ne sebep oldu?

Excel tema yazı tipi ayarlandığında, Excel mevcut dil ortamına göre farklı yazı tipleri arasında otomatik olarak geçiş yapacaktır.

{{% /alert %}}

## **Excel'de, Ana Menü sekmesini seçin, yazı tipi açılır kutusuna tıklayın, İngilizce bölge ayarıyla en üstte iki tema yazı tipi : Üstbilgi (Calibri Light) ve Metin (Calibri) göreceksiniz.**

Excel'de, Ana Sayfa sekmesini seçin, yazı tipi açılır kutusuna tıklayın, "Tema Yazı Tipleri" göreceksiniz ve en üstte İngiliz bölge ayarına sahip iki tema yazı tipi: Calibri Light (Başlıklar) ve Calibri (Gövde).

**![Tema Yazı Tipleri](Theme-Fonts.png)**

Tema Yazı Tipi seçilirse, yazı tipi adı farklı bölgelerde farklı görünecektir.
Yazı tipinin farklı bölgelerde otomatik değiştirilmesini istemiyorsanız, iki Tema Yazı Tipini seçmeyin.

## **Başlıklar Ve Gövde Yazı Tiplerini Programatik Olarak Değiştirme**
Aspose.Cells for C++ ile varsayılan yazı tipinin tema yazı tipi olup olmadığını kontrol edebilir veya [**Font.GetSchemeType()**](https://reference.aspose.com/cells/go-cpp/font/getschemetype/) özelliği kullanarak tema yazı tipini ayarlayabiliriz.

Aşağıdaki örnek kod, tema yazı tipini nasıl manipüle edeceğimizi göstermektedir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MajorMinorFont.go" >}}
## **Dinamik olarak, Yerel Tema Yazı Tipini Programatik Olarak Almak**
Bazı durumlarda, sunucularımız ve kullanıcı makineleri aynı bölgede değildir. Kullanıcıların dosya işleme için istediği aynı yazı tipini nasıl elde edebiliriz?

Dil ve bölge ayarları yüklemeden önce [**LoadOptions.GetRegion()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getregion/) özelliği ile ayarlanmalıdır.

Aşağıdaki örnek kod, yerel tema yazı tipini nasıl alınacağını gösterir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MajorMinorFont-1.go" >}}
