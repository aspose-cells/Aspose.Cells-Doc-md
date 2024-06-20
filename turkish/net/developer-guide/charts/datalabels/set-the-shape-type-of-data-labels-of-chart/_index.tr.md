---
title: Grafiğin Veri Etiketlerinin Şekil Türünü Ayarlama
description: Grafiğin veri etiketlerinin şekil türünü seçerek Aspose.Cells for .NET de nasıl ayarlayacağınızı öğrenin. Kılavuzumuz, mevcut farklı şekil türlerini açıklayacak ve veri etiketleriniz için uygun şekli seçmeyi ve grafiğinizin sunumunu ve kullanılabilirliğini artırmak için bunu nasıl yapacağınızı gösterecektir.
keywords: Aspose.Cells for .NET, grafik, veri etiketleri, şekil türleri, sunum, kullanılabilirlik.
type: docs
weight: 110
url: /tr/net/set-the-shape-type-of-data-labels-of-chart/
---

## **Olası Kullanım Senaryoları**
Grafiğin veri etiketlerinin şekil türünü değiştirebilirsiniz. DataLabels.ShapeType özelliğini kullanarak bu şekilde yapabilirsiniz. Bu, DataLabelShapeType numaralandırmasının bir değerini alır ve buna göre veri etiketlerinin şekil türünü değiştirir. Bazı değerleri şunlardır:

{{< highlight java >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}
## **Grafiğin Veri Etiketlerinin Şekil Türünü Ayarlama**
Aşağıdaki örnek kod, grafiğin veri etiketlerinin şekil türünü DataLabelShapeType.WedgeEllipseCallout olarak değiştirir. Bu kodda kullanılan örnek Excel dosyasını ve bu kod tarafından oluşturulan çıktı Excel dosyasını inceleyin. Ekran görüntüsü, örnek Excel dosyası üzerinde kodun etkisini göstermektedir. 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **Örnek Kod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetShapeTypeOfDataLabelsOfChart.cs" >}}
