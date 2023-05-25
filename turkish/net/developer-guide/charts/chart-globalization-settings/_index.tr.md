---
title:  Grafik Bileşeni İçin Farklı Dil Ayarlamak için ChartGlobalizationSettings Sınıfını Kullanma
type: docs
weight: 2200
url: /tr/net/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---
##  **Olası Kullanım Senaryoları**

 Aspose.Cells API'ler şu bilgileri açığa çıkardı:[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) Kullanıcının grafik bileşenini farklı bir dile ayarlamak istediği senaryolarla başa çıkmak için sınıf. bir e-tablodaki Ara Toplamlar için özel etiketler.

##  **ChartGlobalizationSettings Sınıfına Giriş**

 bu[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/)class şu anda AxisTitle adı, AxisUnit adı, ChartTitle adı ve benzeri gibi farklı bir dile çevirmek için özel bir sınıfta geçersiz kılınabilen aşağıdaki 8 yöntemi sunmaktadır.
1. [**GetAxisTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): Eksen için Başlık adını alır.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): Eksen Biriminin Adını alır.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): Grafik Başlığının adını alır.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): Legend için Azaltma adını alır.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): Legend için artışın adını alır.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): Legend için Total adını alır.
1. [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getothername/): Grafik için "Diğer" etiketlerinin adını alır.
1. [**GetSeriesName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getseriesname/): Grafikteki Serinin adını alır.

###  **Özel dil çevirisi**
Burada, aşağıdaki verilere dayalı olarak bir şelale grafiği oluşturacağız. Grafik bileşenlerinin adları, grafikte İngilizce olarak görüntülenecektir. Grafik Başlığı, Gösterge Arttırma/Azaltma adları, Toplam ad ve Eksen Başlığının Türkçe olarak nasıl görüntüleneceğini göstermek için bir Türkçe dil örneği kullanacağız.

![yapılacaklar:image_alt_text](sample.png)

##  **Basit kod**
 Aşağıdaki örnek kod,[örnek excel dosyası](waterfall.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "chartglobalizationsettings.cs" >}}

##  Örnek kod tarafından oluşturulan çıktı

Bu, yukarıdaki örnek kodun konsol çıktısıdır.

{{< highlight "java" >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
