---
title: Üretilen Sayfa Sayısını Sınırlayın  Excel den PDF ye Dönüştürme ile Golang kullanımı
linktitle: Sayfa Sayısını Sınırlandırma
type: docs
weight: 180
url: /tr/go-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Aspose.Cells ile Golang kullanarak Excel den PDF ye dönüştürürken üretilen sayfa sayısını nasıl sınırlayacağınızı öğrenin.
---

{{% alert color="primary" %}}

Bazı durumlarda, bir aralığı PDF dosyasına dönüştürmek isteyebilirsiniz. Aspose.Cells, bir Excel elektronik tablosunun PDF dosya biçimine dönüştürülürken kaç sayfa oluşturulacağına sınır koyma yeteneğine sahiptir.

{{% /alert %}}

## **Oluşturulan Sayfa Sayısını Sınırlandırmak**

Aşağıdaki örnek, bir Microsoft Excel dosyasındaki (3 ve 4) sayfa aralığını PDF olarak nasıl oluşturacağını göstermektedir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LimitTheNumberOfPagesGeneratedExcelToPdfConversion.go" >}}
{{% alert color="primary" %}}

Eğer elektronik tablo formülleri içeriyorsa, PDF'ye dönüştürmeden önce[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) çağrılması en iyisidir. Bu işlem, formül bağımlı değerlerin yeniden hesaplanmasını sağlar ve çıktı dosyasında doğru değerlerin oluşturulmasını sağlar.

{{% /alert %}}
