---
title: GridDesktop'un Varsayılan Yazı Tipi ve Yazı Tipi Rengi
type: docs
weight: 70
url: /tr/net/default-font-and-font-color-of-the-griddesktop/
---
## **Olası Kullanım Senaryoları**
Bazen, GridDesktop'un varsayılan yazı tipini ve yazı tipi rengini değiştirmek istersiniz. Lütfen bu amaç için aşağıdaki iki özelliği kullanın. Bu özelliklere, ihtiyaçlarınıza bağlı olarak Tasarım Zamanında veya Çalışma Zamanında erişebilirsiniz.

- GridDesktop.DefaultCellFont
- GridDesktop.DefaultCellFontColor
## **Tasarım Zamanında Varsayılan Yazı Tipi ve Yazı Tipi Rengini Değiştirme**
Aşağıdaki ekran görüntüsü, Tasarım Zamanında GridDesktop'un varsayılan yazı tipini ve yazı tipi rengini nasıl değiştireceğinizi gösterir.

![yapılacaklar:resim_alternatif_metin](default-font-and-font-color-of-the-griddesktop_1.png)
## **Çalışma Zamanında Varsayılan Yazı Tipi ve Yazı Tipi Rengini Değiştirme**
Aşağıdaki örnek kod, Çalışma Zamanında GridDesktop'un varsayılan yazı tipini ve yazı tipi rengini nasıl değiştireceğinizi açıklar.

{{< highlight "java" >}}

 //Assign your desired Font object to DefaultCellFont property

System.Drawing.Font fnt = new System.Drawing.Font("Arial Black", 18);

this.gridDesktop1.DefaultCellFont = fnt;

//Assign your desired Font color to DefaultCellFontColor property

this.gridDesktop1.DefaultCellFontColor = System.Drawing.Color.Blue;

{{< /highlight >}}
