---
title: Diagramm als Bild
description: Erfahren Sie, wie Sie Aspose.Cells für Python via .NET verwenden, um ein Diagramm in ein Bildformat wie JPEG oder PNG zu exportieren. Unser Leitfaden zeigt, wie man ein Diagramm aus Microsoft Excel exportiert und als eigenständiges Bild für weitere Verwendung und Bearbeitung speichert.
keywords: Aspose.Cells für Python via .NET, Diagramm zu Bild, Microsoft Excel, Bildkonvertierung, Export, eigenständiges Bild.
linktitle: Diagramm als Bild
type: docs
weight: 46
url: /de/python-net/chart-to-image/
---

## **Diagramme darstellen**

Aspose.Cells für Python via .NET APIs unterstützen die Konvertierung von Excel-Diagrammen in Bildformate, ohne dass zusätzliche Tools oder Anwendungen erforderlich sind. Um die Render-Unterstützung bereitzustellen, hat die [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) Klasse die [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image) Methoden mit verschiedenen Überladungen bereitgestellt, um den Anforderungen der Anwendung bestmöglich gerecht zu werden.

### **Grafiken in Bilder umwandeln**

Die [**Chart.to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image)-Methode verfügt über eine Vielzahl von Überladungen, um sowohl einfache als auch erweiterte Renderings zu unterstützen. Wenn die Anforderung der Anwendung darin besteht, das Diagramm in seinen Standardabmessungen zu rendern, empfehlen wir die Verwendung der [**Chart.to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image)-Methode, wie im Folgenden gezeigt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChartRendering-ChartRenderingChartToImage.py" >}}

Es ist auch möglich, Diagramme mit erweiterten Einstellungen in Bilder zu rendern. Aspose.Cells für Python via .NET APIs haben eine Überladung der [**Chart.to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image)-Methode bereitgestellt, die eine Instanz von [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/) akzeptieren kann, während Parameter wie Auflösung, Glättungsmodus, Bildformat usw. festgelegt werden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.py" >}}

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
- [Diagramm in PDF umwandeln](/cells/de/python-net/chart-to-pdf/)
{{< app/cells/assistant language="python-net" >}}
