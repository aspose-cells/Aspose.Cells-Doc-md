---
title: Hücrenin biçimini değiştirme
description: Yazı tipi, renk, kenarlık vb. dahil olmak üzere hücrelerin biçimlendirmesini değiştirmek için C#'de Aspose.Cells kitaplığı nasıl kullanılır? Bu özellikleri ayarlayarak hücrelerin nasıl görüneceği ve görüneceği üzerinde daha fazla kontrole sahip olursunuz.
keywords: Aspose.Cells, cell formatting, C#, font, color, border
type: docs
weight: 105
url: /tr/net/how-to-change-format-of-cell/
---
##  **Olası Kullanım Senaryoları**
Belirli verileri vurgulamak istediğinizde hücrelerin stilini değiştirebilirsiniz.

##  **Excel'de bir hücrenin biçimi nasıl değiştirilir?**

Excel'de tek bir hücrenin biçimini değiştirmek için şu adımları izleyin:

1. Excel'i açın ve biçimlendirmek istediğiniz hücreyi içeren çalışma kitabını açın.

2. Biçimlendirmek istediğiniz hücreyi bulun.

3. Hücreye sağ tıklayın ve içerik menüsünden "Cells Biçimlendir" seçeneğini seçin. Alternatif olarak, hücreyi seçip Excel şeridindeki Ana Sayfa sekmesine gidebilir, "Cells" grubundaki "Biçim" açılır menüsüne tıklayıp "Cells Biçimlendir"i seçebilirsiniz.

4. "Biçim Cells" iletişim kutusu görünecektir. Burada seçilen hücreye uygulanacak çeşitli biçimlendirme seçeneklerini seçebilirsiniz. Örneğin yazı tipi stilini, yazı tipi boyutunu, yazı tipi rengini, sayı biçimini, kenarlıkları, arka plan rengini vb. değiştirebilirsiniz. Çeşitli biçimlendirme seçeneklerine erişmek için iletişim kutusundaki farklı sekmeleri keşfedin.

5. İstediğiniz biçimlendirme değişikliklerini yaptıktan sonra, biçimlendirmeyi seçilen hücreye uygulamak için "Tamam" düğmesini tıklayın.


##  **C# kullanarak bir hücrenin biçimi nasıl değiştirilir?**

Aspose.Cells'i kullanarak bir hücrenin biçimini değiştirmek için aşağıdaki yöntemleri kullanabilirsiniz:
1. [Cell.SetStyle(Stil stili)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle)
2. [Cell.SetStyle(Stil stili, boolexplicitFlag)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle_2)
3. [Cell.SetStyle(Stil stili, StyleFlag bayrağı)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle_1)


##  **Basit kod**
Bu örnekte, bir Excel çalışma kitabı oluşturuyoruz, bazı örnek veriler ekliyoruz, ilk çalışma sayfasına erişiyoruz ve iki hücre ("A2" ve "B3") elde ediyoruz. Daha sonra hücrenin stilini alırız, çeşitli biçimlendirme seçeneklerini (örneğin yazı tipi rengi, kalın) ayarlayıp hücrenin biçimini değiştiririz. Son olarak çalışma kitabımızı yeni bir dosyaya kaydediyoruz.
![yapılacak şey:image_alt_text](change-format.png)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-change-format.cs" >}}
