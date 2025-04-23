---
title: Yayınlanan İşlenmiş Elektronik Tablolar için Yazı Tiplerini Yapılandırma
type: docs
weight: 10
url: /tr/python-net/configuring-fonts-for-rendering-spreadsheets/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells for Python via .NET API'leri, tabloları resim formatlarında göstermenize ve PDF & XPS formatlarına dönüştürmenize imkan tanır. Dönüşüm doğruluğunu maksimize etmek için, tabloda kullanılan fontların işletim sisteminin varsayılan font dizininde bulunması gerekir. Gerekirse, eksik fontlar yerine kullanılabilir fontlar denenir.

## **Yazı Tiplerinin Seçimi**

Aşağıda, Aspose.Cells for Python via .NET API'lerinin arka planda izlediği süreç yer almaktadır.

1. API, elektronik tabloda kullanılan tam olarak eşleşen yazı tipini dosya sistemi üzerinde bulmaya çalışır.
2. API, aynı ebeveyn düğümü altında kullanılan varsayılan yazı tipini belirleyebilecek olan [**DefaultStyle.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) özelliği altında belirtilen varsayılan yazı tipini kullanmaya çalışır.
3. API, yazı tipini belirleyemiyorsa, [**DefaultStyle.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) veya [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) özelliği altında belirtilen yazı tipini kullanmaya çalışır.
4. API, yazı tipini belirleyemiyorsa, [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) özelliği altında belirtilen yazı tipini kullanmaya çalışır.
1. API, [**FontConfigs.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/default_font_name) özelliği altında tanımlanan yazı tipi bulunamazsa, mevcut yazı tiplerinden en uygun olanını seçmeye çalışır.
1. Son olarak, API dosya sisteminde herhangi bir yazı tipi bulamazsa, çalışsayı Arial kullanarak elektronik tabloyu oluşturur.

## **Özel Yazı Tipi Klasörlerini Ayarlayın**

Aspose.Cells for Python via .NET API'leri, işletim sisteminin varsayılan font dizininde gerekli fontları arar. Gerekli fontlar sistemde yoksa, özel (kullanıcı tanımlı) dizinleri de tarar. [**FontConfigs**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs) sınıfı, özel font dizinleri ayarlamak için çeşitli yollar sunar, aşağıda detaylandırılmıştır.

1. [**FontConfigs.set_font_folder**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folder/): Bu yöntem, sadece bir klasör ayarlanacaksa kullanışlıdır.
1. [**FontConfigs.set_font_folders**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folders/): Bu yöntem, yazı tiplerinin birden fazla klasörde bulunduğu durumda ve kullanıcı tüm klasörleri tek tek birleştirmek yerine ayrı ayrı ayarlamak istediğinde kullanışlıdır.
1. [**FontConfigs.set_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_sources/#list): Bu mekanizma, kullanıcının birden fazla klasörden veya tek bir yazı tipi dosyasından veya bayt dizisinden yazı tiplerini yüklemek istemesi durumunda kullanışlıdır.

{{% alert color="primary" %}}

Hem [**FontConfigs.set_font_folder**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folder/) hem de [**FontConfigs.set_font_folders**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folders/) metodları Booleen türünde ikinci parametre kabul eder. **true** değeri verilirse, Aspose.Cells for Python via .NET API'leri, alt klasörleri de araştırarak font dosyalarını arar.

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetCustomFontFolders-1.py" >}}

{{% alert color="primary" %}}

Lütfen yukarıda anlatılan yöntemlerden herhangi birini uygulamanın başında, yani Aspose.Cells for Python via .NET API'lerini çağırmadan önce kullanın.

{{% /alert %}} {{% alert color="primary" %}}

Yukarıda bahsedilen tüm yöntemler, yazı tiplerini ayarlamak için kullanıldığında, sadece son ayarlamalar etkili olacaktır.

{{% /alert %}}

## **Yazı Tipi Yedekleme Mekanizması**

Aspose.Cells for Python via .NET, ayrıca, dönüştürme sırasında kullanılacak fontun yerine koyulan fontu belirleme imkanı da sunar. Bu mekanizma, gerektiğinde font bulunamadığında faydalıdır. Kullanıcılar, özgün font yerine kullanılacak fontların listesini sağlayabilir. Bunu başarmak için, [**FontConfigs.set_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_substitutes/#str-list) yöntemi kullanılır, bu yöntem 2 parametre alır. İlk parametre, değiştirilecek font adını belirten **string** türündedir. İkinci parametre ise **string** dizisidir ve, kullanıcılar orijinal font adı yerine bu listeden seçim yapabilir.

İşte basit bir kullanım senaryosu.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetCustomFontFolders-FontSubstitution.py" >}}

## **Bilgi Toplama**

Yukarıda anlatılan metodlara ek olarak, Aspose.Cells for Python via .NET API'leri, hangi kaynaklar ve yer değişikliklerinin ayarlandığı hakkında bilgi toplamayı da sağlar.

1. [**FontConfigs.get_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_sources/#) yöntemi, belirtilen yazı tipi kaynaklarının listesini içeren [**FontSourceBase**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsourcebase) türünde bir dizi döndürür. Kaynaklar ayarlanmamışsa, [**FontConfigs.get_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_sources/#) yöntemi boş bir dizi döndürecektir.
1. [**FontConfigs.get_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_substitutes/#str) yöntemi, belirtilen yazı tipi için ayarlama yapılmasını sağlamak için **string** türünde bir parametre kabul eder. Belirtilen yazı tipi için ayarlama yapılmamışsa, [**FontConfigs.get_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_substitutes/#str) yöntemi null döndürecektir.

## **Gelişmiş Konular**
- [Yaygın Olarak Kullanılan Yazı tipini Resimlere Dönüştürürken Belirleme](/cells/tr/python-net/set-default-font-while-rendering-spreadsheet-to-images/)
- [PdfSaveOptions ve ImageOrPrintOptions'ın DefaultFont özelliğini öncelikli şekilde ayarlayın](/cells/tr/python-net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Desteklenen Yazı Tipi Biçimleri](/cells/tr/python-net/supported-font-formats/)
- [Elektronik Tabloyu Görüntüye - Görüntülenen Görüntü İçin Pixel Biçimini Ayarlama](/cells/tr/python-net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)

