---
title: Diagramm als Bild
description: Erfahren Sie, wie Sie Aspose.Cells for .NET verwenden können, um ein Diagramm in ein Bildformat wie JPEG oder PNG zu konvertieren. Unser Leitfaden zeigt, wie Sie ein Diagramm aus Microsoft Excel exportieren und als eigenständiges Bild speichern können, um es weiter zu verwenden und zu bearbeiten.
keywords: Aspose.Cells for .NET, Diagramm als Bild, Microsoft Excel, Bildkonvertierung, Export, eigenständiges Bild.
linktitle: Diagramm als Bild
type: docs
weight: 46
url: /de/net/chart-to-image/
---

## **Diagramme darstellen**

Aspose.Cells APIs unterstützen die Konvertierung der Excel-Diagramme in Bildformate, ohne zusätzliche Tools oder Anwendungen zu benötigen. Um Renderunterstützung bereitzustellen, hat die [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) Klasse [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) Methoden mit einer Vielzahl von Überladungen freigelegt, um den Anforderungen der Anwendung am besten zu entsprechen.

### **Grafiken in Bilder umwandeln**

Die [**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)-Methode verfügt über eine Vielzahl von Überladungen, um sowohl einfache als auch erweiterte Renderings zu unterstützen. Wenn die Anforderung der Anwendung darin besteht, das Diagramm in seinen Standardabmessungen zu rendern, empfehlen wir die Verwendung der [**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)-Methode, wie im Folgenden gezeigt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

Es ist auch möglich, die Diagramme mit erweiterten Einstellungen als Bilder zu rendern. Aspose.Cells APIs haben eine Überladungsversion der [**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)-Methode freigelegt, die eine Instanz von [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) akzeptieren und gleichzeitig Parameter wie Auflösung, Glättungsmodus, Bildformat usw. festlegen kann.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

## **Unterstützte Diagrammtypen für die Darstellung**

Einige Diagrammtypen werden derzeit nicht für die Darstellung unterstützt. Solche Diagrammtypen enthalten ein **N** in der **Unterstützt**-Spalte der unten stehenden Tabelle.

|**Diagrammtyp**|**Diagramm-Subtyp**|**Unterstützt**|
| :- | :- | :- |
|**Column**|Column|**Y**|
| |ColumnStacked|**Y**|
| |Column100PercentStacked|**Y**|
| |Column3DClustered|**Y**|
| |Column3DStacked|**Y**|
| |Column3D100PercentStacked|**Y**|
| |Column3D|**Y**|
|**Bar**|Bar|**Y**|
| |BarStacked|**Y**|
| |Bar100PercentStacked|**Y**|
| |Bar3DClustered|**Y**|
| |Bar3DStacked|**Y**|
| |Bar3D100PercentStacked|**Y**|
|**Line**|Line|**Y**|
| |LineStacked|**Y**|
| |Line100PercentStacked|**Y**|
| |LineWithDataMarkers|**Y**|
| |LineStackedWithDataMarkers|**Y**|
| |Line100PercentStackedWithDataMarkers|**Y**|
| |Line3D|**Y**|
|**Pie**|Pie|**Y**|
| |Pie3D|**Y**|
| |PiePie|**Y**|
| |PieExploded|**Y**|
| |Pie3DExploded|**Y**|
| |PieBar|**Y**|
|**Scatter**|Scatter|**Y**|
| |ScatterConnectedByCurvesWithDataMarker|**Y**|
| |ScatterConnectedByCurvesWithoutDataMarker|**Y**|
| |ScatterConnectedByLinesWithDataMarker|**Y**|
| |ScatterConnectedByLinesWithoutDataMarker|**Y**|
|**Area**|Area|**Y**|
| |AreaStacked|**Y**|
| |Area100PercentStacked|**Y**|
| |Area3D|**Y**|
| |Area3DStacked|**Y**|
| |Area3D100PercentStacked|**Y**|
|**Doughnut**|Doughnut|**Y**|
| |DoughnutExploded|**Y**|
|**Radar**|Radar|**Y**|
| |RadarWithDataMarkers|**Y**|
| |RadarFilled|**Y**|
|**Surface**|Surface3D|N|
| |SurfaceWireframe3D|N|
| |SurfaceContour|N|
| |SurfaceContourWireframe|N|
|**Bubble**|Bubble|**Y**|
| |Bubble3D|N|
|**Stock**|StockHighLowClose|**Y**|
| |StockOpenHighLowClose|**Y**|
| |StockVolumeHighLowClose|**Y**|
| |StockVolumeOpenHighLowClose|**Y**|
|**Cylinder**|Cylinder|**Y**|
| |CylinderStacked|**Y**|
| |Cylinder100PercentStacked|**Y**|
| |CylindricalBar|**Y**|
| |CylindricalBarStacked|**Y**|
| |CylindricalBar100PercentStacked|**Y**|
| |CylindricalColumn3D|**Y**|
|**Cone**|Cone|**Y**|
| |ConeStacked|**Y**|
| |Cone100PercentStacked|**Y**|
| |ConicalBar|**Y**|
| |ConicalBarStacked|**Y**|
| |ConicalBar100PercentStacked|**Y**|
| |ConicalColumn3D|**Y**|
|**Pyramid**|Pyramid|**Y**|
| |PyramidStacked|**Y**|
| |Pyramid100PercentStacked|**Y**|
| |PyramidBar|**Y**|
| |PyramidBarStacked|**Y**|
| |PyramidBar100PercentStacked|**Y**|
| |PyramidColumn3D|**Y**|
|**BoxWhisker**|BoxWhisker|Y|
|**Funnel**|Funnel|**Y**|
|**ParetoLine**|ParetoLine|**Y**|
|**Sunburst**|Sunburst|**Y**|
|**Treemap**|Treemap|**Y**|
|**Waterfall**|Waterfall|**Y**|
|**Histogram**|Histogram|Y|
|**Map**|Map|**N**|

{{% alert color="primary" %}}

Wenn Sie versuchen, die nicht unterstützten Diagrammtypen als Bild oder PDF darzustellen, erhalten Sie möglicherweise Bilder mit der Größe 0 oder leere PDFs.

{{% /alert %}}

## **Erweiterte Themen**
- [Diagramm in PDF umwandeln](/cells/de/net/chart-to-pdf/)
