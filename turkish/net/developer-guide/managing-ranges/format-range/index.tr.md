---
title: Biçim Aralıkları
type: docs
weight: 105
url: /tr/net/how-to-format-a-range/
---
##  **Olası Kullanım Senaryoları**
Bir aralığa stil uygulamanız gerektiğinde aralık biçimlendirmesini kullanabilirsiniz.

##  **Excel'de bir Aralık nasıl biçimlendirilir**

Excel'de bir dizi hücreyi biçimlendirmek için Excel tarafından sağlanan yerleşik biçimlendirme seçeneklerini kullanabilirsiniz. Bir hücre aralığını doğrudan Excel'de şu şekilde biçimlendirebilirsiniz:

1. Excel'i açın ve biçimlendirmek istediğiniz aralığı içeren çalışma kitabını açın.

2. Biçimlendirmek istediğiniz hücre aralığını seçin. Aralığı seçmek için tıklayıp sürükleyebilir veya seçimi genişletmek için Shift + Ok tuşları gibi klavye kısayollarını kullanabilirsiniz.

3. Aralık seçildikten sonra, seçilen aralığa sağ tıklayın ve içerik menüsünden "Cells Biçimlendir" seçeneğini seçin. Alternatif olarak, Excel şeridindeki Ana Sayfa sekmesine gidebilir, "Cells" grubundaki "Biçim" açılır menüsüne tıklayıp "Cells'i Biçimlendir"i seçebilirsiniz.

4. "Biçim Cells" iletişim kutusu görünecektir. Burada, seçilen aralığa uygulanacak çeşitli biçimlendirme seçeneklerini seçebilirsiniz. Örneğin yazı tipi stilini, yazı tipi boyutunu, yazı tipi rengini, sayı biçimini, kenarlıkları, arka plan rengini vb. değiştirebilirsiniz. Çeşitli biçimlendirme seçeneklerine erişmek için iletişim kutusundaki farklı sekmeleri keşfedin.

5. İstediğiniz biçimlendirme değişikliklerini yaptıktan sonra, biçimlendirmeyi seçilen aralığa uygulamak için "Tamam" düğmesini tıklayın.


##  **C# kullanarak bir Aralık nasıl biçimlendirilir**

Aspose.Cells'i kullanarak bir aralığı biçimlendirmek için aşağıdaki yöntemleri kullanabilirsiniz:
1. [Range.ApplyStyle(Stil stili, StyleFlag bayrağı)](https://reference.aspose.com/cells/net/aspose.cells/range/applystyle/)
2. [Range.SetStyle(Stil stili)](https://reference.aspose.com/cells/net/aspose.cells/range/setstyle/#setstyle)
3. [Range.SetStyle(Stil stili)](https://reference.aspose.com/cells/net/aspose.cells/range/setstyle/#setstyle_1)


##  **Basit kod**
Bu örnekte bir Excel çalışma kitabı oluşturuyoruz, bazı örnek veriler ekliyoruz, ilk çalışma sayfasına erişiyoruz ve iki aralık ("A1:C3" ve "A4:C5") tanımlıyoruz. Daha sonra yeni stiller yaratırız, çeşitli biçimlendirme seçeneklerini (örneğin yazı tipi rengi, kalın) ayarlarız ve stili aralığa uygularız. Son olarak çalışma kitabımızı yeni bir dosyaya kaydediyoruz.
![yapılacak şey:image_alt_text](format-range.png)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Range-FormatRanges.cs" >}}
