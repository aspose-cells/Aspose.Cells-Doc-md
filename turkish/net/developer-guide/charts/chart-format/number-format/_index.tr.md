---
title: Grafik Serisinin Değer Biçim Kodunu Ayarlayın
description: Aspose.Cells for .NET içinde grafik serilerinin değerler biçim kodunu nasıl ayarlayacağınızı öğrenin. Kılavuzumuz, verilerinizi doğru ve profesyonelce sunmanıza olanak tanıyan uygun biçim kodu kullanarak grafik serilerinizi biçimlendirmenin nasıl yapıldığını anlamanıza yardımcı olacaktır.
keywords: Aspose.Cells for .NET, grafik serileri, değerler biçim kodu, biçimlendirme, veri sunumu, doğruluk, profesyonellik.
linktitle: Sayı Biçimi
type: docs
weight: 100
url: /tr/net/set-the-values-format-code-of-chart-series/
---

## **Olası Kullanım Senaryoları**
Grafik serilerinin değerler biçim kodunu [Series.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode) özelliğini kullanarak ayarlayabilirsiniz. Bu özellik, çalışma sayfası içindeki aralığa dayalı seriler için yalnızca kullanışlı değildir, aynı zamanda değerler dizisi ile oluşturulan seriler için de iyi çalışır.
## **Grafik Serisinin Değer Biçim Kodunu Ayarlayın**
Aşağıdaki örnek kod, önce hiç serisi olmayan boş grafikte bir seri ekler. Dizilerin dizisi kullanılarak seriler eklenir. Serileri ekledikten sonra [Series.ValuesFormatCode](https://reference.aspose.com/cells/net/aspose.cells.charts/series/properties/valuesformatcode) özelliği ve $#,##0 koduyla biçimler. 10000 sayısı $10,000 olur. Ekran görüntüsü, kodun çalıştırılması sonrasında etkininini [örnek Excel dosyasında](51740712.xlsx) ve [çıktı Excel dosyasında](51740713.xlsx) gösterir.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
## **Örnek Kod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetValuesFormatCodeOfChartSeries.cs" >}}
{{< app/cells/assistant language="csharp" >}}
