---
title: Aralıkları Biçimlendir
type: docs
weight: 105
url: /tr/net/how-to-format-a-range/
---

## **Olası Kullanım Senaryoları**
Bir aralığa stili uygulamanız gerektiğinde, aralık biçimlendirme kullanabilirsiniz.

## **Excel'de bir Aralığı Nasıl Biçimlendirirsiniz**

Excel'de bir aralığı biçimlendirmek için, Excel tarafından sağlanan yerleşik biçimlendirme seçeneklerini kullanabilirsiniz. İşte Excel'de bir aralığı doğrudan nasıl biçimlendireceğiniz:

1. Excel'i açın ve biçimlendirmek istediğiniz aralığı içeren çalışma kitabını açın.

2. Biçimlendirmek istediğiniz hücre aralığını seçin. Aralığı seçmek için tıklayıp sürükleyebilirsiniz veya Shift + Ok tuşları gibi klavye kısayollarını kullanarak seçimi genişletebilirsiniz.

3. Aralık seçildikten sonra, seçilen aralık üzerine sağ tıklayın ve bağlam menüsünden "Hücreleri Biçimlendir" öğesini seçin. Alternatif olarak, Excel şeridindeki Ana sekmesine giderek, "Hücreler" grubundaki "Biçim" açılır menüsüne tıklayın ve "Hücreleri Biçimlendir" seçeneğini belirleyin.

4. "Hücreleri Biçimlendir" iletişim kutusu görünecektir. Burada, seçilen aralığa uygulanacak çeşitli biçimlendirme seçeneklerini seçebilirsiniz. Örneğin, yazı tipi stili, yazı tipi boyutu, yazı tipi rengi, sayı formatı, kenarlıklar, arka plan rengi vb. değiştirebilirsiniz. Farklı sekmeleri keşfetmek için iletişim kutusundaki farklı sekmelere bakın.

5. İstenen biçimlendirme değişikliklerini yaptıktan sonra, seçilen aralığa biçimlendirmeyi uygulamak için "Tamam" düğmesine tıklayın.


## **C# Kullanarak Bir Aralığı Nasıl Biçimlendirirsiniz**

Aspose.Cells kullanarak bir aralığı biçimlendirmek için aşağıdaki yöntemleri kullanabilirsiniz:
1. [Range.ApplyStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/net/aspose.cells/range/applystyle/)
2. [Range.SetStyle(Style style)](https://reference.aspose.com/cells/net/aspose.cells/range/setstyle/#setstyle)
3. [Range.SetStyle(Style style)](https://reference.aspose.com/cells/net/aspose.cells/range/setstyle/#setstyle_1)


## **Örnek Kod**
Bu örnekte bir Excel çalışma kitabı oluşturuyoruz, bazı örnek veri ekliyoruz, ilk çalışma sayfasına erişiyoruz ve iki aralık("A1:C3" ve "A4:C5") tanımlıyoruz. Daha sonra yeni stiller oluşturuyoruz, çeşitli biçimlendirme seçeneklerini belirliyoruz (örneğin, yazı tipi rengi, kalın), ve stili aralığa uyguluyoruz. Son olarak, çalışma kitabını yeni bir dosyaya kaydediyoruz.
<br>
![todo:image_alt_text](format-range.png)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Range-FormatRanges.cs" >}}
{{< app/cells/assistant language="csharp" >}}
