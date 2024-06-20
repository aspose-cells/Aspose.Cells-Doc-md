---
title: GridDesktop ın Varsayılan Yazı Tipi ve Yazı Tipi Rengi
type: docs
weight: 70
url: /tr/net/aspose-cells-griddesktop/default-font-and-font-color-of-the-griddesktop/
keywords: GridDesktop, yazı tipi, renk
description: Bu makale, GridDesktop daki varsayılan fontu ve yazı rengini tanıtır.
---

## **Olası Kullanım Senaryoları**
Bazen, GridDesktop'un varsayılan fontunu ve yazı rengini değiştirmek isteyebilirsiniz. Bu amaçla lütfen aşağıdaki iki özelliği kullanın. Bu özelliklere ihtiyaçlarınıza bağlı olarak Tasarım Zamanında veya Çalışma Zamanında erişebilirsiniz.

- GridDesktop.DefaultCellFont
- GridDesktop.DefaultCellFontColor
## **Tasarım Zamanında Varsayılan Fontu ve Yazı Rengini Değiştirme**
Aşağıdaki ekran görüntüsü, GridDesktop'un Tasarım Zamanında varsayılan fontu ve yazı rengini nasıl değiştireceğinizi göstermektedir.

![todo:image_alt_text](default-font-and-font-color-of-the-griddesktop_1.png)
## **Çalışma Zamanında Varsayılan Fontu ve Yazı Rengini Değiştirme**
Aşağıdaki örnek kod, GridDesktop'un Çalışma Zamanında varsayılan fontunu ve yazı rengini nasıl değiştireceğinizi açıklar.

{{< highlight java >}}

 //Assign your desired Font object to DefaultCellFont property

System.Drawing.Font fnt = new System.Drawing.Font("Arial Black", 18);

this.gridDesktop1.DefaultCellFont = fnt;

//Assign your desired Font color to DefaultCellFontColor property

this.gridDesktop1.DefaultCellFontColor = System.Drawing.Color.Blue;

{{< /highlight >}}
