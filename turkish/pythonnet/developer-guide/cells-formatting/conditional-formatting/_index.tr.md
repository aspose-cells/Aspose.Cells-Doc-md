---
title: Excel ve ODS dosyalarının Koşullu Biçimlerini Ayarlayın.
linktitle: Koşullu Biçimler
type: docs
weight: 60
url: /tr/python-net/conditional-formatting/
description: Python da Excel ve ODS dosyalarına koşullu biçimlendirme nasıl uygulanır.
keywords: koşullu biçimler uygulayın 
---

## **Giriş**

Koşullu biçimlendirme, bir hücreye veya hücre aralığına biçimler uygulamanıza ve bu biçimlendirmenin hücre değerine veya bir formülün değerine bağlı olarak değişmesine olanak tanıyan gelişmiş bir Microsoft Excel özelliğidir. Örneğin, bir hücrenin değeri 500'den büyük olduğunda hücre kalın görünebilir. Hücre değeri koşulu karşıladığında belirtilen biçim, hücreye uygulanır. Hücre değeri biçim koşulunu karşılamazsa, hücrenin varsayılan biçimlendirmesi kullanılır. Microsoft Excel'de **Biçim**, ardından **Koşullu Biçimlendirme**'yi seçerek Koşullu Biçimlendirme iletişim kutusunu açabilirsiniz.

Aspose.Cells for Python via .NET, çalışma zamanında hücrelere koşullu biçimlendirme uygulamayı destekler. Bu makale, nasıl yapıldığını açıklar. Ayrıca, Excel'in renk skalası koşullu biçimlendirme için kullanılan rengi nasıl hesaplayacağınızı da anlatır.

## **Koşullu Biçimlendirme Uygulama**

Aspose.Cells for Python via .NET, çeşitli şekillerde koşullu biçimlendirmeyi destekler:

- Tasarımcı elek tablosu kullanarak
- Kopya yöntemi kullanarak.
- Çalışma zamanında koşullu biçimlendirme oluşturarak.

### **Tasarımcı Elek Tablosu Kullanma**

Geliştiriciler, Microsoft Excel'de koşullu biçimlendirme içeren bir tasarımcı çalışma kitabı oluşturabilir ve ardından bu çalışma kitabını Aspose.Cells for Python via .NET ile açabilir. Aspose.Cells for Python via .NET, tasarımcı çalışma kitabını yükler ve kaydeder, herhangi bir koşullu biçimlendirme ayarını korur.

### **Kopyalama Yöntemi Kullanımı**

Aspose.Cells for Python via .NET, bir hücreden diğerine koşullu biçimlendirme ayarlarını kopyalamayı `[**Range.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy)` yöntemi çağırarak sağlar.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingCopyMethod-1.py" >}}

## **Çalışma Zamanında Koşullu Biçimlendirme Uygulama**

Aspose.Cells for Python via .NET, çalışma zamanında koşullu biçimlendirmeyi ekleme ve kaldırma imkanı sunar. Aşağıdaki kod örnekleri, koşullu biçimlendirmeyi nasıl ayarlayacağınızı gösterir:

1. Bir çalışma kitabı örneği oluşturun.
1. Boş bir koşullu biçimlendirme ekleyin.
1. Biçimlendirmenin uygulanması gereken aralığı belirleyin.
1. Biçimlendirme koşullarını tanımlayın.
1. Dosyayı kaydedin.

Bu örneğin ardından, yazı tipi ayarları, kenarlık ayarları ve desen ayarları nasıl uygulanacağını gösteren birçok diğer küçük örnek gelir.

Microsoft Excel 2007, Aspose.Cells for Python via .NET tarafından da desteklenen daha gelişmiş koşullu biçimlendirme ekledi. Buradaki örnekler, basit biçimlendirmeyi nasıl kullanacağınızı gösterirken, Microsoft Excel 2007 örnekleri daha gelişmiş koşullu biçimlendirmeleri uygulamanın yollarını gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConditionalFormattingatRuntime-1.py" >}}

### **Yazı Tipi Ayarı**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontStyle-1.py" >}}

{{% alert color="primary" %}}

Yalnızca yazı tipi stili, metin rengi, altı çizili stili ve üstü çizili stili değiştirebilirsiniz.

{{% /alert %}}

### **Sınır Ayarı**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetBorder-1.py" >}}

{{% alert color="primary" %}}

Yalnızca ince çizgi stillerini dış sınır çizgisine kullanabilirsiniz. Çapraz çizgiler izin verilmez.

{{% /alert %}}

### **Desen Ayarı**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetPattern-1.py" >}}

## **Gelişmiş Konular**
- [2-Renkli Ölçek ve 3-Renkli Ölçek Koşullu Biçimlendirmeleri Ekle](/cells/tr/python-net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Çalışma Kitaplarında Koşullu Biçimlendirme Uygulamak](/cells/tr/python-net/apply-conditional-formatting-in-worksheets/)
- [Koşullu Biçimlendirme ile Sıfır Satır ve Sütunlara Gölgelendirme Uygulamak](/cells/tr/python-net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [Koşullu Biçimlendirme Veri Çubukları Görüntüleri Oluşturmak](/cells/tr/python-net/generate-conditional-formatting-databars-images/)
- [Kullanılan Koşullu Biçimlendirme İkon Setleri, Veri Çubukları veya Renk Ölçekleri Nesnelerini Almak](/cells/tr/python-net/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)

{{< app/cells/assistant language="csharp" >}}
{{< app/cells/assistant language="python-net" >}}
