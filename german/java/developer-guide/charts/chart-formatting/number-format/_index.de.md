---
title: Legen Sie den Werteformatcode der Diagrammreihe fest
description: Erfahren Sie, wie Sie den Werteformatcode von Diagrammreihen unter Aspose.Cells for Java festlegen. Unser Leitfaden hilft Ihnen zu verstehen, wie Sie Ihre Diagrammreihendaten mit dem entsprechenden Formatcode formatieren, sodass Sie Ihre Daten genau und professionell präsentieren können.
keywords: Aspose.Cells for Java, chart series, values format code, formatting, data presentation, accuracy, professionalism.
linktitle: Zahlenformat
type: docs
weight: 100
url: /de/java/set-the-values-format-code-of-chart-series/
---
##  **Mögliche Nutzungsszenarien**
Sie können den Werteformatcode von Diagrammreihen mithilfe von festlegen[Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-) Methode. Diese Methode ist nicht nur für Reihen nützlich, die auf dem Bereich innerhalb des Arbeitsblatts basieren, sondern eignet sich auch gut für Reihen, die mit einem Array von Werten erstellt werden.
##  **Legen Sie den Werteformatcode der Diagrammreihe fest**
 Der folgende Beispielcode fügt dem leeren Diagramm eine Reihe hinzu, für die es zuvor keine Reihe gab. Es fügt die Reihe mithilfe des Wertearrays hinzu. Sobald die Serie hinzugefügt wurde, formatiert sie sie mit dem Code $#,##0 unter Verwendung von[Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-) Methode und die Zahl 10.000 wird zu 10.000 $. Der Screenshot zeigt die Auswirkung des Codes auf die[Beispiel-Excel-Datei](51740712.xlsx) Und[Excel-Datei ausgeben](51740713.xlsx) nach der Ausführung.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
##  **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SetValuesFormatCodeOfChartSeries.java" >}}
