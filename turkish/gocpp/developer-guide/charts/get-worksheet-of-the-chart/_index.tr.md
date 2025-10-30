---
title: Golang kullanarak C++ ile Grafik Öğesi Al
linktitle: Grafik Çalışsayısını Al
description: Aspose.Cells for C++ kullanarak bir Excel grafik ile ilişkili sayfayı nasıl alacağınızı öğrenin. Rehberimiz, sayfayı nasıl erişeceğinizi ve grafik altyapısındaki verileri nasıl manipüle edeceğinizi gösterecektir.
keywords: Aspose.Cells for C++, Excel grafikler, çalışma sayfaları, veri manipülasyonu, temel veriler, operasyonlar.
type: docs
weight: 1000
url: /tr/go-cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

Bazen, bir grafiğin referansıyla çalışma sayfasına erişmek istersiniz. Aspose.Cells, grafiğin bulunduğu sayfanın referansını dönen [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/) yöntemini sağlar.

{{% /alert %}}

Aşağıdaki örnek, [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/) yönteminin nasıl kullanılacağını gösterir. Kod önce sayfanın adını yazdırır, sonra sayfadaki ilk grafik erişir ve tekrar sayfanın adını [**Chart::GetWorksheet**](https://reference.aspose.com/cells/go-cpp/chart/getworksheet/) yöntemiyle yazdırır.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetWorksheetOfTheChart.go" >}}
Örnek kodun sonucunda ortaya çıkan konsol çıktısı aşağıda verilmiştir. Görebileceğiniz gibi, aynı çalışsayı adını her iki seferde de yazdırır.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
