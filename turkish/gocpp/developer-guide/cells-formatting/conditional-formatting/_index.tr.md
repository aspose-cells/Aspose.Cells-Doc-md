---
title: Golang ile C++ kullanarak Excel ve ODS dosyalarının Koşullu Biçimlendirmelerini Ayarlama
linktitle: Koşullu Biçimler
type: docs
weight: 60
url: /tr/go-cpp/conditional-formatting/
description: C++ ile Excel ve ODS dosyalarına koşullu biçimlendirmeleri nasıl uygularsınız?
keywords: koşullu biçimler uygulayın 
---

## **Giriş**

Koşullu biçimlendirme, bir hücreye veya hücre aralığına biçimler uygulamanıza ve bu biçimlendirmenin hücre değerine veya bir formülün değerine bağlı olarak değişmesine olanak tanıyan gelişmiş bir Microsoft Excel özelliğidir. Örneğin, bir hücrenin değeri 500'den büyük olduğunda hücre kalın görünebilir. Hücre değeri koşulu karşıladığında belirtilen biçim, hücreye uygulanır. Hücre değeri biçim koşulunu karşılamazsa, hücrenin varsayılan biçimlendirmesi kullanılır. Microsoft Excel'de **Biçim**, ardından **Koşullu Biçimlendirme**'yi seçerek Koşullu Biçimlendirme iletişim kutusunu açabilirsiniz.

Aspose.Cells, hücrelere koşullu biçimlendirme uygulamayı destekler. Bu makale, bu konuyu açıklamaktadır. Ayrıca Excel'in renk ölçeği koşullu biçimlendirme için kullandığı rengi nasıl hesapladığını açıklar.

## **Koşullu Biçimlendirme Uygulama**

Aspose.Cells, koşullu biçimlendirme uygulamayı birkaç şekilde destekler:

- Tasarımcı elek tablosu kullanarak
- Kopya yöntemi kullanarak.
- Çalışma zamanında koşullu biçimlendirme oluşturarak.

### **Tasarımcı Elek Tablosu Kullanma**

Geliştiriciler, Microsoft Excel'de koşullu biçimlendirmeler içeren bir tasarımcı elektronik tablo oluşturabilir ve ardından o elektronik tabloyu Aspose.Cells ile açabilirler. Aspose.Cells, tasarımcı elektronik tabloyu yükler ve kaydeder, herhangi bir koşullu biçimlendirme ayarını korur.

### **Kopyalama Yöntemi Kullanımı**

Aspose.Cells, geliştiricilere bir hücreden diğerine koşullu biçimlendirme ayarlarını çağırarak kopyalama imkanı sunar.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConditionalFormatting.go" >}}
## **Çalışma Zamanında Koşullu Biçimlendirme Uygulama**

Aspose.Cells, çalışma zamanında koşullu biçimlendirme eklemeye ve kaldırmaya olanak tanır. Aşağıdaki kod örnekleri, koşullu biçimlendirme ayarlarını nasıl yapacağınızı gösterir:

1. Bir çalışma kitabı örneği oluşturun.
1. Boş bir koşullu biçimlendirme ekleyin.
1. Biçimlendirmenin uygulanması gereken aralığı belirleyin.
1. Biçimlendirme koşullarını tanımlayın.
1. Dosyayı kaydedin.

Bu örneğin ardından, yazı tipi ayarları, kenarlık ayarları ve desen ayarları nasıl uygulanacağını gösteren birçok diğer küçük örnek gelir.

Microsoft Excel 2007, Aspose.Cells'in de desteklediği daha gelişmiş koşullu biçimlendirme ekledi. Buradaki örnekler, basit biçimlendirmeyi nasıl kullanacağınızı gösterir; Microsoft Excel 2007 örnekleri ise daha gelişmiş koşullu biçimlendirmeyi nasıl uygulayabileceğinizi gösterir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConditionalFormatting-1.go" >}}
### **Yazı Tipi Ayarı**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConditionalFormatting-2.go" >}}
{{% alert color="primary" %}}

Yalnızca yazı tipi stili, metin rengi, altı çizili stili ve üstü çizili stili değiştirebilirsiniz.

{{% /alert %}}

### **Sınır Ayarı**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConditionalFormatting-3.go" >}}
{{% alert color="primary" %}}

Yalnızca ince çizgi stillerini dış sınır çizgisine kullanabilirsiniz. Çapraz çizgiler izin verilmez.

{{% /alert %}}

### **Desen Ayarı**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConditionalFormatting-4.go" >}}
## **Gelişmiş Konular**
- [2-Renkli Ölçek ve 3-Renkli Ölçek Koşullu Biçimlendirmeleri Ekle](/cells/tr/cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Gelişmiş Koşullu Biçimlendirme Uygulamak](/cells/tr/cpp/apply-advanced-conditional-formatting/)
- [Çalışma Kitaplarında Koşullu Biçimlendirme Uygulamak](/cells/tr/cpp/apply-conditional-formatting-in-worksheets/)
- [Koşullu Biçimlendirme ile Sıfır Satır ve Sütunlara Gölgelendirme Uygulamak](/cells/tr/cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [Koşullu Biçimlendirme Veri Çubukları Görüntüleri Oluşturmak](/cells/tr/cpp/generate-conditional-formatting-databars-images/)
- [Kullanılan Koşullu Biçimlendirme İkon Setleri, Veri Çubukları veya Renk Ölçekleri Nesnelerini Almak](/cells/tr/cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)
