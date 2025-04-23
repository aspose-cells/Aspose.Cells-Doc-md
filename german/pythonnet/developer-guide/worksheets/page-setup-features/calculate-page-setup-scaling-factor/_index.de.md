---
title: Berechnen des Maßstabsfaktors für die Seiteneinrichtung
type: docs
weight: 300
url: /de/python-net/calculate-page-setup-scaling-factor/
description: Dieser Artikel enthält Beispielcode, der erklärt, wie man die Aspose.Cells für Python via .NET APIs verwendet, um den Maßstabsfaktor der Seitenaufbereitung mithilfe der Option „Anpassen auf n Seite(n) breit x m hoch“ des Excel Arbeitsblatts programmatisch zu berechnen.
keywords: Python Excel Bibliothek, Python Anpassen an n Seite(n) breit und m hoch Excel, Maßstabsfaktor der Seiteneinrichtung in Python berechnen.
---

{{% alert color="primary" %}}

Wenn Sie die Seiteneinrichtung mit der Option **Fit auf n Seite(n) breit x m Seite(n) hoch** festlegen, berechnet Microsoft Excel den Maßstabsfaktor für die Seiteneinrichtung. Sie können dasselbe mit der Eigenschaft [**SheetRender.page_scale**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/page_scale) berechnen. Diese Eigenschaft gibt einen Double-Wert zurück, der in einen Prozentwert umgewandelt werden kann. Wenn beispielsweise 0,5 zurückgegeben wird, bedeutet dies, dass der Maßstabsfaktor 50% beträgt.

{{% /alert %}}

Der folgende Beispielcode veranschaulicht, wie der Maßstabsfaktor für die Seiteneinrichtung mit der Eigenschaft [**SheetRender.page_scale**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/page_scale) berechnet wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-CalculateScalingFactor-CalculatePageSetupScalingFactor.py" >}}
