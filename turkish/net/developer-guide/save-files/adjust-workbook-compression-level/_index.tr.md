---
title: Çalışma Kitabı Sıkıştırma Seviyesini Ayarlayın
type: docs
weight: 180
url: /tr/net/adjust-workbook-compression-level/
---

## **Çalışma kitabının sıkıştırma seviyesini ayarlayın**

Geliştiriciler, daha büyük çalışma kitaplarıyla çalışırken çalışma kitabının sıkıştırma seviyesini ayarlayabilirler. Geliştiriciler, dosya boyutlarını işleme süresinin üzerine tercih edebilir veya tam tersini yapabilir. Aspose.Cells, çalışma kitabının sıkıştırma seviyesini ayarlamak için kullanabileceğiniz [**OoxmlCompressionType**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype) numaralandırmasını sağlar. [**OoxmlCompressionType**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype) numaralandırma aşağıdaki üyeleri sağlar.

- Seviye 1: En hızlı ama en az etkili sıkıştırma.
- Seviye 2: Seviye 1'den biraz daha yavaş, ancak daha iyi.
- Seviye 3: Seviye 2'den biraz daha yavaş, ama daha iyi.
- Seviye 4: Seviye 3'ten biraz daha yavaş, ama daha iyi.
- Seviye 5: Seviye 4'ten biraz daha yavaş, ancak daha iyi sıkıştırma ile.
- Seviye 6: Hız ve sıkıştırma verimliliği için iyi bir denge.
- Seviye 7: Oldukça iyi sıkıştırma!
- Seviye 8: Seviye 7'den daha iyi sıkıştırma!
- Seviye 9: En "iyi" sıkıştırma, en iyi, girdi veri akışının boyutunda en büyük azalma anlamına gelir. Bu aynı zamanda en yavaş sıkıştırmadır.

Aşağıdaki kod parçacığı, [**OoxmlCompressionType**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompressiontype) numaralandırmasının kullanımını gösteriyor ve Düzey1, Düzey6 ve Düzey9 için dönüşüm süresini karşılaştırıyor. Oluşturulan dosyaların boyutlarını da karşılaştırabilirsiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AdjustCompressionLevel-1.cs" >}}
