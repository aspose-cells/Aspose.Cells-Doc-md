---
title: Linux ta Yazı Tipi Nasıl Kurulur
type: docs
description: "Linux ta Yazı Tipi Nasıl Kurulur"
weight: 139
url: /tr/net/how-to-install-font-in-linux/
---

## Genel Bakış

Aspose.Cells'i Linux'ta kullanırken, Linux'un varsayılan fontları daha az olduğu için, Excel dosyanızda referans verilen yazı tipi varsayılan olarak Linux sisteminizde bulunmayabilir.
Bu durumda, Aspose.Cells benzer bir yazı tipini kullanarak karakterleri gösterecektir. Ancak, bu aşağıdaki etkileri yapabilir:

1. Farklı yazı tipleri, Excel'den farklı düzenlerde görüntülenen resimler oluşturabilir.
2. Yazı tipi değiştiği için, çıkan karakterler istediğiniz gibi olmayabilir.

Programınızın daha doğru sonuçlar üretmesi için gereken yazı tiplerini Linux altında kurmalısınız. Kullanacağınız yazı tiplerinin, Excel dosyalarınızda kullandığınız yazı tipleri ortamınızda mevcut olması önemlidir.

## Linux'ta Yazı Tipi Kurulumu Nasıl Yapılır?

Linux'ta fontları kurmanın iki yolu vardır, aşağıda açıklanmıştır:

### Font dosyalarını Linux sistem yoluna kopyalayın

1. Program dizininize "fonts" adlı bir klasör koyun, ihtiyacınız olan font dosyalarını bu klasöre kopyalayın.
2. Aşağıdaki komutu Linux Docker dosyanıza ekleyin:
```
COPY fonts/ /usr/share/fonts
```
3. Yukarıdaki işlemin ardından, font dosyaları Linux sistem yoluna kopyalanacaktır. Aspose.Cells sistem yoluna gidecek ve bunları bulup kullanacaktır. Bu bizim önerdiğimiz senaryodur.

### Aspose.Cells API ile Font Klasörünü Ayarlama
Bazı durumlarda, Linux sistem dizinini kontrol edemeyebilir veya değiştiremeyebilirsiniz. Örneğin, bulut sunucularında. Bu durumda, ikinci senaryoyu kullanabilirsiniz.
1. Program dizininize "fonts" adlı bir klasör koyun ve ihtiyacınız olan font dosyalarını bu klasöre kopyalayın.
2. Program kodunuzda, Aspose.Cells API'yi çağırın:
```
Aspose.Cells.FontConfigs.SetFontFolder("fonts", true);
```
3. Yukarıdaki işlem, programın fontu proje yolundan bulabilmesini sağlayacaktır.

## Ayrıca Bakınız

- [Aspose.Cells for .Net6 nasıl çalıştırılır](https://docs.aspose.com/cells/net/how-to-run-aspose-cells-for-net6/)

{{< app/cells/assistant language="csharp" >}}
