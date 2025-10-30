---
title: Golang kullanarak C++ ile Grafik Bütünleştirme Ayarları Sınıfını kullanarak Grafik Bileşeni için Farklı Dil Ayarlama
linktitle: ChartGlobalizationSettings Sınıfını Kullanma
description: Aspose.Cells for C++ te ChartGlobalizationSettings sınıfını kullanarak grafik bileşenleri için farklı diller nasıl ayarlanır, öğrenin. Rehberimiz, grafik öğelerini, etiketleri ve açıklamaları farklı dillere nasıl yerelleştirileceğini anlamanıza yardımcı olacak, böylece verilerinizi kültürel açıdan uygun şekilde sunabilirsiniz.
keywords: Aspose.Cells for C++, grafik oluşturma, grafik uluslararasılaştırma, diller, yerelleştirme, ChartGlobalizationSettings, öğeler, etiketler, açıklamalar
type: docs
weight: 2200
url: /tr/go-cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells API'ları, kullanıcının bir grafik bileşenini farklı bir dile ayarlamak istediği senaryolarla başa çıkmak için [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/) sınıfını açığa çıkarmıştır. bir elektronik tabloda Ara Toplamlar için özel etiketler. 

## **ChartGlobalizationSettings Sınıfına Giriş**

[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/) sınıfı şu anda özel bir sınıfta üzerine yazılabilecek aşağıdaki 8 yöntemi sunar; bu yöntemler, AxisTitle adı, AxisUnit adı, ChartTitle adı ve benzeri isimleri farklı dillere çevirmek için kullanılabilir.

1. [**GetAxisTitleName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getaxistitlename/): Eksen için Başlık adını alır.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getaxisunitname/): Eksen Birimi için Adı alır.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getcharttitlename/): Grafik Başlığının adını alır.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegenddecreasename/): Efsane için Azalma adını alır.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegendincreasename/): Efsane için Artış adını alır.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getlegendtotalname/): Efsane için Toplam adını alır.
1. [**GetOtherName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getothername/): Grafikte "Diğer" etiketlerinin adını alır.
1. [**GetSeriesName**](https://reference.aspose.com/cells/go-cpp/chartglobalizationsettings/getseriesname/): Grafikteki Serilerin adını alır.

### **Özel dil çevirisi**
Burada, aşağıdaki verilere dayalı bir su dalgası grafiği oluşturacağız. Grafik bileşenlerinin adları, İngilizce olarak grafikte gösterilecektir. Grafik Başlığı, Efsane Artış/Azalma adları, Toplam adı ve Eksen Başlığı'nın Türkçe olarak nasıl gösterileceğini göstermek için bir Türkçe dil örneği kullanacağız.

![todo:image_alt_text](sample.png)

## **Örnek Kod**
Aşağıdaki örnek kod, [örnek Excel dosyasını](waterfall.xlsx) yükler.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChartGlobalizationSettings.go" >}}
Örneğin ürettiği çıktı

Yukarıdaki örnek kodun konsol çıktısı budur.

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
