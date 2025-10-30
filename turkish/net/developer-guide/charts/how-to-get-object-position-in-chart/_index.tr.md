---
title: Grafikte Nesne Konumunu Nasıl Alırım
description: Excel grafiğinde nesne konumlarını Aspose.Cells for .NET kullanarak nasıl alacağınızı öğrenin. 
keywords: Aspose.Cells for .NET, Excel Grafiği, Nesne konumlarını alın.
type: docs
weight: 74
url: /tr/net/how-to-get-object-position-in-chart/
---

## Olası Kullanım Senaryoları
Bazı durumlarda, Excel grafiği kullanırken grafikteki nesnelerin konumunu almanız gerekebilir. Bu ihtiyacı Aspose.Cells ile kolayca karşılayabilirsiniz.

## Örnek: Grafikte nesne konumunu alın

Aşağıdaki örnek kod, [örnek Excel dosyasını](TestFile.xlsx) yükler ve [çıktı Excel dosyasını](Output.xlsx) oluşturur.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "get-object-position-in-chart.cs" >}}

Yukarıdaki kod ile grafik başlığı ve grafik PlotArea'nın konumunu alabilirsiniz. 
Konum bilgisiyle, şekiller ilgili konumlara yerleştirilebilir. 
Aşağıdaki resimde, bir şekil PlotArea'nın sol üst köşesine yerleştirilmiş ve diğer şekil grafik başlığının altına konumlandırılmıştır.
![todo:image_alt_text](OutputResult.png)

## Birim açıklaması ve dönüştürme

Grafikte nesne konumu için üç birim vardır:

1. Grafik alanının oran birimleri.

2. Grafik alanının 1/4000 birimi. Bu eski Excel dosyalarında kullanılan bir birimdir ve önerilmez.

3. Piksel birimi.

Onların dönüşüm kodu aşağıdaki kodda gösterilmektedir: 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "object-position-unit-in-chart.cs" >}}

{{< app/cells/assistant language="csharp" >}}
