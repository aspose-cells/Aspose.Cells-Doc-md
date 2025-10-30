---  
title: Excel ve ODS dosyalarının Koşullu Biçimlendirmelerini ayarla
linktitle: Koşullu Biçimler  
type: docs  
weight: 60  
url: /tr/nodejs-cpp/conditional-formatting/  
description: Node.js via C++ kullanarak Excel ve ODS dosyalarına koşullu biçimlendirme nasıl uygulanır.  
keywords: koşullu biçimlendirme uygulama Node.js via C++  
---  

## **Giriş**

Koşullu biçimlendirme, bir hücreye veya hücre aralığına biçim uygulamanıza ve bu biçimin hücrenin değeri veya bir formülin değeri ne olursa olsun değişmesine olanak tanıyan gelişmiş bir özelliktir. Örneğin, bir hücre değeri 500'den büyük olduğunda kalın görünmesini sağlayabilirsiniz. Hücrenin değeri koşulu karşıladığında, belirtilen biçim hücreye uygulanır. Hücrenin değeri koşulu karşılamıyorsa, hücrenin varsayılan biçimi kullanılır. Microsoft Excel'de, **Biçim** seçin, ardından **Koşullu Biçimlendirme** diyaloğunu açmak için tıklayın.

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

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-CopyConditionalFormattsByCopyRange.js" >}}


## **Çalışma Zamanında Koşullu Biçimlendirme Uygulama**

Aspose.Cells, çalışma zamanında koşullu biçimlendirme eklemeye ve kaldırmaya olanak tanır. Aşağıdaki kod örnekleri, koşullu biçimlendirme ayarlarını nasıl yapacağınızı gösterir:

1. Bir çalışma kitabı örneği oluşturun.
1. Boş bir koşullu biçimlendirme ekleyin.
1. Biçimlendirmenin uygulanması gereken aralığı belirleyin.
1. Biçimlendirme koşullarını tanımlayın.
1. Dosyayı kaydedin.

Bu örneğin ardından, yazı tipi ayarları, kenarlık ayarları ve desen ayarları nasıl uygulanacağını gösteren birçok diğer küçük örnek gelir.

Microsoft Excel 2007, daha gelişmiş koşullu biçimlendirmeyi ekledi ve Aspose.Cells bunu da destekler. Buradaki örnekler, basit biçimlendirmeyi nasıl kullanacağınızı gösterirken, Microsoft Excel 2007 örnekleri daha gelişmiş koşullu biçimlendirme uygulamanın yollarını gösterir.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyingConditionalFormattingAtRuntime.js" >}}


### **Yazı Tipi Ayarı**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetFont.js" >}}



{{% alert color="primary" %}}

Yalnızca yazı tipi stili, metin rengi, altı çizili stili ve üstü çizili stili değiştirebilirsiniz.

{{% /alert %}}

### **Sınır Ayarı**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetBorder.js" >}}


{{% alert color="primary" %}}

Sadece ince çizgi stili sınır sınırı için kullanılabilir. Köşegen çizgiler izin verilmez.

{{% /alert %}}

### **Desen Ayarı**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetPattern.js" >}}



## **Gelişmiş Konular**  
- [2-Renkli Ölçek ve 3-Renkli Ölçek Koşullu Biçimlendirmeleri Ekle](/cells/tr/nodejs-cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/)  
- [Çalışma Kitaplarında Koşullu Biçimlendirme Uygulamak](/cells/tr/nodejs-cpp/apply-conditional-formatting-in-worksheets/)  
- [Koşullu Biçimlendirme ile Sıfır Satır ve Sütunlara Gölgelendirme Uygulamak](/cells/tr/nodejs-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)  
- [Koşullu Biçimlendirme Veri Çubukları Görüntüleri Oluşturmak](/cells/tr/nodejs-cpp/generate-conditional-formatting-databars-images/)  
- [Kullanılan Koşullu Biçimlendirme İkon Setleri, Veri Çubukları veya Renk Ölçekleri Nesnelerini Almak](/cells/tr/nodejs-cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
