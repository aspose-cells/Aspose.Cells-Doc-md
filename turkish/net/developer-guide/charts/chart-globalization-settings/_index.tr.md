---
title: Farklı Dil için Grafik Bileşeni Olarak ChartGlobalizationSettings Sınıfını Kullanma 
description: Aspose.Cells for .NET içinde ChartGlobalizationSettings sınıfını nasıl kullanacağınızı öğrenin. Rehberimiz, grafik öğelerini, etiketlerini ve açıklamalarını farklı dillere yerelleştirmenize olanak tanıyarak verilerinizi kültürel olarak uygun bir şekilde sunmanıza yardımcı olacaktır.
keywords: Aspose.Cells for .NET, grafik oluşturma, grafik küreselleştirme, diller, yerelleştirme, ChartGlobalizationSettings, öğeler, etiketler, açıklamalar.
type: docs
weight: 2200
url: /tr/net/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells API'ları, kullanıcının bir grafik bileşenini farklı bir dile ayarlamak istediği senaryolarla başa çıkmak için [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) sınıfını açığa çıkarmıştır. bir elektronik tabloda Ara Toplamlar için özel etiketler. 

## **ChartGlobalizationSettings Sınıfına Giriş**

Şu anda [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/) sınıfı aşağıdaki 8 yöntemi sunmaktadır, bu yöntemler özel bir sınıfta çeviri için geçersiz kılınabilir; AxisTitle adı, AxisUnit adı, ChartTitle adı vb. gibi farklı dillere.
1. [**GetAxisTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): Eksen için Başlık adını alır.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): Eksen Birimi için Adı alır.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): Grafik Başlığının adını alır.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): Efsane için Azalma adını alır.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): Efsane için Artış adını alır.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): Efsane için Toplam adını alır.
1. [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getothername/): Grafikte "Diğer" etiketlerinin adını alır.
1. [**GetSeriesName**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartglobalizationsettings/getseriesname/): Grafikteki Serilerin adını alır.

### **Özel dil çevirisi**
Burada, aşağıdaki verilere dayalı bir su dalgası grafiği oluşturacağız. Grafik bileşenlerinin adları, İngilizce olarak grafikte gösterilecektir. Grafik Başlığı, Efsane Artış/Azalma adları, Toplam adı ve Eksen Başlığı'nın Türkçe olarak nasıl gösterileceğini göstermek için bir Türkçe dil örneği kullanacağız.

![todo:image_alt_text](sample.png)

## **Örnek Kod**
Aşağıdaki örnek kod, [örnek Excel dosyasını](waterfall.xlsx) yükler.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "chartglobalizationsettings.cs" >}}

Örneğin ürettiği çıktı

Yukarıdaki örnek kodun konsol çıktısı budur.

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
