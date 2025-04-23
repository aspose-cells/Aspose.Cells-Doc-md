---
title: Bir hücrenin biçimini değiştirme
description: C# ile Aspose.Cells kütüphanesini nasıl kullanılır font, renk, sınır vb. gibi hücre biçimlendirmesini nasıl değiştireceğinizi gösterir. Bu özellikleri ayarlayarak, hücrelerin görünümü ve görünümü üzerinde daha fazla kontrol sahibi olursunuz.
keywords: Aspose.Cells, hücre biçimlendirme, C#, font, renk, sınır
type: docs
weight: 20
url: /tr/net/how-to-change-format-of-cell/
---

## **Olası Kullanım Senaryoları**
Belirli verileri vurgulamak istediğinizde, hücrelerin stiline değişiklik yapabilirsiniz.

## **Excel'de bir hücrenin biçimini nasıl değiştirilir**

Excel'de bir tek hücrenin biçimini değiştirmek için şu adımları izleyin:

1. Excel'i açın ve biçimini değiştirmek istediğiniz hücreyi içeren çalışma kitabını açın.

2. Biçimini değiştirmek istediğiniz hücreyi bulun.

3. Hücreye sağ tıklayın ve bağlam menüsünden "Hücre Biçimlendir" seçeneğini seçin. Alternatif olarak, hücreyi seçebilir ve Excel şeridindeki Anahtar sekmesine giderek "Hücreler" grubundaki "Biçim" açılır menüsüne tıklayıp "Hücre Biçimleri"ni seçebilirsiniz.

4. "Hücre Biçimleri" iletişim kutusu görünecektir. Burada, seçilen hücreye uygulanacak çeşitli biçimlendirme seçeneklerini seçebilirsiniz. Örneğin, yazı tipi stilini, yazı tipi boyutunu, yazı tipi rengini, sayı biçimini, sınırları, arka plan rengini vs. değiştirebilirsiniz. Farklı sekmele
rin iletişim kutusunda çeşitli biçimlendirme seçeneklerine erişmek için keşfedin.

5. İstenen biçimlendirme değişiklikleri yapıldıktan sonra, seçilen hücreye biçimlendirmeyi uygulamak için "Tamam" düğmesine tıklayın.


## **C# Kullanarak Bir Hücrenin Biçimini Nasıl Değiştirilir**

Aspose.Cells'i kullanarak bir hücrenin formatını değiştirmek için şu yöntemleri kullanabilirsiniz:
1. [Cell.SetStyle(Style style)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle)
2. [Cell.SetStyle(Style style, bool explicitFlag)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle_2)
3. [Cell.SetStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle_1)


## **Örnek Kod**
Bu örnekte, bir Excel çalışma kitabı oluşturuyoruz, bazı örnek veriler ekliyoruz, ilk çalışsayıya erişiyoruz ve iki hücreye("A2" ve "B3") ulaşıyoruz. Daha sonra, hücrenin stili alınıyor, çeşitli biçimlendirme seçenekleri belirleniyor (örneğin, yazı rengi, kalın), ve hücrenin formatı değiştiriliyor. Son olarak, çalışma kitabı yeni bir dosyaya kaydediliyor.
![todo:image_alt_text](change-format.png)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-change-format.cs" >}}
{{< app/cells/assistant language="csharp" >}}
