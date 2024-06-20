---
title: Berechnen des Maßstabsfaktors für die Seiteneinrichtung
type: docs
weight: 260
url: /de/java/calculate-page-setup-scaling-factor/
---

{{% alert color="primary" %}} 

Wenn Sie die Seiteneinrichtungsskalierung mit der Option **Anpassen auf n Seiten breit und m Seiten hoch** einstellen, berechnet Microsoft Excel den Seiteneinrichtungsfaktor. Sie können dasselbe mithilfe der Eigenschaft [SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale) berechnen. Diese Eigenschaft gibt einen Double-Wert zurück, der in einen Prozentwert umgerechnet werden kann. Zum Beispiel bedeutet eine Rückgabe von 0.5079621076, dass der Skalierungsfaktor 51 % beträgt.

{{% /alert %}} 
## **Seitenformatierungs-Skalierungsfaktor berechnen**
Der folgende Beispielcode veranschaulicht, wie der Seiteneinrichtungsskalierungsfaktor mithilfe der Eigenschaft [SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale) berechnet werden kann.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculatePageSetupScalingFactor-CalculatePageSetupScalingFactor.java" >}}
## **Konsolenausgabe**
Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight java >}}

 0.5079621076583862

{{< /highlight >}}
