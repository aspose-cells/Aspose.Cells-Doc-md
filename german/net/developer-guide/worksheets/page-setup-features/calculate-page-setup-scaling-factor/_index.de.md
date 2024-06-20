---
title: Berechnen des Maßstabsfaktors für die Seiteneinrichtung
type: docs
weight: 300
url: /de/net/calculate-page-setup-scaling-factor/
description: In diesem Artikel wird anhand von Beispielen erläutert, wie die C# API oder die .NET Bibliothek verwendet werden, um den Maßstabsfaktor für die Seiteneinrichtung mithilfe der Option Fit auf n Seite(n) breit x m Seite(n) hoch des Excel Arbeitsblatts programmgesteuert zu berechnen.
keywords: Fit auf n Seite breit x m Seite hoch Excel c#, Maßstabsfaktor für die Seiteneinrichtung berechnen c#
---

{{% alert color="primary" %}}

Wenn Sie die Seiteneinrichtung mit der Option **Fit auf n Seite(n) breit x m Seite(n) hoch** festlegen, berechnet Microsoft Excel den Maßstabsfaktor für die Seiteneinrichtung. Sie können dasselbe mit der Eigenschaft [**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale) berechnen. Diese Eigenschaft gibt einen Double-Wert zurück, der in einen Prozentwert umgewandelt werden kann. Wenn beispielsweise 0,5 zurückgegeben wird, bedeutet dies, dass der Maßstabsfaktor 50% beträgt.

{{% /alert %}}

Der folgende Beispielcode veranschaulicht, wie der Maßstabsfaktor für die Seiteneinrichtung mit der Eigenschaft [**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale) berechnet wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CalculateScalingFactor-CalculatePageSetupScalingFactor.cs" >}}
