---
title: Seçili Grafik Öğelerini Excel Grafiklerine Dönüştür
type: docs
weight: 30
url: /tr/reportingservices/render-selected-chart-items-to-excel-charts/
---
{{% alert color="primary" %}} 

Bir rapordaki yalnızca bazı grafikleri Excel grafiklerine dönüştürmek için:

1. Aç**Aspose.Cells.ReportingServices.xml** dosya.
1.  yapılandırma parametrelerini değiştirin**Aspose.Cells.ReportingServices.xml** dosya.
1. İstenen rapor yapılandırma bilgilerini ekleyin.
1. Düzenlenebilir grafikler olarak dışa aktarmak istemediğiniz grafik öğelerinin bilgilerini ekleyin. Bu öğeler, statik görüntüler olarak dışa aktarılır.

Örneğin:

{{< highlight "java" >}}

 <Chart >

<Report name= "Employee Sales Summary 2008">

<ChartItem name="Chart1" type="image"/>

</Report >

</Chart> 

{{< /highlight >}}

**Resim olarak dışa aktarılan bir grafik** 

![yapılacaklar:resim_alternatif_metin](render-selected-chart-items-to-excel-charts_1.png)

**Düzenlenebilir bir Excel grafiği olarak dışa aktarılan bir grafik** 

![yapılacaklar:resim_alternatif_metin](render-selected-chart-items-to-excel-charts_2.png)

{{% /alert %}}
