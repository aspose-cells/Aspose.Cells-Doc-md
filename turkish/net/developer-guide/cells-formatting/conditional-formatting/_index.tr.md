---
title: Excel ve ODS dosyalarının Koşullu Biçimlerini ayarlayın.
linktitle: Koşullu Biçimler
type: docs
weight: 60
url: /tr/net/conditional-formatting/
description: CSharp'ta koşullu biçimler Excel ve ODS dosyalarına nasıl uygulanır?
keywords: apply conditional formats 
---
## **giriiş**

 Koşullu biçimlendirme, bir hücreye veya hücre aralığına biçimler uygulamanıza ve bu biçimlendirmenin hücrenin değerine veya bir formülün değerine göre değişmesini sağlayan gelişmiş bir Microsoft Excel özelliğidir. Örneğin, bir hücrenin yalnızca değeri 500'den büyük olduğunda kalın görünmesini sağlayabilirsiniz. Hücrenin değeri koşulu sağladığında, hücreye belirtilen biçim uygulanır. Hücrenin değeri biçim koşulunu karşılamıyorsa, hücrenin varsayılan biçimlendirmesi kullanılır. Microsoft Excel'de seçin**Biçim** , sonra**Koşullu biçimlendirme** Koşullu Biçimlendirme iletişim kutusunu açmak için.

Aspose.Cells, çalışma zamanında hücrelere koşullu biçimlendirme uygulanmasını destekler. Bu makale nasıl yapılacağını açıklıyor. Ayrıca renk ölçeği koşullu biçimlendirme için Excel tarafından kullanılan rengin nasıl hesaplanacağını da açıklar.

## **Koşullu Biçimlendirme Uygulamak**

Aspose.Cells, koşullu biçimlendirmeyi birkaç şekilde destekler:

- Tasarımcı e-tablosunu kullanma
- Kopyalama yöntemini kullanma.
- Çalışma zamanında koşullu biçimlendirme oluşturma.

### **Tasarımcı Elektronik Tablosunu Kullanma**

Geliştiriciler, Microsoft Excel'de koşullu biçimlendirme içeren bir tasarımcı elektronik tablosu oluşturabilir ve ardından bu elektronik tabloyu Aspose.Cells ile açabilir. Aspose.Cells, tüm koşullu biçimlendirme ayarlarını koruyarak tasarımcı elektronik tablosunu yükler ve kaydeder.

### **Kopyalama Yöntemini Kullanma**

 Aspose.Cells, geliştiricilerin koşullu biçim ayarlarını çalışma sayfasındaki bir hücreden diğerine kopyalamasına olanak tanır.[**Aralık.Kopya()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index) yöntem.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-UsingCopyMethod-1.cs" >}}

## **Çalışma Zamanında Koşullu Biçimlendirme Uygulamak**

Aspose.Cells, çalışma zamanında hem koşullu biçimlendirme eklemenizi hem de kaldırmanızı sağlar. Aşağıdaki kod örnekleri, koşullu biçimlendirmenin nasıl ayarlanacağını gösterir:

1. Bir çalışma kitabı örneği oluşturun.
1. Boş bir koşullu biçim ekleyin.
1. Biçimlendirmenin uygulanacağı aralığı ayarlayın.
1. Biçimlendirme koşullarını tanımlayın.
1. Dosya 'yı kaydet.

Bu örnekten sonra, yazı tipi ayarlarının, kenarlık ayarlarının ve desenlerin nasıl uygulanacağını gösteren bir dizi daha küçük örnek gelir.

Microsoft Excel 2007, Aspose.Cells'in de desteklediği daha gelişmiş koşullu biçimlendirme ekledi. Buradaki örnekler basit biçimlendirmenin nasıl kullanılacağını göstermektedir, Microsoft Excel 2007 örnekleri daha gelişmiş koşullu biçimlendirmenin nasıl uygulanacağını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConditionalFormattingatRuntime-1.cs" >}}

### **Yazı Tipi Ayarla**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-1.cs" >}}

{{% alert color="primary" %}}

Yalnızca yazı tipi stilini, metin rengini, altı çizili stili ve üzeri çizili stili değiştirebilirsiniz.

{{% /alert %}}

### **Kenarlığı Ayarla**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetBorder-1.cs" >}}

{{% alert color="primary" %}}

Anahat kenarlığında yalnızca ince çizgi stillerini kullanabilirsiniz. Çapraz çizgilere izin verilmez.

{{% /alert %}}

### **Deseni Ayarla**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetPattern-1.cs" >}}

## **ileri konular**
- [2-Renk Skalası ve 3-Renk Skalası Koşullu Biçimlendirmeleri Ekleme](/cells/tr/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Gelişmiş Koşullu Biçimlendirmeyi Uygula](/cells/tr/net/apply-advanced-conditional-formatting/)
- [Çalışma Sayfalarında Koşullu Biçimlendirme Uygula](/cells/tr/net/apply-conditional-formatting-in-worksheets/)
- [Koşullu Biçimlendirme ile Alternatif Satırlara ve Sütunlara Gölgelendirme Uygulayın](/cells/tr/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [Koşullu Biçimlendirme Veri Çubukları Görüntüleri Oluşturun](/cells/tr/net/generate-conditional-formatting-databars-images/)
- [Koşullu Biçimlendirmede kullanılan Simge Setlerini, Veri Çubuklarını veya Renk Ölçeklerini Alın](/cells/tr/net/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)

