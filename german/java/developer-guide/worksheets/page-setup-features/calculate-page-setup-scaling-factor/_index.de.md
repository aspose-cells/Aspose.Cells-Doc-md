---
title: Berechnen Sie den Skalierungsfaktor für die Seiteneinrichtung
type: docs
weight: 260
url: /de/java/calculate-page-setup-scaling-factor/
---
{{% alert color="primary" %}} 

Wenn Sie die Seiteneinrichtungsskalierung mit festlegen**Anpassen an n Seite(n) breit und m hoch** Option, Microsoft Excel berechnet den Seiteneinrichtungs-Skalierungsfaktor. Sie können dasselbe mit berechnen[SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale) Eigentum. Diese Eigenschaft gibt einen Double-Wert zurück, der in einen Prozentwert konvertiert werden kann. Wenn beispielsweise 0,5079621076 zurückgegeben wird, bedeutet dies, dass der Skalierungsfaktor 51 % beträgt.

{{% /alert %}} 
## **Berechnen Sie den Skalierungsfaktor für die Seiteneinrichtung**
 Der folgende Beispielcode veranschaulicht, wie der Skalierungsfaktor für die Seiteneinrichtung mithilfe von berechnet wird[SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale)Eigentum.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculatePageSetupScalingFactor-CalculatePageSetupScalingFactor.java" >}}
## **Konsolenausgabe**
Hier ist die Konsolenausgabe des obigen Beispielcodes.

{{< highlight "java" >}}

 0.5079621076583862

{{< /highlight >}}
