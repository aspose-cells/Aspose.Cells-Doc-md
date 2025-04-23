---
title: Excel Temaları ve Renkler
type: docs
weight: 100
url: /tr/net/excel-themes-and-colors/
description: Aspose.Cells for .NET API ile Excel Renk Düzeni Kullanmak için C# Kodu
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

## **Aspose.Cells'te Renk Şeması Oluşturma ve Uygulama**
Aspose.Cells, temaları ve renkleri özelleştirmek için özellikler sağlar.

### **Aspose.Cells'te Özel Renk Teması Nasıl Oluşturulur**
Dosyada tema renkleri kullanılıyorsa, her bir hücreyi ayrı ayrı değiştirmemize gerek yok, sadece temadaki renkleri değiştirmemiz yeterlidir.

Aşağıdaki örnek, istediğiniz renklerle özel temaları nasıl uygulayacağınızı gösterir. Microsoft Excel 2007'de manuel olarak oluşturulmuş bir örnek şablon dosyası kullanıyoruz.

Aşağıdaki örnek, bir şablon XLSX dosyası yükler, farklı tema renk tipleri için renkleri tanımlar, özel renkleri uygular ve Excel dosyasını kaydeder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-CustomizeThemes-1.cs" >}}

### **Aspose.Cells'te Tema Renklerinin Uygulanması**

Aşağıdaki örnek, bir hücrenin ön planı ve yazı tipi renklerini (çalışbook'un varsayılan temasına göre) uygular. Ayrıca Excel dosyasını diske kaydeder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-UtilizeThemeColors-1.cs" >}}

### **Aspose.Cells'te Tema Renklerinin Alınması ve Ayarlanması**
 Aşağıda temalı renkleri uygulayan ve ayarlayan birkaç yöntem ve özellik bulunmaktadır.

- [**Style.ForegroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundthemecolor): Ön plan rengini ayarlamak için kullanılır.
- [**Style.BackgroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundthemecolor): Arka plan rengini ayarlamak için kullanılır.
- [**Font.ThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/themecolor): Yazı tipi rengini ayarlamak için kullanılır.
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getthemecolor): Bir tema rengini almak için kullanılır.
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/setthemecolor): Bir tema rengini ayarlamak için kullanılır.

Aşağıdaki örnek, temalı renkleri almanın ve ayarlamanın nasıl yapılacağını gösterir.

Aşağıdaki örnek, bir şablon XLSX dosyası kullanır, farklı tema renk tipleri için renkleri alır, renkleri değiştirir ve Microsoft Excel dosyasını kaydeder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-GetSetThemeColors-1.cs" >}}

## **Gelişmiş Konular**
- [Excel Dosyasından Tema Verisi Çıkarın](/cells/tr/net/extract-theme-data-from-excel-file/)
{{< app/cells/assistant language="csharp" >}}
