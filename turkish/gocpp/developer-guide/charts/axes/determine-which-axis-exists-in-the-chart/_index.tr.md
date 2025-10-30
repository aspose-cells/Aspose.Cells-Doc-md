---
title: Golang ile C++ kullanarak Grafikte Hangi Eksenin Var Olduğunu Belirleme
description: Aspose.Cells for C++ kullanılarak oluşturulan diyagramda hangi eksenin var olduğunu belirlemeyi öğrenin. Rehberimiz, diyagramda kategori, değer ve ikincil eksenler dahil olmak üzere farklı eksenleri tanımlama ve erişim hakkında size yardımcı olacaktır.
keywords: Aspose.Cells for C++, diyagram, eksen, varlığı, kategori, değer, ikincil.
type: docs
weight: 140
url: /tr/go-cpp/determine-which-axis-exists-in-the-chart/
---

{{% alert color="primary" %}}

Bazı durumlarda kullanıcı, belirli bir eksenin grafikte var olup olmadığını bilmek isteyebilir. Örneğin, grafikte İkincil Değer Ekseni'nin var olup olmadığını bilmek isteyebilir. Bazı grafikler (Pasta, Patlamış Pasta, PastaPasta, PastaBar, Pasta3D, Patlamış Pasta3D, Donut, Patlamış Donut vb.) ekseni bulundurmaz.

Aspose.Cells, belirli bir eksenin grafikte var olup olmadığını belirlemek için [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/go-cpp/chart/hasaxis/) methodunu sağlar.

{{% /alert %}}

Aşağıdaki örnek kod, [**Chart.HasAxis(AxisType axisType, bool isPrimary)**](https://reference.aspose.com/cells/go-cpp/chart/hasaxis/) kullanarak örnek diyagramın Birincil ve İkincil Kategori ve Değer Ekseni olup olmadığını gösterir.

## C++ kodu ile diyagramda hangi eksenin var olduğunu belirleme

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetermineWhichAxisExistsInTheChart.go" >}}
## Örnek Kod Tarafından Oluşturulan Konsol Çıktısı

Kodun konsol çıktısı aşağıda gösterilmiştir, Birincil Kategori ve Değer Eksenleri için true ve İkincil Kategori ve Değer Eksenleri için false göstermektedir.

{{< highlight java >}}

Has Primary Category Axis: True

Has Secondary Category Axis: False

Has Primary Value Axis: True

Has Secondary Value Axis: False

{{< /highlight >}}
