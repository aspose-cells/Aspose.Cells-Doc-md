---
title: Golanga ve C++ kullanarak Aralıkları Biçimlendir
linktitle: Aralıkları Biçimlendir
type: docs
weight: 105
url: /tr/go-cpp/how-to-format-a-range/
description: Aspose.Cells ve Golang kullanarak Excel de aralıkları nasıl biçimlendireceğinizi öğrenin. Stil, yazı tipi ve renkleri programatik olarak hücre aralıklarına uygulayın.
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

## **C++ Kullanarak Aralık Nasıl Biçimlendirilir**

Bir aralığı biçimlendirmek için Aspose.Cells kullanırken aşağıdaki yöntemleri kullanabilirsiniz:
1. [Range.ApplyStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/go-cpp/range/applystyle/)
2. [Range.SetStyle(Style style)](https://reference.aspose.com/cells/go-cpp/range/setstyle_style_bool/)

## **Örnek Kod**
Bu örnekte, bir Excel çalışma kitabı oluşturuyoruz, bazı örnek veriler ekliyoruz, ilk çalışma sayfasına erişiyoruz ve iki aralık tanımlıyoruz ("A1:C3" ve "A4:C5"). Ardından yeni stiller oluşturuyor, çeşitli biçimlendirme seçenekleri ayarlıyor (örneğin, yazı tipi rengi, kalın) ve bunları aralığa uyguluyoruz. Son olarak, çalışma kitabını yeni bir dosyaya kaydediyoruz.
<br>
![todo:image_alt_text](format-range.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormatRange.go" >}}
