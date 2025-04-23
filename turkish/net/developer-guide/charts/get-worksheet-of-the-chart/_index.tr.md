---
title: Grafik Çalışsayısını Al
description: Bir Excel tablosu grafiği ile ilişkilendirilmiş çalışsayının nasıl alınacağını Aspose.Cells for .NET kullanarak öğrenin. Rehberimiz, çalışsayısına nasıl erişeceğinizi ve tablonun altındaki verileri manipüle etmek için üzerinde işlemler yapacağınızı size gösterecektir.
keywords: Aspose.Cells for .NET, Excel grafikleri, çalışsayıları, veri manipülasyonu, altta yatan veri, işlemler.
type: docs
weight: 1000
url: /tr/net/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Bazen, grafik referansından bir çalışsayısına erişmek istersiniz. Aspose.Cells, grafiği içeren çalışsayısının referansını döndüren [**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet) özelliğini sağlar.

{{% /alert %}}

Aşağıdaki örnek, [**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet) özelliğinin nasıl kullanılacağını göstermektedir. Kod öncelikle çalışsayısının adını yazdırır, daha sonra çalışsayısı üzerindeki ilk grafiğe erişir. Daha sonra [**Chart.Worksheet**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/worksheet) özelliğini kullanarak tekrar çalışsayı adını yazdırır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-GetWorksheetOfTheChart-GetWorksheetOfTheChart.cs" >}}

Örnek kodun sonucunda ortaya çıkan konsol çıktısı aşağıda verilmiştir. Görebileceğiniz gibi, aynı çalışsayı adını her iki seferde de yazdırır.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
