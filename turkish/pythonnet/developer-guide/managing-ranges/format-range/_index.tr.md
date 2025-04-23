---
title: Aralıkları Biçimlendir
type: docs
weight: 105
url: /tr/python-net/how-to-format-a-range/
description: Bu makale, Aspose.Cells for Python via .NET kütüphanesi ile aralıkları nasıl biçimlendireceğinizi açıklar.
keywords: Python Excel Kütüphanesi, Python da Bir Aralığı Biçimlendirme, Python da Aralıkları Nasıl Biçimlendirirsiniz.
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
1. [Range.apply_style(style, flag)](https://reference.aspose.com/cells/python-net/aspose.cells/range/apply_style/#aspose.cells.Style-aspose.cells.StyleFlag)
2. [Range.set_style(style)](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_style/#aspose.cells.Style)
3. [Range.set_style(style, explicit_flag)](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_style/#aspose.cells.Style-bool)


## **Örnek Kod**
Bu örnekte bir Excel çalışma kitabı oluşturuyoruz, bazı örnek veri ekliyoruz, ilk çalışma sayfasına erişiyoruz ve iki aralık("A1:C3" ve "A4:C5") tanımlıyoruz. Daha sonra yeni stiller oluşturuyoruz, çeşitli biçimlendirme seçeneklerini belirliyoruz (örneğin, yazı tipi rengi, kalın), ve stili aralığa uyguluyoruz. Son olarak, çalışma kitabını yeni bir dosyaya kaydediyoruz.
![todo:image_alt_text](format-range.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-FormatRanges.py" >}}
