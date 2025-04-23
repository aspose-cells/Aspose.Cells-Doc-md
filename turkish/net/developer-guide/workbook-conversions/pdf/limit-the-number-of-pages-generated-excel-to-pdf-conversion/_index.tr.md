---
title: Oluşturulan Sayfa Sayısını Sınırlandır  Excel den PDF ye Dönüşüm
type: docs
weight: 180
url: /tr/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

Bazı durumlarda, bir aralığı PDF dosyasına dönüştürmek isteyebilirsiniz. Aspose.Cells, bir Excel elektronik tablosunun PDF dosya biçimine dönüştürülürken kaç sayfa oluşturulacağına sınır koyma yeteneğine sahiptir.

{{% /alert %}}

## **Oluşturulan Sayfa Sayısını Sınırlandırmak**

Aşağıdaki örnek, bir Microsoft Excel dosyasındaki (3 ve 4) sayfa aralığını PDF olarak nasıl oluşturacağını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LimitNumberOfPagesGenerated-1.cs" >}}

{{% alert color="primary" %}}

Eğer elektronik tablo formülleri içeriyorsa, PDF'ye dönüştürmeden önce[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) çağrılması en iyisidir. Bu işlem, formül bağımlı değerlerin yeniden hesaplanmasını sağlar ve çıktı dosyasında doğru değerlerin oluşturulmasını sağlar.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
