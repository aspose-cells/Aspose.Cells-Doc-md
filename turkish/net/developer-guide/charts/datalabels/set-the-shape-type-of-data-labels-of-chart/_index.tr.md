---
title: Grafiğin Veri Etiketlerinin Şekil Türünü Ayarlama
type: docs
weight: 110
url: /tr/net/set-the-shape-type-of-data-labels-of-chart/
---
## **Olası Kullanım Senaryoları**
DataLabels.ShapeType özelliğini kullanarak grafiğin veri etiketlerinin şekil türünü değiştirebilirsiniz. DataLabelShapeType numaralandırmasının değerini alır ve buna göre veri etiketlerinin şekil tipini değiştirir. Değerlerinden bazıları

{{< highlight "java" >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}
## **Grafiğin Veri Etiketlerinin Şekil Türünü Ayarlama**
 Aşağıdaki örnek kod, grafiğin veri etiketlerinin şekil türünü DataLabelShapeType.WedgeEllipseCallout olarak değiştirir. Lütfen bkz[örnek excel dosyası](60489778.xlsx) Bu kodda kullanılan ve[çıktı excel dosyası](60489779.xlsx) onun tarafından oluşturulur. Ekran görüntüsü, kodun örnek Excel dosyası üzerindeki etkisini gösterir.

![yapılacaklar:resim_alternatif_metin](set-the-shape-type-of-data-labels-of-chart_1.png)
## **Basit kod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetShapeTypeOfDataLabelsOfChart.cs" >}}
