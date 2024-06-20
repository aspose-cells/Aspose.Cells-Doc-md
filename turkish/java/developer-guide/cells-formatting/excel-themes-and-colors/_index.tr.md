---
title: Excel Temaları ve Renkler
type: docs
weight: 130
url: /tr/java/excel-2007-themes-and-colors/
---

{{% alert color="primary" %}}

Temalar, bir çalışma kitabında kullanılan adlandırılmış stiller, grafiksel efektler ve diğer nesnelerle birlikte birleştirilmiş bir görünüm sunar. Örneğin, Accent1 stili, Ofis ve Apex temalarında farklı görünür. Genellikle bir belge teması uygular ve ardından ihtiyaçlarınıza göre değiştirirsiniz.

Microsoft Excel'de Temaların Uygulanması

![todo:image_alt_text](excel-2007-themes-and-colors_1.png)

{{% /alert %}}

## **Temaların Alınması ve Ayarlanması**

Aspose.Cells API'leri, temaları ve renkleri özelleştirmek için özellikler sağlar. Aşağıda tema renklerini uygulayan birkaç yöntem ve özellik bulunmaktadır.

- Style.ForegroundThemeColor özelliği önyüz rengini ayarlamak için kullanılabilir.
- Style.BackgroundThemeColor özelliği arka plan rengini ayarlamak için kullanılabilir.
- Font.ThemeColor özelliği yazı tipi rengini ayarlamak için kullanılabilir.
- Workbook.getThemeColor yöntemi bir tema rengi almak için kullanılabilir.
- Workbook.setThemeColor yöntemi bir tema rengi ayarlamak için kullanılabilir.

Aşağıdaki örnek, temalı renkleri almanın ve ayarlamanın nasıl yapılacağını gösterir.

Aşağıdaki örnek, bir şablon XLSX dosyası kullanır, farklı tema renk tipleri için renkleri alır, renkleri değiştirir ve Microsoft Excel dosyasını kaydeder.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSetThemeColors-GetSetThemeColors.java" >}}

### **Temaları Özelleştirme**

Aşağıdaki örnek, istediğiniz renklerle özel temaların nasıl uygulanacağını göstermektedir. Örnek, Microsoft Excel 2007'de manuel olarak oluşturulan bir örnek şablon dosyasını kullanır.

**ÖzelTemaRengi.xlsx dosyası**

![todo:image_alt_text](excel-2007-themes-and-colors_2.png)

Aşağıdaki örnek, bir şablon XLSX dosyası yükler, farklı tema renk tipleri için renkleri tanımlar, özel renkleri uygular ve Excel dosyasını kaydeder.

**Özelleştirilmiş tema renkleriyle oluşturulan dosya**

![todo:image_alt_text](excel-2007-themes-and-colors_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomizingThemes-CustomizingThemes.java" >}}

### **Tema Renklerini Kullanma**

Aşağıdaki örnek, bir hücrenin ön planı ve yazı tipi renklerini (çalışbook'un varsayılan temasına göre) uygular. Ayrıca Excel dosyasını diske kaydeder.

Kodu çalıştırdığınızda aşağıdaki çıktı oluşturulur.

**Çalışma sayfasının D3 hücresine uygulanan tema renkleri** 

![todo:image_alt_text](excel-2007-themes-and-colors_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseThemeColors-UseThemeColors.java" >}}

## **Gelişmiş Konular**
- [Excel Dosyasından Tema Verisi Çıkarın](/cells/tr/java/extract-theme-data-from-excel-file/)
