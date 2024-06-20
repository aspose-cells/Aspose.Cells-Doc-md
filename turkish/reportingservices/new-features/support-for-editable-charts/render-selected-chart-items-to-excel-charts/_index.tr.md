---
title: Seçili Raporun Grafik Öğelerini Excel Grafiklerine Dönüştürme
type: docs
weight: 30
url: /tr/reportingservices/render-selected-chart-items-to-excel-charts/
---

{{% alert color="primary" %}} 

Bir raporda sadece bazı grafikleri Excel grafiklerine dönüştürmek için:

1. **Aspose.Cells.ReportingServices.xml** dosyasını açın.
1. **Aspose.Cells.ReportingServices.xml** dosyasının yapılandırma parametrelerini değiştirin.
1. İstenen raporun yapılandırma bilgilerini ekleyin.
1. Düzenlenebilir grafik olarak dışa aktarmak istemediğiniz grafik öğeleri için bilgileri ekleyin. Bu öğeler statik görüntüler olarak dışa aktarılır.

Örneğin:

{{< highlight java >}}

 <Chart >

<Report name= "Employee Sales Summary 2008">

<ChartItem name="Chart1" type="image"/>

</Report >

</Chart> 

{{< /highlight >}}

**Bir görüntü olarak dışa aktarılan bir grafik** 

![todo:image_alt_text](render-selected-chart-items-to-excel-charts_1.png)

**Düzenlenebilir bir Excel grafik olarak dışa aktarılan bir grafik** 

![todo:image_alt_text](render-selected-chart-items-to-excel-charts_2.png)

{{% /alert %}}
