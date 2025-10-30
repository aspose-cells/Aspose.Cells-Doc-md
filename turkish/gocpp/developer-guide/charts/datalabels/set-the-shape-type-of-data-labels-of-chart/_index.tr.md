---
title: Golang ile C++ kullanarak Grafik Veri Etiketlerinin Şekil Türünü Ayarlama
linktitle: Grafiğin Veri Etiketlerinin Şekil Türünü Ayarlama
description: Aspose.Cells for C++ te tablo daki veri etiketlerinin şekil türünü ayarlamayı öğrenin. Rehberimiz, mevcut farklı şekil türlerini açıklayacak ve verilerinizi daha iyi sunmak ve kullanımı kolaylaştırmak için uygun şekli seçmenize yardımcı olacaktır.
keywords: Aspose.Cells for C++, tablo oluşturma, veri etiketleri, şekil türleri, sunum, kullanım kolaylığı.
type: docs
weight: 110
url: /tr/go-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **Olası Kullanım Senaryoları**
Grafiklerde veri etiketlerinin şekil türünü `DataLabels.ShapeType` özelliği ile değiştirebilirsiniz. Bu özellik, `DataLabelShapeType` enum değerini alır ve veri etiketlerinin şeklini buna göre değiştirir. Bazı değerleri şunlardır:

{{< highlight java >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}

## **Grafiğin Veri Etiketlerinin Şekil Türünü Ayarlama**
 Aşağıdaki örnek kod, grafik veri etiketlerinin şekil türünü `DataLabelShapeType.WedgeEllipseCallout` olarak değiştirir. Lütfen bu kodda kullanılan [örnek Excel dosyasını](60489778.xlsx) ve onun tarafından oluşturulan [çıktı Excel dosyasını](60489779.xlsx) görün. Ekran görüntüsü, kodun örnek Excel dosyasındaki etkisini göstermektedir. 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)

## **Örnek Kod**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetTheShapeTypeOfDataLabelsOfChart.go" >}}
