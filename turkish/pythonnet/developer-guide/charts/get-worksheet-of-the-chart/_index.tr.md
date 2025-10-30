---
title: Grafik Çalışsayısını Al
description: Aspose.Cells for Python via .NET kullanarak bir Excel grafiğiyle ilişkili çalışma sayfasını nasıl alacağınızı öğrenin. Kılavuzumuz, çalışma sayfasına erişme ve bu sayfa üzerinde işlem yaparak grafiğin temel verilerini manipüle etme yollarını gösterecek.
keywords: Aspose.Cells for Python via .NET, Excel grafikleri, çalışma sayfaları, veri manipülasyonu, temel veriler, işlemler.
type: docs
weight: 1000
url: /tr/python-net/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Bazen, bir grafik referansından çalışma sayfasına erişmek isteyebilirsiniz. Aspose.Cells for Python via .NET, grafiğin bulunduğu çalışma sayfasının referansını döndüren [**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet) özelliği sağlar.

{{% /alert %}}

Aşağıdaki örnek, [**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet) özelliğinin nasıl kullanılacağını göstermektedir. Kod öncelikle çalışsayısının adını yazdırır, daha sonra çalışsayısı üzerindeki ilk grafiğe erişir. Daha sonra [**Chart.worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/worksheet) özelliğini kullanarak tekrar çalışsayı adını yazdırır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-GetWorksheetOfTheChart.py" >}}

Örnek kodun sonucunda ortaya çıkan konsol çıktısı aşağıda verilmiştir. Görebileceğiniz gibi, aynı çalışsayı adını her iki seferde de yazdırır.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
