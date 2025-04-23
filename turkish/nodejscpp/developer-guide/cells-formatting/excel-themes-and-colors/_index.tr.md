---  
title: Excel Temaları ve Renkler
linktitle: Excel Temaları ve Renkler  
type: docs  
weight: 100  
url: /tr/nodejs-cpp/excel-themes-and-colors/  
description: Aspose.Cells for Node.js via C++ ile özel renk şemalarını nasıl kullanacağınızı öğrenin.  
keywords: Node.js Renk Düzeni Oluştur ve Uygula, Node.js programlama ile Özelleştirilmiş Renk Düzeni Oluştur, programlı nasıl Özelleştirilmiş Renk Düzeni Uygulanır Node.js, Node.js de Renk Düzeni nasıl Kullanılır Excel de  
---  

## **Excel'de Tema Uygulama ve Oluşturma**  
Belge temaları, Excel belgelerinin renklerini, yazı tiplerini ve grafik biçimlendirme efektlerini kolayca koordine etmenizi ve bunları hızlı bir şekilde güncellemenizi sağlar.  
Temalar, kitapçıkta kullanılan isimlendirilmiş stiller, grafik efektleri ve diğer nesnelerle birleşik bir görünüm sağlar. Örneğin, Accent1 stili Office ve Apex temalarında farklı görünür. Sıkça, bir belge teması uygular ve ardından istediğiniz gibi değiştirirsiniz.  

### **Excel'de Bir Renk Şeması Nasıl Uygulanır**  
1. Excel'i açın ve Excel menü şeridinde "Sayfa Düzeni" sekmesine gidin.  
1. "Temalar" bölümündeki "Renkler" düğmesine tıklayın.  
<br>  
<img src="color.png" width=70% />  
1. Gereksinimlerinize uygun bir renk paleti seçin veya canlı bir önizleme görmek için şema üzerinde gezdirin.  

### **Excel'de Özel Renk Şeması Nasıl Oluşturulur**  
Belgenize taze, benzersiz bir görünüm vermek veya kuruluşunuzun marka standartlarına uygun olmak için kendi renk setinizi oluşturabilirsiniz.  

1. Excel'i açın ve Excel menü şeridinde "Sayfa Düzeni" sekmesine gidin.  
1. "Temalar" bölümündeki "Renkler" düğmesine tıklayın.  
1. "Renkleri Özelleştir..." düğmesine tıklayın.  
<br>  
<img src="color2.png" width=70% />  

1. "Yeni Tema Renkleri Oluştur" iletişim kutusunda, her bir öğe için renk seçmek için yanlarındaki renk açılır listelerine tıklayabilirsiniz. Renkleri paletten seçebilir veya "Daha Fazla Renkler" seçeneğini kullanarak özel renkler tanımlayabilirsiniz.  
<br>  
<img src="color3.png" width=70% />  
1. Tüm istenen renkleri seçtikten sonra, özel renk şemanıza bir ad sağlamak için "Ad" alanına bir ad girin.  

1. Özel renk şemanızı kaydetmek için "Kaydet" düğmesine tıklayın. Özel renk şemanız artık gelecekte kullanılmak üzere "Renkler" açılır menüsünde mevcut olacaktır.  

## **Aspose.Cells'te Renk Şeması Oluşturma ve Uygulama**  
Aspose.Cells, temaları ve renkleri özelleştirmek için özellikler sağlar.  

### **Aspose.Cells'te Özel Renk Teması Nasıl Oluşturulur**  
Eğer dosyada tema renkleri kullanıldıysa, her hücreyi ayrı ayrı değiştirmemize gerek kalmaz; temanın renklerini değiştiririz.  

Aşağıdaki örnek, istediğiniz renklerle özel temaları nasıl uygulayacağınızı gösterir. Microsoft Excel 2007'de manuel olarak oluşturulmuş bir örnek şablon dosyası kullanıyoruz.  

Aşağıdaki örnek, bir şablon XLSX dosyasını yükler, farklı tema renk türleri için renkleri tanımlar, özelleştirilmiş renkleri uygular ve Excel dosyasını kaydeder.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-CreateCustomColorTheme.js" >}}



### **Aspose.Cells'te Tema Renklerinin Uygulanması**  
Aşağıdaki örnek, bir hücrenin ön plan ve yazı tipi renklerini varsayılan tema renk türlerine göre uygular. Ayrıca, Excel dosyasını diske kaydeder.  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-ApplyThemeColors.js" >}}


### **Aspose.Cells'te Tema Renklerinin Alınması ve Ayarlanması**  
Aşağıda temalı renkleri uygulayan ve ayarlayan birkaç yöntem ve özellik bulunmaktadır.  

- [**Style.setForegroundThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundThemeColor-themecolor-): Ön plan rengini ayarlamak için kullanılır.  
- [**Style.setBackgroundThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setBackgroundThemeColor-themecolor-): Arka plan rengini ayarlamak için kullanılır.  
- [**Font.setThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setThemeColor-themecolor-): Yazı tipi rengini ayarlamak için kullanılır.  
- [**Workbook.getThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getThemeColor-themecolortype-): Tema rengini almak için kullanılır.  
- [**Workbook.setThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#setThemeColor-themecolortype-color-): Tema rengini ayarlamak için kullanılır.  

Aşağıdaki örnek, temalı renkleri almanın ve ayarlamanın nasıl yapılacağını gösterir.  

Aşağıdaki örnek, şablon XLSX dosyasını kullanır, farklı tema renkleri için renkleri alır, renkleri değiştirir ve Microsoft Excel dosyasını kaydeder.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-GetAndSetThemeColors.js" >}}


## **Gelişmiş Konular**  
- [Excel Dosyasından Tema Verisi Çıkarın](/cells/tr/nodejs-cpp/extract-theme-data-from-excel-file/)  

