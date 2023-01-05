---
title: Excel Temaları ve Renkleri
type: docs
weight: 130
url: /tr/java/excel-2007-themes-and-colors/
---
{{% alert color="primary" %}}

Temalar, bir çalışma kitabında kullanılan adlandırılmış stiller, grafik efektler ve diğer nesnelerle birleşik bir görünüm sağlar. Örneğin, Accent1 stili Office ve Apex temalarında farklı görünüyor. Genellikle, bir belge teması uygularsınız ve ardından onu ihtiyaçlarınıza göre değiştirirsiniz.

**Microsoft Excel'de temaları uygulama**

![yapılacaklar:resim_alternatif_metin](excel-2007-themes-and-colors_1.png)

{{% /alert %}}

## **Tema Renklerini Alma ve Ayarlama**

Aspose.Cells API'ler, temaları ve renkleri özelleştirmek için özellikler sağlar. Aşağıda, tema renklerini uygulayan birkaç yöntem ve özellik bulunmaktadır.

- Style.ForegroundThemeColor özelliği, ön plan rengini ayarlamak için kullanılabilir.
- Style.BackgroundThemeColor özelliği, arka plan rengini ayarlamak için kullanılabilir.
- Font.ThemeColor özelliği, yazı tipi rengini ayarlamak için kullanılabilir.
- Workbook.getThemeColor yöntemi, bir tema rengi elde etmek için kullanılabilir.
- Workbook.setThemeColor yöntemi, bir tema rengi ayarlamak için kullanılabilir.

Aşağıdaki örnek, tema renklerinin nasıl alınacağını ve ayarlanacağını gösterir.

Aşağıdaki örnek, bir şablon XLSX dosyasını kullanır, farklı tema renk türleri için renkleri alır, renkleri değiştirir ve Microsoft Excel dosyasını kaydeder.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSetThemeColors-GetSetThemeColors.java" >}}

### **Temaları Özelleştirme**

Aşağıdaki örnek, istediğiniz renklerle özel temaların nasıl uygulanacağını gösterir. Örnekte, Microsoft Excel 2007'de el ile oluşturulmuş örnek bir şablon dosyası kullanılmıştır.

**Şablon CustomThemeColor.xlsx dosyası**

![yapılacaklar:resim_alternatif_metin](excel-2007-themes-and-colors_2.png)

Aşağıdaki örnek, bir şablon XLSX dosyası yükler, farklı tema renk türleri için renkleri tanımlar, özel renkleri uygular ve excel dosyasını kaydeder.

**Özelleştirilmiş tema renkleri ile oluşturulan dosya**

![yapılacaklar:resim_alternatif_metin](excel-2007-themes-and-colors_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomizingThemes-CustomizingThemes.java" >}}

### **Tema Renklerini Kullanma**

Aşağıdaki örnek, varsayılan tema (çalışma kitabının) renk türlerine göre bir hücrenin ön planı ve yazı tipi renklerini uygular. Ayrıca excel dosyasını diskete kaydeder.

Kod yürütülürken aşağıdaki çıktı oluşturulur.

**Çalışma sayfasının D3 hücresine uygulanan tema renkleri** 

![yapılacaklar:resim_alternatif_metin](excel-2007-themes-and-colors_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseThemeColors-UseThemeColors.java" >}}

## **ileri konular**
- [Tema Verilerini Excel Dosyasından Çıkarın](/cells/tr/java/extract-theme-data-from-excel-file/)
