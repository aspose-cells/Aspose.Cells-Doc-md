---
title: Excel Temaları ve Renkleri
type: docs
weight: 100
url: /tr/net/excel-themes-and-colors/
description: Aspose.Cells for .NET API ile Excel Renk Düzenini kullanmak için C# kodu
keywords: C# to Create and Apply Color Schemes, c# programmatically Create a Custom Color Scheme, programmatically how to Apply a Custom Color Scheme, c# how to Use Color Scheme in excel
---
##  **Excel'de Renk Düzeni Nasıl Uygulanır ve Oluşturulur**
Belge temaları, Excel belgelerinin renklerini, yazı tiplerini ve grafik biçimlendirme efektlerini koordine etmeyi ve bunları hızlı bir şekilde güncellemeyi kolaylaştırır.
Temalar, çalışma kitabında kullanılan adlandırılmış stiller, grafik efektleri ve diğer nesnelerle birleşik bir görünüm sağlar. Örneğin Accent1 stili Office ve Apex temalarında farklı görünüyor. Genellikle bir belge temasını uygular ve ardından onu istediğiniz şekilde değiştirirsiniz.

###  **Excel'de Renk Düzeni Nasıl Uygulanır?**
1. Excel'i açın ve Excel şeridindeki "Sayfa Düzeni" sekmesine gidin.
1. "Temalar" bölümündeki "Renkler" butonuna tıklayın.
<br>
<img src="color.png" width=70% />
1. Gereksinimlerinize uygun bir renk paleti seçin veya canlı bir önizleme görmek için bir şemanın üzerine gelin.

###  **Excel'de Özel Renk Düzeni Nasıl Oluşturulur**
Belgenize yeni, benzersiz bir görünüm kazandırmak veya kuruluşunuzun marka standartlarına uymak için kendi renk setinizi oluşturabilirsiniz.

1. Excel'i açın ve Excel şeridindeki "Sayfa Düzeni" sekmesine gidin.
1. "Temalar" bölümündeki "Renkler" butonuna tıklayın.
1. "Renkleri Özelleştir..." düğmesini tıklayın.
<br>
<img src="color2.png" width=70% />

1. "Yeni Tema Renkleri Oluştur" iletişim kutusunda, her öğenin yanındaki renk açılır menülerine tıklayarak renkleri seçebilirsiniz. Paletten renk seçebilir veya "Diğer Renkler" seçeneğini kullanarak özel renkler tanımlayabilirsiniz.
<br>
<img src="color3.png" width=70% />
1. İstediğiniz tüm renkleri seçtikten sonra "Ad" alanına özel renk düzeniniz için bir ad girin.

1. Özel renk düzeninizi kaydetmek için "Kaydet" düğmesine tıklayın. Özel renk düzeniniz artık ileride kullanmak üzere "Renkler" açılır menüsünde mevcut olacaktır.

##  **Aspose.Cells'de Renk Düzeni Nasıl Oluşturulur ve Uygulanır?**
Aspose.Cells, temaları ve renkleri özelleştirmeye yönelik özellikler sağlar.

###  **Aspose.Cells'de Özel Renk Teması Nasıl Oluşturulur**
Dosyada tema renkleri kullanılıyorsa her hücreyi tek tek değiştirmemize gerek yok, sadece temadaki renkleri değiştirmemiz yeterli.

Aşağıdaki örnek, özel temaların istediğiniz renklerle nasıl uygulanacağını gösterir. Microsoft Excel 2007'de manuel olarak oluşturulan örnek bir şablon dosyasını kullanıyoruz.

Aşağıdaki örnek, bir şablon XLSX dosyası yükler, farklı tema renk türleri için renkleri tanımlar, özel renkleri uygular ve excel dosyasını kaydeder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-CustomizeThemes-1.cs" >}}

###  **Aspose.Cells'de Tema Renkleri Nasıl Uygulanır?**

Aşağıdaki örnek, varsayılan tema (çalışma kitabının) renk türlerine göre bir hücrenin ön plan ve yazı tipi renklerini uygular. Ayrıca excel dosyasını diske kaydeder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-UtilizeThemeColors-1.cs" >}}

###  **Aspose.Cells'de Tema Renkleri Nasıl Alınır ve Ayarlanır**
 Aşağıda tema renklerini uygulayan birkaç yöntem ve özellik bulunmaktadır.

- [**Stil.Ön PlanTemaRenk**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundthemecolor): Ön plan rengini ayarlamak için kullanılır.
- [**Style.BackgroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundthemecolor): Arka plan rengini ayarlamak için kullanılır.
- [**Font.ThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/themecolor): Yazı tipi rengini ayarlamak için kullanılır.
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getthemecolor): Bir tema rengi elde etmek için kullanılır.
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/setthemecolor): Tema rengini ayarlamak için kullanılır.

Aşağıdaki örnekte tema renklerinin nasıl alınacağı ve ayarlanacağı gösterilmektedir.

Aşağıdaki örnekte XLSX şablon dosyası kullanılıyor, farklı tema renk türleri için renkler elde ediliyor, renkler değiştiriliyor ve Microsoft Excel dosyası kaydediliyor.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-GetSetThemeColors-1.cs" >}}

##  **İleri konular**
- [Tema Verilerini Excel Dosyasından Çıkarma](/cells/tr/net/extract-theme-data-from-excel-file/)
