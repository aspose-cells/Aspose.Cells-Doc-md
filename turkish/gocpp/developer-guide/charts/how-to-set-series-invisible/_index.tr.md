---
title: Golang kullanarak C++ ile Seriyi görünmez yapma nasıl yapılır
linktitle: Seriyi görünmez yapma
description: Excel grafiklerinde, seriyi görünmez yapmanız gerekebilir. Bu makale, Golang kullanarak C++ ile Aspose.Cells i nasıl kullanacağınızı anlatmaktadır.
keywords: Excel grafiği, Seri, Görünmez, Filtre edildi.
type: docs
weight: 74
url: /tr/go-cpp/how-to-set-series-invisible/
---

## Excel Grafiğinde Seriyi görünmez yapma

Excel grafiğinde, bir grafiğe sağ tıklayın, "Veri Seç"e tıklayın ve açılan pencerede, seriyi görünür olup olmadığını işaretleyerek veya işareti kaldırarak ayarlayabilirsiniz. Aşağıdaki [örnek dosyayı](SeriesFiltered.xlsx) indirebilir ve figürde gösterildiği gibi Excel'de kullanarak bu fonksiyonu gerçekleştirebilirsiniz. Şimdi, bunu Aspose.Cells kütüphanesini kullanarak nasıl yapacağınızı anlatacağız.

![todo:image_alt_text](series-invisible.png)

## Aspose.Cells kullanarak seriyi görünmez yapma 

Aspose.Cells kullanarak seriyi görünmez yapmak için aşağıdaki kodu kullanıyoruz:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetSeriesInvisible.go" >}}
Aşağıdaki [girdi dosyasını](SeriesFiltered.xlsx) ve [çıktı dosyasını](output.xlsx) edinebilirsiniz.

Aşağıdaki şekilde gösterildiği gibi, orijinalde görünür olan ilk iki seri, çıktı dosyasında görünmez hale geldi.  
![todo:image_alt_text](output.png)
