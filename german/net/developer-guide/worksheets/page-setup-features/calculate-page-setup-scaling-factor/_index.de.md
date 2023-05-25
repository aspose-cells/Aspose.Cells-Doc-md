---
title: Berechnen Sie den Skalierungsfaktor für die Seiteneinrichtung
type: docs
weight: 300
url: /de/net/calculate-page-setup-scaling-factor/
description: Dieser Artikel enthält Beispielcode, der erklärt, wie Sie die Bibliothek C# API oder .NET verwenden, um den Skalierungsfaktor „Seite einrichten“ mithilfe der Option „An n Seiten breit mal hoch anpassen“ des Excel-Arbeitsblatts programmgesteuert zu berechnen.
keywords: Fit to n page wide by m tall excel c#, calculate page setup scaling factor c#
---
{{% alert color="primary" %}}

 Wenn Sie die Skalierung der Seiteneinrichtung mit festlegen**Passt auf n Seite(n) breit und m hoch** Option Microsoft Excel berechnet den Skalierungsfaktor für die Seiteneinrichtung. Das Gleiche können Sie mit berechnen[**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale)Eigentum. Diese Eigenschaft gibt einen Double-Wert zurück, der in einen Prozentwert umgewandelt werden kann. Wenn beispielsweise 0,5 zurückgegeben wird, bedeutet dies, dass der Skalierungsfaktor 50 % beträgt.

{{% /alert %}}

 Der folgende Beispielcode veranschaulicht, wie der Skalierungsfaktor für die Seiteneinrichtung berechnet wird[**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale) Eigentum.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CalculateScalingFactor-CalculatePageSetupScalingFactor.cs" >}}
