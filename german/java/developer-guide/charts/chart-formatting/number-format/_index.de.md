---
title: Setzen Sie den Werteformatcode der Diagrammserie
description: Erfahren Sie, wie Sie den Werteformatcode der Diagrammreihe in Aspose.Cells for Java festlegen. Unser Leitfaden hilft Ihnen zu verstehen, wie Sie Ihre Diagrammreihendaten mit dem entsprechenden Formatcode formatieren können, um Ihre Daten genau und professionell zu präsentieren.
keywords: Aspose.Cells for Java, Diagrammreihe, Werteformatcode, Formatierung, Datenpräsentation, Genauigkeit, Professionalität.
linktitle: Zahlenformat
type: docs
weight: 100
url: /de/java/set-the-values-format-code-of-chart-series/
---

## **Mögliche Verwendungsszenarien**
Sie können den Werteformatcode der Diagrammreihe mit der Methode [Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-) festlegen. Diese Methode ist nicht nur für die Reihe nützlich, die auf dem Bereich innerhalb des Arbeitsblatts basiert, sondern funktioniert auch gut für die mit einem Array von Werten erstellten Reihen.
## **Setzen des Werteformatcodes der Diagrammserie**
Der folgende Beispielcode fügt eine Serie in das leere Diagramm ein, das zuvor keine Serie hatte. Es fügt die Serie mithilfe des Arrays von Werten hinzu. Nachdem die Serie hinzugefügt wurde, wird sie mit dem Code $#,##0 formatiert, indem die Methode [Series.setValuesFormatCode](https://reference.aspose.com/cells/java/com.aspose.cells/series/#setValuesFormatCode-java.lang.String-) und die Zahl 10000 zu $10,000 werden. Der Screenshot zeigt die Auswirkung des Codes auf die [Beispiel-Excel-Datei](51740712.xlsx) und die [ausgegebene Excel-Datei](51740713.xlsx) nach der Ausführung.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "SetValuesFormatCodeOfChartSeries.java" >}}
{{< app/cells/assistant language="java" >}}
