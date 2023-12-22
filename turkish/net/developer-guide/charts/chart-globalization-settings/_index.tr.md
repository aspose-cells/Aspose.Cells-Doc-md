---
title:  Grafik Bileşeni için Farklı Dil Ayarlamak amacıyla ChartGlobalizationSettings Sınıfını Kullanma
description: Grafik bileşenleri için farklı diller ayarlamak üzere Aspose.Cells for .NET numaralı telefondan ChartGlobalizationSettings sınıfını nasıl kullanacağınızı öğrenin. Kılavuzumuz, grafik öğelerini, etiketleri ve açıklamaları farklı dillere nasıl yerelleştireceğinizi anlamanıza yardımcı olacak ve verilerinizi kültürel açıdan uygun bir şekilde sunmanıza olanak tanıyacaktır.
keywords: Aspose.Cells for .NET, charting, chart globalization, languages, localization, ChartGlobalizationSettings, elements, labels, legends.
type: docs
weight: 2200
url: /tr/net/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---
##  **Olası Kullanım Senaryoları**

 Aspose.Cells API'ler şunları ortaya çıkardı:[**GrafikKüreselleşmeAyarlar**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) Kullanıcının grafik bileşenini farklı dile ayarlamak istediği senaryolarla başa çıkmak için sınıf. Bir elektronik tablodaki Alt Toplamlar için özel etiketler.

##  **ChartGlobalizationSettings Sınıfına Giriş**

[**GrafikKüreselleşmeAyarlar**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)class şu anda AxisTitle adı, AxisUnit adı, ChartTitle adı vb. gibi farklı dillere çevrilmek üzere özel bir sınıfta geçersiz kılınabilecek aşağıdaki 8 yöntemi sunmaktadır.
1. [**GetAxisTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): Eksen Başlığının adını alır.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): Eksen Biriminin Adını alır.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): Grafik Başlığının adını alır.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): Efsaneye Azalma adını alır.
1. [**GetLegendArtışAdı**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): Efsaneye artış adını alır.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): Legend için Total ismini alır.
1. [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getothername/): Grafik için "Diğer" etiketlerinin adını alır.
1. [**GetSeriesName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getseriesname/): Grafikteki Serinin adını alır.

###  **Özel dil çevirisi**
Burada aşağıdaki verilere dayanarak şelale grafiği oluşturacağız. Grafik bileşenlerinin adları grafikte İngilizce olarak görüntülenecektir. Grafik Başlığı, Gösterge Arttırma/Azaltma adları, Toplam ad ve Eksen Başlığının Türkçe olarak nasıl görüntüleneceğini göstermek için Türkçe bir örnek kullanacağız.

![yapılacak şey:image_alt_text](sample.png)

##  **Basit kod**
 Aşağıdaki örnek kod,[örnek Excel dosyası](waterfall.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "chartglobalizationsettings.cs" >}}

##  Örnek kod tarafından oluşturulan çıktı

Bu yukarıdaki örnek kodun konsol çıktısıdır.

{{< highlight "java" >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
