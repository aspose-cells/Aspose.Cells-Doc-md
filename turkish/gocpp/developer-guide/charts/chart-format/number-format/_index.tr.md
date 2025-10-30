---
title: Grafik Serisinin Değer Format Kodunu Golang ile C++ kullanarak ayarlayın
linktitle: Sayı Biçimi
type: docs
weight: 100
url: /tr/go-cpp/set-the-values-format-code-of-chart-series/
description: Aspose.Cells for C++ te grafik serisinin değer format kodunu nasıl ayarlayacağınızı öğrenin. Kılavuzumuz, verilerinizi doğru ve profesyonel bir şekilde sunmanız için uygun format kodunu kullanarak grafik serisi verilerinizi nasıl biçimlendireceğinizi anlamanıza yardımcı olacaktır.
keywords: Aspose.Cells for C++, grafik serisi, değer format kodu, biçimlendirme, veri sunumu, doğruluk, profesyonellik.
---

## **Olası Kullanım Senaryoları**
Grafik serisinin değer format kodunu [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/go-cpp/series/getvaluesformatcode/) özelliğini kullanarak ayarlayabilirsiniz. Bu özellik, yalnızca çalışma sayfasındaki aralıktan türetilen seriler için değil, ayrıca değer dizisi kullanılarak oluşturulan seriler için de uygundur.

## **Grafik Serisinin Değer Biçim Kodunu Ayarlayın**
Aşağıdaki örnek kod, önceden seri olmayan boş grafiğe bir seri ekler. Seriyi değerler dizisi kullanarak ekler. Seri eklendikten sonra, [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/go-cpp/series/getvaluesformatcode/) özelliği kullanılarak `$#,##0` biçimlendirme kodu ile formata sokar ve sayı `10000` `$10,000` olur. Ekran görüntüsü, kodun [örnek Excel dosyası](51740712.xlsx) ve yürütmeden sonra [çıktı Excel dosyası](51740713.xlsx) üzerindeki etkisini gösterir.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Örnek Kod**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NumberFormat.go" >}}
