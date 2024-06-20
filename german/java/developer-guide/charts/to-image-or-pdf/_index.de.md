---
title: Diagrammdarstellung
linktitle: In Bild oder PDF
type: docs
weight: 40
url: /de/java/chart-rendering/
---

## **Erstellen von Diagrammen**

Aspose.Cells APIs unterstützen die Erstellung verschiedener Excel-Diagramme, wie unter dem Thema [Erstellen & Anpassen von Excel-Diagrammen](/cells/de/java/creating-and-customizing-charts/) detailliert beschrieben. Um den Gebrauch von Aspose.Cells APIs zur Darstellung der Diagramme in Bild- & PDF-Format zu zeigen, werden wir gemäß des folgenden Ausschnitts ein Säulendiagramm erstellen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

## **Diagramme darstellen**

Aspose.Cells APIs unterstützen die Konvertierung von Excel-Diagrammen in Bilder und PDF-Formate, ohne dass zusätzliche Tools oder Anwendungen erforderlich sind. Um die Rendering-Unterstützung zu bieten, hat die [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)-Klasse [**toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) & [**toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf(java.io.OutputStream))-Methoden mit einer Vielzahl von Überladungen bereitgestellt, um den Anforderungen der Anwendung am besten gerecht zu werden.

### **Grafiken in Bilder umwandeln**

Die [**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions))-Methode hat eine Vielzahl von Überladungen, um einfaches sowie fortgeschrittenes Rendering zu unterstützen. Wenn die Anforderung der Anwendung darin besteht, das Diagramm in seinen Standardabmessungen darzustellen, empfehlen wir die Verwendung der [**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions))-Methode wie folgt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-RenderChartsToImages-RenderChartsToImages.java" >}}

Es ist auch möglich, die Diagramme mit erweiterten Einstellungen in Bilder zu rendern. Aspose.Cells APIs haben eine Überladungsversion der [**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions))-Methode freigegeben, die eine Instanz von [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) akzeptieren kann, während es erlaubt, Parameter wie Auflösung, Rendering-Hinweise, Bildformat und so weiter zu spezifizieren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChartRendering-ChartRendering.java" >}}

### **Diagramm in PDF umwandeln**

Um das Diagramm in PDF-Format zu rendern, haben die Aspose.Cells APIs die [**Chart.toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf(java.io.OutputStream))-Methode freigegeben, die die Möglichkeit bietet, das resultierende PDF-PDF auf dem Datenträgerpfad oder einer Instanz von OutputStream zu speichern.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-chartsRenderChartsToPdf-RenderChartsToPdf.java" >}}

## **Unterstützte Diagrammtypen für die Darstellung**

Derzeit gibt es einige Diagrammtypen, die nicht für das Rendering unterstützt werden. Solche Diagrammtypen enthalten **N** in der **Unterstützt**-Spalte der untenstehenden Tabelle.

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
- [Konvertieren eines Diagramms in ein Bild im SVG-Format](/cells/de/java/converting-chart-to-image-in-svg-format/)
- [Erstellen Sie ein Diagramm-PDF mit gewünschter Seitengröße](/cells/de/java/create-chart-pdf-with-desired-page-size/)
- [Diagramm in SVG mit viewBox-Attribut exportieren](/cells/de/java/export-chart-to-svg-with-viewbox-attribute/)
