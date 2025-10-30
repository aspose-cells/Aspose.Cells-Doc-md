---
title: Grafiğin Veri Etiketlerinin Şekil Türünü Ayarlama
description: Grafiklerde veri etiketlerinin şekil türünü nasıl ayarlayacağınızı öğrenin; Aspose.Cells for Python via .NET. Rehberimiz, mevcut farklı şekil türlerini açıklayacak ve sunumunuzu ve kullanım kolaylığını artırmak için uygun şekli nasıl seçeceğinizi gösterecek.
keywords: Aspose.Cells for Python via .NET, grafikleme, veri etiketleri, şekil türleri, sunum, kullanılabilirlik.
type: docs
weight: 110
url: /tr/python-net/set-the-shape-type-of-data-labels-of-chart/
---

## **Olası Kullanım Senaryoları**
Grafiğin veri etiketlerinin şekil türünü değiştirebilirsiniz. DataLabels.ShapeType özelliğini kullanarak bu şekilde yapabilirsiniz. Bu, DataLabelShapeType numaralandırmasının bir değerini alır ve buna göre veri etiketlerinin şekil türünü değiştirir. Bazı değerleri şunlardır:

{{< highlight java >}}

DataLabelShapeType.BENT_LINE_CALLOUT

DataLabelShapeType.DOWN_ARROW_CALLOUT

DataLabelShapeType.ELLIPSE

DataLabelShapeType.LINE_CALLOUT

DataLabelShapeType.RECT

etc.

{{< /highlight >}}

## **Grafiğin Veri Etiketlerinin Şekil Türünü Ayarlama**
Aşağıdaki örnek kod, grafiğin veri etiketlerinin şekil türünü DataLabelShapeType.WedgeEllipseCallout olarak değiştirir. Bu kodda kullanılan örnek Excel dosyasını ve bu kod tarafından oluşturulan çıktı Excel dosyasını inceleyin. Ekran görüntüsü, örnek Excel dosyası üzerinde kodun etkisini göstermektedir. 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)

## **Örnek Kod**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SetShapeTypeOfDataLabelsOfChart.py" >}}
{{< app/cells/assistant language="python-net" >}}
