---
title: Başlık ve Metin Tema Yazı Tipi
description: Aspose.Cells, hesap tabloları ile çalışma yapmak için kullanılan bir Python kütüphanesidir. Excel belgelerinde başlık ve gövde tema yazı tiplerini ayarlamayı destekler, böylece belgenin görünüm ve stilini özelleştirebilirsiniz. Bu makale, Aspose.Cells for Python via .NET kütüphanesi kullanılarak Excel belgelerinde başlık ve gövde tema yazı tipleri ile çalışma yöntemini gösterecek.
keywords: Aspose.Cells for Python via .NET, Excel Belgesi, Başlık, Gövde, Tema Yazı Tipi, Görünüm, Stil
type: docs
weight: 120
url: /tr/python-net/headings-and-body-theme-font/
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
Aspose.Cells for Python via .NET ile varsayılan yazı tipinin tema yazı tipi olup olmadığını kontrol edebilir veya [**Font.scheme_type**](https://reference.aspose.com/cells/python-net/aspose.cells/font/scheme_type) özelliği ile tema yazı tipi ayarlayabiliriz.

Aşağıdaki örnek kod, tema yazı tipini nasıl manipüle edeceğimizi göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Headings-and-body-font.py" >}}


## **Dinamik Olarak Yerel Tema Yazı Tipini Programlama Yoluyla Almak**
Bazı durumlarda, sunucularımız ve kullanıcı makineleri aynı bölgede değildir. Kullanıcıların dosya işleme için istediği aynı yazı tipini nasıl elde edebiliriz?

Dosyayı [**LoadOptions.region**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/region) özelliği ile yüklemeden önce sistem bölgesel ayarlarını ayarlamamız gerekiyor.

Aşağıdaki örnek kod, yerel tema yazı tipini nasıl alacağımızı göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Local-Theme-Font.py" >}}

{{< app/cells/assistant language="python-net" >}}
