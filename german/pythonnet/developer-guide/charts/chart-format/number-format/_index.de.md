---
title: Setzen Sie den Werteformatcode der Diagrammserie
description: Erfahren Sie, wie Sie das Werteformat Ihrer Diagrammserie in Aspose.Cells für Python via .NET festlegen. Unser Leitfaden zeigt Ihnen, wie Sie Ihre Diagrammdaten mit dem entsprechenden Formatcode formatieren, um Ihre Daten genau und professionell darzustellen.
keywords: Aspose.Cells für Python via .NET, Diagrammserie, Werte Formatcode, Formatierung, Datenpräsentation, Genauigkeit, Professionalität.
linktitle: Zahlenformat
type: docs
weight: 100
url: /de/python-net/set-the-values-format-code-of-chart-series/
---

## **Mögliche Verwendungsszenarien**
Sie können den Werte-Formatcode der Diagrammserie mit der Eigenschaft [Series.values_format_code](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series/values_format_code) festlegen. Diese Eigenschaft ist nicht nur für Serien geeignet, die auf einem Bereich im Arbeitsblatt basieren, sondern funktioniert auch gut für Serien, die mit einem Werte-Array erstellt wurden.

## **Setzen des Werteformatcodes der Diagrammserie**
Der folgende Beispielcode fügt einer leeren Diagrammserie, die zuvor keine Serie hatte, eine Serie hinzu. Es nutzt das Werte-Array, und nachdem die Serie hinzugefügt wurde, wird sie mit dem Code $#,##0 formatiert, wobei die Zahl 10000 zu $10.000 wird, unter Verwendung der Eigenschaft [Series.values_format_code](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series/values_format_code). Der Screenshot zeigt die Wirkung des Codes auf die [Beispiel-Excel-Datei](51740712.xlsx) und die [Ausgabedatei](51740713.xlsx) nach der Ausführung.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Beispielcode**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-SetValuesFormatCodeOfChartSeries.py" >}}
{{< app/cells/assistant language="python-net" >}}
