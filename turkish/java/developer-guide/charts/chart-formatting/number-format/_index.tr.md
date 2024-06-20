---
title: Grafik Serisinin Değer Biçim Kodunu Ayarlayın
description: Aspose.Cells for Java de grafik serisinin değer biçim kodunu nasıl ayarlayacağınızı öğrenin. Rehberimiz, uygun biçim kodunu kullanarak verilerinizi doğru ve profesyonel bir şekilde sunmanıza olanak tanıyarak, grafik serisi verilerinizi nasıl biçimlendireceğinizi anlamanıza yardımcı olacaktır.
keywords: Aspose.Cells for Java, grafik serisi, değer biçim kodu, biçimlendirme, veri sunumu, doğruluk, profesyonellik.
linktitle: Sayı Biçimi
type: docs
weight: 100
url: /tr/java/set-the-values-format-code-of-chart-series/
---

## **Olası Kullanım Senaryoları**
Grafik serisinin değer biçim kodunu [Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-) yöntemini kullanarak ayarlayabilirsiniz. Bu yöntem, çalışma sayfası içindeki aralığa dayalı olan seriler için değil, aynı zamanda değerler dizisi ile oluşturulan seriler için de iyi çalışır.
## **Grafik Serisinin Değer Biçim Kodunu Ayarlayın**
Aşağıdaki örnek kod, önceden serisi olmayan boş bir grafikte bir seri ekler. Seriyi değerler dizisi kullanarak ekler. Seriyi ekledikten sonra, $#,##0 kodunu kullanarak [Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-) yöntemiyle biçimlendirir ve 10000 sayısı $10,000 olur. Ekran görüntüsü, [örnek Excel dosyası](51740712.xlsx) ve [çıktı Excel dosyası](51740713.xlsx) üzerinde kodun etkisini gösterir.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
## **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SetValuesFormatCodeOfChartSeries.java" >}}
