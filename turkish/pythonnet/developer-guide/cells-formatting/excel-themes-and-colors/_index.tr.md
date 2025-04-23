---
title: Excel Temaları ve Renkler
type: docs
weight: 100
url: /tr/python-net/excel-themes-and-colors/
description: C# kodu ile Aspose.Cells for Python via .NET API kullanarak Excel Renk Şeması nasıl kullanılır
keywords: C#, Özelleştirilmiş Renk Düzeni Oluşturmak ve Uygulamak için c# Programatik Olarak bir Özel Renk Düzeni Oluşturmak, Programatik Olarak Nasıl Özel Renk Düzeni Uygulanır, c# İle Excel de Renk Düzeni Kullanma
---

## **Excel'de Tema Uygulama ve Oluşturma**
Belge temaları, Excel belgelerinin renklerini, yazı tiplerini ve grafik biçimlendirme efektlerini kolayca koordine etmenizi ve bunları hızlı bir şekilde güncellemenizi sağlar. 
Temalar, bir çalışma kitabında kullanılan adlandırılmış stiller, grafik efektleri ve diğer nesneler ile birleştirilmiş bir görünüm sunar. Örneğin, Accent1 stili, Ofis ve Apex temalarında farklı görünür. Genellikle, bir belge teması uygular ve ardından istediğiniz şekilde değiştirirsiniz.

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

## **Aspose.Cells for Python via .NET'de Renk Şeması Oluşturma ve Uygulama**
Aspose.Cells for Python via .NET, temalar ve renkler özelleştirme özellikleri sunar.

### **Aspose.Cells for Python via .NET'de Özelleştirilmiş Renk Teması Nasıl Oluşturulur**
Dosyada tema renkleri kullanılıyorsa, her bir hücreyi ayrı ayrı değiştirmemize gerek yok, sadece temadaki renkleri değiştirmemiz yeterlidir.

Aşağıdaki örnek, istediğiniz renklerle özel temaları nasıl uygulayacağınızı gösterir. Microsoft Excel 2007'de manuel olarak oluşturulmuş bir örnek şablon dosyası kullanıyoruz.

Aşağıdaki örnek, bir şablon XLSX dosyası yükler, farklı tema renk tipleri için renkleri tanımlar, özel renkleri uygular ve Excel dosyasını kaydeder.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-CustomizeThemes-1.py" >}}

### **Aspose.Cells for Python via .NET'de Tema Renkleri Nasıl Uygulanır**

Aşağıdaki örnek, bir hücrenin ön planı ve yazı tipi renklerini (çalışbook'un varsayılan temasına göre) uygular. Ayrıca Excel dosyasını diske kaydeder.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UtilizeThemeColors-1.py" >}}

### **Aspose.Cells for Python via .NET'de Tema Renkleri Nasıl Alınır ve Ayarlanır**
 Aşağıda temalı renkleri uygulayan ve ayarlayan birkaç yöntem ve özellik bulunmaktadır.

- [**Style.foreground_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_theme_color): Ön plan rengini ayarlamak için kullanılır.
- [**Style.background_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/background_theme_color): Arka plan rengini ayarlamak için kullanılır.
- [**Font.theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/theme_color): Yazı tipi rengini ayarlamak için kullanılır.
- [**Workbook.get_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/get_theme_color): Bir tema rengini almak için kullanılır.
- [**Workbook.set_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/set_theme_color): Bir tema rengini ayarlamak için kullanılır.

Aşağıdaki örnek, temalı renkleri almanın ve ayarlamanın nasıl yapılacağını gösterir.

Aşağıdaki örnek, bir şablon XLSX dosyası kullanır, farklı tema renk tipleri için renkleri alır, renkleri değiştirir ve Microsoft Excel dosyasını kaydeder.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-GetSetThemeColors-1.py" >}}

## **Gelişmiş Konular**
- [Excel Dosyasından Tema Verisi Çıkarın](/cells/tr/python-net/extract-theme-data-from-excel-file/)

